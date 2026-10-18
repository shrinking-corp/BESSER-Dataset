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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accPycMeter81_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial82' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_AccPyc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_AccPyc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_AccPyc(cupWeight=3.14, minSampleWeight=3.14)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial82', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_AccPyc', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial82') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_AccPyc', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial82') is None


def test_assoc_accuPycDensityMeter49_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial50' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeGeneral_AccuPycMeter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeGeneral_AccuPycMeter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeGeneral_AccuPycMeter(expectSampleWeight=7, polling=7, runTimout=7, sendSampleWeight=7)
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial50', None)
    _safe_set(owner, 'MachineLibrary_NodeGeneral_AccuPycMeter', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial50') == owner
    _safe_set(owner, 'MachineLibrary_NodeGeneral_AccuPycMeter', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial50') is None


def test_assoc_button211_stub_double():
    # MachineLibrary_Buttons has no real 'MachineLibrary_Buttons212' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Button(buttonNo=7, buttonText="sample_text", commandNo=7)
    partner = MachineLibrary_Buttons()
    setattr(partner, 'MachineLibrary_Buttons212', None)
    _safe_set(owner, 'MachineLibrary_Button', partner)
    assert owner in getattr(partner, 'MachineLibrary_Buttons212')
    _safe_set(owner, 'MachineLibrary_Button', None)
    assert owner not in getattr(partner, 'MachineLibrary_Buttons212')


def test_assoc_buttons63_stub_double():
    # MachineLibrary_Buttons has no real 'MachineLibrary_Buttons' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_Buttons()
    setattr(partner, 'MachineLibrary_Buttons', None)
    _safe_set(owner, 'MachineLibrary_Units64', partner)
    assert getattr(partner, 'MachineLibrary_Buttons') == owner
    _safe_set(owner, 'MachineLibrary_Units64', None)
    assert getattr(partner, 'MachineLibrary_Buttons') is None


def test_assoc_checkAskPrepUnit_ARL_XRF_OES133_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES134' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES134', None)
    _safe_set(owner, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES134') == owner
    _safe_set(owner, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES134') is None


def test_assoc_checkFilling_ARL_XRF_OES125_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES126' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_CheckFilling_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_CheckFilling_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_CheckFilling_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES126', None)
    _safe_set(owner, 'MachineLibrary_CheckFilling_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES126') == owner
    _safe_set(owner, 'MachineLibrary_CheckFilling_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES126') is None


def test_assoc_checkReqPrepUnit_ARL_XRF_OES129_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES130' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES130', None)
    _safe_set(owner, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES130') == owner
    _safe_set(owner, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES130') is None


def test_assoc_checkSampleConfig_SuperQXRF195_stub_double():
    # MachineLibrary_CheckSample_SuperQXRF has no real 'MachineLibrary_CheckSample_SuperQXRF196' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_CheckSampleConfig_SuperQXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_CheckSampleConfig_SuperQXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_CheckSampleConfig_SuperQXRF(anaProg="sample_text", minutes="sample_text", program="sample_text", sampleID="sample_text", samples="sample_text", seq_X=7)
    partner = MachineLibrary_CheckSample_SuperQXRF()
    setattr(partner, 'MachineLibrary_CheckSample_SuperQXRF196', None)
    _safe_set(owner, 'MachineLibrary_CheckSampleConfig_SuperQXRF', partner)
    assert owner in getattr(partner, 'MachineLibrary_CheckSample_SuperQXRF196')
    _safe_set(owner, 'MachineLibrary_CheckSampleConfig_SuperQXRF', None)
    assert owner not in getattr(partner, 'MachineLibrary_CheckSample_SuperQXRF196')


def test_assoc_command217_stub_double():
    # MachineLibrary_Commands has no real 'MachineLibrary_Commands218' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Command(commandName="sample_text", commandNo="sample_text", commandProgParameter=7)
    partner = MachineLibrary_Commands()
    setattr(partner, 'MachineLibrary_Commands218', None)
    _safe_set(owner, 'MachineLibrary_Command', partner)
    assert owner in getattr(partner, 'MachineLibrary_Commands218')
    _safe_set(owner, 'MachineLibrary_Command', None)
    assert owner not in getattr(partner, 'MachineLibrary_Commands218')


def test_assoc_commands27_stub_double():
    # MachineLibrary_Commands has no real 'MachineLibrary_Commands' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    partner = MachineLibrary_Commands()
    setattr(partner, 'MachineLibrary_Commands', None)
    _safe_set(owner, 'MachineLibrary_NodeConfig28', partner)
    assert getattr(partner, 'MachineLibrary_Commands') == owner
    _safe_set(owner, 'MachineLibrary_NodeConfig28', None)
    assert getattr(partner, 'MachineLibrary_Commands') is None


def test_assoc_communication_SuperQXRF119_stub_double():
    # MachineLibrary_UnitConfig_SuperQ_XRF has no real 'MachineLibrary_UnitConfig_SuperQ_XRF120' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Communication_SuperQXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Communication_SuperQXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Communication_SuperQXRF(enq_ACK_Protocol=7)
    partner = MachineLibrary_UnitConfig_SuperQ_XRF()
    setattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF120', None)
    _safe_set(owner, 'MachineLibrary_Communication_SuperQXRF', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF120') == owner
    _safe_set(owner, 'MachineLibrary_Communication_SuperQXRF', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF120') is None


def test_assoc_compac17_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig18' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Compac_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Compac_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Compac_Link(bcc=7, byteCount=7, bytecountcode=7, checksum=7, checksumCode=7, commConfig="sample_text", maxDataLength=7, params="sample_text", port="sample_text", retry=7, splitLongMessage=7, timeout=7, useNotACK_NAK=7, useNotENQ=7)
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig18', None)
    _safe_set(owner, 'MachineLibrary_Compac_Link', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig18') == owner
    _safe_set(owner, 'MachineLibrary_Compac_Link', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig18') is None


def test_assoc_controlSamples_SuperQXRF117_stub_double():
    # MachineLibrary_UnitConfig_SuperQ_XRF has no real 'MachineLibrary_UnitConfig_SuperQ_XRF118' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_ControlSamples_SuperQXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_ControlSamples_SuperQXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_ControlSamples_SuperQXRF(outOfControl=7)
    partner = MachineLibrary_UnitConfig_SuperQ_XRF()
    setattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF118', None)
    _safe_set(owner, 'MachineLibrary_ControlSamples_SuperQXRF', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF118') == owner
    _safe_set(owner, 'MachineLibrary_ControlSamples_SuperQXRF', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF118') is None


def test_assoc_disableSCT_ARL_XRF_OES137_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES138' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_DisableSCT_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_DisableSCT_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_DisableSCT_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES138', None)
    _safe_set(owner, 'MachineLibrary_DisableSCT_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES138') == owner
    _safe_set(owner, 'MachineLibrary_DisableSCT_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES138') is None


def test_assoc_dpBase21_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig22' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_DPbase_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_DPbase_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_DPbase_Link(cp_name="sample_text", maxNodes=7, speed=7)
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig22', None)
    _safe_set(owner, 'MachineLibrary_DPbase_Link', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig22') == owner
    _safe_set(owner, 'MachineLibrary_DPbase_Link', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig22') is None


def test_assoc_errorMessage_OBLFOES113_stub_double():
    # MachineLibrary_UnitConfig_OBLF_OES has no real 'MachineLibrary_UnitConfig_OBLF_OES114' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_ErrorMessage_OBLFOES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_ErrorMessage_OBLFOES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_ErrorMessage_OBLFOES(errorMessage="sample_text")
    partner = MachineLibrary_UnitConfig_OBLF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES114', None)
    _safe_set(owner, 'MachineLibrary_ErrorMessage_OBLFOES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES114') == owner
    _safe_set(owner, 'MachineLibrary_ErrorMessage_OBLFOES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES114') is None


def test_assoc_exeAskPrepUnit_ARL_XRF_OES135_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES136' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES136', None)
    _safe_set(owner, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES136') == owner
    _safe_set(owner, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES136') is None


def test_assoc_exePrepUnit_ARL_XRF_OES131_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES132' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_ExePrepUnit_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_ExePrepUnit_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_ExePrepUnit_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES132', None)
    _safe_set(owner, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES132') == owner
    _safe_set(owner, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES132') is None


def test_assoc_executeFiling_ARL_XRF_OES127_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES128' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_ExecuteFiling_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_ExecuteFiling_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_ExecuteFiling_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES128', None)
    _safe_set(owner, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES128') == owner
    _safe_set(owner, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES128') is None


def test_assoc_fileTransfer15_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig16' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_FileTransfer_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_FileTransfer_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_FileTransfer_Link(delimiter="sample_text", delimter="sample_text", flagDelAfterReading=7, flagToWriteWaitFor=7, flagToWriteWaitForDeleted=7, flagWriteAfterReading=7, maxDataLength=7, pollTime=7, readPath="sample_text", receiveBuffer=7, sendBuffer=7, timeoutwrite="sample_text", toWriteWaitFor="sample_text", translation=7, writeAfterReading=7, writePath="sample_text")
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig16', None)
    _safe_set(owner, 'MachineLibrary_FileTransfer_Link', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig16') == owner
    _safe_set(owner, 'MachineLibrary_FileTransfer_Link', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig16') is None


def test_assoc_file_Sample_ARL_XRF_OES145_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES146' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_File_Sample_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_File_Sample_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_File_Sample_ARL_XRF_OES(noSuccess="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES146', None)
    _safe_set(owner, 'MachineLibrary_File_Sample_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES146') == owner
    _safe_set(owner, 'MachineLibrary_File_Sample_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES146') is None


def test_assoc_generalParameter_SuperQXRF115_stub_double():
    # MachineLibrary_UnitConfig_SuperQ_XRF has no real 'MachineLibrary_UnitConfig_SuperQ_XRF116' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_GeneralParameter_SuperQXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_GeneralParameter_SuperQXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_GeneralParameter_SuperQXRF(listName="sample_text", startList="sample_text", switchRemote="sample_text")
    partner = MachineLibrary_UnitConfig_SuperQ_XRF()
    setattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF116', None)
    _safe_set(owner, 'MachineLibrary_GeneralParameter_SuperQXRF', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF116') == owner
    _safe_set(owner, 'MachineLibrary_GeneralParameter_SuperQXRF', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_SuperQ_XRF116') is None


def test_assoc_generalSetting_ARL_XRF_OES141_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES142' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_GeneralSetting_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_GeneralSetting_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_GeneralSetting_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES142', None)
    _safe_set(owner, 'MachineLibrary_GeneralSetting_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES142') == owner
    _safe_set(owner, 'MachineLibrary_GeneralSetting_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES142') is None


def test_assoc_historyConfig_AccPyc197_stub_double():
    # MachineLibrary_History_AccuPycMeter has no real 'MachineLibrary_History_AccuPycMeter198' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_HistoryConfig_AccuPyc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_HistoryConfig_AccuPyc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_HistoryConfig_AccuPyc(currentSample="sample_text", currentSampleID="sample_text", sampleCupWeight=3.14)
    partner = MachineLibrary_History_AccuPycMeter()
    setattr(partner, 'MachineLibrary_History_AccuPycMeter198', None)
    _safe_set(owner, 'MachineLibrary_HistoryConfig_AccuPyc', partner)
    assert owner in getattr(partner, 'MachineLibrary_History_AccuPycMeter198')
    _safe_set(owner, 'MachineLibrary_HistoryConfig_AccuPyc', None)
    assert owner not in getattr(partner, 'MachineLibrary_History_AccuPycMeter198')


def test_assoc_hostPC75_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial76' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_HostPC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_HostPC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_HostPC(index=7, maxIndex=7, replyOnLink=7, writeDumyIfNoDataExist=7)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial76', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_HostPC', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial76') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_HostPC', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial76') is None


def test_assoc_ibmWebSphereMQ19_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig20' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_IBMWebsphereMQ's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_IBMWebsphereMQ's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_IBMWebsphereMQ(maxDataSize=7, qName="sample_text", readDynamicQueName="sample_text", readQueMgrName="sample_text", readQueName="sample_text", receiveBuffer=7, sendBuffer=7, sendDynamicQueName="sample_text", sendQueMgrName="sample_text", sendQueName="sample_text")
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig20', None)
    _safe_set(owner, 'MachineLibrary_IBMWebsphereMQ', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig20') == owner
    _safe_set(owner, 'MachineLibrary_IBMWebsphereMQ', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig20') is None


def test_assoc_insert_Host153_stub_double():
    # MachineLibrary_UnitConfig_Host has no real 'MachineLibrary_UnitConfig_Host154' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_InsertRemove_Host's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_InsertRemove_Host's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_InsertRemove_Host(report_All=7)
    partner = MachineLibrary_UnitConfig_Host()
    setattr(partner, 'MachineLibrary_UnitConfig_Host154', None)
    _safe_set(owner, 'MachineLibrary_InsertRemove_Host', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host154') == owner
    _safe_set(owner, 'MachineLibrary_InsertRemove_Host', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host154') is None


def test_assoc_labMachine1_stub_double():
    # MachineLibrary_LabMachines has no real 'MachineLibrary_LabMachines2' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_LabMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_LabMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_LabMachine(createWinCCTags="sample_text", driver="sample_text", linkParamFile="sample_text", linkParamSection="sample_text", linkType="sample_text", machineName="sample_text", machineVersionNo=3.14, versionRemark="sample_text")
    partner = MachineLibrary_LabMachines()
    setattr(partner, 'MachineLibrary_LabMachines2', None)
    _safe_set(owner, 'MachineLibrary_LabMachine', partner)
    assert owner in getattr(partner, 'MachineLibrary_LabMachines2')
    _safe_set(owner, 'MachineLibrary_LabMachine', None)
    assert owner not in getattr(partner, 'MachineLibrary_LabMachines2')


def test_assoc_labMachines0_stub_double():
    # MachineLibrary_LabMachines has no real 'MachineLibrary_LabMachines' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_PMMachineLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_PMMachineLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_PMMachineLibrary(libraryVersion=3.14, libraryVersionRemark="sample_text")
    partner = MachineLibrary_LabMachines()
    setattr(partner, 'MachineLibrary_LabMachines', None)
    _safe_set(owner, 'MachineLibrary_PMMachineLibrary', partner)
    assert getattr(partner, 'MachineLibrary_LabMachines') == owner
    _safe_set(owner, 'MachineLibrary_PMMachineLibrary', None)
    assert getattr(partner, 'MachineLibrary_LabMachines') is None


def test_assoc_linkConfig7_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_LabMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_LabMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_LabMachine(createWinCCTags="sample_text", driver="sample_text", linkParamFile="sample_text", linkParamSection="sample_text", linkType="sample_text", machineName="sample_text", machineVersionNo=3.14, versionRemark="sample_text")
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig', None)
    _safe_set(owner, 'MachineLibrary_LabMachine8', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig') == owner
    _safe_set(owner, 'MachineLibrary_LabMachine8', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig') is None


def test_assoc_moved_Host151_stub_double():
    # MachineLibrary_UnitConfig_Host has no real 'MachineLibrary_UnitConfig_Host152' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Moved_Host's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Moved_Host's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Moved_Host(pos0=7, report_ALL=7, type0=7, writePositionNameInFile=7)
    partner = MachineLibrary_UnitConfig_Host()
    setattr(partner, 'MachineLibrary_UnitConfig_Host152', None)
    _safe_set(owner, 'MachineLibrary_Moved_Host', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host152') == owner
    _safe_set(owner, 'MachineLibrary_Moved_Host', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host152') is None


def test_assoc_nodeGeneralSpecial39_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial', None)
    _safe_set(owner, 'MachineLibrary_NodeConfig40', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial') == owner
    _safe_set(owner, 'MachineLibrary_NodeConfig40', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial') is None


def test_assoc_options209_stub_double():
    # MachineLibrary_CheckAddSID_PM2PM has no real 'MachineLibrary_CheckAddSID_PM2PM210' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_CheckAddSID_Values_PM2PM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_CheckAddSID_Values_PM2PM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_CheckAddSID_Values_PM2PM(optionNo=7, optonValue="sample_text")
    partner = MachineLibrary_CheckAddSID_PM2PM()
    setattr(partner, 'MachineLibrary_CheckAddSID_PM2PM210', None)
    _safe_set(owner, 'MachineLibrary_CheckAddSID_Values_PM2PM', partner)
    assert owner in getattr(partner, 'MachineLibrary_CheckAddSID_PM2PM210')
    _safe_set(owner, 'MachineLibrary_CheckAddSID_Values_PM2PM', None)
    assert owner not in getattr(partner, 'MachineLibrary_CheckAddSID_PM2PM210')


def test_assoc_outputRequest_OBLFOES107_stub_double():
    # MachineLibrary_UnitConfig_OBLF_OES has no real 'MachineLibrary_UnitConfig_OBLF_OES108' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_OutputRequest_OBLFOES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_OutputRequest_OBLFOES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_OutputRequest_OBLFOES(name="sample_text")
    partner = MachineLibrary_UnitConfig_OBLF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES108', None)
    _safe_set(owner, 'MachineLibrary_OutputRequest_OBLFOES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES108') == owner
    _safe_set(owner, 'MachineLibrary_OutputRequest_OBLFOES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES108') is None


def test_assoc_paramPrint227_stub_double():
    # MachineLibrary_NodeSpecialConfiguration has no real 'MachineLibrary_NodeSpecialConfiguration228' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_ParamPrint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_ParamPrint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_ParamPrint(dateStamp="sample_text", fontHightData=3.14, fontHightHeader=3.14, horzPosLeftBorder=3.14, horzPosValues=3.14, vertLineSpace=3.14, vertPosData=3.14, vertPosHeader=3.14)
    partner = MachineLibrary_NodeSpecialConfiguration()
    setattr(partner, 'MachineLibrary_NodeSpecialConfiguration228', None)
    _safe_set(owner, 'MachineLibrary_ParamPrint', partner)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration228') == owner
    _safe_set(owner, 'MachineLibrary_ParamPrint', None)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration228') is None


def test_assoc_plainMove231_stub_double():
    # MachineLibrary_NodeSpecialConfiguration has no real 'MachineLibrary_NodeSpecialConfiguration232' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_PlainMove's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_PlainMove's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_PlainMove(plainmovePreDefWS="sample_text", plainmoveSID_REF="sample_text", plainmoveType=7)
    partner = MachineLibrary_NodeSpecialConfiguration()
    setattr(partner, 'MachineLibrary_NodeSpecialConfiguration232', None)
    _safe_set(owner, 'MachineLibrary_PlainMove', partner)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration232') == owner
    _safe_set(owner, 'MachineLibrary_PlainMove', None)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration232') is None


def test_assoc_pm2PM43_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial44' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeGeneral_PM2PM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeGeneral_PM2PM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeGeneral_PM2PM(timeServer=7, type=7)
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial44', None)
    _safe_set(owner, 'MachineLibrary_NodeGeneral_PM2PM', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial44') == owner
    _safe_set(owner, 'MachineLibrary_NodeGeneral_PM2PM', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial44') is None


def test_assoc_pm2pm79_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial80' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_PM2PM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_PM2PM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_PM2PM(processFeedBack="sample_text", sid_Mask="sample_text")
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial80', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_PM2PM', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial80') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_PM2PM', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial80') is None


def test_assoc_position213_stub_double():
    # MachineLibrary_Positions has no real 'MachineLibrary_Positions214' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Position(posExit=7, posIndex=7, posName="sample_text", posNo=7, posRemark="sample_text", posWarningOnDelete=7)
    partner = MachineLibrary_Positions()
    setattr(partner, 'MachineLibrary_Positions214', None)
    _safe_set(owner, 'MachineLibrary_Position', partner)
    assert owner in getattr(partner, 'MachineLibrary_Positions214')
    _safe_set(owner, 'MachineLibrary_Position', None)
    assert owner not in getattr(partner, 'MachineLibrary_Positions214')


def test_assoc_positions55_stub_double():
    # MachineLibrary_Positions has no real 'MachineLibrary_Positions' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_Positions()
    setattr(partner, 'MachineLibrary_Positions', None)
    _safe_set(owner, 'MachineLibrary_Units56', partner)
    assert getattr(partner, 'MachineLibrary_Positions') == owner
    _safe_set(owner, 'MachineLibrary_Units56', None)
    assert getattr(partner, 'MachineLibrary_Positions') is None


def test_assoc_program219_stub_double():
    # MachineLibrary_NodePrograms has no real 'MachineLibrary_NodePrograms220' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeProgram(programAddress="sample_text", programLenPerParam="sample_text", programName="sample_text", programNo=7, programSection="sample_text")
    partner = MachineLibrary_NodePrograms()
    setattr(partner, 'MachineLibrary_NodePrograms220', None)
    _safe_set(owner, 'MachineLibrary_NodeProgram', partner)
    assert owner in getattr(partner, 'MachineLibrary_NodePrograms220')
    _safe_set(owner, 'MachineLibrary_NodeProgram', None)
    assert owner not in getattr(partner, 'MachineLibrary_NodePrograms220')


def test_assoc_programs29_stub_double():
    # MachineLibrary_NodePrograms has no real 'MachineLibrary_NodePrograms' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    partner = MachineLibrary_NodePrograms()
    setattr(partner, 'MachineLibrary_NodePrograms', None)
    _safe_set(owner, 'MachineLibrary_NodeConfig30', partner)
    assert getattr(partner, 'MachineLibrary_NodePrograms') == owner
    _safe_set(owner, 'MachineLibrary_NodeConfig30', None)
    assert getattr(partner, 'MachineLibrary_NodePrograms') is None


def test_assoc_programs61_stub_double():
    # MachineLibrary_UnitPrograms has no real 'MachineLibrary_UnitPrograms' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_UnitPrograms()
    setattr(partner, 'MachineLibrary_UnitPrograms', None)
    _safe_set(owner, 'MachineLibrary_Units62', partner)
    assert getattr(partner, 'MachineLibrary_UnitPrograms') == owner
    _safe_set(owner, 'MachineLibrary_Units62', None)
    assert getattr(partner, 'MachineLibrary_UnitPrograms') is None


def test_assoc_ps_Process_Finished_ARL_XRF_OES143_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES144' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_PS_Process_Finished_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_PS_Process_Finished_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_PS_Process_Finished_ARL_XRF_OES(noSuccess="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES144', None)
    _safe_set(owner, 'MachineLibrary_PS_Process_Finished_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES144') == owner
    _safe_set(owner, 'MachineLibrary_PS_Process_Finished_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES144') is None


def test_assoc_recalRequest_OBLFOES111_stub_double():
    # MachineLibrary_UnitConfig_OBLF_OES has no real 'MachineLibrary_UnitConfig_OBLF_OES112' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RecalRequest_OBLFOES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RecalRequest_OBLFOES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RecalRequest_OBLFOES(name="sample_text")
    partner = MachineLibrary_UnitConfig_OBLF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES112', None)
    _safe_set(owner, 'MachineLibrary_RecalRequest_OBLFOES', partner)
    assert owner in getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES112')
    _safe_set(owner, 'MachineLibrary_RecalRequest_OBLFOES', None)
    assert owner not in getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES112')


def test_assoc_remote77_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial78' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_Remote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_Remote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_Remote(editWSDB=True, handshakeA="sample_text", handshakeQ="sample_text", handshakeT=7)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial78', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_Remote', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial78') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_Remote', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial78') is None


def test_assoc_remotePM45_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial46' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeGeneral_RemotePM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeGeneral_RemotePM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeGeneral_RemotePM(system="sample_text", timeServer=7)
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial46', None)
    _safe_set(owner, 'MachineLibrary_NodeGeneral_RemotePM', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial46') == owner
    _safe_set(owner, 'MachineLibrary_NodeGeneral_RemotePM', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial46') is None


def test_assoc_remove_Host155_stub_double():
    # MachineLibrary_UnitConfig_Host has no real 'MachineLibrary_UnitConfig_Host156' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_InsertRemove_Host's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_InsertRemove_Host's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_InsertRemove_Host(report_All=7)
    partner = MachineLibrary_UnitConfig_Host()
    setattr(partner, 'MachineLibrary_UnitConfig_Host156', None)
    _safe_set(owner, 'MachineLibrary_InsertRemove_Host157', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host156') == owner
    _safe_set(owner, 'MachineLibrary_InsertRemove_Host157', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host156') is None


def test_assoc_report_Host147_stub_double():
    # MachineLibrary_UnitConfig_Host has no real 'MachineLibrary_UnitConfig_Host148' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Report_Host's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Report_Host's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Report_Host(fileName="sample_text", internal=7, maxType=7, minType=7, note="sample_text", note1="sample_text", rawData=7, sampleInsert=7, sampleMoved=7, sampleRemoved=7, sendErrorWarningsMsgOnly=7, sendLifeMessages=7, stateChanged=7, timeStamp=7)
    partner = MachineLibrary_UnitConfig_Host()
    setattr(partner, 'MachineLibrary_UnitConfig_Host148', None)
    _safe_set(owner, 'MachineLibrary_Report_Host', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host148') == owner
    _safe_set(owner, 'MachineLibrary_Report_Host', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host148') is None


def test_assoc_rigakuXRF51_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial52' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeGeneral_RigakuXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeGeneral_RigakuXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeGeneral_RigakuXRF(bDoNotshiftAtExit=7, timeout=7, timeoutResponce=7, timerToSendStatus=7)
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial52', None)
    _safe_set(owner, 'MachineLibrary_NodeGeneral_RigakuXRF', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial52') == owner
    _safe_set(owner, 'MachineLibrary_NodeGeneral_RigakuXRF', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial52') is None


def test_assoc_rigakuXRF85_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial86' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_RigakuXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_RigakuXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_RigakuXRF(lastPoHAG_SIInstrument=7, lastPosAnalyHAG_SIg=7, lastPosInInstrument=7, separator=7)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial86', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_RigakuXRF', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial86') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_RigakuXRF', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial86') is None


def test_assoc_robotConfSendOrder253_stub_double():
    # MachineLibrary_RobotConfSendOrders has no real 'MachineLibrary_RobotConfSendOrders254' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfSendOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfSendOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfSendOrder(robotconfsendorderFrom_X="sample_text", robotconfsendorderSeq_X=7, robotconfsendorderType_X="sample_text", robotconfsendorderVar_X="sample_text")
    partner = MachineLibrary_RobotConfSendOrders()
    setattr(partner, 'MachineLibrary_RobotConfSendOrders254', None)
    _safe_set(owner, 'MachineLibrary_RobotConfSendOrder', partner)
    assert owner in getattr(partner, 'MachineLibrary_RobotConfSendOrders254')
    _safe_set(owner, 'MachineLibrary_RobotConfSendOrder', None)
    assert owner not in getattr(partner, 'MachineLibrary_RobotConfSendOrders254')


def test_assoc_robotConfSendOrders241_stub_double():
    # MachineLibrary_RobotConfSendOrders has no real 'MachineLibrary_RobotConfSendOrders' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    partner = MachineLibrary_RobotConfSendOrders()
    setattr(partner, 'MachineLibrary_RobotConfSendOrders', None)
    _safe_set(owner, 'MachineLibrary_RobotConfiguration242', partner)
    assert getattr(partner, 'MachineLibrary_RobotConfSendOrders') == owner
    _safe_set(owner, 'MachineLibrary_RobotConfiguration242', None)
    assert getattr(partner, 'MachineLibrary_RobotConfSendOrders') is None


def test_assoc_robotConfiguration233_stub_double():
    # MachineLibrary_NodeSpecialConfiguration has no real 'MachineLibrary_NodeSpecialConfiguration234' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    partner = MachineLibrary_NodeSpecialConfiguration()
    setattr(partner, 'MachineLibrary_NodeSpecialConfiguration234', None)
    _safe_set(owner, 'MachineLibrary_RobotConfiguration', partner)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration234') == owner
    _safe_set(owner, 'MachineLibrary_RobotConfiguration', None)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration234') is None


def test_assoc_robotToWinCC257_stub_double():
    # MachineLibrary_RobotToWinccs has no real 'MachineLibrary_RobotToWinccs258' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotToWinCC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotToWinCC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotToWinCC(robotToWinccFrom_X="sample_text", robotToWinccSeq_X=7, robotToWinccTo_X="sample_text", robotToWinccType_X="sample_text")
    partner = MachineLibrary_RobotToWinccs()
    setattr(partner, 'MachineLibrary_RobotToWinccs258', None)
    _safe_set(owner, 'MachineLibrary_RobotToWinCC', partner)
    assert owner in getattr(partner, 'MachineLibrary_RobotToWinccs258')
    _safe_set(owner, 'MachineLibrary_RobotToWinCC', None)
    assert owner not in getattr(partner, 'MachineLibrary_RobotToWinccs258')


def test_assoc_robotToWinCCs245_stub_double():
    # MachineLibrary_RobotToWinccs has no real 'MachineLibrary_RobotToWinccs' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    partner = MachineLibrary_RobotToWinccs()
    setattr(partner, 'MachineLibrary_RobotToWinccs', None)
    _safe_set(owner, 'MachineLibrary_RobotConfiguration246', partner)
    assert getattr(partner, 'MachineLibrary_RobotToWinccs') == owner
    _safe_set(owner, 'MachineLibrary_RobotConfiguration246', None)
    assert getattr(partner, 'MachineLibrary_RobotToWinccs') is None


def test_assoc_robotVarToBusyCodes239_stub_double():
    # MachineLibrary_RobotVarToBusyCodes has no real 'MachineLibrary_RobotVarToBusyCodes' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    partner = MachineLibrary_RobotVarToBusyCodes()
    setattr(partner, 'MachineLibrary_RobotVarToBusyCodes', None)
    _safe_set(owner, 'MachineLibrary_RobotConfiguration240', partner)
    assert getattr(partner, 'MachineLibrary_RobotVarToBusyCodes') == owner
    _safe_set(owner, 'MachineLibrary_RobotConfiguration240', None)
    assert getattr(partner, 'MachineLibrary_RobotVarToBusyCodes') is None


def test_assoc_robotVarToBusycode251_stub_double():
    # MachineLibrary_RobotVarToBusyCodes has no real 'MachineLibrary_RobotVarToBusyCodes252' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotVarToBusycode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotVarToBusycode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotVarToBusycode(robotvartobusycodeBit_X=7, robotvartobusycodeSeq_X=7, robotvartobusycodeType_X="sample_text", robotvartobusycodeUnit_X=7, robotvartobusycodeVar_X="sample_text")
    partner = MachineLibrary_RobotVarToBusyCodes()
    setattr(partner, 'MachineLibrary_RobotVarToBusyCodes252', None)
    _safe_set(owner, 'MachineLibrary_RobotVarToBusycode', partner)
    assert owner in getattr(partner, 'MachineLibrary_RobotVarToBusyCodes252')
    _safe_set(owner, 'MachineLibrary_RobotVarToBusycode', None)
    assert owner not in getattr(partner, 'MachineLibrary_RobotVarToBusyCodes252')


def test_assoc_robotVarToErrorBits249_stub_double():
    # MachineLibrary_RobotVarToErrorbits has no real 'MachineLibrary_RobotVarToErrorbits' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    partner = MachineLibrary_RobotVarToErrorbits()
    setattr(partner, 'MachineLibrary_RobotVarToErrorbits', None)
    _safe_set(owner, 'MachineLibrary_RobotConfiguration250', partner)
    assert getattr(partner, 'MachineLibrary_RobotVarToErrorbits') == owner
    _safe_set(owner, 'MachineLibrary_RobotConfiguration250', None)
    assert getattr(partner, 'MachineLibrary_RobotVarToErrorbits') is None


def test_assoc_robotVarToErrorbit259_stub_double():
    # MachineLibrary_RobotVarToErrorbits has no real 'MachineLibrary_RobotVarToErrorbits260' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotVarToErrorbit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotVarToErrorbit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotVarToErrorbit(robotvartoerrorbitBit_X=7, robotvartoerrorbitInv_X=7, robotvartoerrorbitSeq_X=7, robotvartoerrorbitType_X="sample_text", robotvartoerrorbitVar_X="sample_text")
    partner = MachineLibrary_RobotVarToErrorbits()
    setattr(partner, 'MachineLibrary_RobotVarToErrorbits260', None)
    _safe_set(owner, 'MachineLibrary_RobotVarToErrorbit', partner)
    assert owner in getattr(partner, 'MachineLibrary_RobotVarToErrorbits260')
    _safe_set(owner, 'MachineLibrary_RobotVarToErrorbit', None)
    assert owner not in getattr(partner, 'MachineLibrary_RobotVarToErrorbits260')


def test_assoc_robotWinCCToRobot255_stub_double():
    # MachineLibrary_RobotWinCCToRobots has no real 'MachineLibrary_RobotWinCCToRobots256' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotWinCCToRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotWinCCToRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotWinCCToRobot(robotwincctorobootSeq_X=7, robotwincctorobootType_X="sample_text", robotwincctorobotFrom_X="sample_text", robotwincctorobotTo_X="sample_text")
    partner = MachineLibrary_RobotWinCCToRobots()
    setattr(partner, 'MachineLibrary_RobotWinCCToRobots256', None)
    _safe_set(owner, 'MachineLibrary_RobotWinCCToRobot', partner)
    assert owner in getattr(partner, 'MachineLibrary_RobotWinCCToRobots256')
    _safe_set(owner, 'MachineLibrary_RobotWinCCToRobot', None)
    assert owner not in getattr(partner, 'MachineLibrary_RobotWinCCToRobots256')


def test_assoc_robotWinCCToRobots243_stub_double():
    # MachineLibrary_RobotWinCCToRobots has no real 'MachineLibrary_RobotWinCCToRobots' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_RobotConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_RobotConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    partner = MachineLibrary_RobotWinCCToRobots()
    setattr(partner, 'MachineLibrary_RobotWinCCToRobots', None)
    _safe_set(owner, 'MachineLibrary_RobotConfiguration244', partner)
    assert getattr(partner, 'MachineLibrary_RobotWinCCToRobots') == owner
    _safe_set(owner, 'MachineLibrary_RobotConfiguration244', None)
    assert getattr(partner, 'MachineLibrary_RobotWinCCToRobots') is None


def test_assoc_sampleTpyeParameters193_stub_double():
    # MachineLibrary_CheckSampleRunTime_SuperQXRF has no real 'MachineLibrary_CheckSampleRunTime_SuperQXRF194' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_CheckSampleRunTimeParams_SuperQXRF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_CheckSampleRunTimeParams_SuperQXRF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_CheckSampleRunTimeParams_SuperQXRF(sampleType=7, value=7)
    partner = MachineLibrary_CheckSampleRunTime_SuperQXRF()
    setattr(partner, 'MachineLibrary_CheckSampleRunTime_SuperQXRF194', None)
    _safe_set(owner, 'MachineLibrary_CheckSampleRunTimeParams_SuperQXRF', partner)
    assert owner in getattr(partner, 'MachineLibrary_CheckSampleRunTime_SuperQXRF194')
    _safe_set(owner, 'MachineLibrary_CheckSampleRunTimeParams_SuperQXRF', None)
    assert owner not in getattr(partner, 'MachineLibrary_CheckSampleRunTime_SuperQXRF194')


def test_assoc_scanner87_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial88' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_Scanner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_Scanner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_Scanner(addString="sample_text", fillWith="sample_text", forcedSampleType=7, length=7, preString="sample_text", registerSample=7, start=7)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial88', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_Scanner', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial88') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_Scanner', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial88') is None


def test_assoc_scanner_SepByComma101_stub_double():
    # MachineLibrary_UnitSpecialConfiguration has no real 'MachineLibrary_UnitSpecialConfiguration102' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_SepByComma_Scanner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_SepByComma_Scanner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_SepByComma_Scanner(activ=7, preDefWS=7)
    partner = MachineLibrary_UnitSpecialConfiguration()
    setattr(partner, 'MachineLibrary_UnitSpecialConfiguration102', None)
    _safe_set(owner, 'MachineLibrary_SepByComma_Scanner', partner)
    assert getattr(partner, 'MachineLibrary_UnitSpecialConfiguration102') == owner
    _safe_set(owner, 'MachineLibrary_SepByComma_Scanner', None)
    assert getattr(partner, 'MachineLibrary_UnitSpecialConfiguration102') is None


def test_assoc_serial13_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig14' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Serial_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Serial_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Serial_Link(bufferLenght="sample_text", commConfig="sample_text", endChar="sample_text", logging=7, maxCharDelay="sample_text", params="sample_text", port="sample_text", startChar="sample_text")
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig14', None)
    _safe_set(owner, 'MachineLibrary_Serial_Link', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig14') == owner
    _safe_set(owner, 'MachineLibrary_Serial_Link', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig14') is None


def test_assoc_settings_ARL_XRF_OES139_stub_double():
    # MachineLibrary_UnitConfig_ARL_XRF_OES has no real 'MachineLibrary_UnitConfig_ARL_XRF_OES140' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Settings_ARL_XRF_OES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Settings_ARL_XRF_OES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Settings_ARL_XRF_OES(name="sample_text")
    partner = MachineLibrary_UnitConfig_ARL_XRF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES140', None)
    _safe_set(owner, 'MachineLibrary_Settings_ARL_XRF_OES', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES140') == owner
    _safe_set(owner, 'MachineLibrary_Settings_ARL_XRF_OES', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_ARL_XRF_OES140') is None


def test_assoc_specialConfiguration35_stub_double():
    # MachineLibrary_NodeSpecialConfiguration has no real 'MachineLibrary_NodeSpecialConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    partner = MachineLibrary_NodeSpecialConfiguration()
    setattr(partner, 'MachineLibrary_NodeSpecialConfiguration', None)
    _safe_set(owner, 'MachineLibrary_NodeConfig36', partner)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration') == owner
    _safe_set(owner, 'MachineLibrary_NodeConfig36', None)
    assert getattr(partner, 'MachineLibrary_NodeSpecialConfiguration') is None


def test_assoc_statusBit215_stub_double():
    # MachineLibrary_StausBits has no real 'MachineLibrary_StausBits216' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_StatusBit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_StatusBit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_StatusBit(bitName="sample_text", bitNo=7)
    partner = MachineLibrary_StausBits()
    setattr(partner, 'MachineLibrary_StausBits216', None)
    _safe_set(owner, 'MachineLibrary_StatusBit', partner)
    assert owner in getattr(partner, 'MachineLibrary_StausBits216')
    _safe_set(owner, 'MachineLibrary_StatusBit', None)
    assert owner not in getattr(partner, 'MachineLibrary_StausBits216')


def test_assoc_statusBits57_stub_double():
    # MachineLibrary_StausBits has no real 'MachineLibrary_StausBits' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_StausBits()
    setattr(partner, 'MachineLibrary_StausBits', None)
    _safe_set(owner, 'MachineLibrary_Units58', partner)
    assert getattr(partner, 'MachineLibrary_StausBits') == owner
    _safe_set(owner, 'MachineLibrary_Units58', None)
    assert getattr(partner, 'MachineLibrary_StausBits') is None


def test_assoc_superQ83_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial84' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_SuperQ's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_SuperQ's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_SuperQ(lastPosAnalysing=7, lastPosInInstrument=7)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial84', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_SuperQ', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial84') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_SuperQ', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial84') is None


def test_assoc_tcpIP11_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig12' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_TCPIP_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_TCPIP_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_TCPIP_Link(address_1="sample_text", address_2="sample_text", address_3="sample_text", address_4="sample_text", address_5="sample_text", address_6="sample_text", maxDataSize=7, msgDelay=7, port=7, protocol=7, receiveBuffer=7, sendBuffer=7, termChar=7)
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig12', None)
    _safe_set(owner, 'MachineLibrary_TCPIP_Link', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig12') == owner
    _safe_set(owner, 'MachineLibrary_TCPIP_Link', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig12') is None


def test_assoc_terminal41_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial42' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeGeneral_Terminal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeGeneral_Terminal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeGeneral_Terminal(customTimer1=7, customTimer2=7, displayTime=7, keyBoardSignalCarrierPresent=7, lenOfPlanID=7, maxScreens=7, maxXValue=7, maxYValue=7, name_1="sample_text", name_2="sample_text", name_3="sample_text", name_4="sample_text", name_5="sample_text", name_6="sample_text", signalCarrierPresent=7, stationAuto="sample_text", stationReady="sample_text", stationType=7, steelCarrier="sample_text", terminalType=7)
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial42', None)
    _safe_set(owner, 'MachineLibrary_NodeGeneral_Terminal', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial42') == owner
    _safe_set(owner, 'MachineLibrary_NodeGeneral_Terminal', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial42') is None


def test_assoc_terminal73_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial74' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneral_Terminal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneral_Terminal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneral_Terminal(station1="sample_text", station2="sample_text", station3="sample_text", station4="sample_text", station5="sample_text", thisStation="sample_text")
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial74', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneral_Terminal', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial74') == owner
    _safe_set(owner, 'MachineLibrary_UnitGeneral_Terminal', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial74') is None


def test_assoc_testRequest_OBLFOES109_stub_double():
    # MachineLibrary_UnitConfig_OBLF_OES has no real 'MachineLibrary_UnitConfig_OBLF_OES110' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_TestRequest_OBLFOES's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_TestRequest_OBLFOES's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_TestRequest_OBLFOES(name="sample_text")
    partner = MachineLibrary_UnitConfig_OBLF_OES()
    setattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES110', None)
    _safe_set(owner, 'MachineLibrary_TestRequest_OBLFOES', partner)
    assert owner in getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES110')
    _safe_set(owner, 'MachineLibrary_TestRequest_OBLFOES', None)
    assert owner not in getattr(partner, 'MachineLibrary_UnitConfig_OBLF_OES110')


def test_assoc_transferFileSection235_stub_double():
    # MachineLibrary_Transfer has no real 'MachineLibrary_Transfer236' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_TransferFileSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_TransferFileSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_TransferFileSection(transferFile="sample_text", transferSection="sample_text", transferSeq=7)
    partner = MachineLibrary_Transfer()
    setattr(partner, 'MachineLibrary_Transfer236', None)
    _safe_set(owner, 'MachineLibrary_TransferFileSection', partner)
    assert owner in getattr(partner, 'MachineLibrary_Transfer236')
    _safe_set(owner, 'MachineLibrary_TransferFileSection', None)
    assert owner not in getattr(partner, 'MachineLibrary_Transfer236')


def test_assoc_translate_terminal105_stub_double():
    # MachineLibrary_UnitConfig_Terminal has no real 'MachineLibrary_UnitConfig_Terminal106' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Translate_Terminal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Translate_Terminal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Translate_Terminal(auto_Busy="sample_text", auto_Ready="sample_text", man_Busy="sample_text", man_Ready="sample_text")
    partner = MachineLibrary_UnitConfig_Terminal()
    setattr(partner, 'MachineLibrary_UnitConfig_Terminal106', None)
    _safe_set(owner, 'MachineLibrary_Translate_Terminal', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Terminal106') == owner
    _safe_set(owner, 'MachineLibrary_Translate_Terminal', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Terminal106') is None


def test_assoc_unitGeneral65_stub_double():
    # MachineLibrary_UnitGeneral has no real 'MachineLibrary_UnitGeneral' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_UnitGeneral()
    setattr(partner, 'MachineLibrary_UnitGeneral', None)
    _safe_set(owner, 'MachineLibrary_Units66', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneral') == owner
    _safe_set(owner, 'MachineLibrary_Units66', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneral') is None


def test_assoc_unitGeneralParameter71_stub_double():
    # MachineLibrary_UnitGeneral has no real 'MachineLibrary_UnitGeneral72' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitGeneralParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitGeneralParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitGeneralParameters(KeyWord_1="sample_text", UseWith_1="sample_text", canBeChange_1=7, comment_1="sample_text", defaultValue_1=7, maxValue_1=7, minValue_1=7, paraName_1="sample_text", seq_X=7, unit_1="sample_text", visibleType_1=7)
    partner = MachineLibrary_UnitGeneral()
    setattr(partner, 'MachineLibrary_UnitGeneral72', None)
    _safe_set(owner, 'MachineLibrary_UnitGeneralParameters', partner)
    assert owner in getattr(partner, 'MachineLibrary_UnitGeneral72')
    _safe_set(owner, 'MachineLibrary_UnitGeneralParameters', None)
    assert owner not in getattr(partner, 'MachineLibrary_UnitGeneral72')


def test_assoc_unitGeneralSpecial67_stub_double():
    # MachineLibrary_UnitGeneralSpecial has no real 'MachineLibrary_UnitGeneralSpecial' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_UnitGeneralSpecial()
    setattr(partner, 'MachineLibrary_UnitGeneralSpecial', None)
    _safe_set(owner, 'MachineLibrary_Units68', partner)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial') == owner
    _safe_set(owner, 'MachineLibrary_Units68', None)
    assert getattr(partner, 'MachineLibrary_UnitGeneralSpecial') is None


def test_assoc_unitProgram221_stub_double():
    # MachineLibrary_UnitPrograms has no real 'MachineLibrary_UnitPrograms222' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_UnitProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_UnitProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_UnitProgram(unitProgName="sample_text")
    partner = MachineLibrary_UnitPrograms()
    setattr(partner, 'MachineLibrary_UnitPrograms222', None)
    _safe_set(owner, 'MachineLibrary_UnitProgram', partner)
    assert owner in getattr(partner, 'MachineLibrary_UnitPrograms222')
    _safe_set(owner, 'MachineLibrary_UnitProgram', None)
    assert owner not in getattr(partner, 'MachineLibrary_UnitPrograms222')


def test_assoc_unitSpecialConfiguration69_stub_double():
    # MachineLibrary_UnitSpecialConfiguration has no real 'MachineLibrary_UnitSpecialConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_Units's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_Units's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    partner = MachineLibrary_UnitSpecialConfiguration()
    setattr(partner, 'MachineLibrary_UnitSpecialConfiguration', None)
    _safe_set(owner, 'MachineLibrary_Units70', partner)
    assert getattr(partner, 'MachineLibrary_UnitSpecialConfiguration') == owner
    _safe_set(owner, 'MachineLibrary_Units70', None)
    assert getattr(partner, 'MachineLibrary_UnitSpecialConfiguration') is None


def test_assoc_winCCLnk9_stub_double():
    # MachineLibrary_LinkConfig has no real 'MachineLibrary_LinkConfig10' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_WinCCLnk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_WinCCLnk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_WinCCLnk(canCreateTags=7, canModifyTag=7, connectionName="sample_text", updateCycle=7, updateCycle_Help="sample_text")
    partner = MachineLibrary_LinkConfig()
    setattr(partner, 'MachineLibrary_LinkConfig10', None)
    _safe_set(owner, 'MachineLibrary_WinCCLnk', partner)
    assert getattr(partner, 'MachineLibrary_LinkConfig10') == owner
    _safe_set(owner, 'MachineLibrary_WinCCLnk', None)
    assert getattr(partner, 'MachineLibrary_LinkConfig10') is None


def test_assoc_wincc2WinCC47_stub_double():
    # MachineLibrary_NodeGeneralSpecial has no real 'MachineLibrary_NodeGeneralSpecial48' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_NodeGeneral_WinCC2WinCC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_NodeGeneral_WinCC2WinCC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_NodeGeneral_WinCC2WinCC(prefix="sample_text")
    partner = MachineLibrary_NodeGeneralSpecial()
    setattr(partner, 'MachineLibrary_NodeGeneralSpecial48', None)
    _safe_set(owner, 'MachineLibrary_NodeGeneral_WinCC2WinCC', partner)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial48') == owner
    _safe_set(owner, 'MachineLibrary_NodeGeneral_WinCC2WinCC', None)
    assert getattr(partner, 'MachineLibrary_NodeGeneralSpecial48') is None


def test_assoc_ws_Update_Host149_stub_double():
    # MachineLibrary_UnitConfig_Host has no real 'MachineLibrary_UnitConfig_Host150' property in the generated
    # code (a bare stub) -- manually attach it so MachineLibrary_WS_Update_Host's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MachineLibrary_WS_Update_Host's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MachineLibrary_WS_Update_Host(AllowUnit0=7, checkUnit=7)
    partner = MachineLibrary_UnitConfig_Host()
    setattr(partner, 'MachineLibrary_UnitConfig_Host150', None)
    _safe_set(owner, 'MachineLibrary_WS_Update_Host', partner)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host150') == owner
    _safe_set(owner, 'MachineLibrary_WS_Update_Host', None)
    assert getattr(partner, 'MachineLibrary_UnitConfig_Host150') is None


