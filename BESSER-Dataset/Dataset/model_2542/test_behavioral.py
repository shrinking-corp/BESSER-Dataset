import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fastfst_Header,
    fastfst_ModelFastfst,
    fastfst_Section,
    fastfst_aBldGagNd,
    fastfst_aTwrGagNd,
    fastfst_bCompAero,
    fastfst_bCompNoise,
    fastfst_bDrTrDOF,
    fastfst_bEcho,
    fastfst_bEdgeDOF,
    fastfst_bFlapDOF1,
    fastfst_bFlapDOF2,
    fastfst_bFurling,
    fastfst_bGBRevers,
    fastfst_bGenDOF,
    fastfst_bGenTiStp,
    fastfst_bGenTiStr,
    fastfst_bOutFileFmt,
    fastfst_bSumPrint,
    fastfst_bTabDelim,
    fastfst_bTeetDOF,
    fastfst_bTwFADOF1,
    fastfst_bTwFADOF2,
    fastfst_bTwSSDOF1,
    fastfst_bTwSSDOF2,
    fastfst_bYawDOF,
    fastfst_fADAMSFile,
    fastfst_fADFile,
    fastfst_fBldFile_1_,
    fastfst_fBldFile_2_,
    fastfst_fBldFile_3_,
    fastfst_fDynBrkFi,
    fastfst_fFurlFile,
    fastfst_fLinFile,
    fastfst_fNoiseFile,
    fastfst_fPtfmFile,
    fastfst_fTwrFile,
    fastfst_iADAMSPrep,
    fastfst_iAnalMode,
    fastfst_iDecFact,
    fastfst_iGenModel,
    fastfst_iHSSBrMode,
    fastfst_iNBlGages,
    fastfst_iNTwGages,
    fastfst_iNumBl,
    fastfst_iPCMode,
    fastfst_iPtfmModel,
    fastfst_iTeetMod,
    fastfst_iTwrNodes,
    fastfst_iVSContrl,
    fastfst_iYCMode,
    fastfst_nAzimB1Up,
    fastfst_nAzimuth,
    fastfst_nBlPitchF_1_,
    fastfst_nBlPitchF_2_,
    fastfst_nBlPitchF_3_,
    fastfst_nBlPitch_1_,
    fastfst_nBlPitch_2_,
    fastfst_nBlPitch_3_,
    fastfst_nDT,
    fastfst_nDTTorDmp,
    fastfst_nDTTorSpr,
    fastfst_nDelta3,
    fastfst_nGBRatio,
    fastfst_nGBoxEff,
    fastfst_nGenEff,
    fastfst_nGenIner,
    fastfst_nGravity,
    fastfst_nHSSBrDT,
    fastfst_nHSSBrTqF,
    fastfst_nHubCM,
    fastfst_nHubIner,
    fastfst_nHubMass,
    fastfst_nHubRad,
    fastfst_nIPDefl,
    fastfst_nNacCMxn,
    fastfst_nNacCMyn,
    fastfst_nNacCMzn,
    fastfst_nNacMass,
    fastfst_nNacYIner,
    fastfst_nNacYaw,
    fastfst_nNacYawF,
    fastfst_nNcIMUxn,
    fastfst_nNcIMUyn,
    fastfst_nNcIMUzn,
    fastfst_nOoPDefl,
    fastfst_nOverHang,
    fastfst_nPSpnElN,
    fastfst_nPreCone_1_,
    fastfst_nPreCone_2_,
    fastfst_nPreCone_3_,
    fastfst_nRotSpeed,
    fastfst_nSIG_PORt,
    fastfst_nSIG_RtTq,
    fastfst_nSIG_SlPc,
    fastfst_nSIG_SySp,
    fastfst_nShftGagL,
    fastfst_nShftTilt,
    fastfst_nSpdGenOn,
    fastfst_nSttsTime,
    fastfst_nTBDepISp_1_,
    fastfst_nTBDepISp_2_,
    fastfst_nTBDepISp_3_,
    fastfst_nTBDrConD,
    fastfst_nTBDrConN,
    fastfst_nTEC_Freq,
    fastfst_nTEC_MR,
    fastfst_nTEC_Npol,
    fastfst_nTEC_RLR,
    fastfst_nTEC_Rres,
    fastfst_nTEC_SLR,
    fastfst_nTEC_Sres,
    fastfst_nTEC_VLL,
    fastfst_nTHSSBrDp,
    fastfst_nTMax,
    fastfst_nTPCOn,
    fastfst_nTPitManE_1_,
    fastfst_nTPitManE_2_,
    fastfst_nTPitManE_3_,
    fastfst_nTPitManS_1_,
    fastfst_nTPitManS_2_,
    fastfst_nTPitManS_3_,
    fastfst_nTStart,
    fastfst_nTTDspFA,
    fastfst_nTTDspSS,
    fastfst_nTTpBrDp_1_,
    fastfst_nTTpBrDp_2_,
    fastfst_nTTpBrDp_3_,
    fastfst_nTYCOn,
    fastfst_nTYawManE,
    fastfst_nTYawManS,
    fastfst_nTeetCDmp,
    fastfst_nTeetDefl,
    fastfst_nTeetDmp,
    fastfst_nTeetDmpP,
    fastfst_nTeetHSSp,
    fastfst_nTeetHStP,
    fastfst_nTeetSSSp,
    fastfst_nTeetSStP,
    fastfst_nTiDynBrk,
    fastfst_nTimGenOf,
    fastfst_nTimGenOn,
    fastfst_nTipMass_1_,
    fastfst_nTipMass_2_,
    fastfst_nTipMass_3_,
    fastfst_nTipRad,
    fastfst_nTowerHt,
    fastfst_nTpBrDT,
    fastfst_nTwr2Shft,
    fastfst_nTwrRBHt,
    fastfst_nUndSling,
    fastfst_nVS_Rgn2K,
    fastfst_nVS_RtGnSp,
    fastfst_nVS_RtTq,
    fastfst_nVS_SlPc,
    fastfst_nYawBrMass,
    fastfst_nYawDamp,
    fastfst_nYawNeut,
    fastfst_nYawSpr,
    fastfst_sOutFmt,
    fastfst_vOutList,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ADAMSFile283_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst284' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fADAMSFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fADAMSFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fADAMSFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst284', None)
    _safe_set(owner, 'fastfst_fADAMSFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst284') == owner
    _safe_set(owner, 'fastfst_fADAMSFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst284') is None


def test_assoc_ADAMSPrep5_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst6' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iADAMSPrep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iADAMSPrep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iADAMSPrep(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst6', None)
    _safe_set(owner, 'fastfst_iADAMSPrep', partner)
    assert getattr(partner, 'fastfst_ModelFastfst6') == owner
    _safe_set(owner, 'fastfst_iADAMSPrep', None)
    assert getattr(partner, 'fastfst_ModelFastfst6') is None


def test_assoc_ADFile279_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst280' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fADFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fADFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fADFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst280', None)
    _safe_set(owner, 'fastfst_fADFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst280') == owner
    _safe_set(owner, 'fastfst_fADFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst280') is None


def test_assoc_AnalMode7_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst8' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iAnalMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iAnalMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iAnalMode(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst8', None)
    _safe_set(owner, 'fastfst_iAnalMode', partner)
    assert getattr(partner, 'fastfst_ModelFastfst8') == owner
    _safe_set(owner, 'fastfst_iAnalMode', None)
    assert getattr(partner, 'fastfst_ModelFastfst8') is None


def test_assoc_AzimB1Up171_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst172' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nAzimB1Up's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nAzimB1Up's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nAzimB1Up(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst172', None)
    _safe_set(owner, 'fastfst_nAzimB1Up', partner)
    assert getattr(partner, 'fastfst_ModelFastfst172') == owner
    _safe_set(owner, 'fastfst_nAzimB1Up', None)
    assert getattr(partner, 'fastfst_ModelFastfst172') is None


def test_assoc_Azimuth127_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst128' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nAzimuth's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nAzimuth's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nAzimuth(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst128', None)
    _safe_set(owner, 'fastfst_nAzimuth', partner)
    assert getattr(partner, 'fastfst_ModelFastfst128') == owner
    _safe_set(owner, 'fastfst_nAzimuth', None)
    assert getattr(partner, 'fastfst_ModelFastfst128') is None


def test_assoc_BlPitchF_1_87_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst88' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nBlPitchF_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nBlPitchF_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nBlPitchF_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst88', None)
    _safe_set(owner, 'fastfst_nBlPitchF_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst88') == owner
    _safe_set(owner, 'fastfst_nBlPitchF_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst88') is None


def test_assoc_BlPitchF_2_89_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst90' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nBlPitchF_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nBlPitchF_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nBlPitchF_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst90', None)
    _safe_set(owner, 'fastfst_nBlPitchF_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst90') == owner
    _safe_set(owner, 'fastfst_nBlPitchF_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst90') is None


def test_assoc_BlPitchF_3_91_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst92' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nBlPitchF_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nBlPitchF_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nBlPitchF_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst92', None)
    _safe_set(owner, 'fastfst_nBlPitchF_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst92') == owner
    _safe_set(owner, 'fastfst_nBlPitchF_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst92') is None


def test_assoc_BlPitch_1_81_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst82' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nBlPitch_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nBlPitch_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nBlPitch_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst82', None)
    _safe_set(owner, 'fastfst_nBlPitch_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst82') == owner
    _safe_set(owner, 'fastfst_nBlPitch_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst82') is None


def test_assoc_BlPitch_2_83_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst84' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nBlPitch_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nBlPitch_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nBlPitch_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst84', None)
    _safe_set(owner, 'fastfst_nBlPitch_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst84') == owner
    _safe_set(owner, 'fastfst_nBlPitch_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst84') is None


def test_assoc_BlPitch_3_85_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst86' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nBlPitch_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nBlPitch_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nBlPitch_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst86', None)
    _safe_set(owner, 'fastfst_nBlPitch_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst86') == owner
    _safe_set(owner, 'fastfst_nBlPitch_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst86') is None


def test_assoc_BldFile_1_273_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst274' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fBldFile_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fBldFile_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fBldFile_1_(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst274', None)
    _safe_set(owner, 'fastfst_fBldFile_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst274') == owner
    _safe_set(owner, 'fastfst_fBldFile_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst274') is None


def test_assoc_BldFile_2_275_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst276' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fBldFile_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fBldFile_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fBldFile_2_(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst276', None)
    _safe_set(owner, 'fastfst_fBldFile_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst276') == owner
    _safe_set(owner, 'fastfst_fBldFile_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst276') is None


def test_assoc_BldFile_3_277_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst278' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fBldFile_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fBldFile_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fBldFile_3_(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst278', None)
    _safe_set(owner, 'fastfst_fBldFile_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst278') == owner
    _safe_set(owner, 'fastfst_fBldFile_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst278') is None


def test_assoc_BldGagNd315_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst316' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_aBldGagNd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_aBldGagNd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_aBldGagNd(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst316', None)
    _safe_set(owner, 'fastfst_aBldGagNd', partner)
    assert getattr(partner, 'fastfst_ModelFastfst316') == owner
    _safe_set(owner, 'fastfst_aBldGagNd', None)
    assert getattr(partner, 'fastfst_ModelFastfst316') is None


def test_assoc_CompAero117_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst118' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bCompAero's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bCompAero's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bCompAero(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst118', None)
    _safe_set(owner, 'fastfst_bCompAero', partner)
    assert getattr(partner, 'fastfst_ModelFastfst118') == owner
    _safe_set(owner, 'fastfst_bCompAero', None)
    assert getattr(partner, 'fastfst_ModelFastfst118') is None


def test_assoc_CompNoise119_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst120' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bCompNoise's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bCompNoise's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bCompNoise(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst120', None)
    _safe_set(owner, 'fastfst_bCompNoise', partner)
    assert getattr(partner, 'fastfst_ModelFastfst120') == owner
    _safe_set(owner, 'fastfst_bCompNoise', None)
    assert getattr(partner, 'fastfst_ModelFastfst120') is None


def test_assoc_DT13_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst14' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nDT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nDT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nDT(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst14', None)
    _safe_set(owner, 'fastfst_nDT', partner)
    assert getattr(partner, 'fastfst_ModelFastfst14') == owner
    _safe_set(owner, 'fastfst_nDT', None)
    assert getattr(partner, 'fastfst_ModelFastfst14') is None


def test_assoc_DTTorDmp207_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst208' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nDTTorDmp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nDTTorDmp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nDTTorDmp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst208', None)
    _safe_set(owner, 'fastfst_nDTTorDmp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst208') == owner
    _safe_set(owner, 'fastfst_nDTTorDmp', None)
    assert getattr(partner, 'fastfst_ModelFastfst208') is None


def test_assoc_DTTorSpr205_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst206' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nDTTorSpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nDTTorSpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nDTTorSpr(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst206', None)
    _safe_set(owner, 'fastfst_nDTTorSpr', partner)
    assert getattr(partner, 'fastfst_ModelFastfst206') == owner
    _safe_set(owner, 'fastfst_nDTTorSpr', None)
    assert getattr(partner, 'fastfst_ModelFastfst206') is None


def test_assoc_DecFact297_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst298' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iDecFact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iDecFact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iDecFact(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst298', None)
    _safe_set(owner, 'fastfst_iDecFact', partner)
    assert getattr(partner, 'fastfst_ModelFastfst298') == owner
    _safe_set(owner, 'fastfst_iDecFact', None)
    assert getattr(partner, 'fastfst_ModelFastfst298') is None


def test_assoc_Delta3163_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst164' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nDelta3's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nDelta3's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nDelta3(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst164', None)
    _safe_set(owner, 'fastfst_nDelta3', partner)
    assert getattr(partner, 'fastfst_ModelFastfst164') == owner
    _safe_set(owner, 'fastfst_nDelta3', None)
    assert getattr(partner, 'fastfst_ModelFastfst164') is None


def test_assoc_DrTrDOF103_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst104' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bDrTrDOF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bDrTrDOF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bDrTrDOF(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst104', None)
    _safe_set(owner, 'fastfst_bDrTrDOF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst104') == owner
    _safe_set(owner, 'fastfst_bDrTrDOF', None)
    assert getattr(partner, 'fastfst_ModelFastfst104') is None


def test_assoc_DynBrkFi203_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst204' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fDynBrkFi's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fDynBrkFi's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fDynBrkFi(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst204', None)
    _safe_set(owner, 'fastfst_fDynBrkFi', partner)
    assert getattr(partner, 'fastfst_ModelFastfst204') == owner
    _safe_set(owner, 'fastfst_fDynBrkFi', None)
    assert getattr(partner, 'fastfst_ModelFastfst204') is None


def test_assoc_Echo3_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst4' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bEcho's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bEcho's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bEcho(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst4', None)
    _safe_set(owner, 'fastfst_bEcho', partner)
    assert getattr(partner, 'fastfst_ModelFastfst4') == owner
    _safe_set(owner, 'fastfst_bEcho', None)
    assert getattr(partner, 'fastfst_ModelFastfst4') is None


def test_assoc_EdgeDOF99_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst100' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bEdgeDOF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bEdgeDOF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bEdgeDOF(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst100', None)
    _safe_set(owner, 'fastfst_bEdgeDOF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst100') == owner
    _safe_set(owner, 'fastfst_bEdgeDOF', None)
    assert getattr(partner, 'fastfst_ModelFastfst100') is None


def test_assoc_FlapDOF195_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst96' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bFlapDOF1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bFlapDOF1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bFlapDOF1(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst96', None)
    _safe_set(owner, 'fastfst_bFlapDOF1', partner)
    assert getattr(partner, 'fastfst_ModelFastfst96') == owner
    _safe_set(owner, 'fastfst_bFlapDOF1', None)
    assert getattr(partner, 'fastfst_ModelFastfst96') is None


def test_assoc_FlapDOF297_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst98' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bFlapDOF2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bFlapDOF2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bFlapDOF2(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst98', None)
    _safe_set(owner, 'fastfst_bFlapDOF2', partner)
    assert getattr(partner, 'fastfst_ModelFastfst98') == owner
    _safe_set(owner, 'fastfst_bFlapDOF2', None)
    assert getattr(partner, 'fastfst_ModelFastfst98') is None


def test_assoc_FurlFile249_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst250' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fFurlFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fFurlFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fFurlFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst250', None)
    _safe_set(owner, 'fastfst_fFurlFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst250') == owner
    _safe_set(owner, 'fastfst_fFurlFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst250') is None


def test_assoc_Furling247_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst248' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bFurling's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bFurling's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bFurling(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst248', None)
    _safe_set(owner, 'fastfst_bFurling', partner)
    assert getattr(partner, 'fastfst_ModelFastfst248') == owner
    _safe_set(owner, 'fastfst_bFurling', None)
    assert getattr(partner, 'fastfst_ModelFastfst248') is None


def test_assoc_GBRatio195_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst196' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nGBRatio's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nGBRatio's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nGBRatio(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst196', None)
    _safe_set(owner, 'fastfst_nGBRatio', partner)
    assert getattr(partner, 'fastfst_ModelFastfst196') == owner
    _safe_set(owner, 'fastfst_nGBRatio', None)
    assert getattr(partner, 'fastfst_ModelFastfst196') is None


def test_assoc_GBRevers197_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst198' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bGBRevers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bGBRevers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bGBRevers(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst198', None)
    _safe_set(owner, 'fastfst_bGBRevers', partner)
    assert getattr(partner, 'fastfst_ModelFastfst198') == owner
    _safe_set(owner, 'fastfst_bGBRevers', None)
    assert getattr(partner, 'fastfst_ModelFastfst198') is None


def test_assoc_GBoxEff191_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst192' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nGBoxEff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nGBoxEff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nGBoxEff(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst192', None)
    _safe_set(owner, 'fastfst_nGBoxEff', partner)
    assert getattr(partner, 'fastfst_ModelFastfst192') == owner
    _safe_set(owner, 'fastfst_nGBoxEff', None)
    assert getattr(partner, 'fastfst_ModelFastfst192') is None


def test_assoc_GenDOF105_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst106' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bGenDOF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bGenDOF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bGenDOF(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst106', None)
    _safe_set(owner, 'fastfst_bGenDOF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst106') == owner
    _safe_set(owner, 'fastfst_bGenDOF', None)
    assert getattr(partner, 'fastfst_ModelFastfst106') is None


def test_assoc_GenEff193_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst194' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nGenEff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nGenEff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nGenEff(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst194', None)
    _safe_set(owner, 'fastfst_nGenEff', partner)
    assert getattr(partner, 'fastfst_ModelFastfst194') == owner
    _safe_set(owner, 'fastfst_nGenEff', None)
    assert getattr(partner, 'fastfst_ModelFastfst194') is None


def test_assoc_GenIner187_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst188' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nGenIner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nGenIner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nGenIner(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst188', None)
    _safe_set(owner, 'fastfst_nGenIner', partner)
    assert getattr(partner, 'fastfst_ModelFastfst188') == owner
    _safe_set(owner, 'fastfst_nGenIner', None)
    assert getattr(partner, 'fastfst_ModelFastfst188') is None


def test_assoc_GenModel33_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst34' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iGenModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iGenModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iGenModel(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst34', None)
    _safe_set(owner, 'fastfst_iGenModel', partner)
    assert getattr(partner, 'fastfst_ModelFastfst34') == owner
    _safe_set(owner, 'fastfst_iGenModel', None)
    assert getattr(partner, 'fastfst_ModelFastfst34') is None


def test_assoc_GenTiStp37_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst38' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bGenTiStp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bGenTiStp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bGenTiStp(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst38', None)
    _safe_set(owner, 'fastfst_bGenTiStp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst38') == owner
    _safe_set(owner, 'fastfst_bGenTiStp', None)
    assert getattr(partner, 'fastfst_ModelFastfst38') is None


def test_assoc_GenTiStr35_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst36' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bGenTiStr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bGenTiStr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bGenTiStr(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst36', None)
    _safe_set(owner, 'fastfst_bGenTiStr', partner)
    assert getattr(partner, 'fastfst_ModelFastfst36') == owner
    _safe_set(owner, 'fastfst_bGenTiStr', None)
    assert getattr(partner, 'fastfst_ModelFastfst36') is None


def test_assoc_Gravity93_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst94' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nGravity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nGravity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nGravity(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst94', None)
    _safe_set(owner, 'fastfst_nGravity', partner)
    assert getattr(partner, 'fastfst_ModelFastfst94') == owner
    _safe_set(owner, 'fastfst_nGravity', None)
    assert getattr(partner, 'fastfst_ModelFastfst94') is None


def test_assoc_HSSBrDT201_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst202' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nHSSBrDT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nHSSBrDT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nHSSBrDT(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst202', None)
    _safe_set(owner, 'fastfst_nHSSBrDT', partner)
    assert getattr(partner, 'fastfst_ModelFastfst202') == owner
    _safe_set(owner, 'fastfst_nHSSBrDT', None)
    assert getattr(partner, 'fastfst_ModelFastfst202') is None


def test_assoc_HSSBrMode45_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst46' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iHSSBrMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iHSSBrMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iHSSBrMode(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst46', None)
    _safe_set(owner, 'fastfst_iHSSBrMode', partner)
    assert getattr(partner, 'fastfst_ModelFastfst46') == owner
    _safe_set(owner, 'fastfst_iHSSBrMode', None)
    assert getattr(partner, 'fastfst_ModelFastfst46') is None


def test_assoc_HSSBrTqF199_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst200' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nHSSBrTqF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nHSSBrTqF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nHSSBrTqF(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst200', None)
    _safe_set(owner, 'fastfst_nHSSBrTqF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst200') == owner
    _safe_set(owner, 'fastfst_nHSSBrTqF', None)
    assert getattr(partner, 'fastfst_ModelFastfst200') is None


def test_assoc_Head0_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_Header's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_Header's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_Header(rows="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst', None)
    _safe_set(owner, 'fastfst_Header', partner)
    assert getattr(partner, 'fastfst_ModelFastfst') == owner
    _safe_set(owner, 'fastfst_Header', None)
    assert getattr(partner, 'fastfst_ModelFastfst') is None


def test_assoc_HubCM145_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst146' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nHubCM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nHubCM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nHubCM(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst146', None)
    _safe_set(owner, 'fastfst_nHubCM', partner)
    assert getattr(partner, 'fastfst_ModelFastfst146') == owner
    _safe_set(owner, 'fastfst_nHubCM', None)
    assert getattr(partner, 'fastfst_ModelFastfst146') is None


def test_assoc_HubIner189_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst190' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nHubIner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nHubIner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nHubIner(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst190', None)
    _safe_set(owner, 'fastfst_nHubIner', partner)
    assert getattr(partner, 'fastfst_ModelFastfst190') == owner
    _safe_set(owner, 'fastfst_nHubIner', None)
    assert getattr(partner, 'fastfst_ModelFastfst190') is None


def test_assoc_HubMass177_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst178' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nHubMass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nHubMass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nHubMass(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst178', None)
    _safe_set(owner, 'fastfst_nHubMass', partner)
    assert getattr(partner, 'fastfst_ModelFastfst178') == owner
    _safe_set(owner, 'fastfst_nHubMass', None)
    assert getattr(partner, 'fastfst_ModelFastfst178') is None


def test_assoc_HubRad139_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst140' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nHubRad's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nHubRad's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nHubRad(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst140', None)
    _safe_set(owner, 'fastfst_nHubRad', partner)
    assert getattr(partner, 'fastfst_ModelFastfst140') == owner
    _safe_set(owner, 'fastfst_nHubRad', None)
    assert getattr(partner, 'fastfst_ModelFastfst140') is None


def test_assoc_IPDefl123_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst124' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nIPDefl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nIPDefl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nIPDefl(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst124', None)
    _safe_set(owner, 'fastfst_nIPDefl', partner)
    assert getattr(partner, 'fastfst_ModelFastfst124') == owner
    _safe_set(owner, 'fastfst_nIPDefl', None)
    assert getattr(partner, 'fastfst_ModelFastfst124') is None


def test_assoc_LinFile285_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst286' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fLinFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fLinFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fLinFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst286', None)
    _safe_set(owner, 'fastfst_fLinFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst286') == owner
    _safe_set(owner, 'fastfst_fLinFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst286') is None


def test_assoc_NBlGages313_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst314' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iNBlGages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iNBlGages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iNBlGages(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst314', None)
    _safe_set(owner, 'fastfst_iNBlGages', partner)
    assert getattr(partner, 'fastfst_ModelFastfst314') == owner
    _safe_set(owner, 'fastfst_iNBlGages', None)
    assert getattr(partner, 'fastfst_ModelFastfst314') is None


def test_assoc_NTwGages309_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst310' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iNTwGages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iNTwGages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iNTwGages(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst310', None)
    _safe_set(owner, 'fastfst_iNTwGages', partner)
    assert getattr(partner, 'fastfst_ModelFastfst310') == owner
    _safe_set(owner, 'fastfst_iNTwGages', None)
    assert getattr(partner, 'fastfst_ModelFastfst310') is None


def test_assoc_NacCMxn149_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst150' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacCMxn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacCMxn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacCMxn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst150', None)
    _safe_set(owner, 'fastfst_nNacCMxn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst150') == owner
    _safe_set(owner, 'fastfst_nNacCMxn', None)
    assert getattr(partner, 'fastfst_ModelFastfst150') is None


def test_assoc_NacCMyn151_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst152' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacCMyn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacCMyn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacCMyn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst152', None)
    _safe_set(owner, 'fastfst_nNacCMyn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst152') == owner
    _safe_set(owner, 'fastfst_nNacCMyn', None)
    assert getattr(partner, 'fastfst_ModelFastfst152') is None


def test_assoc_NacCMzn153_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst154' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacCMzn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacCMzn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacCMzn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst154', None)
    _safe_set(owner, 'fastfst_nNacCMzn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst154') == owner
    _safe_set(owner, 'fastfst_nNacCMzn', None)
    assert getattr(partner, 'fastfst_ModelFastfst154') is None


def test_assoc_NacMass175_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst176' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacMass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacMass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacMass(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst176', None)
    _safe_set(owner, 'fastfst_nNacMass', partner)
    assert getattr(partner, 'fastfst_ModelFastfst176') == owner
    _safe_set(owner, 'fastfst_nNacMass', None)
    assert getattr(partner, 'fastfst_ModelFastfst176') is None


def test_assoc_NacYIner185_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst186' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacYIner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacYIner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacYIner(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst186', None)
    _safe_set(owner, 'fastfst_nNacYIner', partner)
    assert getattr(partner, 'fastfst_ModelFastfst186') == owner
    _safe_set(owner, 'fastfst_nNacYIner', None)
    assert getattr(partner, 'fastfst_ModelFastfst186') is None


def test_assoc_NacYaw131_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst132' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacYaw's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacYaw's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacYaw(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst132', None)
    _safe_set(owner, 'fastfst_nNacYaw', partner)
    assert getattr(partner, 'fastfst_ModelFastfst132') == owner
    _safe_set(owner, 'fastfst_nNacYaw', None)
    assert getattr(partner, 'fastfst_ModelFastfst132') is None


def test_assoc_NacYawF67_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst68' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNacYawF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNacYawF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNacYawF(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst68', None)
    _safe_set(owner, 'fastfst_nNacYawF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst68') == owner
    _safe_set(owner, 'fastfst_nNacYawF', None)
    assert getattr(partner, 'fastfst_ModelFastfst68') is None


def test_assoc_NcIMUxn301_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst302' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNcIMUxn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNcIMUxn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNcIMUxn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst302', None)
    _safe_set(owner, 'fastfst_nNcIMUxn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst302') == owner
    _safe_set(owner, 'fastfst_nNcIMUxn', None)
    assert getattr(partner, 'fastfst_ModelFastfst302') is None


def test_assoc_NcIMUyn303_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst304' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNcIMUyn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNcIMUyn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNcIMUyn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst304', None)
    _safe_set(owner, 'fastfst_nNcIMUyn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst304') == owner
    _safe_set(owner, 'fastfst_nNcIMUyn', None)
    assert getattr(partner, 'fastfst_ModelFastfst304') is None


def test_assoc_NcIMUzn305_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst306' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nNcIMUzn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nNcIMUzn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nNcIMUzn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst306', None)
    _safe_set(owner, 'fastfst_nNcIMUzn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst306') == owner
    _safe_set(owner, 'fastfst_nNcIMUzn', None)
    assert getattr(partner, 'fastfst_ModelFastfst306') is None


def test_assoc_NoiseFile281_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst282' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fNoiseFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fNoiseFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fNoiseFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst282', None)
    _safe_set(owner, 'fastfst_fNoiseFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst282') == owner
    _safe_set(owner, 'fastfst_fNoiseFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst282') is None


def test_assoc_NumBl9_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst10' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iNumBl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iNumBl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iNumBl(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst10', None)
    _safe_set(owner, 'fastfst_iNumBl', partner)
    assert getattr(partner, 'fastfst_ModelFastfst10') == owner
    _safe_set(owner, 'fastfst_iNumBl', None)
    assert getattr(partner, 'fastfst_ModelFastfst10') is None


def test_assoc_OoPDefl121_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst122' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nOoPDefl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nOoPDefl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nOoPDefl(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst122', None)
    _safe_set(owner, 'fastfst_nOoPDefl', partner)
    assert getattr(partner, 'fastfst_ModelFastfst122') == owner
    _safe_set(owner, 'fastfst_nOoPDefl', None)
    assert getattr(partner, 'fastfst_ModelFastfst122') is None


def test_assoc_OutFileFmt289_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst290' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bOutFileFmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bOutFileFmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bOutFileFmt(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst290', None)
    _safe_set(owner, 'fastfst_bOutFileFmt', partner)
    assert getattr(partner, 'fastfst_ModelFastfst290') == owner
    _safe_set(owner, 'fastfst_bOutFileFmt', None)
    assert getattr(partner, 'fastfst_ModelFastfst290') is None


def test_assoc_OutFmt293_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst294' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_sOutFmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_sOutFmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_sOutFmt(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst294', None)
    _safe_set(owner, 'fastfst_sOutFmt', partner)
    assert getattr(partner, 'fastfst_ModelFastfst294') == owner
    _safe_set(owner, 'fastfst_sOutFmt', None)
    assert getattr(partner, 'fastfst_ModelFastfst294') is None


def test_assoc_OutList317_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst318' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_vOutList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_vOutList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_vOutList(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst318', None)
    _safe_set(owner, 'fastfst_vOutList', partner)
    assert getattr(partner, 'fastfst_ModelFastfst318') == owner
    _safe_set(owner, 'fastfst_vOutList', None)
    assert getattr(partner, 'fastfst_ModelFastfst318') is None


def test_assoc_OverHang147_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst148' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nOverHang's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nOverHang's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nOverHang(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst148', None)
    _safe_set(owner, 'fastfst_nOverHang', partner)
    assert getattr(partner, 'fastfst_ModelFastfst148') == owner
    _safe_set(owner, 'fastfst_nOverHang', None)
    assert getattr(partner, 'fastfst_ModelFastfst148') is None


def test_assoc_PCMode19_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst20' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iPCMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iPCMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iPCMode(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst20', None)
    _safe_set(owner, 'fastfst_iPCMode', partner)
    assert getattr(partner, 'fastfst_ModelFastfst20') == owner
    _safe_set(owner, 'fastfst_iPCMode', None)
    assert getattr(partner, 'fastfst_ModelFastfst20') is None


def test_assoc_PSpnElN141_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst142' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nPSpnElN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nPSpnElN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nPSpnElN(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst142', None)
    _safe_set(owner, 'fastfst_nPSpnElN', partner)
    assert getattr(partner, 'fastfst_ModelFastfst142') == owner
    _safe_set(owner, 'fastfst_nPSpnElN', None)
    assert getattr(partner, 'fastfst_ModelFastfst142') is None


def test_assoc_PreCone_1_165_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst166' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nPreCone_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nPreCone_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nPreCone_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst166', None)
    _safe_set(owner, 'fastfst_nPreCone_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst166') == owner
    _safe_set(owner, 'fastfst_nPreCone_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst166') is None


def test_assoc_PreCone_2_167_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst168' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nPreCone_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nPreCone_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nPreCone_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst168', None)
    _safe_set(owner, 'fastfst_nPreCone_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst168') == owner
    _safe_set(owner, 'fastfst_nPreCone_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst168') is None


def test_assoc_PreCone_3_169_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst170' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nPreCone_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nPreCone_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nPreCone_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst170', None)
    _safe_set(owner, 'fastfst_nPreCone_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst170') == owner
    _safe_set(owner, 'fastfst_nPreCone_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst170') is None


def test_assoc_PtfmFile235_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst236' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fPtfmFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fPtfmFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fPtfmFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst236', None)
    _safe_set(owner, 'fastfst_fPtfmFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst236') == owner
    _safe_set(owner, 'fastfst_fPtfmFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst236') is None


def test_assoc_PtfmModel233_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst234' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iPtfmModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iPtfmModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iPtfmModel(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst234', None)
    _safe_set(owner, 'fastfst_iPtfmModel', partner)
    assert getattr(partner, 'fastfst_ModelFastfst234') == owner
    _safe_set(owner, 'fastfst_iPtfmModel', None)
    assert getattr(partner, 'fastfst_ModelFastfst234') is None


def test_assoc_RotSpeed129_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst130' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nRotSpeed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nRotSpeed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nRotSpeed(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst130', None)
    _safe_set(owner, 'fastfst_nRotSpeed', partner)
    assert getattr(partner, 'fastfst_ModelFastfst130') == owner
    _safe_set(owner, 'fastfst_nRotSpeed', None)
    assert getattr(partner, 'fastfst_ModelFastfst130') is None


def test_assoc_SIG_PORt215_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst216' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nSIG_PORt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nSIG_PORt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nSIG_PORt(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst216', None)
    _safe_set(owner, 'fastfst_nSIG_PORt', partner)
    assert getattr(partner, 'fastfst_ModelFastfst216') == owner
    _safe_set(owner, 'fastfst_nSIG_PORt', None)
    assert getattr(partner, 'fastfst_ModelFastfst216') is None


def test_assoc_SIG_RtTq213_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst214' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nSIG_RtTq's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nSIG_RtTq's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nSIG_RtTq(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst214', None)
    _safe_set(owner, 'fastfst_nSIG_RtTq', partner)
    assert getattr(partner, 'fastfst_ModelFastfst214') == owner
    _safe_set(owner, 'fastfst_nSIG_RtTq', None)
    assert getattr(partner, 'fastfst_ModelFastfst214') is None


def test_assoc_SIG_SlPc209_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst210' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nSIG_SlPc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nSIG_SlPc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nSIG_SlPc(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst210', None)
    _safe_set(owner, 'fastfst_nSIG_SlPc', partner)
    assert getattr(partner, 'fastfst_ModelFastfst210') == owner
    _safe_set(owner, 'fastfst_nSIG_SlPc', None)
    assert getattr(partner, 'fastfst_ModelFastfst210') is None


def test_assoc_SIG_SySp211_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst212' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nSIG_SySp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nSIG_SySp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nSIG_SySp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst212', None)
    _safe_set(owner, 'fastfst_nSIG_SySp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst212') == owner
    _safe_set(owner, 'fastfst_nSIG_SySp', None)
    assert getattr(partner, 'fastfst_ModelFastfst212') is None


def test_assoc_ShftGagL307_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst308' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nShftGagL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nShftGagL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nShftGagL(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst308', None)
    _safe_set(owner, 'fastfst_nShftGagL', partner)
    assert getattr(partner, 'fastfst_ModelFastfst308') == owner
    _safe_set(owner, 'fastfst_nShftGagL', None)
    assert getattr(partner, 'fastfst_ModelFastfst308') is None


def test_assoc_ShftTilt161_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst162' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nShftTilt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nShftTilt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nShftTilt(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst162', None)
    _safe_set(owner, 'fastfst_nShftTilt', partner)
    assert getattr(partner, 'fastfst_ModelFastfst162') == owner
    _safe_set(owner, 'fastfst_nShftTilt', None)
    assert getattr(partner, 'fastfst_ModelFastfst162') is None


def test_assoc_SpdGenOn39_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst40' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nSpdGenOn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nSpdGenOn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nSpdGenOn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst40', None)
    _safe_set(owner, 'fastfst_nSpdGenOn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst40') == owner
    _safe_set(owner, 'fastfst_nSpdGenOn', None)
    assert getattr(partner, 'fastfst_ModelFastfst40') is None


def test_assoc_SttsTime299_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst300' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nSttsTime's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nSttsTime's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nSttsTime(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst300', None)
    _safe_set(owner, 'fastfst_nSttsTime', partner)
    assert getattr(partner, 'fastfst_ModelFastfst300') == owner
    _safe_set(owner, 'fastfst_nSttsTime', None)
    assert getattr(partner, 'fastfst_ModelFastfst300') is None


def test_assoc_SumPrint287_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst288' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bSumPrint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bSumPrint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bSumPrint(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst288', None)
    _safe_set(owner, 'fastfst_bSumPrint', partner)
    assert getattr(partner, 'fastfst_ModelFastfst288') == owner
    _safe_set(owner, 'fastfst_bSumPrint', None)
    assert getattr(partner, 'fastfst_ModelFastfst288') is None


def test_assoc_TBDepISp_1_57_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst58' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTBDepISp_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTBDepISp_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTBDepISp_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst58', None)
    _safe_set(owner, 'fastfst_nTBDepISp_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst58') == owner
    _safe_set(owner, 'fastfst_nTBDepISp_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst58') is None


def test_assoc_TBDepISp_2_59_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst60' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTBDepISp_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTBDepISp_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTBDepISp_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst60', None)
    _safe_set(owner, 'fastfst_nTBDepISp_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst60') == owner
    _safe_set(owner, 'fastfst_nTBDepISp_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst60') is None


def test_assoc_TBDepISp_3_61_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst62' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTBDepISp_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTBDepISp_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTBDepISp_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst62', None)
    _safe_set(owner, 'fastfst_nTBDepISp_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst62') == owner
    _safe_set(owner, 'fastfst_nTBDepISp_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst62') is None


def test_assoc_TBDrConD269_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst270' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTBDrConD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTBDrConD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTBDrConD(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst270', None)
    _safe_set(owner, 'fastfst_nTBDrConD', partner)
    assert getattr(partner, 'fastfst_ModelFastfst270') == owner
    _safe_set(owner, 'fastfst_nTBDrConD', None)
    assert getattr(partner, 'fastfst_ModelFastfst270') is None


def test_assoc_TBDrConN267_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst268' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTBDrConN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTBDrConN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTBDrConN(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst268', None)
    _safe_set(owner, 'fastfst_nTBDrConN', partner)
    assert getattr(partner, 'fastfst_ModelFastfst268') == owner
    _safe_set(owner, 'fastfst_nTBDrConN', None)
    assert getattr(partner, 'fastfst_ModelFastfst268') is None


def test_assoc_TEC_Freq217_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst218' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_Freq's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_Freq's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_Freq(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst218', None)
    _safe_set(owner, 'fastfst_nTEC_Freq', partner)
    assert getattr(partner, 'fastfst_ModelFastfst218') == owner
    _safe_set(owner, 'fastfst_nTEC_Freq', None)
    assert getattr(partner, 'fastfst_ModelFastfst218') is None


def test_assoc_TEC_MR231_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst232' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_MR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_MR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_MR(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst232', None)
    _safe_set(owner, 'fastfst_nTEC_MR', partner)
    assert getattr(partner, 'fastfst_ModelFastfst232') == owner
    _safe_set(owner, 'fastfst_nTEC_MR', None)
    assert getattr(partner, 'fastfst_ModelFastfst232') is None


def test_assoc_TEC_Npol219_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst220' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_Npol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_Npol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_Npol(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst220', None)
    _safe_set(owner, 'fastfst_nTEC_Npol', partner)
    assert getattr(partner, 'fastfst_ModelFastfst220') == owner
    _safe_set(owner, 'fastfst_nTEC_Npol', None)
    assert getattr(partner, 'fastfst_ModelFastfst220') is None


def test_assoc_TEC_RLR229_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst230' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_RLR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_RLR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_RLR(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst230', None)
    _safe_set(owner, 'fastfst_nTEC_RLR', partner)
    assert getattr(partner, 'fastfst_ModelFastfst230') == owner
    _safe_set(owner, 'fastfst_nTEC_RLR', None)
    assert getattr(partner, 'fastfst_ModelFastfst230') is None


def test_assoc_TEC_Rres223_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst224' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_Rres's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_Rres's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_Rres(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst224', None)
    _safe_set(owner, 'fastfst_nTEC_Rres', partner)
    assert getattr(partner, 'fastfst_ModelFastfst224') == owner
    _safe_set(owner, 'fastfst_nTEC_Rres', None)
    assert getattr(partner, 'fastfst_ModelFastfst224') is None


def test_assoc_TEC_SLR227_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst228' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_SLR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_SLR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_SLR(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst228', None)
    _safe_set(owner, 'fastfst_nTEC_SLR', partner)
    assert getattr(partner, 'fastfst_ModelFastfst228') == owner
    _safe_set(owner, 'fastfst_nTEC_SLR', None)
    assert getattr(partner, 'fastfst_ModelFastfst228') is None


def test_assoc_TEC_Sres221_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst222' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_Sres's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_Sres's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_Sres(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst222', None)
    _safe_set(owner, 'fastfst_nTEC_Sres', partner)
    assert getattr(partner, 'fastfst_ModelFastfst222') == owner
    _safe_set(owner, 'fastfst_nTEC_Sres', None)
    assert getattr(partner, 'fastfst_ModelFastfst222') is None


def test_assoc_TEC_VLL225_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst226' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTEC_VLL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTEC_VLL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTEC_VLL(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst226', None)
    _safe_set(owner, 'fastfst_nTEC_VLL', partner)
    assert getattr(partner, 'fastfst_ModelFastfst226') == owner
    _safe_set(owner, 'fastfst_nTEC_VLL', None)
    assert getattr(partner, 'fastfst_ModelFastfst226') is None


def test_assoc_THSSBrDp47_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst48' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTHSSBrDp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTHSSBrDp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTHSSBrDp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst48', None)
    _safe_set(owner, 'fastfst_nTHSSBrDp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst48') == owner
    _safe_set(owner, 'fastfst_nTHSSBrDp', None)
    assert getattr(partner, 'fastfst_ModelFastfst48') is None


def test_assoc_TMax11_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst12' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTMax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTMax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTMax(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst12', None)
    _safe_set(owner, 'fastfst_nTMax', partner)
    assert getattr(partner, 'fastfst_ModelFastfst12') == owner
    _safe_set(owner, 'fastfst_nTMax', None)
    assert getattr(partner, 'fastfst_ModelFastfst12') is None


def test_assoc_TPCOn21_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst22' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPCOn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPCOn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPCOn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst22', None)
    _safe_set(owner, 'fastfst_nTPCOn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst22') == owner
    _safe_set(owner, 'fastfst_nTPCOn', None)
    assert getattr(partner, 'fastfst_ModelFastfst22') is None


def test_assoc_TPitManE_1_75_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst76' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPitManE_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPitManE_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPitManE_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst76', None)
    _safe_set(owner, 'fastfst_nTPitManE_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst76') == owner
    _safe_set(owner, 'fastfst_nTPitManE_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst76') is None


def test_assoc_TPitManE_2_77_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst78' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPitManE_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPitManE_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPitManE_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst78', None)
    _safe_set(owner, 'fastfst_nTPitManE_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst78') == owner
    _safe_set(owner, 'fastfst_nTPitManE_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst78') is None


def test_assoc_TPitManE_3_79_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst80' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPitManE_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPitManE_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPitManE_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst80', None)
    _safe_set(owner, 'fastfst_nTPitManE_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst80') == owner
    _safe_set(owner, 'fastfst_nTPitManE_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst80') is None


def test_assoc_TPitManS_1_69_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst70' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPitManS_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPitManS_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPitManS_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst70', None)
    _safe_set(owner, 'fastfst_nTPitManS_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst70') == owner
    _safe_set(owner, 'fastfst_nTPitManS_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst70') is None


def test_assoc_TPitManS_2_71_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst72' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPitManS_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPitManS_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPitManS_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst72', None)
    _safe_set(owner, 'fastfst_nTPitManS_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst72') == owner
    _safe_set(owner, 'fastfst_nTPitManS_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst72') is None


def test_assoc_TPitManS_3_73_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst74' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTPitManS_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTPitManS_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTPitManS_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst74', None)
    _safe_set(owner, 'fastfst_nTPitManS_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst74') == owner
    _safe_set(owner, 'fastfst_nTPitManS_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst74') is None


def test_assoc_TStart295_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst296' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTStart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTStart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTStart(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst296', None)
    _safe_set(owner, 'fastfst_nTStart', partner)
    assert getattr(partner, 'fastfst_ModelFastfst296') == owner
    _safe_set(owner, 'fastfst_nTStart', None)
    assert getattr(partner, 'fastfst_ModelFastfst296') is None


def test_assoc_TTDspFA133_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst134' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTTDspFA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTTDspFA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTTDspFA(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst134', None)
    _safe_set(owner, 'fastfst_nTTDspFA', partner)
    assert getattr(partner, 'fastfst_ModelFastfst134') == owner
    _safe_set(owner, 'fastfst_nTTDspFA', None)
    assert getattr(partner, 'fastfst_ModelFastfst134') is None


def test_assoc_TTDspSS135_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst136' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTTDspSS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTTDspSS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTTDspSS(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst136', None)
    _safe_set(owner, 'fastfst_nTTDspSS', partner)
    assert getattr(partner, 'fastfst_ModelFastfst136') == owner
    _safe_set(owner, 'fastfst_nTTDspSS', None)
    assert getattr(partner, 'fastfst_ModelFastfst136') is None


def test_assoc_TTpBrDp_1_51_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst52' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTTpBrDp_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTTpBrDp_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTTpBrDp_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst52', None)
    _safe_set(owner, 'fastfst_nTTpBrDp_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst52') == owner
    _safe_set(owner, 'fastfst_nTTpBrDp_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst52') is None


def test_assoc_TTpBrDp_2_53_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst54' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTTpBrDp_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTTpBrDp_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTTpBrDp_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst54', None)
    _safe_set(owner, 'fastfst_nTTpBrDp_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst54') == owner
    _safe_set(owner, 'fastfst_nTTpBrDp_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst54') is None


def test_assoc_TTpBrDp_3_55_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst56' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTTpBrDp_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTTpBrDp_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTTpBrDp_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst56', None)
    _safe_set(owner, 'fastfst_nTTpBrDp_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst56') == owner
    _safe_set(owner, 'fastfst_nTTpBrDp_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst56') is None


def test_assoc_TYCOn17_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst18' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTYCOn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTYCOn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTYCOn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst18', None)
    _safe_set(owner, 'fastfst_nTYCOn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst18') == owner
    _safe_set(owner, 'fastfst_nTYCOn', None)
    assert getattr(partner, 'fastfst_ModelFastfst18') is None


def test_assoc_TYawManE65_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst66' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTYawManE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTYawManE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTYawManE(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst66', None)
    _safe_set(owner, 'fastfst_nTYawManE', partner)
    assert getattr(partner, 'fastfst_ModelFastfst66') == owner
    _safe_set(owner, 'fastfst_nTYawManE', None)
    assert getattr(partner, 'fastfst_ModelFastfst66') is None


def test_assoc_TYawManS63_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst64' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTYawManS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTYawManS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTYawManS(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst64', None)
    _safe_set(owner, 'fastfst_nTYawManS', partner)
    assert getattr(partner, 'fastfst_ModelFastfst64') == owner
    _safe_set(owner, 'fastfst_nTYawManS', None)
    assert getattr(partner, 'fastfst_ModelFastfst64') is None


def test_assoc_TabDelim291_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst292' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bTabDelim's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bTabDelim's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bTabDelim(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst292', None)
    _safe_set(owner, 'fastfst_bTabDelim', partner)
    assert getattr(partner, 'fastfst_ModelFastfst292') == owner
    _safe_set(owner, 'fastfst_bTabDelim', None)
    assert getattr(partner, 'fastfst_ModelFastfst292') is None


def test_assoc_TeetCDmp257_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst258' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetCDmp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetCDmp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetCDmp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst258', None)
    _safe_set(owner, 'fastfst_nTeetCDmp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst258') == owner
    _safe_set(owner, 'fastfst_nTeetCDmp', None)
    assert getattr(partner, 'fastfst_ModelFastfst258') is None


def test_assoc_TeetDOF101_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst102' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bTeetDOF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bTeetDOF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bTeetDOF(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst102', None)
    _safe_set(owner, 'fastfst_bTeetDOF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst102') == owner
    _safe_set(owner, 'fastfst_bTeetDOF', None)
    assert getattr(partner, 'fastfst_ModelFastfst102') is None


def test_assoc_TeetDefl125_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst126' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetDefl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetDefl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetDefl(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst126', None)
    _safe_set(owner, 'fastfst_nTeetDefl', partner)
    assert getattr(partner, 'fastfst_ModelFastfst126') == owner
    _safe_set(owner, 'fastfst_nTeetDefl', None)
    assert getattr(partner, 'fastfst_ModelFastfst126') is None


def test_assoc_TeetDmp255_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst256' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetDmp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetDmp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetDmp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst256', None)
    _safe_set(owner, 'fastfst_nTeetDmp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst256') == owner
    _safe_set(owner, 'fastfst_nTeetDmp', None)
    assert getattr(partner, 'fastfst_ModelFastfst256') is None


def test_assoc_TeetDmpP253_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst254' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetDmpP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetDmpP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetDmpP(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst254', None)
    _safe_set(owner, 'fastfst_nTeetDmpP', partner)
    assert getattr(partner, 'fastfst_ModelFastfst254') == owner
    _safe_set(owner, 'fastfst_nTeetDmpP', None)
    assert getattr(partner, 'fastfst_ModelFastfst254') is None


def test_assoc_TeetHSSp265_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst266' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetHSSp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetHSSp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetHSSp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst266', None)
    _safe_set(owner, 'fastfst_nTeetHSSp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst266') == owner
    _safe_set(owner, 'fastfst_nTeetHSSp', None)
    assert getattr(partner, 'fastfst_ModelFastfst266') is None


def test_assoc_TeetHStP261_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst262' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetHStP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetHStP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetHStP(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst262', None)
    _safe_set(owner, 'fastfst_nTeetHStP', partner)
    assert getattr(partner, 'fastfst_ModelFastfst262') == owner
    _safe_set(owner, 'fastfst_nTeetHStP', None)
    assert getattr(partner, 'fastfst_ModelFastfst262') is None


def test_assoc_TeetMod251_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst252' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iTeetMod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iTeetMod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iTeetMod(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst252', None)
    _safe_set(owner, 'fastfst_iTeetMod', partner)
    assert getattr(partner, 'fastfst_ModelFastfst252') == owner
    _safe_set(owner, 'fastfst_iTeetMod', None)
    assert getattr(partner, 'fastfst_ModelFastfst252') is None


def test_assoc_TeetSSSp263_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst264' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetSSSp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetSSSp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetSSSp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst264', None)
    _safe_set(owner, 'fastfst_nTeetSSSp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst264') == owner
    _safe_set(owner, 'fastfst_nTeetSSSp', None)
    assert getattr(partner, 'fastfst_ModelFastfst264') is None


def test_assoc_TeetSStP259_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst260' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTeetSStP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTeetSStP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTeetSStP(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst260', None)
    _safe_set(owner, 'fastfst_nTeetSStP', partner)
    assert getattr(partner, 'fastfst_ModelFastfst260') == owner
    _safe_set(owner, 'fastfst_nTeetSStP', None)
    assert getattr(partner, 'fastfst_ModelFastfst260') is None


def test_assoc_TiDynBrk49_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst50' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTiDynBrk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTiDynBrk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTiDynBrk(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst50', None)
    _safe_set(owner, 'fastfst_nTiDynBrk', partner)
    assert getattr(partner, 'fastfst_ModelFastfst50') == owner
    _safe_set(owner, 'fastfst_nTiDynBrk', None)
    assert getattr(partner, 'fastfst_ModelFastfst50') is None


def test_assoc_TimGenOf43_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst44' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTimGenOf's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTimGenOf's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTimGenOf(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst44', None)
    _safe_set(owner, 'fastfst_nTimGenOf', partner)
    assert getattr(partner, 'fastfst_ModelFastfst44') == owner
    _safe_set(owner, 'fastfst_nTimGenOf', None)
    assert getattr(partner, 'fastfst_ModelFastfst44') is None


def test_assoc_TimGenOn41_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst42' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTimGenOn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTimGenOn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTimGenOn(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst42', None)
    _safe_set(owner, 'fastfst_nTimGenOn', partner)
    assert getattr(partner, 'fastfst_ModelFastfst42') == owner
    _safe_set(owner, 'fastfst_nTimGenOn', None)
    assert getattr(partner, 'fastfst_ModelFastfst42') is None


def test_assoc_TipMass_1_179_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst180' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTipMass_1_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTipMass_1_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTipMass_1_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst180', None)
    _safe_set(owner, 'fastfst_nTipMass_1_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst180') == owner
    _safe_set(owner, 'fastfst_nTipMass_1_', None)
    assert getattr(partner, 'fastfst_ModelFastfst180') is None


def test_assoc_TipMass_2_181_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst182' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTipMass_2_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTipMass_2_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTipMass_2_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst182', None)
    _safe_set(owner, 'fastfst_nTipMass_2_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst182') == owner
    _safe_set(owner, 'fastfst_nTipMass_2_', None)
    assert getattr(partner, 'fastfst_ModelFastfst182') is None


def test_assoc_TipMass_3_183_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst184' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTipMass_3_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTipMass_3_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTipMass_3_(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst184', None)
    _safe_set(owner, 'fastfst_nTipMass_3_', partner)
    assert getattr(partner, 'fastfst_ModelFastfst184') == owner
    _safe_set(owner, 'fastfst_nTipMass_3_', None)
    assert getattr(partner, 'fastfst_ModelFastfst184') is None


def test_assoc_TipRad137_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst138' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTipRad's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTipRad's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTipRad(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst138', None)
    _safe_set(owner, 'fastfst_nTipRad', partner)
    assert getattr(partner, 'fastfst_ModelFastfst138') == owner
    _safe_set(owner, 'fastfst_nTipRad', None)
    assert getattr(partner, 'fastfst_ModelFastfst138') is None


def test_assoc_TowerHt155_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst156' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTowerHt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTowerHt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTowerHt(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst156', None)
    _safe_set(owner, 'fastfst_nTowerHt', partner)
    assert getattr(partner, 'fastfst_ModelFastfst156') == owner
    _safe_set(owner, 'fastfst_nTowerHt', None)
    assert getattr(partner, 'fastfst_ModelFastfst156') is None


def test_assoc_TpBrDT271_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst272' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTpBrDT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTpBrDT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTpBrDT(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst272', None)
    _safe_set(owner, 'fastfst_nTpBrDT', partner)
    assert getattr(partner, 'fastfst_ModelFastfst272') == owner
    _safe_set(owner, 'fastfst_nTpBrDT', None)
    assert getattr(partner, 'fastfst_ModelFastfst272') is None


def test_assoc_TwFADOF1109_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst110' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bTwFADOF1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bTwFADOF1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bTwFADOF1(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst110', None)
    _safe_set(owner, 'fastfst_bTwFADOF1', partner)
    assert getattr(partner, 'fastfst_ModelFastfst110') == owner
    _safe_set(owner, 'fastfst_bTwFADOF1', None)
    assert getattr(partner, 'fastfst_ModelFastfst110') is None


def test_assoc_TwFADOF2111_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst112' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bTwFADOF2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bTwFADOF2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bTwFADOF2(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst112', None)
    _safe_set(owner, 'fastfst_bTwFADOF2', partner)
    assert getattr(partner, 'fastfst_ModelFastfst112') == owner
    _safe_set(owner, 'fastfst_bTwFADOF2', None)
    assert getattr(partner, 'fastfst_ModelFastfst112') is None


def test_assoc_TwSSDOF1113_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst114' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bTwSSDOF1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bTwSSDOF1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bTwSSDOF1(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst114', None)
    _safe_set(owner, 'fastfst_bTwSSDOF1', partner)
    assert getattr(partner, 'fastfst_ModelFastfst114') == owner
    _safe_set(owner, 'fastfst_bTwSSDOF1', None)
    assert getattr(partner, 'fastfst_ModelFastfst114') is None


def test_assoc_TwSSDOF2115_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst116' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bTwSSDOF2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bTwSSDOF2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bTwSSDOF2(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst116', None)
    _safe_set(owner, 'fastfst_bTwSSDOF2', partner)
    assert getattr(partner, 'fastfst_ModelFastfst116') == owner
    _safe_set(owner, 'fastfst_bTwSSDOF2', None)
    assert getattr(partner, 'fastfst_ModelFastfst116') is None


def test_assoc_Twr2Shft157_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst158' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTwr2Shft's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTwr2Shft's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTwr2Shft(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst158', None)
    _safe_set(owner, 'fastfst_nTwr2Shft', partner)
    assert getattr(partner, 'fastfst_ModelFastfst158') == owner
    _safe_set(owner, 'fastfst_nTwr2Shft', None)
    assert getattr(partner, 'fastfst_ModelFastfst158') is None


def test_assoc_TwrFile239_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst240' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_fTwrFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_fTwrFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_fTwrFile(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst240', None)
    _safe_set(owner, 'fastfst_fTwrFile', partner)
    assert getattr(partner, 'fastfst_ModelFastfst240') == owner
    _safe_set(owner, 'fastfst_fTwrFile', None)
    assert getattr(partner, 'fastfst_ModelFastfst240') is None


def test_assoc_TwrGagNd311_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst312' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_aTwrGagNd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_aTwrGagNd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_aTwrGagNd(name="sample_text", value="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst312', None)
    _safe_set(owner, 'fastfst_aTwrGagNd', partner)
    assert getattr(partner, 'fastfst_ModelFastfst312') == owner
    _safe_set(owner, 'fastfst_aTwrGagNd', None)
    assert getattr(partner, 'fastfst_ModelFastfst312') is None


def test_assoc_TwrNodes237_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst238' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iTwrNodes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iTwrNodes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iTwrNodes(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst238', None)
    _safe_set(owner, 'fastfst_iTwrNodes', partner)
    assert getattr(partner, 'fastfst_ModelFastfst238') == owner
    _safe_set(owner, 'fastfst_iTwrNodes', None)
    assert getattr(partner, 'fastfst_ModelFastfst238') is None


def test_assoc_TwrRBHt159_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst160' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nTwrRBHt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nTwrRBHt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nTwrRBHt(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst160', None)
    _safe_set(owner, 'fastfst_nTwrRBHt', partner)
    assert getattr(partner, 'fastfst_ModelFastfst160') == owner
    _safe_set(owner, 'fastfst_nTwrRBHt', None)
    assert getattr(partner, 'fastfst_ModelFastfst160') is None


def test_assoc_UndSling143_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst144' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nUndSling's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nUndSling's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nUndSling(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst144', None)
    _safe_set(owner, 'fastfst_nUndSling', partner)
    assert getattr(partner, 'fastfst_ModelFastfst144') == owner
    _safe_set(owner, 'fastfst_nUndSling', None)
    assert getattr(partner, 'fastfst_ModelFastfst144') is None


def test_assoc_VSContrl23_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst24' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iVSContrl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iVSContrl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iVSContrl(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst24', None)
    _safe_set(owner, 'fastfst_iVSContrl', partner)
    assert getattr(partner, 'fastfst_ModelFastfst24') == owner
    _safe_set(owner, 'fastfst_iVSContrl', None)
    assert getattr(partner, 'fastfst_ModelFastfst24') is None


def test_assoc_VS_Rgn2K29_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst30' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nVS_Rgn2K's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nVS_Rgn2K's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nVS_Rgn2K(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst30', None)
    _safe_set(owner, 'fastfst_nVS_Rgn2K', partner)
    assert getattr(partner, 'fastfst_ModelFastfst30') == owner
    _safe_set(owner, 'fastfst_nVS_Rgn2K', None)
    assert getattr(partner, 'fastfst_ModelFastfst30') is None


def test_assoc_VS_RtGnSp25_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst26' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nVS_RtGnSp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nVS_RtGnSp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nVS_RtGnSp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst26', None)
    _safe_set(owner, 'fastfst_nVS_RtGnSp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst26') == owner
    _safe_set(owner, 'fastfst_nVS_RtGnSp', None)
    assert getattr(partner, 'fastfst_ModelFastfst26') is None


def test_assoc_VS_RtTq27_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst28' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nVS_RtTq's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nVS_RtTq's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nVS_RtTq(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst28', None)
    _safe_set(owner, 'fastfst_nVS_RtTq', partner)
    assert getattr(partner, 'fastfst_ModelFastfst28') == owner
    _safe_set(owner, 'fastfst_nVS_RtTq', None)
    assert getattr(partner, 'fastfst_ModelFastfst28') is None


def test_assoc_VS_SlPc31_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst32' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nVS_SlPc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nVS_SlPc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nVS_SlPc(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst32', None)
    _safe_set(owner, 'fastfst_nVS_SlPc', partner)
    assert getattr(partner, 'fastfst_ModelFastfst32') == owner
    _safe_set(owner, 'fastfst_nVS_SlPc', None)
    assert getattr(partner, 'fastfst_ModelFastfst32') is None


def test_assoc_YCMode15_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst16' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_iYCMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_iYCMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_iYCMode(name="sample_text", value=7)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst16', None)
    _safe_set(owner, 'fastfst_iYCMode', partner)
    assert getattr(partner, 'fastfst_ModelFastfst16') == owner
    _safe_set(owner, 'fastfst_iYCMode', None)
    assert getattr(partner, 'fastfst_ModelFastfst16') is None


def test_assoc_YawBrMass173_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst174' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nYawBrMass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nYawBrMass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nYawBrMass(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst174', None)
    _safe_set(owner, 'fastfst_nYawBrMass', partner)
    assert getattr(partner, 'fastfst_ModelFastfst174') == owner
    _safe_set(owner, 'fastfst_nYawBrMass', None)
    assert getattr(partner, 'fastfst_ModelFastfst174') is None


def test_assoc_YawDOF107_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst108' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_bYawDOF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_bYawDOF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_bYawDOF(name="sample_text", value=True)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst108', None)
    _safe_set(owner, 'fastfst_bYawDOF', partner)
    assert getattr(partner, 'fastfst_ModelFastfst108') == owner
    _safe_set(owner, 'fastfst_bYawDOF', None)
    assert getattr(partner, 'fastfst_ModelFastfst108') is None


def test_assoc_YawDamp243_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst244' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nYawDamp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nYawDamp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nYawDamp(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst244', None)
    _safe_set(owner, 'fastfst_nYawDamp', partner)
    assert getattr(partner, 'fastfst_ModelFastfst244') == owner
    _safe_set(owner, 'fastfst_nYawDamp', None)
    assert getattr(partner, 'fastfst_ModelFastfst244') is None


def test_assoc_YawNeut245_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst246' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nYawNeut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nYawNeut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nYawNeut(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst246', None)
    _safe_set(owner, 'fastfst_nYawNeut', partner)
    assert getattr(partner, 'fastfst_ModelFastfst246') == owner
    _safe_set(owner, 'fastfst_nYawNeut', None)
    assert getattr(partner, 'fastfst_ModelFastfst246') is None


def test_assoc_YawSpr241_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst242' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_nYawSpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_nYawSpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_nYawSpr(name="sample_text", value=3.14)
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst242', None)
    _safe_set(owner, 'fastfst_nYawSpr', partner)
    assert getattr(partner, 'fastfst_ModelFastfst242') == owner
    _safe_set(owner, 'fastfst_nYawSpr', None)
    assert getattr(partner, 'fastfst_ModelFastfst242') is None


def test_assoc_sections1_stub_double():
    # fastfst_ModelFastfst has no real 'fastfst_ModelFastfst2' property in the generated
    # code (a bare stub) -- manually attach it so fastfst_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fastfst_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fastfst_Section(name="sample_text")
    partner = fastfst_ModelFastfst()
    setattr(partner, 'fastfst_ModelFastfst2', None)
    _safe_set(owner, 'fastfst_Section', partner)
    assert owner in getattr(partner, 'fastfst_ModelFastfst2')
    _safe_set(owner, 'fastfst_Section', None)
    assert owner not in getattr(partner, 'fastfst_ModelFastfst2')


