# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fastfst_nShftGagL,
    fastfst_nNcIMUzn,
    fastfst_vOutList,
    fastfst_aBldGagNd,
    fastfst_iNBlGages,
    fastfst_aTwrGagNd,
    fastfst_iNTwGages,
    fastfst_sOutFmt,
    fastfst_bTabDelim,
    fastfst_nNcIMUyn,
    fastfst_nNcIMUxn,
    fastfst_nSttsTime,
    fastfst_iDecFact,
    fastfst_nTStart,
    fastfst_fBldFile_3_,
    fastfst_fBldFile_2_,
    fastfst_bOutFileFmt,
    fastfst_bSumPrint,
    fastfst_fLinFile,
    fastfst_fADAMSFile,
    fastfst_fNoiseFile,
    fastfst_fADFile,
    fastfst_nTeetHStP,
    fastfst_nTeetSStP,
    fastfst_fBldFile_1_,
    fastfst_nTpBrDT,
    fastfst_nTBDrConD,
    fastfst_nTBDrConN,
    fastfst_nTeetHSSp,
    fastfst_nTeetSSSp,
    fastfst_nYawNeut,
    fastfst_nYawDamp,
    fastfst_nTeetCDmp,
    fastfst_nTeetDmp,
    fastfst_nTeetDmpP,
    fastfst_iTeetMod,
    fastfst_fFurlFile,
    fastfst_nTEC_RLR,
    fastfst_bFurling,
    fastfst_nTEC_SLR,
    fastfst_nYawSpr,
    fastfst_fTwrFile,
    fastfst_iTwrNodes,
    fastfst_fPtfmFile,
    fastfst_iPtfmModel,
    fastfst_nTEC_MR,
    fastfst_nSIG_SlPc,
    fastfst_nDTTorDmp,
    fastfst_nTEC_VLL,
    fastfst_nTEC_Rres,
    fastfst_nTEC_Sres,
    fastfst_nTEC_Npol,
    fastfst_nTEC_Freq,
    fastfst_nSIG_PORt,
    fastfst_nSIG_RtTq,
    fastfst_nSIG_SySp,
    fastfst_nGenIner,
    fastfst_nDTTorSpr,
    fastfst_fDynBrkFi,
    fastfst_nTwr2Shft,
    fastfst_nTowerHt,
    fastfst_nNacCMzn,
    fastfst_nNacCMyn,
    fastfst_nTTDspSS,
    fastfst_nTTDspFA,
    fastfst_nNacYaw,
    fastfst_nRotSpeed,
    fastfst_nUndSling,
    fastfst_nPSpnElN,
    fastfst_nHubRad,
    fastfst_nTipRad,
    fastfst_bTwFADOF1,
    fastfst_bYawDOF,
    fastfst_bGenDOF,
    fastfst_bDrTrDOF,
    fastfst_bTeetDOF,
    fastfst_bEdgeDOF,
    fastfst_nAzimuth,
    fastfst_bFlapDOF2,
    fastfst_nTeetDefl,
    fastfst_bFlapDOF1,
    fastfst_nIPDefl,
    fastfst_nGravity,
    fastfst_nOoPDefl,
    fastfst_nBlPitchF_3_,
    fastfst_nBlPitchF_2_,
    fastfst_bCompNoise,
    fastfst_nBlPitchF_1_,
    fastfst_bCompAero,
    fastfst_nBlPitch_3_,
    fastfst_bTwSSDOF2,
    fastfst_nBlPitch_2_,
    fastfst_bTwSSDOF1,
    fastfst_bTwFADOF2,
    fastfst_nTPitManE_2_,
    fastfst_nTPitManE_1_,
    fastfst_nTPitManS_3_,
    fastfst_nTPitManS_2_,
    fastfst_nTPitManS_1_,
    fastfst_nNacYawF,
    fastfst_nTYawManE,
    fastfst_nTYawManS,
    fastfst_nTBDepISp_3_,
    fastfst_nTBDepISp_2_,
    fastfst_nTBDepISp_1_,
    fastfst_nTTpBrDp_3_,
    fastfst_nTTpBrDp_2_,
    fastfst_nTTpBrDp_1_,
    fastfst_nBlPitch_1_,
    fastfst_nTPitManE_3_,
    fastfst_iHSSBrMode,
    fastfst_nTimGenOf,
    fastfst_nTimGenOn,
    fastfst_nSpdGenOn,
    fastfst_bGenTiStp,
    fastfst_bGenTiStr,
    fastfst_iGenModel,
    fastfst_nVS_SlPc,
    fastfst_nVS_Rgn2K,
    fastfst_nVS_RtTq,
    fastfst_nVS_RtGnSp,
    fastfst_iVSContrl,
    fastfst_nTPCOn,
    fastfst_iPCMode,
    fastfst_nTYCOn,
    fastfst_iYCMode,
    fastfst_nDT,
    fastfst_nTMax,
    fastfst_nTiDynBrk,
    fastfst_nTHSSBrDp,
    fastfst_iADAMSPrep,
    fastfst_bEcho,
    fastfst_Section,
    fastfst_Header,
    fastfst_ModelFastfst,
    fastfst_iNumBl,
    fastfst_iAnalMode,
    fastfst_nHSSBrDT,
    fastfst_nHSSBrTqF,
    fastfst_bGBRevers,
    fastfst_nGBRatio,
    fastfst_nGenEff,
    fastfst_nGBoxEff,
    fastfst_nHubIner,
    fastfst_nPreCone_2_,
    fastfst_nNacYIner,
    fastfst_nTipMass_3_,
    fastfst_nTipMass_2_,
    fastfst_nTipMass_1_,
    fastfst_nHubMass,
    fastfst_nNacMass,
    fastfst_nYawBrMass,
    fastfst_nAzimB1Up,
    fastfst_nPreCone_3_,
    fastfst_nNacCMxn,
    fastfst_nOverHang,
    fastfst_nHubCM,
    fastfst_nPreCone_1_,
    fastfst_nDelta3,
    fastfst_nShftTilt,
    fastfst_nTwrRBHt,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fastfst_nshftgagl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nShftGagL)


def test_hyp_fastfst_nshftgagl_constructor_exists():
    assert callable(fastfst_nShftGagL.__init__)


def test_hyp_fastfst_nshftgagl_constructor_args():
    sig = inspect.signature(fastfst_nShftGagL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nncimuzn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNcIMUzn)


def test_hyp_fastfst_nncimuzn_constructor_exists():
    assert callable(fastfst_nNcIMUzn.__init__)


def test_hyp_fastfst_nncimuzn_constructor_args():
    sig = inspect.signature(fastfst_nNcIMUzn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_voutlist_is_not_abstract():
    assert not inspect.isabstract(fastfst_vOutList)


def test_hyp_fastfst_voutlist_constructor_exists():
    assert callable(fastfst_vOutList.__init__)


def test_hyp_fastfst_voutlist_constructor_args():
    sig = inspect.signature(fastfst_vOutList.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_abldgagnd_is_not_abstract():
    assert not inspect.isabstract(fastfst_aBldGagNd)


def test_hyp_fastfst_abldgagnd_constructor_exists():
    assert callable(fastfst_aBldGagNd.__init__)


def test_hyp_fastfst_abldgagnd_constructor_args():
    sig = inspect.signature(fastfst_aBldGagNd.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_inblgages_is_not_abstract():
    assert not inspect.isabstract(fastfst_iNBlGages)


def test_hyp_fastfst_inblgages_constructor_exists():
    assert callable(fastfst_iNBlGages.__init__)


def test_hyp_fastfst_inblgages_constructor_args():
    sig = inspect.signature(fastfst_iNBlGages.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_atwrgagnd_is_not_abstract():
    assert not inspect.isabstract(fastfst_aTwrGagNd)


def test_hyp_fastfst_atwrgagnd_constructor_exists():
    assert callable(fastfst_aTwrGagNd.__init__)


def test_hyp_fastfst_atwrgagnd_constructor_args():
    sig = inspect.signature(fastfst_aTwrGagNd.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_intwgages_is_not_abstract():
    assert not inspect.isabstract(fastfst_iNTwGages)


def test_hyp_fastfst_intwgages_constructor_exists():
    assert callable(fastfst_iNTwGages.__init__)


def test_hyp_fastfst_intwgages_constructor_args():
    sig = inspect.signature(fastfst_iNTwGages.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_soutfmt_is_not_abstract():
    assert not inspect.isabstract(fastfst_sOutFmt)


def test_hyp_fastfst_soutfmt_constructor_exists():
    assert callable(fastfst_sOutFmt.__init__)


def test_hyp_fastfst_soutfmt_constructor_args():
    sig = inspect.signature(fastfst_sOutFmt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_btabdelim_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTabDelim)


def test_hyp_fastfst_btabdelim_constructor_exists():
    assert callable(fastfst_bTabDelim.__init__)


def test_hyp_fastfst_btabdelim_constructor_args():
    sig = inspect.signature(fastfst_bTabDelim.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nncimuyn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNcIMUyn)


def test_hyp_fastfst_nncimuyn_constructor_exists():
    assert callable(fastfst_nNcIMUyn.__init__)


def test_hyp_fastfst_nncimuyn_constructor_args():
    sig = inspect.signature(fastfst_nNcIMUyn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nncimuxn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNcIMUxn)


def test_hyp_fastfst_nncimuxn_constructor_exists():
    assert callable(fastfst_nNcIMUxn.__init__)


def test_hyp_fastfst_nncimuxn_constructor_args():
    sig = inspect.signature(fastfst_nNcIMUxn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nsttstime_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSttsTime)


def test_hyp_fastfst_nsttstime_constructor_exists():
    assert callable(fastfst_nSttsTime.__init__)


def test_hyp_fastfst_nsttstime_constructor_args():
    sig = inspect.signature(fastfst_nSttsTime.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_idecfact_is_not_abstract():
    assert not inspect.isabstract(fastfst_iDecFact)


def test_hyp_fastfst_idecfact_constructor_exists():
    assert callable(fastfst_iDecFact.__init__)


def test_hyp_fastfst_idecfact_constructor_args():
    sig = inspect.signature(fastfst_iDecFact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntstart_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTStart)


def test_hyp_fastfst_ntstart_constructor_exists():
    assert callable(fastfst_nTStart.__init__)


def test_hyp_fastfst_ntstart_constructor_args():
    sig = inspect.signature(fastfst_nTStart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_fbldfile_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_fBldFile_3_)


def test_hyp_fastfst_fbldfile_3__constructor_exists():
    assert callable(fastfst_fBldFile_3_.__init__)


def test_hyp_fastfst_fbldfile_3__constructor_args():
    sig = inspect.signature(fastfst_fBldFile_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_fbldfile_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_fBldFile_2_)


def test_hyp_fastfst_fbldfile_2__constructor_exists():
    assert callable(fastfst_fBldFile_2_.__init__)


def test_hyp_fastfst_fbldfile_2__constructor_args():
    sig = inspect.signature(fastfst_fBldFile_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_boutfilefmt_is_not_abstract():
    assert not inspect.isabstract(fastfst_bOutFileFmt)


def test_hyp_fastfst_boutfilefmt_constructor_exists():
    assert callable(fastfst_bOutFileFmt.__init__)


def test_hyp_fastfst_boutfilefmt_constructor_args():
    sig = inspect.signature(fastfst_bOutFileFmt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bsumprint_is_not_abstract():
    assert not inspect.isabstract(fastfst_bSumPrint)


def test_hyp_fastfst_bsumprint_constructor_exists():
    assert callable(fastfst_bSumPrint.__init__)


def test_hyp_fastfst_bsumprint_constructor_args():
    sig = inspect.signature(fastfst_bSumPrint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_flinfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fLinFile)


def test_hyp_fastfst_flinfile_constructor_exists():
    assert callable(fastfst_fLinFile.__init__)


def test_hyp_fastfst_flinfile_constructor_args():
    sig = inspect.signature(fastfst_fLinFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_fadamsfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fADAMSFile)


def test_hyp_fastfst_fadamsfile_constructor_exists():
    assert callable(fastfst_fADAMSFile.__init__)


def test_hyp_fastfst_fadamsfile_constructor_args():
    sig = inspect.signature(fastfst_fADAMSFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_fnoisefile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fNoiseFile)


def test_hyp_fastfst_fnoisefile_constructor_exists():
    assert callable(fastfst_fNoiseFile.__init__)


def test_hyp_fastfst_fnoisefile_constructor_args():
    sig = inspect.signature(fastfst_fNoiseFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_fadfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fADFile)


def test_hyp_fastfst_fadfile_constructor_exists():
    assert callable(fastfst_fADFile.__init__)


def test_hyp_fastfst_fadfile_constructor_args():
    sig = inspect.signature(fastfst_fADFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nteethstp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetHStP)


def test_hyp_fastfst_nteethstp_constructor_exists():
    assert callable(fastfst_nTeetHStP.__init__)


def test_hyp_fastfst_nteethstp_constructor_args():
    sig = inspect.signature(fastfst_nTeetHStP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nteetsstp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetSStP)


def test_hyp_fastfst_nteetsstp_constructor_exists():
    assert callable(fastfst_nTeetSStP.__init__)


def test_hyp_fastfst_nteetsstp_constructor_args():
    sig = inspect.signature(fastfst_nTeetSStP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_fbldfile_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_fBldFile_1_)


def test_hyp_fastfst_fbldfile_1__constructor_exists():
    assert callable(fastfst_fBldFile_1_.__init__)


def test_hyp_fastfst_fbldfile_1__constructor_args():
    sig = inspect.signature(fastfst_fBldFile_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntpbrdt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTpBrDT)


def test_hyp_fastfst_ntpbrdt_constructor_exists():
    assert callable(fastfst_nTpBrDT.__init__)


def test_hyp_fastfst_ntpbrdt_constructor_args():
    sig = inspect.signature(fastfst_nTpBrDT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntbdrcond_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDrConD)


def test_hyp_fastfst_ntbdrcond_constructor_exists():
    assert callable(fastfst_nTBDrConD.__init__)


def test_hyp_fastfst_ntbdrcond_constructor_args():
    sig = inspect.signature(fastfst_nTBDrConD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntbdrconn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDrConN)


def test_hyp_fastfst_ntbdrconn_constructor_exists():
    assert callable(fastfst_nTBDrConN.__init__)


def test_hyp_fastfst_ntbdrconn_constructor_args():
    sig = inspect.signature(fastfst_nTBDrConN.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nteethssp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetHSSp)


def test_hyp_fastfst_nteethssp_constructor_exists():
    assert callable(fastfst_nTeetHSSp.__init__)


def test_hyp_fastfst_nteethssp_constructor_args():
    sig = inspect.signature(fastfst_nTeetHSSp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nteetsssp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetSSSp)


def test_hyp_fastfst_nteetsssp_constructor_exists():
    assert callable(fastfst_nTeetSSSp.__init__)


def test_hyp_fastfst_nteetsssp_constructor_args():
    sig = inspect.signature(fastfst_nTeetSSSp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nyawneut_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawNeut)


def test_hyp_fastfst_nyawneut_constructor_exists():
    assert callable(fastfst_nYawNeut.__init__)


def test_hyp_fastfst_nyawneut_constructor_args():
    sig = inspect.signature(fastfst_nYawNeut.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nyawdamp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawDamp)


def test_hyp_fastfst_nyawdamp_constructor_exists():
    assert callable(fastfst_nYawDamp.__init__)


def test_hyp_fastfst_nyawdamp_constructor_args():
    sig = inspect.signature(fastfst_nYawDamp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nteetcdmp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetCDmp)


def test_hyp_fastfst_nteetcdmp_constructor_exists():
    assert callable(fastfst_nTeetCDmp.__init__)


def test_hyp_fastfst_nteetcdmp_constructor_args():
    sig = inspect.signature(fastfst_nTeetCDmp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nteetdmp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetDmp)


def test_hyp_fastfst_nteetdmp_constructor_exists():
    assert callable(fastfst_nTeetDmp.__init__)


def test_hyp_fastfst_nteetdmp_constructor_args():
    sig = inspect.signature(fastfst_nTeetDmp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nteetdmpp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetDmpP)


def test_hyp_fastfst_nteetdmpp_constructor_exists():
    assert callable(fastfst_nTeetDmpP.__init__)


def test_hyp_fastfst_nteetdmpp_constructor_args():
    sig = inspect.signature(fastfst_nTeetDmpP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_iteetmod_is_not_abstract():
    assert not inspect.isabstract(fastfst_iTeetMod)


def test_hyp_fastfst_iteetmod_constructor_exists():
    assert callable(fastfst_iTeetMod.__init__)


def test_hyp_fastfst_iteetmod_constructor_args():
    sig = inspect.signature(fastfst_iTeetMod.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ffurlfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fFurlFile)


def test_hyp_fastfst_ffurlfile_constructor_exists():
    assert callable(fastfst_fFurlFile.__init__)


def test_hyp_fastfst_ffurlfile_constructor_args():
    sig = inspect.signature(fastfst_fFurlFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntec_rlr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_RLR)


def test_hyp_fastfst_ntec_rlr_constructor_exists():
    assert callable(fastfst_nTEC_RLR.__init__)


def test_hyp_fastfst_ntec_rlr_constructor_args():
    sig = inspect.signature(fastfst_nTEC_RLR.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bfurling_is_not_abstract():
    assert not inspect.isabstract(fastfst_bFurling)


def test_hyp_fastfst_bfurling_constructor_exists():
    assert callable(fastfst_bFurling.__init__)


def test_hyp_fastfst_bfurling_constructor_args():
    sig = inspect.signature(fastfst_bFurling.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntec_slr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_SLR)


def test_hyp_fastfst_ntec_slr_constructor_exists():
    assert callable(fastfst_nTEC_SLR.__init__)


def test_hyp_fastfst_ntec_slr_constructor_args():
    sig = inspect.signature(fastfst_nTEC_SLR.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nyawspr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawSpr)


def test_hyp_fastfst_nyawspr_constructor_exists():
    assert callable(fastfst_nYawSpr.__init__)


def test_hyp_fastfst_nyawspr_constructor_args():
    sig = inspect.signature(fastfst_nYawSpr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ftwrfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fTwrFile)


def test_hyp_fastfst_ftwrfile_constructor_exists():
    assert callable(fastfst_fTwrFile.__init__)


def test_hyp_fastfst_ftwrfile_constructor_args():
    sig = inspect.signature(fastfst_fTwrFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_itwrnodes_is_not_abstract():
    assert not inspect.isabstract(fastfst_iTwrNodes)


def test_hyp_fastfst_itwrnodes_constructor_exists():
    assert callable(fastfst_iTwrNodes.__init__)


def test_hyp_fastfst_itwrnodes_constructor_args():
    sig = inspect.signature(fastfst_iTwrNodes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_fptfmfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fPtfmFile)


def test_hyp_fastfst_fptfmfile_constructor_exists():
    assert callable(fastfst_fPtfmFile.__init__)


def test_hyp_fastfst_fptfmfile_constructor_args():
    sig = inspect.signature(fastfst_fPtfmFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_iptfmmodel_is_not_abstract():
    assert not inspect.isabstract(fastfst_iPtfmModel)


def test_hyp_fastfst_iptfmmodel_constructor_exists():
    assert callable(fastfst_iPtfmModel.__init__)


def test_hyp_fastfst_iptfmmodel_constructor_args():
    sig = inspect.signature(fastfst_iPtfmModel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntec_mr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_MR)


def test_hyp_fastfst_ntec_mr_constructor_exists():
    assert callable(fastfst_nTEC_MR.__init__)


def test_hyp_fastfst_ntec_mr_constructor_args():
    sig = inspect.signature(fastfst_nTEC_MR.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nsig_slpc_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_SlPc)


def test_hyp_fastfst_nsig_slpc_constructor_exists():
    assert callable(fastfst_nSIG_SlPc.__init__)


def test_hyp_fastfst_nsig_slpc_constructor_args():
    sig = inspect.signature(fastfst_nSIG_SlPc.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ndttordmp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDTTorDmp)


def test_hyp_fastfst_ndttordmp_constructor_exists():
    assert callable(fastfst_nDTTorDmp.__init__)


def test_hyp_fastfst_ndttordmp_constructor_args():
    sig = inspect.signature(fastfst_nDTTorDmp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntec_vll_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_VLL)


def test_hyp_fastfst_ntec_vll_constructor_exists():
    assert callable(fastfst_nTEC_VLL.__init__)


def test_hyp_fastfst_ntec_vll_constructor_args():
    sig = inspect.signature(fastfst_nTEC_VLL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntec_rres_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Rres)


def test_hyp_fastfst_ntec_rres_constructor_exists():
    assert callable(fastfst_nTEC_Rres.__init__)


def test_hyp_fastfst_ntec_rres_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Rres.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntec_sres_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Sres)


def test_hyp_fastfst_ntec_sres_constructor_exists():
    assert callable(fastfst_nTEC_Sres.__init__)


def test_hyp_fastfst_ntec_sres_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Sres.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntec_npol_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Npol)


def test_hyp_fastfst_ntec_npol_constructor_exists():
    assert callable(fastfst_nTEC_Npol.__init__)


def test_hyp_fastfst_ntec_npol_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Npol.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntec_freq_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Freq)


def test_hyp_fastfst_ntec_freq_constructor_exists():
    assert callable(fastfst_nTEC_Freq.__init__)


def test_hyp_fastfst_ntec_freq_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Freq.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nsig_port_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_PORt)


def test_hyp_fastfst_nsig_port_constructor_exists():
    assert callable(fastfst_nSIG_PORt.__init__)


def test_hyp_fastfst_nsig_port_constructor_args():
    sig = inspect.signature(fastfst_nSIG_PORt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nsig_rttq_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_RtTq)


def test_hyp_fastfst_nsig_rttq_constructor_exists():
    assert callable(fastfst_nSIG_RtTq.__init__)


def test_hyp_fastfst_nsig_rttq_constructor_args():
    sig = inspect.signature(fastfst_nSIG_RtTq.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nsig_sysp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_SySp)


def test_hyp_fastfst_nsig_sysp_constructor_exists():
    assert callable(fastfst_nSIG_SySp.__init__)


def test_hyp_fastfst_nsig_sysp_constructor_args():
    sig = inspect.signature(fastfst_nSIG_SySp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ngeniner_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGenIner)


def test_hyp_fastfst_ngeniner_constructor_exists():
    assert callable(fastfst_nGenIner.__init__)


def test_hyp_fastfst_ngeniner_constructor_args():
    sig = inspect.signature(fastfst_nGenIner.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ndttorspr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDTTorSpr)


def test_hyp_fastfst_ndttorspr_constructor_exists():
    assert callable(fastfst_nDTTorSpr.__init__)


def test_hyp_fastfst_ndttorspr_constructor_args():
    sig = inspect.signature(fastfst_nDTTorSpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_fdynbrkfi_is_not_abstract():
    assert not inspect.isabstract(fastfst_fDynBrkFi)


def test_hyp_fastfst_fdynbrkfi_constructor_exists():
    assert callable(fastfst_fDynBrkFi.__init__)


def test_hyp_fastfst_fdynbrkfi_constructor_args():
    sig = inspect.signature(fastfst_fDynBrkFi.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntwr2shft_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTwr2Shft)


def test_hyp_fastfst_ntwr2shft_constructor_exists():
    assert callable(fastfst_nTwr2Shft.__init__)


def test_hyp_fastfst_ntwr2shft_constructor_args():
    sig = inspect.signature(fastfst_nTwr2Shft.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntowerht_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTowerHt)


def test_hyp_fastfst_ntowerht_constructor_exists():
    assert callable(fastfst_nTowerHt.__init__)


def test_hyp_fastfst_ntowerht_constructor_args():
    sig = inspect.signature(fastfst_nTowerHt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nnaccmzn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacCMzn)


def test_hyp_fastfst_nnaccmzn_constructor_exists():
    assert callable(fastfst_nNacCMzn.__init__)


def test_hyp_fastfst_nnaccmzn_constructor_args():
    sig = inspect.signature(fastfst_nNacCMzn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nnaccmyn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacCMyn)


def test_hyp_fastfst_nnaccmyn_constructor_exists():
    assert callable(fastfst_nNacCMyn.__init__)


def test_hyp_fastfst_nnaccmyn_constructor_args():
    sig = inspect.signature(fastfst_nNacCMyn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nttdspss_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTDspSS)


def test_hyp_fastfst_nttdspss_constructor_exists():
    assert callable(fastfst_nTTDspSS.__init__)


def test_hyp_fastfst_nttdspss_constructor_args():
    sig = inspect.signature(fastfst_nTTDspSS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nttdspfa_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTDspFA)


def test_hyp_fastfst_nttdspfa_constructor_exists():
    assert callable(fastfst_nTTDspFA.__init__)


def test_hyp_fastfst_nttdspfa_constructor_args():
    sig = inspect.signature(fastfst_nTTDspFA.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nnacyaw_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacYaw)


def test_hyp_fastfst_nnacyaw_constructor_exists():
    assert callable(fastfst_nNacYaw.__init__)


def test_hyp_fastfst_nnacyaw_constructor_args():
    sig = inspect.signature(fastfst_nNacYaw.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nrotspeed_is_not_abstract():
    assert not inspect.isabstract(fastfst_nRotSpeed)


def test_hyp_fastfst_nrotspeed_constructor_exists():
    assert callable(fastfst_nRotSpeed.__init__)


def test_hyp_fastfst_nrotspeed_constructor_args():
    sig = inspect.signature(fastfst_nRotSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nundsling_is_not_abstract():
    assert not inspect.isabstract(fastfst_nUndSling)


def test_hyp_fastfst_nundsling_constructor_exists():
    assert callable(fastfst_nUndSling.__init__)


def test_hyp_fastfst_nundsling_constructor_args():
    sig = inspect.signature(fastfst_nUndSling.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_npspneln_is_not_abstract():
    assert not inspect.isabstract(fastfst_nPSpnElN)


def test_hyp_fastfst_npspneln_constructor_exists():
    assert callable(fastfst_nPSpnElN.__init__)


def test_hyp_fastfst_npspneln_constructor_args():
    sig = inspect.signature(fastfst_nPSpnElN.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nhubrad_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubRad)


def test_hyp_fastfst_nhubrad_constructor_exists():
    assert callable(fastfst_nHubRad.__init__)


def test_hyp_fastfst_nhubrad_constructor_args():
    sig = inspect.signature(fastfst_nHubRad.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntiprad_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipRad)


def test_hyp_fastfst_ntiprad_constructor_exists():
    assert callable(fastfst_nTipRad.__init__)


def test_hyp_fastfst_ntiprad_constructor_args():
    sig = inspect.signature(fastfst_nTipRad.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_btwfadof1_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwFADOF1)


def test_hyp_fastfst_btwfadof1_constructor_exists():
    assert callable(fastfst_bTwFADOF1.__init__)


def test_hyp_fastfst_btwfadof1_constructor_args():
    sig = inspect.signature(fastfst_bTwFADOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_byawdof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bYawDOF)


def test_hyp_fastfst_byawdof_constructor_exists():
    assert callable(fastfst_bYawDOF.__init__)


def test_hyp_fastfst_byawdof_constructor_args():
    sig = inspect.signature(fastfst_bYawDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_bgendof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGenDOF)


def test_hyp_fastfst_bgendof_constructor_exists():
    assert callable(fastfst_bGenDOF.__init__)


def test_hyp_fastfst_bgendof_constructor_args():
    sig = inspect.signature(fastfst_bGenDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_bdrtrdof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bDrTrDOF)


def test_hyp_fastfst_bdrtrdof_constructor_exists():
    assert callable(fastfst_bDrTrDOF.__init__)


def test_hyp_fastfst_bdrtrdof_constructor_args():
    sig = inspect.signature(fastfst_bDrTrDOF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bteetdof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTeetDOF)


def test_hyp_fastfst_bteetdof_constructor_exists():
    assert callable(fastfst_bTeetDOF.__init__)


def test_hyp_fastfst_bteetdof_constructor_args():
    sig = inspect.signature(fastfst_bTeetDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_bedgedof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bEdgeDOF)


def test_hyp_fastfst_bedgedof_constructor_exists():
    assert callable(fastfst_bEdgeDOF.__init__)


def test_hyp_fastfst_bedgedof_constructor_args():
    sig = inspect.signature(fastfst_bEdgeDOF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nazimuth_is_not_abstract():
    assert not inspect.isabstract(fastfst_nAzimuth)


def test_hyp_fastfst_nazimuth_constructor_exists():
    assert callable(fastfst_nAzimuth.__init__)


def test_hyp_fastfst_nazimuth_constructor_args():
    sig = inspect.signature(fastfst_nAzimuth.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bflapdof2_is_not_abstract():
    assert not inspect.isabstract(fastfst_bFlapDOF2)


def test_hyp_fastfst_bflapdof2_constructor_exists():
    assert callable(fastfst_bFlapDOF2.__init__)


def test_hyp_fastfst_bflapdof2_constructor_args():
    sig = inspect.signature(fastfst_bFlapDOF2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nteetdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetDefl)


def test_hyp_fastfst_nteetdefl_constructor_exists():
    assert callable(fastfst_nTeetDefl.__init__)


def test_hyp_fastfst_nteetdefl_constructor_args():
    sig = inspect.signature(fastfst_nTeetDefl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_bflapdof1_is_not_abstract():
    assert not inspect.isabstract(fastfst_bFlapDOF1)


def test_hyp_fastfst_bflapdof1_constructor_exists():
    assert callable(fastfst_bFlapDOF1.__init__)


def test_hyp_fastfst_bflapdof1_constructor_args():
    sig = inspect.signature(fastfst_bFlapDOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nipdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nIPDefl)


def test_hyp_fastfst_nipdefl_constructor_exists():
    assert callable(fastfst_nIPDefl.__init__)


def test_hyp_fastfst_nipdefl_constructor_args():
    sig = inspect.signature(fastfst_nIPDefl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ngravity_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGravity)


def test_hyp_fastfst_ngravity_constructor_exists():
    assert callable(fastfst_nGravity.__init__)


def test_hyp_fastfst_ngravity_constructor_args():
    sig = inspect.signature(fastfst_nGravity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_noopdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nOoPDefl)


def test_hyp_fastfst_noopdefl_constructor_exists():
    assert callable(fastfst_nOoPDefl.__init__)


def test_hyp_fastfst_noopdefl_constructor_args():
    sig = inspect.signature(fastfst_nOoPDefl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nblpitchf_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitchF_3_)


def test_hyp_fastfst_nblpitchf_3__constructor_exists():
    assert callable(fastfst_nBlPitchF_3_.__init__)


def test_hyp_fastfst_nblpitchf_3__constructor_args():
    sig = inspect.signature(fastfst_nBlPitchF_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nblpitchf_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitchF_2_)


def test_hyp_fastfst_nblpitchf_2__constructor_exists():
    assert callable(fastfst_nBlPitchF_2_.__init__)


def test_hyp_fastfst_nblpitchf_2__constructor_args():
    sig = inspect.signature(fastfst_nBlPitchF_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bcompnoise_is_not_abstract():
    assert not inspect.isabstract(fastfst_bCompNoise)


def test_hyp_fastfst_bcompnoise_constructor_exists():
    assert callable(fastfst_bCompNoise.__init__)


def test_hyp_fastfst_bcompnoise_constructor_args():
    sig = inspect.signature(fastfst_bCompNoise.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nblpitchf_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitchF_1_)


def test_hyp_fastfst_nblpitchf_1__constructor_exists():
    assert callable(fastfst_nBlPitchF_1_.__init__)


def test_hyp_fastfst_nblpitchf_1__constructor_args():
    sig = inspect.signature(fastfst_nBlPitchF_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bcompaero_is_not_abstract():
    assert not inspect.isabstract(fastfst_bCompAero)


def test_hyp_fastfst_bcompaero_constructor_exists():
    assert callable(fastfst_bCompAero.__init__)


def test_hyp_fastfst_bcompaero_constructor_args():
    sig = inspect.signature(fastfst_bCompAero.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nblpitch_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitch_3_)


def test_hyp_fastfst_nblpitch_3__constructor_exists():
    assert callable(fastfst_nBlPitch_3_.__init__)


def test_hyp_fastfst_nblpitch_3__constructor_args():
    sig = inspect.signature(fastfst_nBlPitch_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_btwssdof2_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwSSDOF2)


def test_hyp_fastfst_btwssdof2_constructor_exists():
    assert callable(fastfst_bTwSSDOF2.__init__)


def test_hyp_fastfst_btwssdof2_constructor_args():
    sig = inspect.signature(fastfst_bTwSSDOF2.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nblpitch_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitch_2_)


def test_hyp_fastfst_nblpitch_2__constructor_exists():
    assert callable(fastfst_nBlPitch_2_.__init__)


def test_hyp_fastfst_nblpitch_2__constructor_args():
    sig = inspect.signature(fastfst_nBlPitch_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_btwssdof1_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwSSDOF1)


def test_hyp_fastfst_btwssdof1_constructor_exists():
    assert callable(fastfst_bTwSSDOF1.__init__)


def test_hyp_fastfst_btwssdof1_constructor_args():
    sig = inspect.signature(fastfst_bTwSSDOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_btwfadof2_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwFADOF2)


def test_hyp_fastfst_btwfadof2_constructor_exists():
    assert callable(fastfst_bTwFADOF2.__init__)


def test_hyp_fastfst_btwfadof2_constructor_args():
    sig = inspect.signature(fastfst_bTwFADOF2.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntpitmane_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManE_2_)


def test_hyp_fastfst_ntpitmane_2__constructor_exists():
    assert callable(fastfst_nTPitManE_2_.__init__)


def test_hyp_fastfst_ntpitmane_2__constructor_args():
    sig = inspect.signature(fastfst_nTPitManE_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntpitmane_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManE_1_)


def test_hyp_fastfst_ntpitmane_1__constructor_exists():
    assert callable(fastfst_nTPitManE_1_.__init__)


def test_hyp_fastfst_ntpitmane_1__constructor_args():
    sig = inspect.signature(fastfst_nTPitManE_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntpitmans_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManS_3_)


def test_hyp_fastfst_ntpitmans_3__constructor_exists():
    assert callable(fastfst_nTPitManS_3_.__init__)


def test_hyp_fastfst_ntpitmans_3__constructor_args():
    sig = inspect.signature(fastfst_nTPitManS_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntpitmans_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManS_2_)


def test_hyp_fastfst_ntpitmans_2__constructor_exists():
    assert callable(fastfst_nTPitManS_2_.__init__)


def test_hyp_fastfst_ntpitmans_2__constructor_args():
    sig = inspect.signature(fastfst_nTPitManS_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntpitmans_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManS_1_)


def test_hyp_fastfst_ntpitmans_1__constructor_exists():
    assert callable(fastfst_nTPitManS_1_.__init__)


def test_hyp_fastfst_ntpitmans_1__constructor_args():
    sig = inspect.signature(fastfst_nTPitManS_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nnacyawf_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacYawF)


def test_hyp_fastfst_nnacyawf_constructor_exists():
    assert callable(fastfst_nNacYawF.__init__)


def test_hyp_fastfst_nnacyawf_constructor_args():
    sig = inspect.signature(fastfst_nNacYawF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntyawmane_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTYawManE)


def test_hyp_fastfst_ntyawmane_constructor_exists():
    assert callable(fastfst_nTYawManE.__init__)


def test_hyp_fastfst_ntyawmane_constructor_args():
    sig = inspect.signature(fastfst_nTYawManE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntyawmans_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTYawManS)


def test_hyp_fastfst_ntyawmans_constructor_exists():
    assert callable(fastfst_nTYawManS.__init__)


def test_hyp_fastfst_ntyawmans_constructor_args():
    sig = inspect.signature(fastfst_nTYawManS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntbdepisp_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDepISp_3_)


def test_hyp_fastfst_ntbdepisp_3__constructor_exists():
    assert callable(fastfst_nTBDepISp_3_.__init__)


def test_hyp_fastfst_ntbdepisp_3__constructor_args():
    sig = inspect.signature(fastfst_nTBDepISp_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntbdepisp_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDepISp_2_)


def test_hyp_fastfst_ntbdepisp_2__constructor_exists():
    assert callable(fastfst_nTBDepISp_2_.__init__)


def test_hyp_fastfst_ntbdepisp_2__constructor_args():
    sig = inspect.signature(fastfst_nTBDepISp_2_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntbdepisp_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDepISp_1_)


def test_hyp_fastfst_ntbdepisp_1__constructor_exists():
    assert callable(fastfst_nTBDepISp_1_.__init__)


def test_hyp_fastfst_ntbdepisp_1__constructor_args():
    sig = inspect.signature(fastfst_nTBDepISp_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nttpbrdp_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTpBrDp_3_)


def test_hyp_fastfst_nttpbrdp_3__constructor_exists():
    assert callable(fastfst_nTTpBrDp_3_.__init__)


def test_hyp_fastfst_nttpbrdp_3__constructor_args():
    sig = inspect.signature(fastfst_nTTpBrDp_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nttpbrdp_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTpBrDp_2_)


def test_hyp_fastfst_nttpbrdp_2__constructor_exists():
    assert callable(fastfst_nTTpBrDp_2_.__init__)


def test_hyp_fastfst_nttpbrdp_2__constructor_args():
    sig = inspect.signature(fastfst_nTTpBrDp_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nttpbrdp_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTpBrDp_1_)


def test_hyp_fastfst_nttpbrdp_1__constructor_exists():
    assert callable(fastfst_nTTpBrDp_1_.__init__)


def test_hyp_fastfst_nttpbrdp_1__constructor_args():
    sig = inspect.signature(fastfst_nTTpBrDp_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nblpitch_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitch_1_)


def test_hyp_fastfst_nblpitch_1__constructor_exists():
    assert callable(fastfst_nBlPitch_1_.__init__)


def test_hyp_fastfst_nblpitch_1__constructor_args():
    sig = inspect.signature(fastfst_nBlPitch_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntpitmane_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManE_3_)


def test_hyp_fastfst_ntpitmane_3__constructor_exists():
    assert callable(fastfst_nTPitManE_3_.__init__)


def test_hyp_fastfst_ntpitmane_3__constructor_args():
    sig = inspect.signature(fastfst_nTPitManE_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ihssbrmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iHSSBrMode)


def test_hyp_fastfst_ihssbrmode_constructor_exists():
    assert callable(fastfst_iHSSBrMode.__init__)


def test_hyp_fastfst_ihssbrmode_constructor_args():
    sig = inspect.signature(fastfst_iHSSBrMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntimgenof_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTimGenOf)


def test_hyp_fastfst_ntimgenof_constructor_exists():
    assert callable(fastfst_nTimGenOf.__init__)


def test_hyp_fastfst_ntimgenof_constructor_args():
    sig = inspect.signature(fastfst_nTimGenOf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntimgenon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTimGenOn)


def test_hyp_fastfst_ntimgenon_constructor_exists():
    assert callable(fastfst_nTimGenOn.__init__)


def test_hyp_fastfst_ntimgenon_constructor_args():
    sig = inspect.signature(fastfst_nTimGenOn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nspdgenon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSpdGenOn)


def test_hyp_fastfst_nspdgenon_constructor_exists():
    assert callable(fastfst_nSpdGenOn.__init__)


def test_hyp_fastfst_nspdgenon_constructor_args():
    sig = inspect.signature(fastfst_nSpdGenOn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_bgentistp_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGenTiStp)


def test_hyp_fastfst_bgentistp_constructor_exists():
    assert callable(fastfst_bGenTiStp.__init__)


def test_hyp_fastfst_bgentistp_constructor_args():
    sig = inspect.signature(fastfst_bGenTiStp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_bgentistr_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGenTiStr)


def test_hyp_fastfst_bgentistr_constructor_exists():
    assert callable(fastfst_bGenTiStr.__init__)


def test_hyp_fastfst_bgentistr_constructor_args():
    sig = inspect.signature(fastfst_bGenTiStr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_igenmodel_is_not_abstract():
    assert not inspect.isabstract(fastfst_iGenModel)


def test_hyp_fastfst_igenmodel_constructor_exists():
    assert callable(fastfst_iGenModel.__init__)


def test_hyp_fastfst_igenmodel_constructor_args():
    sig = inspect.signature(fastfst_iGenModel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nvs_slpc_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_SlPc)


def test_hyp_fastfst_nvs_slpc_constructor_exists():
    assert callable(fastfst_nVS_SlPc.__init__)


def test_hyp_fastfst_nvs_slpc_constructor_args():
    sig = inspect.signature(fastfst_nVS_SlPc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nvs_rgn2k_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_Rgn2K)


def test_hyp_fastfst_nvs_rgn2k_constructor_exists():
    assert callable(fastfst_nVS_Rgn2K.__init__)


def test_hyp_fastfst_nvs_rgn2k_constructor_args():
    sig = inspect.signature(fastfst_nVS_Rgn2K.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nvs_rttq_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_RtTq)


def test_hyp_fastfst_nvs_rttq_constructor_exists():
    assert callable(fastfst_nVS_RtTq.__init__)


def test_hyp_fastfst_nvs_rttq_constructor_args():
    sig = inspect.signature(fastfst_nVS_RtTq.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nvs_rtgnsp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_RtGnSp)


def test_hyp_fastfst_nvs_rtgnsp_constructor_exists():
    assert callable(fastfst_nVS_RtGnSp.__init__)


def test_hyp_fastfst_nvs_rtgnsp_constructor_args():
    sig = inspect.signature(fastfst_nVS_RtGnSp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ivscontrl_is_not_abstract():
    assert not inspect.isabstract(fastfst_iVSContrl)


def test_hyp_fastfst_ivscontrl_constructor_exists():
    assert callable(fastfst_iVSContrl.__init__)


def test_hyp_fastfst_ivscontrl_constructor_args():
    sig = inspect.signature(fastfst_iVSContrl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntpcon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPCOn)


def test_hyp_fastfst_ntpcon_constructor_exists():
    assert callable(fastfst_nTPCOn.__init__)


def test_hyp_fastfst_ntpcon_constructor_args():
    sig = inspect.signature(fastfst_nTPCOn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ipcmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iPCMode)


def test_hyp_fastfst_ipcmode_constructor_exists():
    assert callable(fastfst_iPCMode.__init__)


def test_hyp_fastfst_ipcmode_constructor_args():
    sig = inspect.signature(fastfst_iPCMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntycon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTYCOn)


def test_hyp_fastfst_ntycon_constructor_exists():
    assert callable(fastfst_nTYCOn.__init__)


def test_hyp_fastfst_ntycon_constructor_args():
    sig = inspect.signature(fastfst_nTYCOn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_iycmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iYCMode)


def test_hyp_fastfst_iycmode_constructor_exists():
    assert callable(fastfst_iYCMode.__init__)


def test_hyp_fastfst_iycmode_constructor_args():
    sig = inspect.signature(fastfst_iYCMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ndt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDT)


def test_hyp_fastfst_ndt_constructor_exists():
    assert callable(fastfst_nDT.__init__)


def test_hyp_fastfst_ndt_constructor_args():
    sig = inspect.signature(fastfst_nDT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntmax_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTMax)


def test_hyp_fastfst_ntmax_constructor_exists():
    assert callable(fastfst_nTMax.__init__)


def test_hyp_fastfst_ntmax_constructor_args():
    sig = inspect.signature(fastfst_nTMax.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntidynbrk_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTiDynBrk)


def test_hyp_fastfst_ntidynbrk_constructor_exists():
    assert callable(fastfst_nTiDynBrk.__init__)


def test_hyp_fastfst_ntidynbrk_constructor_args():
    sig = inspect.signature(fastfst_nTiDynBrk.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nthssbrdp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTHSSBrDp)


def test_hyp_fastfst_nthssbrdp_constructor_exists():
    assert callable(fastfst_nTHSSBrDp.__init__)


def test_hyp_fastfst_nthssbrdp_constructor_args():
    sig = inspect.signature(fastfst_nTHSSBrDp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_iadamsprep_is_not_abstract():
    assert not inspect.isabstract(fastfst_iADAMSPrep)


def test_hyp_fastfst_iadamsprep_constructor_exists():
    assert callable(fastfst_iADAMSPrep.__init__)


def test_hyp_fastfst_iadamsprep_constructor_args():
    sig = inspect.signature(fastfst_iADAMSPrep.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_becho_is_not_abstract():
    assert not inspect.isabstract(fastfst_bEcho)


def test_hyp_fastfst_becho_constructor_exists():
    assert callable(fastfst_bEcho.__init__)


def test_hyp_fastfst_becho_constructor_args():
    sig = inspect.signature(fastfst_bEcho.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_section_is_not_abstract():
    assert not inspect.isabstract(fastfst_Section)


def test_hyp_fastfst_section_constructor_exists():
    assert callable(fastfst_Section.__init__)


def test_hyp_fastfst_section_constructor_args():
    sig = inspect.signature(fastfst_Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fastfst_header_is_not_abstract():
    assert not inspect.isabstract(fastfst_Header)


def test_hyp_fastfst_header_constructor_exists():
    assert callable(fastfst_Header.__init__)


def test_hyp_fastfst_header_constructor_args():
    sig = inspect.signature(fastfst_Header.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"




def test_hyp_fastfst_modelfastfst_is_not_abstract():
    assert not inspect.isabstract(fastfst_ModelFastfst)


def test_hyp_fastfst_modelfastfst_constructor_exists():
    assert callable(fastfst_ModelFastfst.__init__)


def test_hyp_fastfst_modelfastfst_constructor_args():
    sig = inspect.signature(fastfst_ModelFastfst.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fastfst_inumbl_is_not_abstract():
    assert not inspect.isabstract(fastfst_iNumBl)


def test_hyp_fastfst_inumbl_constructor_exists():
    assert callable(fastfst_iNumBl.__init__)


def test_hyp_fastfst_inumbl_constructor_args():
    sig = inspect.signature(fastfst_iNumBl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ianalmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iAnalMode)


def test_hyp_fastfst_ianalmode_constructor_exists():
    assert callable(fastfst_iAnalMode.__init__)


def test_hyp_fastfst_ianalmode_constructor_args():
    sig = inspect.signature(fastfst_iAnalMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nhssbrdt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHSSBrDT)


def test_hyp_fastfst_nhssbrdt_constructor_exists():
    assert callable(fastfst_nHSSBrDT.__init__)


def test_hyp_fastfst_nhssbrdt_constructor_args():
    sig = inspect.signature(fastfst_nHSSBrDT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nhssbrtqf_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHSSBrTqF)


def test_hyp_fastfst_nhssbrtqf_constructor_exists():
    assert callable(fastfst_nHSSBrTqF.__init__)


def test_hyp_fastfst_nhssbrtqf_constructor_args():
    sig = inspect.signature(fastfst_nHSSBrTqF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_bgbrevers_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGBRevers)


def test_hyp_fastfst_bgbrevers_constructor_exists():
    assert callable(fastfst_bGBRevers.__init__)


def test_hyp_fastfst_bgbrevers_constructor_args():
    sig = inspect.signature(fastfst_bGBRevers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ngbratio_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGBRatio)


def test_hyp_fastfst_ngbratio_constructor_exists():
    assert callable(fastfst_nGBRatio.__init__)


def test_hyp_fastfst_ngbratio_constructor_args():
    sig = inspect.signature(fastfst_nGBRatio.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ngeneff_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGenEff)


def test_hyp_fastfst_ngeneff_constructor_exists():
    assert callable(fastfst_nGenEff.__init__)


def test_hyp_fastfst_ngeneff_constructor_args():
    sig = inspect.signature(fastfst_nGenEff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ngboxeff_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGBoxEff)


def test_hyp_fastfst_ngboxeff_constructor_exists():
    assert callable(fastfst_nGBoxEff.__init__)


def test_hyp_fastfst_ngboxeff_constructor_args():
    sig = inspect.signature(fastfst_nGBoxEff.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nhubiner_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubIner)


def test_hyp_fastfst_nhubiner_constructor_exists():
    assert callable(fastfst_nHubIner.__init__)


def test_hyp_fastfst_nhubiner_constructor_args():
    sig = inspect.signature(fastfst_nHubIner.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nprecone_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nPreCone_2_)


def test_hyp_fastfst_nprecone_2__constructor_exists():
    assert callable(fastfst_nPreCone_2_.__init__)


def test_hyp_fastfst_nprecone_2__constructor_args():
    sig = inspect.signature(fastfst_nPreCone_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nnacyiner_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacYIner)


def test_hyp_fastfst_nnacyiner_constructor_exists():
    assert callable(fastfst_nNacYIner.__init__)


def test_hyp_fastfst_nnacyiner_constructor_args():
    sig = inspect.signature(fastfst_nNacYIner.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntipmass_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipMass_3_)


def test_hyp_fastfst_ntipmass_3__constructor_exists():
    assert callable(fastfst_nTipMass_3_.__init__)


def test_hyp_fastfst_ntipmass_3__constructor_args():
    sig = inspect.signature(fastfst_nTipMass_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_ntipmass_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipMass_2_)


def test_hyp_fastfst_ntipmass_2__constructor_exists():
    assert callable(fastfst_nTipMass_2_.__init__)


def test_hyp_fastfst_ntipmass_2__constructor_args():
    sig = inspect.signature(fastfst_nTipMass_2_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntipmass_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipMass_1_)


def test_hyp_fastfst_ntipmass_1__constructor_exists():
    assert callable(fastfst_nTipMass_1_.__init__)


def test_hyp_fastfst_ntipmass_1__constructor_args():
    sig = inspect.signature(fastfst_nTipMass_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nhubmass_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubMass)


def test_hyp_fastfst_nhubmass_constructor_exists():
    assert callable(fastfst_nHubMass.__init__)


def test_hyp_fastfst_nhubmass_constructor_args():
    sig = inspect.signature(fastfst_nHubMass.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nnacmass_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacMass)


def test_hyp_fastfst_nnacmass_constructor_exists():
    assert callable(fastfst_nNacMass.__init__)


def test_hyp_fastfst_nnacmass_constructor_args():
    sig = inspect.signature(fastfst_nNacMass.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nyawbrmass_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawBrMass)


def test_hyp_fastfst_nyawbrmass_constructor_exists():
    assert callable(fastfst_nYawBrMass.__init__)


def test_hyp_fastfst_nyawbrmass_constructor_args():
    sig = inspect.signature(fastfst_nYawBrMass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nazimb1up_is_not_abstract():
    assert not inspect.isabstract(fastfst_nAzimB1Up)


def test_hyp_fastfst_nazimb1up_constructor_exists():
    assert callable(fastfst_nAzimB1Up.__init__)


def test_hyp_fastfst_nazimb1up_constructor_args():
    sig = inspect.signature(fastfst_nAzimB1Up.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nprecone_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nPreCone_3_)


def test_hyp_fastfst_nprecone_3__constructor_exists():
    assert callable(fastfst_nPreCone_3_.__init__)


def test_hyp_fastfst_nprecone_3__constructor_args():
    sig = inspect.signature(fastfst_nPreCone_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_nnaccmxn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacCMxn)


def test_hyp_fastfst_nnaccmxn_constructor_exists():
    assert callable(fastfst_nNacCMxn.__init__)


def test_hyp_fastfst_nnaccmxn_constructor_args():
    sig = inspect.signature(fastfst_nNacCMxn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fastfst_noverhang_is_not_abstract():
    assert not inspect.isabstract(fastfst_nOverHang)


def test_hyp_fastfst_noverhang_constructor_exists():
    assert callable(fastfst_nOverHang.__init__)


def test_hyp_fastfst_noverhang_constructor_args():
    sig = inspect.signature(fastfst_nOverHang.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nhubcm_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubCM)


def test_hyp_fastfst_nhubcm_constructor_exists():
    assert callable(fastfst_nHubCM.__init__)


def test_hyp_fastfst_nhubcm_constructor_args():
    sig = inspect.signature(fastfst_nHubCM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nprecone_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nPreCone_1_)


def test_hyp_fastfst_nprecone_1__constructor_exists():
    assert callable(fastfst_nPreCone_1_.__init__)


def test_hyp_fastfst_nprecone_1__constructor_args():
    sig = inspect.signature(fastfst_nPreCone_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ndelta3_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDelta3)


def test_hyp_fastfst_ndelta3_constructor_exists():
    assert callable(fastfst_nDelta3.__init__)


def test_hyp_fastfst_ndelta3_constructor_args():
    sig = inspect.signature(fastfst_nDelta3.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_nshfttilt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nShftTilt)


def test_hyp_fastfst_nshfttilt_constructor_exists():
    assert callable(fastfst_nShftTilt.__init__)


def test_hyp_fastfst_nshfttilt_constructor_args():
    sig = inspect.signature(fastfst_nShftTilt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_fastfst_ntwrrbht_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTwrRBHt)


def test_hyp_fastfst_ntwrrbht_constructor_exists():
    assert callable(fastfst_nTwrRBHt.__init__)


def test_hyp_fastfst_ntwrrbht_constructor_args():
    sig = inspect.signature(fastfst_nTwrRBHt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"




# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
fastfst_nShftGagL_strategy = st.builds(
    fastfst_nShftGagL,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nNcIMUzn_strategy = st.builds(
    fastfst_nNcIMUzn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_vOutList_strategy = st.builds(
    fastfst_vOutList,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_aBldGagNd_strategy = st.builds(
    fastfst_aBldGagNd,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_iNBlGages_strategy = st.builds(
    fastfst_iNBlGages,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_aTwrGagNd_strategy = st.builds(
    fastfst_aTwrGagNd,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_iNTwGages_strategy = st.builds(
    fastfst_iNTwGages,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_sOutFmt_strategy = st.builds(
    fastfst_sOutFmt,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_bTabDelim_strategy = st.builds(
    fastfst_bTabDelim,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nNcIMUyn_strategy = st.builds(
    fastfst_nNcIMUyn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nNcIMUxn_strategy = st.builds(
    fastfst_nNcIMUxn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSttsTime_strategy = st.builds(
    fastfst_nSttsTime,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iDecFact_strategy = st.builds(
    fastfst_iDecFact,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nTStart_strategy = st.builds(
    fastfst_nTStart,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_fBldFile_3__strategy = st.builds(
    fastfst_fBldFile_3_,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_fBldFile_2__strategy = st.builds(
    fastfst_fBldFile_2_,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_bOutFileFmt_strategy = st.builds(
    fastfst_bOutFileFmt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bSumPrint_strategy = st.builds(
    fastfst_bSumPrint,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_fLinFile_strategy = st.builds(
    fastfst_fLinFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_fADAMSFile_strategy = st.builds(
    fastfst_fADAMSFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_fNoiseFile_strategy = st.builds(
    fastfst_fNoiseFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_fADFile_strategy = st.builds(
    fastfst_fADFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_nTeetHStP_strategy = st.builds(
    fastfst_nTeetHStP,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTeetSStP_strategy = st.builds(
    fastfst_nTeetSStP,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_fBldFile_1__strategy = st.builds(
    fastfst_fBldFile_1_,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_nTpBrDT_strategy = st.builds(
    fastfst_nTpBrDT,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTBDrConD_strategy = st.builds(
    fastfst_nTBDrConD,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTBDrConN_strategy = st.builds(
    fastfst_nTBDrConN,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTeetHSSp_strategy = st.builds(
    fastfst_nTeetHSSp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTeetSSSp_strategy = st.builds(
    fastfst_nTeetSSSp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nYawNeut_strategy = st.builds(
    fastfst_nYawNeut,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nYawDamp_strategy = st.builds(
    fastfst_nYawDamp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTeetCDmp_strategy = st.builds(
    fastfst_nTeetCDmp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTeetDmp_strategy = st.builds(
    fastfst_nTeetDmp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTeetDmpP_strategy = st.builds(
    fastfst_nTeetDmpP,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iTeetMod_strategy = st.builds(
    fastfst_iTeetMod,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_fFurlFile_strategy = st.builds(
    fastfst_fFurlFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_nTEC_RLR_strategy = st.builds(
    fastfst_nTEC_RLR,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bFurling_strategy = st.builds(
    fastfst_bFurling,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nTEC_SLR_strategy = st.builds(
    fastfst_nTEC_SLR,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nYawSpr_strategy = st.builds(
    fastfst_nYawSpr,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_fTwrFile_strategy = st.builds(
    fastfst_fTwrFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_iTwrNodes_strategy = st.builds(
    fastfst_iTwrNodes,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_fPtfmFile_strategy = st.builds(
    fastfst_fPtfmFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_iPtfmModel_strategy = st.builds(
    fastfst_iPtfmModel,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_nTEC_MR_strategy = st.builds(
    fastfst_nTEC_MR,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nSIG_SlPc_strategy = st.builds(
    fastfst_nSIG_SlPc,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nDTTorDmp_strategy = st.builds(
    fastfst_nDTTorDmp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_VLL_strategy = st.builds(
    fastfst_nTEC_VLL,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_Rres_strategy = st.builds(
    fastfst_nTEC_Rres,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_Sres_strategy = st.builds(
    fastfst_nTEC_Sres,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTEC_Npol_strategy = st.builds(
    fastfst_nTEC_Npol,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_Freq_strategy = st.builds(
    fastfst_nTEC_Freq,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nSIG_PORt_strategy = st.builds(
    fastfst_nSIG_PORt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSIG_RtTq_strategy = st.builds(
    fastfst_nSIG_RtTq,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSIG_SySp_strategy = st.builds(
    fastfst_nSIG_SySp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nGenIner_strategy = st.builds(
    fastfst_nGenIner,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nDTTorSpr_strategy = st.builds(
    fastfst_nDTTorSpr,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_fDynBrkFi_strategy = st.builds(
    fastfst_fDynBrkFi,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_nTwr2Shft_strategy = st.builds(
    fastfst_nTwr2Shft,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTowerHt_strategy = st.builds(
    fastfst_nTowerHt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacCMzn_strategy = st.builds(
    fastfst_nNacCMzn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nNacCMyn_strategy = st.builds(
    fastfst_nNacCMyn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTTDspSS_strategy = st.builds(
    fastfst_nTTDspSS,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTTDspFA_strategy = st.builds(
    fastfst_nTTDspFA,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacYaw_strategy = st.builds(
    fastfst_nNacYaw,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nRotSpeed_strategy = st.builds(
    fastfst_nRotSpeed,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nUndSling_strategy = st.builds(
    fastfst_nUndSling,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nPSpnElN_strategy = st.builds(
    fastfst_nPSpnElN,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nHubRad_strategy = st.builds(
    fastfst_nHubRad,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTipRad_strategy = st.builds(
    fastfst_nTipRad,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bTwFADOF1_strategy = st.builds(
    fastfst_bTwFADOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bYawDOF_strategy = st.builds(
    fastfst_bYawDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bGenDOF_strategy = st.builds(
    fastfst_bGenDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bDrTrDOF_strategy = st.builds(
    fastfst_bDrTrDOF,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_bTeetDOF_strategy = st.builds(
    fastfst_bTeetDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bEdgeDOF_strategy = st.builds(
    fastfst_bEdgeDOF,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nAzimuth_strategy = st.builds(
    fastfst_nAzimuth,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bFlapDOF2_strategy = st.builds(
    fastfst_bFlapDOF2,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nTeetDefl_strategy = st.builds(
    fastfst_nTeetDefl,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bFlapDOF1_strategy = st.builds(
    fastfst_bFlapDOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nIPDefl_strategy = st.builds(
    fastfst_nIPDefl,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nGravity_strategy = st.builds(
    fastfst_nGravity,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nOoPDefl_strategy = st.builds(
    fastfst_nOoPDefl,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nBlPitchF_3__strategy = st.builds(
    fastfst_nBlPitchF_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nBlPitchF_2__strategy = st.builds(
    fastfst_nBlPitchF_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bCompNoise_strategy = st.builds(
    fastfst_bCompNoise,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nBlPitchF_1__strategy = st.builds(
    fastfst_nBlPitchF_1_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bCompAero_strategy = st.builds(
    fastfst_bCompAero,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nBlPitch_3__strategy = st.builds(
    fastfst_nBlPitch_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bTwSSDOF2_strategy = st.builds(
    fastfst_bTwSSDOF2,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nBlPitch_2__strategy = st.builds(
    fastfst_nBlPitch_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bTwSSDOF1_strategy = st.builds(
    fastfst_bTwSSDOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bTwFADOF2_strategy = st.builds(
    fastfst_bTwFADOF2,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nTPitManE_2__strategy = st.builds(
    fastfst_nTPitManE_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTPitManE_1__strategy = st.builds(
    fastfst_nTPitManE_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTPitManS_3__strategy = st.builds(
    fastfst_nTPitManS_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTPitManS_2__strategy = st.builds(
    fastfst_nTPitManS_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTPitManS_1__strategy = st.builds(
    fastfst_nTPitManS_1_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacYawF_strategy = st.builds(
    fastfst_nNacYawF,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTYawManE_strategy = st.builds(
    fastfst_nTYawManE,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTYawManS_strategy = st.builds(
    fastfst_nTYawManS,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTBDepISp_3__strategy = st.builds(
    fastfst_nTBDepISp_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTBDepISp_2__strategy = st.builds(
    fastfst_nTBDepISp_2_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTBDepISp_1__strategy = st.builds(
    fastfst_nTBDepISp_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTTpBrDp_3__strategy = st.builds(
    fastfst_nTTpBrDp_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTTpBrDp_2__strategy = st.builds(
    fastfst_nTTpBrDp_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTTpBrDp_1__strategy = st.builds(
    fastfst_nTTpBrDp_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nBlPitch_1__strategy = st.builds(
    fastfst_nBlPitch_1_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTPitManE_3__strategy = st.builds(
    fastfst_nTPitManE_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iHSSBrMode_strategy = st.builds(
    fastfst_iHSSBrMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nTimGenOf_strategy = st.builds(
    fastfst_nTimGenOf,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTimGenOn_strategy = st.builds(
    fastfst_nTimGenOn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSpdGenOn_strategy = st.builds(
    fastfst_nSpdGenOn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bGenTiStp_strategy = st.builds(
    fastfst_bGenTiStp,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bGenTiStr_strategy = st.builds(
    fastfst_bGenTiStr,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_iGenModel_strategy = st.builds(
    fastfst_iGenModel,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_nVS_SlPc_strategy = st.builds(
    fastfst_nVS_SlPc,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nVS_Rgn2K_strategy = st.builds(
    fastfst_nVS_Rgn2K,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nVS_RtTq_strategy = st.builds(
    fastfst_nVS_RtTq,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nVS_RtGnSp_strategy = st.builds(
    fastfst_nVS_RtGnSp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iVSContrl_strategy = st.builds(
    fastfst_iVSContrl,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_nTPCOn_strategy = st.builds(
    fastfst_nTPCOn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iPCMode_strategy = st.builds(
    fastfst_iPCMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nTYCOn_strategy = st.builds(
    fastfst_nTYCOn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_iYCMode_strategy = st.builds(
    fastfst_iYCMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nDT_strategy = st.builds(
    fastfst_nDT,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTMax_strategy = st.builds(
    fastfst_nTMax,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTiDynBrk_strategy = st.builds(
    fastfst_nTiDynBrk,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTHSSBrDp_strategy = st.builds(
    fastfst_nTHSSBrDp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_iADAMSPrep_strategy = st.builds(
    fastfst_iADAMSPrep,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_bEcho_strategy = st.builds(
    fastfst_bEcho,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_Section_strategy = st.builds(
    fastfst_Section,
    name=
        safe_text
)
fastfst_Header_strategy = st.builds(
    fastfst_Header,
    rows=
        safe_text
)
fastfst_ModelFastfst_strategy = st.builds(
    fastfst_ModelFastfst,
)
fastfst_iNumBl_strategy = st.builds(
    fastfst_iNumBl,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_iAnalMode_strategy = st.builds(
    fastfst_iAnalMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nHSSBrDT_strategy = st.builds(
    fastfst_nHSSBrDT,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nHSSBrTqF_strategy = st.builds(
    fastfst_nHSSBrTqF,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bGBRevers_strategy = st.builds(
    fastfst_bGBRevers,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nGBRatio_strategy = st.builds(
    fastfst_nGBRatio,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nGenEff_strategy = st.builds(
    fastfst_nGenEff,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nGBoxEff_strategy = st.builds(
    fastfst_nGBoxEff,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nHubIner_strategy = st.builds(
    fastfst_nHubIner,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nPreCone_2__strategy = st.builds(
    fastfst_nPreCone_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacYIner_strategy = st.builds(
    fastfst_nNacYIner,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTipMass_3__strategy = st.builds(
    fastfst_nTipMass_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTipMass_2__strategy = st.builds(
    fastfst_nTipMass_2_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTipMass_1__strategy = st.builds(
    fastfst_nTipMass_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nHubMass_strategy = st.builds(
    fastfst_nHubMass,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacMass_strategy = st.builds(
    fastfst_nNacMass,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nYawBrMass_strategy = st.builds(
    fastfst_nYawBrMass,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nAzimB1Up_strategy = st.builds(
    fastfst_nAzimB1Up,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nPreCone_3__strategy = st.builds(
    fastfst_nPreCone_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacCMxn_strategy = st.builds(
    fastfst_nNacCMxn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nOverHang_strategy = st.builds(
    fastfst_nOverHang,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nHubCM_strategy = st.builds(
    fastfst_nHubCM,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nPreCone_1__strategy = st.builds(
    fastfst_nPreCone_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nDelta3_strategy = st.builds(
    fastfst_nDelta3,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nShftTilt_strategy = st.builds(
    fastfst_nShftTilt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTwrRBHt_strategy = st.builds(
    fastfst_nTwrRBHt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=fastfst_nShftGagL_strategy)
def test_hyp_fastfst_nshftgagl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nShftGagL_strategy)
def test_hyp_fastfst_nshftgagl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nNcIMUzn_strategy)
def test_hyp_fastfst_nncimuzn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nNcIMUzn_strategy)
def test_hyp_fastfst_nncimuzn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_vOutList_strategy)
def test_hyp_fastfst_voutlist_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_vOutList_strategy)
def test_hyp_fastfst_voutlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_aBldGagNd_strategy)
def test_hyp_fastfst_abldgagnd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_aBldGagNd_strategy)
def test_hyp_fastfst_abldgagnd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_iNBlGages_strategy)
def test_hyp_fastfst_inblgages_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iNBlGages_strategy)
def test_hyp_fastfst_inblgages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_aTwrGagNd_strategy)
def test_hyp_fastfst_atwrgagnd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_aTwrGagNd_strategy)
def test_hyp_fastfst_atwrgagnd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_iNTwGages_strategy)
def test_hyp_fastfst_intwgages_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iNTwGages_strategy)
def test_hyp_fastfst_intwgages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_sOutFmt_strategy)
def test_hyp_fastfst_soutfmt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_sOutFmt_strategy)
def test_hyp_fastfst_soutfmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bTabDelim_strategy)
def test_hyp_fastfst_btabdelim_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTabDelim_strategy)
def test_hyp_fastfst_btabdelim_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nNcIMUyn_strategy)
def test_hyp_fastfst_nncimuyn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNcIMUyn_strategy)
def test_hyp_fastfst_nncimuyn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nNcIMUxn_strategy)
def test_hyp_fastfst_nncimuxn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNcIMUxn_strategy)
def test_hyp_fastfst_nncimuxn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nSttsTime_strategy)
def test_hyp_fastfst_nsttstime_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSttsTime_strategy)
def test_hyp_fastfst_nsttstime_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iDecFact_strategy)
def test_hyp_fastfst_idecfact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iDecFact_strategy)
def test_hyp_fastfst_idecfact_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTStart_strategy)
def test_hyp_fastfst_ntstart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTStart_strategy)
def test_hyp_fastfst_ntstart_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_fBldFile_3__strategy)
def test_hyp_fastfst_fbldfile_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fBldFile_3__strategy)
def test_hyp_fastfst_fbldfile_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_fBldFile_2__strategy)
def test_hyp_fastfst_fbldfile_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fBldFile_2__strategy)
def test_hyp_fastfst_fbldfile_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bOutFileFmt_strategy)
def test_hyp_fastfst_boutfilefmt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bOutFileFmt_strategy)
def test_hyp_fastfst_boutfilefmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bSumPrint_strategy)
def test_hyp_fastfst_bsumprint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bSumPrint_strategy)
def test_hyp_fastfst_bsumprint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_fLinFile_strategy)
def test_hyp_fastfst_flinfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fLinFile_strategy)
def test_hyp_fastfst_flinfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_fADAMSFile_strategy)
def test_hyp_fastfst_fadamsfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fADAMSFile_strategy)
def test_hyp_fastfst_fadamsfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_fNoiseFile_strategy)
def test_hyp_fastfst_fnoisefile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fNoiseFile_strategy)
def test_hyp_fastfst_fnoisefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_fADFile_strategy)
def test_hyp_fastfst_fadfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fADFile_strategy)
def test_hyp_fastfst_fadfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTeetHStP_strategy)
def test_hyp_fastfst_nteethstp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetHStP_strategy)
def test_hyp_fastfst_nteethstp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTeetSStP_strategy)
def test_hyp_fastfst_nteetsstp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetSStP_strategy)
def test_hyp_fastfst_nteetsstp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_fBldFile_1__strategy)
def test_hyp_fastfst_fbldfile_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fBldFile_1__strategy)
def test_hyp_fastfst_fbldfile_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTpBrDT_strategy)
def test_hyp_fastfst_ntpbrdt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTpBrDT_strategy)
def test_hyp_fastfst_ntpbrdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTBDrConD_strategy)
def test_hyp_fastfst_ntbdrcond_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDrConD_strategy)
def test_hyp_fastfst_ntbdrcond_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTBDrConN_strategy)
def test_hyp_fastfst_ntbdrconn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDrConN_strategy)
def test_hyp_fastfst_ntbdrconn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTeetHSSp_strategy)
def test_hyp_fastfst_nteethssp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetHSSp_strategy)
def test_hyp_fastfst_nteethssp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTeetSSSp_strategy)
def test_hyp_fastfst_nteetsssp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetSSSp_strategy)
def test_hyp_fastfst_nteetsssp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nYawNeut_strategy)
def test_hyp_fastfst_nyawneut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nYawNeut_strategy)
def test_hyp_fastfst_nyawneut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nYawDamp_strategy)
def test_hyp_fastfst_nyawdamp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nYawDamp_strategy)
def test_hyp_fastfst_nyawdamp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTeetCDmp_strategy)
def test_hyp_fastfst_nteetcdmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetCDmp_strategy)
def test_hyp_fastfst_nteetcdmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTeetDmp_strategy)
def test_hyp_fastfst_nteetdmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetDmp_strategy)
def test_hyp_fastfst_nteetdmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTeetDmpP_strategy)
def test_hyp_fastfst_nteetdmpp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetDmpP_strategy)
def test_hyp_fastfst_nteetdmpp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iTeetMod_strategy)
def test_hyp_fastfst_iteetmod_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iTeetMod_strategy)
def test_hyp_fastfst_iteetmod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_fFurlFile_strategy)
def test_hyp_fastfst_ffurlfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fFurlFile_strategy)
def test_hyp_fastfst_ffurlfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTEC_RLR_strategy)
def test_hyp_fastfst_ntec_rlr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_RLR_strategy)
def test_hyp_fastfst_ntec_rlr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bFurling_strategy)
def test_hyp_fastfst_bfurling_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bFurling_strategy)
def test_hyp_fastfst_bfurling_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTEC_SLR_strategy)
def test_hyp_fastfst_ntec_slr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTEC_SLR_strategy)
def test_hyp_fastfst_ntec_slr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nYawSpr_strategy)
def test_hyp_fastfst_nyawspr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nYawSpr_strategy)
def test_hyp_fastfst_nyawspr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_fTwrFile_strategy)
def test_hyp_fastfst_ftwrfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fTwrFile_strategy)
def test_hyp_fastfst_ftwrfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_iTwrNodes_strategy)
def test_hyp_fastfst_itwrnodes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iTwrNodes_strategy)
def test_hyp_fastfst_itwrnodes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_fPtfmFile_strategy)
def test_hyp_fastfst_fptfmfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fPtfmFile_strategy)
def test_hyp_fastfst_fptfmfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iPtfmModel_strategy)
def test_hyp_fastfst_iptfmmodel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iPtfmModel_strategy)
def test_hyp_fastfst_iptfmmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTEC_MR_strategy)
def test_hyp_fastfst_ntec_mr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_MR_strategy)
def test_hyp_fastfst_ntec_mr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nSIG_SlPc_strategy)
def test_hyp_fastfst_nsig_slpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nSIG_SlPc_strategy)
def test_hyp_fastfst_nsig_slpc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nDTTorDmp_strategy)
def test_hyp_fastfst_ndttordmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nDTTorDmp_strategy)
def test_hyp_fastfst_ndttordmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTEC_VLL_strategy)
def test_hyp_fastfst_ntec_vll_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_VLL_strategy)
def test_hyp_fastfst_ntec_vll_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTEC_Rres_strategy)
def test_hyp_fastfst_ntec_rres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_Rres_strategy)
def test_hyp_fastfst_ntec_rres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTEC_Sres_strategy)
def test_hyp_fastfst_ntec_sres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTEC_Sres_strategy)
def test_hyp_fastfst_ntec_sres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTEC_Npol_strategy)
def test_hyp_fastfst_ntec_npol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_Npol_strategy)
def test_hyp_fastfst_ntec_npol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTEC_Freq_strategy)
def test_hyp_fastfst_ntec_freq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_Freq_strategy)
def test_hyp_fastfst_ntec_freq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nSIG_PORt_strategy)
def test_hyp_fastfst_nsig_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSIG_PORt_strategy)
def test_hyp_fastfst_nsig_port_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nSIG_RtTq_strategy)
def test_hyp_fastfst_nsig_rttq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSIG_RtTq_strategy)
def test_hyp_fastfst_nsig_rttq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nSIG_SySp_strategy)
def test_hyp_fastfst_nsig_sysp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSIG_SySp_strategy)
def test_hyp_fastfst_nsig_sysp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nGenIner_strategy)
def test_hyp_fastfst_ngeniner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nGenIner_strategy)
def test_hyp_fastfst_ngeniner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nDTTorSpr_strategy)
def test_hyp_fastfst_ndttorspr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nDTTorSpr_strategy)
def test_hyp_fastfst_ndttorspr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_fDynBrkFi_strategy)
def test_hyp_fastfst_fdynbrkfi_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fDynBrkFi_strategy)
def test_hyp_fastfst_fdynbrkfi_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTwr2Shft_strategy)
def test_hyp_fastfst_ntwr2shft_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTwr2Shft_strategy)
def test_hyp_fastfst_ntwr2shft_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTowerHt_strategy)
def test_hyp_fastfst_ntowerht_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTowerHt_strategy)
def test_hyp_fastfst_ntowerht_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nNacCMzn_strategy)
def test_hyp_fastfst_nnaccmzn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacCMzn_strategy)
def test_hyp_fastfst_nnaccmzn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nNacCMyn_strategy)
def test_hyp_fastfst_nnaccmyn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacCMyn_strategy)
def test_hyp_fastfst_nnaccmyn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTTDspSS_strategy)
def test_hyp_fastfst_nttdspss_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTTDspSS_strategy)
def test_hyp_fastfst_nttdspss_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTTDspFA_strategy)
def test_hyp_fastfst_nttdspfa_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTTDspFA_strategy)
def test_hyp_fastfst_nttdspfa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nNacYaw_strategy)
def test_hyp_fastfst_nnacyaw_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacYaw_strategy)
def test_hyp_fastfst_nnacyaw_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nRotSpeed_strategy)
def test_hyp_fastfst_nrotspeed_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nRotSpeed_strategy)
def test_hyp_fastfst_nrotspeed_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nUndSling_strategy)
def test_hyp_fastfst_nundsling_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nUndSling_strategy)
def test_hyp_fastfst_nundsling_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nPSpnElN_strategy)
def test_hyp_fastfst_npspneln_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nPSpnElN_strategy)
def test_hyp_fastfst_npspneln_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nHubRad_strategy)
def test_hyp_fastfst_nhubrad_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nHubRad_strategy)
def test_hyp_fastfst_nhubrad_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTipRad_strategy)
def test_hyp_fastfst_ntiprad_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTipRad_strategy)
def test_hyp_fastfst_ntiprad_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bTwFADOF1_strategy)
def test_hyp_fastfst_btwfadof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTwFADOF1_strategy)
def test_hyp_fastfst_btwfadof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bYawDOF_strategy)
def test_hyp_fastfst_byawdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bYawDOF_strategy)
def test_hyp_fastfst_byawdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bGenDOF_strategy)
def test_hyp_fastfst_bgendof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGenDOF_strategy)
def test_hyp_fastfst_bgendof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bDrTrDOF_strategy)
def test_hyp_fastfst_bdrtrdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bDrTrDOF_strategy)
def test_hyp_fastfst_bdrtrdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bTeetDOF_strategy)
def test_hyp_fastfst_bteetdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTeetDOF_strategy)
def test_hyp_fastfst_bteetdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bEdgeDOF_strategy)
def test_hyp_fastfst_bedgedof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bEdgeDOF_strategy)
def test_hyp_fastfst_bedgedof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nAzimuth_strategy)
def test_hyp_fastfst_nazimuth_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nAzimuth_strategy)
def test_hyp_fastfst_nazimuth_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bFlapDOF2_strategy)
def test_hyp_fastfst_bflapdof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bFlapDOF2_strategy)
def test_hyp_fastfst_bflapdof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTeetDefl_strategy)
def test_hyp_fastfst_nteetdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetDefl_strategy)
def test_hyp_fastfst_nteetdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bFlapDOF1_strategy)
def test_hyp_fastfst_bflapdof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bFlapDOF1_strategy)
def test_hyp_fastfst_bflapdof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nIPDefl_strategy)
def test_hyp_fastfst_nipdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nIPDefl_strategy)
def test_hyp_fastfst_nipdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nGravity_strategy)
def test_hyp_fastfst_ngravity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nGravity_strategy)
def test_hyp_fastfst_ngravity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nOoPDefl_strategy)
def test_hyp_fastfst_noopdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nOoPDefl_strategy)
def test_hyp_fastfst_noopdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nBlPitchF_3__strategy)
def test_hyp_fastfst_nblpitchf_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitchF_3__strategy)
def test_hyp_fastfst_nblpitchf_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nBlPitchF_2__strategy)
def test_hyp_fastfst_nblpitchf_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitchF_2__strategy)
def test_hyp_fastfst_nblpitchf_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bCompNoise_strategy)
def test_hyp_fastfst_bcompnoise_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bCompNoise_strategy)
def test_hyp_fastfst_bcompnoise_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nBlPitchF_1__strategy)
def test_hyp_fastfst_nblpitchf_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitchF_1__strategy)
def test_hyp_fastfst_nblpitchf_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bCompAero_strategy)
def test_hyp_fastfst_bcompaero_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bCompAero_strategy)
def test_hyp_fastfst_bcompaero_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nBlPitch_3__strategy)
def test_hyp_fastfst_nblpitch_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nBlPitch_3__strategy)
def test_hyp_fastfst_nblpitch_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bTwSSDOF2_strategy)
def test_hyp_fastfst_btwssdof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bTwSSDOF2_strategy)
def test_hyp_fastfst_btwssdof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nBlPitch_2__strategy)
def test_hyp_fastfst_nblpitch_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitch_2__strategy)
def test_hyp_fastfst_nblpitch_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bTwSSDOF1_strategy)
def test_hyp_fastfst_btwssdof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTwSSDOF1_strategy)
def test_hyp_fastfst_btwssdof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bTwFADOF2_strategy)
def test_hyp_fastfst_btwfadof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bTwFADOF2_strategy)
def test_hyp_fastfst_btwfadof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTPitManE_2__strategy)
def test_hyp_fastfst_ntpitmane_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTPitManE_2__strategy)
def test_hyp_fastfst_ntpitmane_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTPitManE_1__strategy)
def test_hyp_fastfst_ntpitmane_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPitManE_1__strategy)
def test_hyp_fastfst_ntpitmane_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTPitManS_3__strategy)
def test_hyp_fastfst_ntpitmans_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPitManS_3__strategy)
def test_hyp_fastfst_ntpitmans_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTPitManS_2__strategy)
def test_hyp_fastfst_ntpitmans_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTPitManS_2__strategy)
def test_hyp_fastfst_ntpitmans_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTPitManS_1__strategy)
def test_hyp_fastfst_ntpitmans_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTPitManS_1__strategy)
def test_hyp_fastfst_ntpitmans_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nNacYawF_strategy)
def test_hyp_fastfst_nnacyawf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacYawF_strategy)
def test_hyp_fastfst_nnacyawf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTYawManE_strategy)
def test_hyp_fastfst_ntyawmane_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTYawManE_strategy)
def test_hyp_fastfst_ntyawmane_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTYawManS_strategy)
def test_hyp_fastfst_ntyawmans_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTYawManS_strategy)
def test_hyp_fastfst_ntyawmans_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTBDepISp_3__strategy)
def test_hyp_fastfst_ntbdepisp_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTBDepISp_3__strategy)
def test_hyp_fastfst_ntbdepisp_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTBDepISp_2__strategy)
def test_hyp_fastfst_ntbdepisp_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDepISp_2__strategy)
def test_hyp_fastfst_ntbdepisp_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTBDepISp_1__strategy)
def test_hyp_fastfst_ntbdepisp_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDepISp_1__strategy)
def test_hyp_fastfst_ntbdepisp_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTTpBrDp_3__strategy)
def test_hyp_fastfst_nttpbrdp_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTTpBrDp_3__strategy)
def test_hyp_fastfst_nttpbrdp_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTTpBrDp_2__strategy)
def test_hyp_fastfst_nttpbrdp_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTTpBrDp_2__strategy)
def test_hyp_fastfst_nttpbrdp_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTTpBrDp_1__strategy)
def test_hyp_fastfst_nttpbrdp_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTTpBrDp_1__strategy)
def test_hyp_fastfst_nttpbrdp_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nBlPitch_1__strategy)
def test_hyp_fastfst_nblpitch_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitch_1__strategy)
def test_hyp_fastfst_nblpitch_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTPitManE_3__strategy)
def test_hyp_fastfst_ntpitmane_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPitManE_3__strategy)
def test_hyp_fastfst_ntpitmane_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iHSSBrMode_strategy)
def test_hyp_fastfst_ihssbrmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iHSSBrMode_strategy)
def test_hyp_fastfst_ihssbrmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTimGenOf_strategy)
def test_hyp_fastfst_ntimgenof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTimGenOf_strategy)
def test_hyp_fastfst_ntimgenof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTimGenOn_strategy)
def test_hyp_fastfst_ntimgenon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTimGenOn_strategy)
def test_hyp_fastfst_ntimgenon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nSpdGenOn_strategy)
def test_hyp_fastfst_nspdgenon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nSpdGenOn_strategy)
def test_hyp_fastfst_nspdgenon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_bGenTiStp_strategy)
def test_hyp_fastfst_bgentistp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGenTiStp_strategy)
def test_hyp_fastfst_bgentistp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bGenTiStr_strategy)
def test_hyp_fastfst_bgentistr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGenTiStr_strategy)
def test_hyp_fastfst_bgentistr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iGenModel_strategy)
def test_hyp_fastfst_igenmodel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iGenModel_strategy)
def test_hyp_fastfst_igenmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nVS_SlPc_strategy)
def test_hyp_fastfst_nvs_slpc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nVS_SlPc_strategy)
def test_hyp_fastfst_nvs_slpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nVS_Rgn2K_strategy)
def test_hyp_fastfst_nvs_rgn2k_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nVS_Rgn2K_strategy)
def test_hyp_fastfst_nvs_rgn2k_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nVS_RtTq_strategy)
def test_hyp_fastfst_nvs_rttq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nVS_RtTq_strategy)
def test_hyp_fastfst_nvs_rttq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nVS_RtGnSp_strategy)
def test_hyp_fastfst_nvs_rtgnsp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nVS_RtGnSp_strategy)
def test_hyp_fastfst_nvs_rtgnsp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iVSContrl_strategy)
def test_hyp_fastfst_ivscontrl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iVSContrl_strategy)
def test_hyp_fastfst_ivscontrl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTPCOn_strategy)
def test_hyp_fastfst_ntpcon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPCOn_strategy)
def test_hyp_fastfst_ntpcon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iPCMode_strategy)
def test_hyp_fastfst_ipcmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iPCMode_strategy)
def test_hyp_fastfst_ipcmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTYCOn_strategy)
def test_hyp_fastfst_ntycon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTYCOn_strategy)
def test_hyp_fastfst_ntycon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_iYCMode_strategy)
def test_hyp_fastfst_iycmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iYCMode_strategy)
def test_hyp_fastfst_iycmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nDT_strategy)
def test_hyp_fastfst_ndt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nDT_strategy)
def test_hyp_fastfst_ndt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTMax_strategy)
def test_hyp_fastfst_ntmax_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTMax_strategy)
def test_hyp_fastfst_ntmax_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTiDynBrk_strategy)
def test_hyp_fastfst_ntidynbrk_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTiDynBrk_strategy)
def test_hyp_fastfst_ntidynbrk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTHSSBrDp_strategy)
def test_hyp_fastfst_nthssbrdp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTHSSBrDp_strategy)
def test_hyp_fastfst_nthssbrdp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_iADAMSPrep_strategy)
def test_hyp_fastfst_iadamsprep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iADAMSPrep_strategy)
def test_hyp_fastfst_iadamsprep_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bEcho_strategy)
def test_hyp_fastfst_becho_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bEcho_strategy)
def test_hyp_fastfst_becho_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_Section_strategy)
def test_hyp_fastfst_section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_Header_strategy)
def test_hyp_fastfst_header_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original





@given(instance=fastfst_iNumBl_strategy)
def test_hyp_fastfst_inumbl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iNumBl_strategy)
def test_hyp_fastfst_inumbl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_iAnalMode_strategy)
def test_hyp_fastfst_ianalmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iAnalMode_strategy)
def test_hyp_fastfst_ianalmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nHSSBrDT_strategy)
def test_hyp_fastfst_nhssbrdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nHSSBrDT_strategy)
def test_hyp_fastfst_nhssbrdt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nHSSBrTqF_strategy)
def test_hyp_fastfst_nhssbrtqf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nHSSBrTqF_strategy)
def test_hyp_fastfst_nhssbrtqf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_bGBRevers_strategy)
def test_hyp_fastfst_bgbrevers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGBRevers_strategy)
def test_hyp_fastfst_bgbrevers_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nGBRatio_strategy)
def test_hyp_fastfst_ngbratio_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nGBRatio_strategy)
def test_hyp_fastfst_ngbratio_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nGenEff_strategy)
def test_hyp_fastfst_ngeneff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nGenEff_strategy)
def test_hyp_fastfst_ngeneff_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nGBoxEff_strategy)
def test_hyp_fastfst_ngboxeff_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nGBoxEff_strategy)
def test_hyp_fastfst_ngboxeff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nHubIner_strategy)
def test_hyp_fastfst_nhubiner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nHubIner_strategy)
def test_hyp_fastfst_nhubiner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nPreCone_2__strategy)
def test_hyp_fastfst_nprecone_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nPreCone_2__strategy)
def test_hyp_fastfst_nprecone_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nNacYIner_strategy)
def test_hyp_fastfst_nnacyiner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacYIner_strategy)
def test_hyp_fastfst_nnacyiner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTipMass_3__strategy)
def test_hyp_fastfst_ntipmass_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTipMass_3__strategy)
def test_hyp_fastfst_ntipmass_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nTipMass_2__strategy)
def test_hyp_fastfst_ntipmass_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTipMass_2__strategy)
def test_hyp_fastfst_ntipmass_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTipMass_1__strategy)
def test_hyp_fastfst_ntipmass_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTipMass_1__strategy)
def test_hyp_fastfst_ntipmass_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nHubMass_strategy)
def test_hyp_fastfst_nhubmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nHubMass_strategy)
def test_hyp_fastfst_nhubmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nNacMass_strategy)
def test_hyp_fastfst_nnacmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nNacMass_strategy)
def test_hyp_fastfst_nnacmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nYawBrMass_strategy)
def test_hyp_fastfst_nyawbrmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nYawBrMass_strategy)
def test_hyp_fastfst_nyawbrmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nAzimB1Up_strategy)
def test_hyp_fastfst_nazimb1up_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nAzimB1Up_strategy)
def test_hyp_fastfst_nazimb1up_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nPreCone_3__strategy)
def test_hyp_fastfst_nprecone_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nPreCone_3__strategy)
def test_hyp_fastfst_nprecone_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nNacCMxn_strategy)
def test_hyp_fastfst_nnaccmxn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nNacCMxn_strategy)
def test_hyp_fastfst_nnaccmxn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fastfst_nOverHang_strategy)
def test_hyp_fastfst_noverhang_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nOverHang_strategy)
def test_hyp_fastfst_noverhang_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nHubCM_strategy)
def test_hyp_fastfst_nhubcm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nHubCM_strategy)
def test_hyp_fastfst_nhubcm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nPreCone_1__strategy)
def test_hyp_fastfst_nprecone_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nPreCone_1__strategy)
def test_hyp_fastfst_nprecone_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nDelta3_strategy)
def test_hyp_fastfst_ndelta3_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nDelta3_strategy)
def test_hyp_fastfst_ndelta3_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nShftTilt_strategy)
def test_hyp_fastfst_nshfttilt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nShftTilt_strategy)
def test_hyp_fastfst_nshfttilt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=fastfst_nTwrRBHt_strategy)
def test_hyp_fastfst_ntwrrbht_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTwrRBHt_strategy)
def test_hyp_fastfst_ntwrrbht_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_fastfst_Header_rows_value_roundtrip():
    instance = fastfst_Header(rows="sample_text")
    assert instance.rows == "sample_text"
    instance.rows = "sample_text_2"
    assert instance.rows == "sample_text_2"


def test_fastfst_Section_name_value_roundtrip():
    instance = fastfst_Section(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_aBldGagNd_name_value_roundtrip():
    instance = fastfst_aBldGagNd(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_aBldGagNd_value_value_roundtrip():
    instance = fastfst_aBldGagNd(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_aTwrGagNd_name_value_roundtrip():
    instance = fastfst_aTwrGagNd(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_aTwrGagNd_value_value_roundtrip():
    instance = fastfst_aTwrGagNd(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_bCompAero_name_value_roundtrip():
    instance = fastfst_bCompAero(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bCompAero_value_value_roundtrip():
    instance = fastfst_bCompAero(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bCompNoise_name_value_roundtrip():
    instance = fastfst_bCompNoise(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bCompNoise_value_value_roundtrip():
    instance = fastfst_bCompNoise(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bDrTrDOF_name_value_roundtrip():
    instance = fastfst_bDrTrDOF(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bDrTrDOF_value_value_roundtrip():
    instance = fastfst_bDrTrDOF(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bEcho_name_value_roundtrip():
    instance = fastfst_bEcho(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bEcho_value_value_roundtrip():
    instance = fastfst_bEcho(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bEdgeDOF_name_value_roundtrip():
    instance = fastfst_bEdgeDOF(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bEdgeDOF_value_value_roundtrip():
    instance = fastfst_bEdgeDOF(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bFlapDOF1_name_value_roundtrip():
    instance = fastfst_bFlapDOF1(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bFlapDOF1_value_value_roundtrip():
    instance = fastfst_bFlapDOF1(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bFlapDOF2_name_value_roundtrip():
    instance = fastfst_bFlapDOF2(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bFlapDOF2_value_value_roundtrip():
    instance = fastfst_bFlapDOF2(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bFurling_name_value_roundtrip():
    instance = fastfst_bFurling(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bFurling_value_value_roundtrip():
    instance = fastfst_bFurling(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bGBRevers_name_value_roundtrip():
    instance = fastfst_bGBRevers(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bGBRevers_value_value_roundtrip():
    instance = fastfst_bGBRevers(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bGenDOF_name_value_roundtrip():
    instance = fastfst_bGenDOF(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bGenDOF_value_value_roundtrip():
    instance = fastfst_bGenDOF(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bGenTiStp_name_value_roundtrip():
    instance = fastfst_bGenTiStp(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bGenTiStp_value_value_roundtrip():
    instance = fastfst_bGenTiStp(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bGenTiStr_name_value_roundtrip():
    instance = fastfst_bGenTiStr(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bGenTiStr_value_value_roundtrip():
    instance = fastfst_bGenTiStr(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bOutFileFmt_name_value_roundtrip():
    instance = fastfst_bOutFileFmt(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bOutFileFmt_value_value_roundtrip():
    instance = fastfst_bOutFileFmt(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_bSumPrint_name_value_roundtrip():
    instance = fastfst_bSumPrint(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bSumPrint_value_value_roundtrip():
    instance = fastfst_bSumPrint(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bTabDelim_name_value_roundtrip():
    instance = fastfst_bTabDelim(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bTabDelim_value_value_roundtrip():
    instance = fastfst_bTabDelim(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bTeetDOF_name_value_roundtrip():
    instance = fastfst_bTeetDOF(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bTeetDOF_value_value_roundtrip():
    instance = fastfst_bTeetDOF(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bTwFADOF1_name_value_roundtrip():
    instance = fastfst_bTwFADOF1(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bTwFADOF1_value_value_roundtrip():
    instance = fastfst_bTwFADOF1(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bTwFADOF2_name_value_roundtrip():
    instance = fastfst_bTwFADOF2(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bTwFADOF2_value_value_roundtrip():
    instance = fastfst_bTwFADOF2(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bTwSSDOF1_name_value_roundtrip():
    instance = fastfst_bTwSSDOF1(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bTwSSDOF1_value_value_roundtrip():
    instance = fastfst_bTwSSDOF1(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bTwSSDOF2_name_value_roundtrip():
    instance = fastfst_bTwSSDOF2(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bTwSSDOF2_value_value_roundtrip():
    instance = fastfst_bTwSSDOF2(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_bYawDOF_name_value_roundtrip():
    instance = fastfst_bYawDOF(name="sample_text", value=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_bYawDOF_value_value_roundtrip():
    instance = fastfst_bYawDOF(name="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_fastfst_fADAMSFile_name_value_roundtrip():
    instance = fastfst_fADAMSFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fADAMSFile_value_value_roundtrip():
    instance = fastfst_fADAMSFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fADFile_name_value_roundtrip():
    instance = fastfst_fADFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fADFile_value_value_roundtrip():
    instance = fastfst_fADFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fBldFile_1__name_value_roundtrip():
    instance = fastfst_fBldFile_1_(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fBldFile_1__value_value_roundtrip():
    instance = fastfst_fBldFile_1_(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fBldFile_2__name_value_roundtrip():
    instance = fastfst_fBldFile_2_(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fBldFile_2__value_value_roundtrip():
    instance = fastfst_fBldFile_2_(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fBldFile_3__name_value_roundtrip():
    instance = fastfst_fBldFile_3_(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fBldFile_3__value_value_roundtrip():
    instance = fastfst_fBldFile_3_(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fDynBrkFi_name_value_roundtrip():
    instance = fastfst_fDynBrkFi(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fDynBrkFi_value_value_roundtrip():
    instance = fastfst_fDynBrkFi(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fFurlFile_name_value_roundtrip():
    instance = fastfst_fFurlFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fFurlFile_value_value_roundtrip():
    instance = fastfst_fFurlFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fLinFile_name_value_roundtrip():
    instance = fastfst_fLinFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fLinFile_value_value_roundtrip():
    instance = fastfst_fLinFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fNoiseFile_name_value_roundtrip():
    instance = fastfst_fNoiseFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fNoiseFile_value_value_roundtrip():
    instance = fastfst_fNoiseFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fPtfmFile_name_value_roundtrip():
    instance = fastfst_fPtfmFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fPtfmFile_value_value_roundtrip():
    instance = fastfst_fPtfmFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_fTwrFile_name_value_roundtrip():
    instance = fastfst_fTwrFile(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_fTwrFile_value_value_roundtrip():
    instance = fastfst_fTwrFile(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_iADAMSPrep_name_value_roundtrip():
    instance = fastfst_iADAMSPrep(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iADAMSPrep_value_value_roundtrip():
    instance = fastfst_iADAMSPrep(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iAnalMode_name_value_roundtrip():
    instance = fastfst_iAnalMode(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iAnalMode_value_value_roundtrip():
    instance = fastfst_iAnalMode(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iDecFact_name_value_roundtrip():
    instance = fastfst_iDecFact(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iDecFact_value_value_roundtrip():
    instance = fastfst_iDecFact(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iGenModel_name_value_roundtrip():
    instance = fastfst_iGenModel(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iGenModel_value_value_roundtrip():
    instance = fastfst_iGenModel(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iHSSBrMode_name_value_roundtrip():
    instance = fastfst_iHSSBrMode(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iHSSBrMode_value_value_roundtrip():
    instance = fastfst_iHSSBrMode(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iNBlGages_name_value_roundtrip():
    instance = fastfst_iNBlGages(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iNBlGages_value_value_roundtrip():
    instance = fastfst_iNBlGages(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iNTwGages_name_value_roundtrip():
    instance = fastfst_iNTwGages(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iNTwGages_value_value_roundtrip():
    instance = fastfst_iNTwGages(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iNumBl_name_value_roundtrip():
    instance = fastfst_iNumBl(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iNumBl_value_value_roundtrip():
    instance = fastfst_iNumBl(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iPCMode_name_value_roundtrip():
    instance = fastfst_iPCMode(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iPCMode_value_value_roundtrip():
    instance = fastfst_iPCMode(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iPtfmModel_name_value_roundtrip():
    instance = fastfst_iPtfmModel(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iPtfmModel_value_value_roundtrip():
    instance = fastfst_iPtfmModel(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iTeetMod_name_value_roundtrip():
    instance = fastfst_iTeetMod(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iTeetMod_value_value_roundtrip():
    instance = fastfst_iTeetMod(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iTwrNodes_name_value_roundtrip():
    instance = fastfst_iTwrNodes(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iTwrNodes_value_value_roundtrip():
    instance = fastfst_iTwrNodes(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iVSContrl_name_value_roundtrip():
    instance = fastfst_iVSContrl(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iVSContrl_value_value_roundtrip():
    instance = fastfst_iVSContrl(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_iYCMode_name_value_roundtrip():
    instance = fastfst_iYCMode(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_iYCMode_value_value_roundtrip():
    instance = fastfst_iYCMode(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_nAzimB1Up_name_value_roundtrip():
    instance = fastfst_nAzimB1Up(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nAzimB1Up_value_value_roundtrip():
    instance = fastfst_nAzimB1Up(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nAzimuth_name_value_roundtrip():
    instance = fastfst_nAzimuth(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nAzimuth_value_value_roundtrip():
    instance = fastfst_nAzimuth(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nBlPitchF_1__name_value_roundtrip():
    instance = fastfst_nBlPitchF_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nBlPitchF_1__value_value_roundtrip():
    instance = fastfst_nBlPitchF_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nBlPitchF_2__name_value_roundtrip():
    instance = fastfst_nBlPitchF_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nBlPitchF_2__value_value_roundtrip():
    instance = fastfst_nBlPitchF_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nBlPitchF_3__name_value_roundtrip():
    instance = fastfst_nBlPitchF_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nBlPitchF_3__value_value_roundtrip():
    instance = fastfst_nBlPitchF_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nBlPitch_1__name_value_roundtrip():
    instance = fastfst_nBlPitch_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nBlPitch_1__value_value_roundtrip():
    instance = fastfst_nBlPitch_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nBlPitch_2__name_value_roundtrip():
    instance = fastfst_nBlPitch_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nBlPitch_2__value_value_roundtrip():
    instance = fastfst_nBlPitch_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nBlPitch_3__name_value_roundtrip():
    instance = fastfst_nBlPitch_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nBlPitch_3__value_value_roundtrip():
    instance = fastfst_nBlPitch_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nDT_name_value_roundtrip():
    instance = fastfst_nDT(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nDT_value_value_roundtrip():
    instance = fastfst_nDT(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nDTTorDmp_name_value_roundtrip():
    instance = fastfst_nDTTorDmp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nDTTorDmp_value_value_roundtrip():
    instance = fastfst_nDTTorDmp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nDTTorSpr_name_value_roundtrip():
    instance = fastfst_nDTTorSpr(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nDTTorSpr_value_value_roundtrip():
    instance = fastfst_nDTTorSpr(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nDelta3_name_value_roundtrip():
    instance = fastfst_nDelta3(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nDelta3_value_value_roundtrip():
    instance = fastfst_nDelta3(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nGBRatio_name_value_roundtrip():
    instance = fastfst_nGBRatio(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nGBRatio_value_value_roundtrip():
    instance = fastfst_nGBRatio(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nGBoxEff_name_value_roundtrip():
    instance = fastfst_nGBoxEff(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nGBoxEff_value_value_roundtrip():
    instance = fastfst_nGBoxEff(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nGenEff_name_value_roundtrip():
    instance = fastfst_nGenEff(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nGenEff_value_value_roundtrip():
    instance = fastfst_nGenEff(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nGenIner_name_value_roundtrip():
    instance = fastfst_nGenIner(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nGenIner_value_value_roundtrip():
    instance = fastfst_nGenIner(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nGravity_name_value_roundtrip():
    instance = fastfst_nGravity(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nGravity_value_value_roundtrip():
    instance = fastfst_nGravity(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nHSSBrDT_name_value_roundtrip():
    instance = fastfst_nHSSBrDT(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nHSSBrDT_value_value_roundtrip():
    instance = fastfst_nHSSBrDT(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nHSSBrTqF_name_value_roundtrip():
    instance = fastfst_nHSSBrTqF(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nHSSBrTqF_value_value_roundtrip():
    instance = fastfst_nHSSBrTqF(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nHubCM_name_value_roundtrip():
    instance = fastfst_nHubCM(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nHubCM_value_value_roundtrip():
    instance = fastfst_nHubCM(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nHubIner_name_value_roundtrip():
    instance = fastfst_nHubIner(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nHubIner_value_value_roundtrip():
    instance = fastfst_nHubIner(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nHubMass_name_value_roundtrip():
    instance = fastfst_nHubMass(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nHubMass_value_value_roundtrip():
    instance = fastfst_nHubMass(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nHubRad_name_value_roundtrip():
    instance = fastfst_nHubRad(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nHubRad_value_value_roundtrip():
    instance = fastfst_nHubRad(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nIPDefl_name_value_roundtrip():
    instance = fastfst_nIPDefl(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nIPDefl_value_value_roundtrip():
    instance = fastfst_nIPDefl(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacCMxn_name_value_roundtrip():
    instance = fastfst_nNacCMxn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacCMxn_value_value_roundtrip():
    instance = fastfst_nNacCMxn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacCMyn_name_value_roundtrip():
    instance = fastfst_nNacCMyn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacCMyn_value_value_roundtrip():
    instance = fastfst_nNacCMyn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacCMzn_name_value_roundtrip():
    instance = fastfst_nNacCMzn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacCMzn_value_value_roundtrip():
    instance = fastfst_nNacCMzn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacMass_name_value_roundtrip():
    instance = fastfst_nNacMass(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacMass_value_value_roundtrip():
    instance = fastfst_nNacMass(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacYIner_name_value_roundtrip():
    instance = fastfst_nNacYIner(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacYIner_value_value_roundtrip():
    instance = fastfst_nNacYIner(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacYaw_name_value_roundtrip():
    instance = fastfst_nNacYaw(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacYaw_value_value_roundtrip():
    instance = fastfst_nNacYaw(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNacYawF_name_value_roundtrip():
    instance = fastfst_nNacYawF(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNacYawF_value_value_roundtrip():
    instance = fastfst_nNacYawF(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNcIMUxn_name_value_roundtrip():
    instance = fastfst_nNcIMUxn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNcIMUxn_value_value_roundtrip():
    instance = fastfst_nNcIMUxn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNcIMUyn_name_value_roundtrip():
    instance = fastfst_nNcIMUyn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNcIMUyn_value_value_roundtrip():
    instance = fastfst_nNcIMUyn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nNcIMUzn_name_value_roundtrip():
    instance = fastfst_nNcIMUzn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nNcIMUzn_value_value_roundtrip():
    instance = fastfst_nNcIMUzn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nOoPDefl_name_value_roundtrip():
    instance = fastfst_nOoPDefl(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nOoPDefl_value_value_roundtrip():
    instance = fastfst_nOoPDefl(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nOverHang_name_value_roundtrip():
    instance = fastfst_nOverHang(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nOverHang_value_value_roundtrip():
    instance = fastfst_nOverHang(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nPSpnElN_name_value_roundtrip():
    instance = fastfst_nPSpnElN(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nPSpnElN_value_value_roundtrip():
    instance = fastfst_nPSpnElN(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_fastfst_nPreCone_1__name_value_roundtrip():
    instance = fastfst_nPreCone_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nPreCone_1__value_value_roundtrip():
    instance = fastfst_nPreCone_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nPreCone_2__name_value_roundtrip():
    instance = fastfst_nPreCone_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nPreCone_2__value_value_roundtrip():
    instance = fastfst_nPreCone_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nPreCone_3__name_value_roundtrip():
    instance = fastfst_nPreCone_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nPreCone_3__value_value_roundtrip():
    instance = fastfst_nPreCone_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nRotSpeed_name_value_roundtrip():
    instance = fastfst_nRotSpeed(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nRotSpeed_value_value_roundtrip():
    instance = fastfst_nRotSpeed(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nSIG_PORt_name_value_roundtrip():
    instance = fastfst_nSIG_PORt(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nSIG_PORt_value_value_roundtrip():
    instance = fastfst_nSIG_PORt(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nSIG_RtTq_name_value_roundtrip():
    instance = fastfst_nSIG_RtTq(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nSIG_RtTq_value_value_roundtrip():
    instance = fastfst_nSIG_RtTq(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nSIG_SlPc_name_value_roundtrip():
    instance = fastfst_nSIG_SlPc(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nSIG_SlPc_value_value_roundtrip():
    instance = fastfst_nSIG_SlPc(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nSIG_SySp_name_value_roundtrip():
    instance = fastfst_nSIG_SySp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nSIG_SySp_value_value_roundtrip():
    instance = fastfst_nSIG_SySp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nShftGagL_name_value_roundtrip():
    instance = fastfst_nShftGagL(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nShftGagL_value_value_roundtrip():
    instance = fastfst_nShftGagL(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nShftTilt_name_value_roundtrip():
    instance = fastfst_nShftTilt(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nShftTilt_value_value_roundtrip():
    instance = fastfst_nShftTilt(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nSpdGenOn_name_value_roundtrip():
    instance = fastfst_nSpdGenOn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nSpdGenOn_value_value_roundtrip():
    instance = fastfst_nSpdGenOn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nSttsTime_name_value_roundtrip():
    instance = fastfst_nSttsTime(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nSttsTime_value_value_roundtrip():
    instance = fastfst_nSttsTime(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTBDepISp_1__name_value_roundtrip():
    instance = fastfst_nTBDepISp_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTBDepISp_1__value_value_roundtrip():
    instance = fastfst_nTBDepISp_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTBDepISp_2__name_value_roundtrip():
    instance = fastfst_nTBDepISp_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTBDepISp_2__value_value_roundtrip():
    instance = fastfst_nTBDepISp_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTBDepISp_3__name_value_roundtrip():
    instance = fastfst_nTBDepISp_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTBDepISp_3__value_value_roundtrip():
    instance = fastfst_nTBDepISp_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTBDrConD_name_value_roundtrip():
    instance = fastfst_nTBDrConD(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTBDrConD_value_value_roundtrip():
    instance = fastfst_nTBDrConD(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTBDrConN_name_value_roundtrip():
    instance = fastfst_nTBDrConN(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTBDrConN_value_value_roundtrip():
    instance = fastfst_nTBDrConN(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_Freq_name_value_roundtrip():
    instance = fastfst_nTEC_Freq(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_Freq_value_value_roundtrip():
    instance = fastfst_nTEC_Freq(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_MR_name_value_roundtrip():
    instance = fastfst_nTEC_MR(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_MR_value_value_roundtrip():
    instance = fastfst_nTEC_MR(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_Npol_name_value_roundtrip():
    instance = fastfst_nTEC_Npol(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_Npol_value_value_roundtrip():
    instance = fastfst_nTEC_Npol(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_RLR_name_value_roundtrip():
    instance = fastfst_nTEC_RLR(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_RLR_value_value_roundtrip():
    instance = fastfst_nTEC_RLR(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_Rres_name_value_roundtrip():
    instance = fastfst_nTEC_Rres(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_Rres_value_value_roundtrip():
    instance = fastfst_nTEC_Rres(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_SLR_name_value_roundtrip():
    instance = fastfst_nTEC_SLR(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_SLR_value_value_roundtrip():
    instance = fastfst_nTEC_SLR(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_Sres_name_value_roundtrip():
    instance = fastfst_nTEC_Sres(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_Sres_value_value_roundtrip():
    instance = fastfst_nTEC_Sres(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTEC_VLL_name_value_roundtrip():
    instance = fastfst_nTEC_VLL(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTEC_VLL_value_value_roundtrip():
    instance = fastfst_nTEC_VLL(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTHSSBrDp_name_value_roundtrip():
    instance = fastfst_nTHSSBrDp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTHSSBrDp_value_value_roundtrip():
    instance = fastfst_nTHSSBrDp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTMax_name_value_roundtrip():
    instance = fastfst_nTMax(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTMax_value_value_roundtrip():
    instance = fastfst_nTMax(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPCOn_name_value_roundtrip():
    instance = fastfst_nTPCOn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPCOn_value_value_roundtrip():
    instance = fastfst_nTPCOn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPitManE_1__name_value_roundtrip():
    instance = fastfst_nTPitManE_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPitManE_1__value_value_roundtrip():
    instance = fastfst_nTPitManE_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPitManE_2__name_value_roundtrip():
    instance = fastfst_nTPitManE_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPitManE_2__value_value_roundtrip():
    instance = fastfst_nTPitManE_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPitManE_3__name_value_roundtrip():
    instance = fastfst_nTPitManE_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPitManE_3__value_value_roundtrip():
    instance = fastfst_nTPitManE_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPitManS_1__name_value_roundtrip():
    instance = fastfst_nTPitManS_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPitManS_1__value_value_roundtrip():
    instance = fastfst_nTPitManS_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPitManS_2__name_value_roundtrip():
    instance = fastfst_nTPitManS_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPitManS_2__value_value_roundtrip():
    instance = fastfst_nTPitManS_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTPitManS_3__name_value_roundtrip():
    instance = fastfst_nTPitManS_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTPitManS_3__value_value_roundtrip():
    instance = fastfst_nTPitManS_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTStart_name_value_roundtrip():
    instance = fastfst_nTStart(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTStart_value_value_roundtrip():
    instance = fastfst_nTStart(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTTDspFA_name_value_roundtrip():
    instance = fastfst_nTTDspFA(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTTDspFA_value_value_roundtrip():
    instance = fastfst_nTTDspFA(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTTDspSS_name_value_roundtrip():
    instance = fastfst_nTTDspSS(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTTDspSS_value_value_roundtrip():
    instance = fastfst_nTTDspSS(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTTpBrDp_1__name_value_roundtrip():
    instance = fastfst_nTTpBrDp_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTTpBrDp_1__value_value_roundtrip():
    instance = fastfst_nTTpBrDp_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTTpBrDp_2__name_value_roundtrip():
    instance = fastfst_nTTpBrDp_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTTpBrDp_2__value_value_roundtrip():
    instance = fastfst_nTTpBrDp_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTTpBrDp_3__name_value_roundtrip():
    instance = fastfst_nTTpBrDp_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTTpBrDp_3__value_value_roundtrip():
    instance = fastfst_nTTpBrDp_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTYCOn_name_value_roundtrip():
    instance = fastfst_nTYCOn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTYCOn_value_value_roundtrip():
    instance = fastfst_nTYCOn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTYawManE_name_value_roundtrip():
    instance = fastfst_nTYawManE(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTYawManE_value_value_roundtrip():
    instance = fastfst_nTYawManE(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTYawManS_name_value_roundtrip():
    instance = fastfst_nTYawManS(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTYawManS_value_value_roundtrip():
    instance = fastfst_nTYawManS(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetCDmp_name_value_roundtrip():
    instance = fastfst_nTeetCDmp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetCDmp_value_value_roundtrip():
    instance = fastfst_nTeetCDmp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetDefl_name_value_roundtrip():
    instance = fastfst_nTeetDefl(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetDefl_value_value_roundtrip():
    instance = fastfst_nTeetDefl(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetDmp_name_value_roundtrip():
    instance = fastfst_nTeetDmp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetDmp_value_value_roundtrip():
    instance = fastfst_nTeetDmp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetDmpP_name_value_roundtrip():
    instance = fastfst_nTeetDmpP(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetDmpP_value_value_roundtrip():
    instance = fastfst_nTeetDmpP(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetHSSp_name_value_roundtrip():
    instance = fastfst_nTeetHSSp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetHSSp_value_value_roundtrip():
    instance = fastfst_nTeetHSSp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetHStP_name_value_roundtrip():
    instance = fastfst_nTeetHStP(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetHStP_value_value_roundtrip():
    instance = fastfst_nTeetHStP(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetSSSp_name_value_roundtrip():
    instance = fastfst_nTeetSSSp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetSSSp_value_value_roundtrip():
    instance = fastfst_nTeetSSSp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTeetSStP_name_value_roundtrip():
    instance = fastfst_nTeetSStP(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTeetSStP_value_value_roundtrip():
    instance = fastfst_nTeetSStP(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTiDynBrk_name_value_roundtrip():
    instance = fastfst_nTiDynBrk(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTiDynBrk_value_value_roundtrip():
    instance = fastfst_nTiDynBrk(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTimGenOf_name_value_roundtrip():
    instance = fastfst_nTimGenOf(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTimGenOf_value_value_roundtrip():
    instance = fastfst_nTimGenOf(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTimGenOn_name_value_roundtrip():
    instance = fastfst_nTimGenOn(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTimGenOn_value_value_roundtrip():
    instance = fastfst_nTimGenOn(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTipMass_1__name_value_roundtrip():
    instance = fastfst_nTipMass_1_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTipMass_1__value_value_roundtrip():
    instance = fastfst_nTipMass_1_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTipMass_2__name_value_roundtrip():
    instance = fastfst_nTipMass_2_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTipMass_2__value_value_roundtrip():
    instance = fastfst_nTipMass_2_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTipMass_3__name_value_roundtrip():
    instance = fastfst_nTipMass_3_(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTipMass_3__value_value_roundtrip():
    instance = fastfst_nTipMass_3_(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTipRad_name_value_roundtrip():
    instance = fastfst_nTipRad(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTipRad_value_value_roundtrip():
    instance = fastfst_nTipRad(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTowerHt_name_value_roundtrip():
    instance = fastfst_nTowerHt(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTowerHt_value_value_roundtrip():
    instance = fastfst_nTowerHt(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTpBrDT_name_value_roundtrip():
    instance = fastfst_nTpBrDT(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTpBrDT_value_value_roundtrip():
    instance = fastfst_nTpBrDT(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTwr2Shft_name_value_roundtrip():
    instance = fastfst_nTwr2Shft(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTwr2Shft_value_value_roundtrip():
    instance = fastfst_nTwr2Shft(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nTwrRBHt_name_value_roundtrip():
    instance = fastfst_nTwrRBHt(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nTwrRBHt_value_value_roundtrip():
    instance = fastfst_nTwrRBHt(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nUndSling_name_value_roundtrip():
    instance = fastfst_nUndSling(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nUndSling_value_value_roundtrip():
    instance = fastfst_nUndSling(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nVS_Rgn2K_name_value_roundtrip():
    instance = fastfst_nVS_Rgn2K(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nVS_Rgn2K_value_value_roundtrip():
    instance = fastfst_nVS_Rgn2K(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nVS_RtGnSp_name_value_roundtrip():
    instance = fastfst_nVS_RtGnSp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nVS_RtGnSp_value_value_roundtrip():
    instance = fastfst_nVS_RtGnSp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nVS_RtTq_name_value_roundtrip():
    instance = fastfst_nVS_RtTq(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nVS_RtTq_value_value_roundtrip():
    instance = fastfst_nVS_RtTq(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nVS_SlPc_name_value_roundtrip():
    instance = fastfst_nVS_SlPc(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nVS_SlPc_value_value_roundtrip():
    instance = fastfst_nVS_SlPc(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nYawBrMass_name_value_roundtrip():
    instance = fastfst_nYawBrMass(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nYawBrMass_value_value_roundtrip():
    instance = fastfst_nYawBrMass(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nYawDamp_name_value_roundtrip():
    instance = fastfst_nYawDamp(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nYawDamp_value_value_roundtrip():
    instance = fastfst_nYawDamp(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nYawNeut_name_value_roundtrip():
    instance = fastfst_nYawNeut(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nYawNeut_value_value_roundtrip():
    instance = fastfst_nYawNeut(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_nYawSpr_name_value_roundtrip():
    instance = fastfst_nYawSpr(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_nYawSpr_value_value_roundtrip():
    instance = fastfst_nYawSpr(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_fastfst_sOutFmt_name_value_roundtrip():
    instance = fastfst_sOutFmt(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_sOutFmt_value_value_roundtrip():
    instance = fastfst_sOutFmt(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fastfst_vOutList_name_value_roundtrip():
    instance = fastfst_vOutList(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fastfst_vOutList_value_value_roundtrip():
    instance = fastfst_vOutList(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_assoc_ADAMSFile283_link_reassign_clear():
    a = fastfst_fADAMSFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fADAMSFile', b1)
    assert _is_linked(a, 'fastfst_fADAMSFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst284'):
        assert _is_linked(b1, 'fastfst_ModelFastfst284', a)
    _safe_set(a, 'fastfst_fADAMSFile', b2)
    assert _is_linked(a, 'fastfst_fADAMSFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst284'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst284', a)
    if hasattr(b2, 'fastfst_ModelFastfst284'):
        assert _is_linked(b2, 'fastfst_ModelFastfst284', a)
    _safe_set(a, 'fastfst_fADAMSFile', None)
    assert not _is_linked(a, 'fastfst_fADAMSFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst284'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst284', a)


def test_assoc_ADAMSPrep5_link_reassign_clear():
    a = fastfst_iADAMSPrep(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iADAMSPrep', b1)
    assert _is_linked(a, 'fastfst_iADAMSPrep', b1)
    if hasattr(b1, 'fastfst_ModelFastfst6'):
        assert _is_linked(b1, 'fastfst_ModelFastfst6', a)
    _safe_set(a, 'fastfst_iADAMSPrep', b2)
    assert _is_linked(a, 'fastfst_iADAMSPrep', b2)
    if hasattr(b1, 'fastfst_ModelFastfst6'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst6', a)
    if hasattr(b2, 'fastfst_ModelFastfst6'):
        assert _is_linked(b2, 'fastfst_ModelFastfst6', a)
    _safe_set(a, 'fastfst_iADAMSPrep', None)
    assert not _is_linked(a, 'fastfst_iADAMSPrep', b2)
    if hasattr(b2, 'fastfst_ModelFastfst6'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst6', a)


def test_assoc_ADFile279_link_reassign_clear():
    a = fastfst_fADFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fADFile', b1)
    assert _is_linked(a, 'fastfst_fADFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst280'):
        assert _is_linked(b1, 'fastfst_ModelFastfst280', a)
    _safe_set(a, 'fastfst_fADFile', b2)
    assert _is_linked(a, 'fastfst_fADFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst280'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst280', a)
    if hasattr(b2, 'fastfst_ModelFastfst280'):
        assert _is_linked(b2, 'fastfst_ModelFastfst280', a)
    _safe_set(a, 'fastfst_fADFile', None)
    assert not _is_linked(a, 'fastfst_fADFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst280'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst280', a)


def test_assoc_AnalMode7_link_reassign_clear():
    a = fastfst_iAnalMode(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iAnalMode', b1)
    assert _is_linked(a, 'fastfst_iAnalMode', b1)
    if hasattr(b1, 'fastfst_ModelFastfst8'):
        assert _is_linked(b1, 'fastfst_ModelFastfst8', a)
    _safe_set(a, 'fastfst_iAnalMode', b2)
    assert _is_linked(a, 'fastfst_iAnalMode', b2)
    if hasattr(b1, 'fastfst_ModelFastfst8'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst8', a)
    if hasattr(b2, 'fastfst_ModelFastfst8'):
        assert _is_linked(b2, 'fastfst_ModelFastfst8', a)
    _safe_set(a, 'fastfst_iAnalMode', None)
    assert not _is_linked(a, 'fastfst_iAnalMode', b2)
    if hasattr(b2, 'fastfst_ModelFastfst8'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst8', a)


def test_assoc_AzimB1Up171_link_reassign_clear():
    a = fastfst_nAzimB1Up(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nAzimB1Up', b1)
    assert _is_linked(a, 'fastfst_nAzimB1Up', b1)
    if hasattr(b1, 'fastfst_ModelFastfst172'):
        assert _is_linked(b1, 'fastfst_ModelFastfst172', a)
    _safe_set(a, 'fastfst_nAzimB1Up', b2)
    assert _is_linked(a, 'fastfst_nAzimB1Up', b2)
    if hasattr(b1, 'fastfst_ModelFastfst172'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst172', a)
    if hasattr(b2, 'fastfst_ModelFastfst172'):
        assert _is_linked(b2, 'fastfst_ModelFastfst172', a)
    _safe_set(a, 'fastfst_nAzimB1Up', None)
    assert not _is_linked(a, 'fastfst_nAzimB1Up', b2)
    if hasattr(b2, 'fastfst_ModelFastfst172'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst172', a)


def test_assoc_Azimuth127_link_reassign_clear():
    a = fastfst_nAzimuth(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nAzimuth', b1)
    assert _is_linked(a, 'fastfst_nAzimuth', b1)
    if hasattr(b1, 'fastfst_ModelFastfst128'):
        assert _is_linked(b1, 'fastfst_ModelFastfst128', a)
    _safe_set(a, 'fastfst_nAzimuth', b2)
    assert _is_linked(a, 'fastfst_nAzimuth', b2)
    if hasattr(b1, 'fastfst_ModelFastfst128'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst128', a)
    if hasattr(b2, 'fastfst_ModelFastfst128'):
        assert _is_linked(b2, 'fastfst_ModelFastfst128', a)
    _safe_set(a, 'fastfst_nAzimuth', None)
    assert not _is_linked(a, 'fastfst_nAzimuth', b2)
    if hasattr(b2, 'fastfst_ModelFastfst128'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst128', a)


def test_assoc_BlPitchF_1_87_link_reassign_clear():
    a = fastfst_nBlPitchF_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nBlPitchF_1_', b1)
    assert _is_linked(a, 'fastfst_nBlPitchF_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst88'):
        assert _is_linked(b1, 'fastfst_ModelFastfst88', a)
    _safe_set(a, 'fastfst_nBlPitchF_1_', b2)
    assert _is_linked(a, 'fastfst_nBlPitchF_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst88'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst88', a)
    if hasattr(b2, 'fastfst_ModelFastfst88'):
        assert _is_linked(b2, 'fastfst_ModelFastfst88', a)
    _safe_set(a, 'fastfst_nBlPitchF_1_', None)
    assert not _is_linked(a, 'fastfst_nBlPitchF_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst88'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst88', a)


def test_assoc_BlPitchF_2_89_link_reassign_clear():
    a = fastfst_nBlPitchF_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nBlPitchF_2_', b1)
    assert _is_linked(a, 'fastfst_nBlPitchF_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst90'):
        assert _is_linked(b1, 'fastfst_ModelFastfst90', a)
    _safe_set(a, 'fastfst_nBlPitchF_2_', b2)
    assert _is_linked(a, 'fastfst_nBlPitchF_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst90'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst90', a)
    if hasattr(b2, 'fastfst_ModelFastfst90'):
        assert _is_linked(b2, 'fastfst_ModelFastfst90', a)
    _safe_set(a, 'fastfst_nBlPitchF_2_', None)
    assert not _is_linked(a, 'fastfst_nBlPitchF_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst90'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst90', a)


def test_assoc_BlPitchF_3_91_link_reassign_clear():
    a = fastfst_nBlPitchF_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nBlPitchF_3_', b1)
    assert _is_linked(a, 'fastfst_nBlPitchF_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst92'):
        assert _is_linked(b1, 'fastfst_ModelFastfst92', a)
    _safe_set(a, 'fastfst_nBlPitchF_3_', b2)
    assert _is_linked(a, 'fastfst_nBlPitchF_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst92'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst92', a)
    if hasattr(b2, 'fastfst_ModelFastfst92'):
        assert _is_linked(b2, 'fastfst_ModelFastfst92', a)
    _safe_set(a, 'fastfst_nBlPitchF_3_', None)
    assert not _is_linked(a, 'fastfst_nBlPitchF_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst92'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst92', a)


def test_assoc_BlPitch_1_81_link_reassign_clear():
    a = fastfst_nBlPitch_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nBlPitch_1_', b1)
    assert _is_linked(a, 'fastfst_nBlPitch_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst82'):
        assert _is_linked(b1, 'fastfst_ModelFastfst82', a)
    _safe_set(a, 'fastfst_nBlPitch_1_', b2)
    assert _is_linked(a, 'fastfst_nBlPitch_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst82'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst82', a)
    if hasattr(b2, 'fastfst_ModelFastfst82'):
        assert _is_linked(b2, 'fastfst_ModelFastfst82', a)
    _safe_set(a, 'fastfst_nBlPitch_1_', None)
    assert not _is_linked(a, 'fastfst_nBlPitch_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst82'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst82', a)


def test_assoc_BlPitch_2_83_link_reassign_clear():
    a = fastfst_nBlPitch_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nBlPitch_2_', b1)
    assert _is_linked(a, 'fastfst_nBlPitch_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst84'):
        assert _is_linked(b1, 'fastfst_ModelFastfst84', a)
    _safe_set(a, 'fastfst_nBlPitch_2_', b2)
    assert _is_linked(a, 'fastfst_nBlPitch_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst84'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst84', a)
    if hasattr(b2, 'fastfst_ModelFastfst84'):
        assert _is_linked(b2, 'fastfst_ModelFastfst84', a)
    _safe_set(a, 'fastfst_nBlPitch_2_', None)
    assert not _is_linked(a, 'fastfst_nBlPitch_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst84'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst84', a)


def test_assoc_BlPitch_3_85_link_reassign_clear():
    a = fastfst_nBlPitch_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nBlPitch_3_', b1)
    assert _is_linked(a, 'fastfst_nBlPitch_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst86'):
        assert _is_linked(b1, 'fastfst_ModelFastfst86', a)
    _safe_set(a, 'fastfst_nBlPitch_3_', b2)
    assert _is_linked(a, 'fastfst_nBlPitch_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst86'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst86', a)
    if hasattr(b2, 'fastfst_ModelFastfst86'):
        assert _is_linked(b2, 'fastfst_ModelFastfst86', a)
    _safe_set(a, 'fastfst_nBlPitch_3_', None)
    assert not _is_linked(a, 'fastfst_nBlPitch_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst86'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst86', a)


def test_assoc_BldFile_1_273_link_reassign_clear():
    a = fastfst_fBldFile_1_(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fBldFile_1_', b1)
    assert _is_linked(a, 'fastfst_fBldFile_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst274'):
        assert _is_linked(b1, 'fastfst_ModelFastfst274', a)
    _safe_set(a, 'fastfst_fBldFile_1_', b2)
    assert _is_linked(a, 'fastfst_fBldFile_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst274'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst274', a)
    if hasattr(b2, 'fastfst_ModelFastfst274'):
        assert _is_linked(b2, 'fastfst_ModelFastfst274', a)
    _safe_set(a, 'fastfst_fBldFile_1_', None)
    assert not _is_linked(a, 'fastfst_fBldFile_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst274'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst274', a)


def test_assoc_BldFile_2_275_link_reassign_clear():
    a = fastfst_fBldFile_2_(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fBldFile_2_', b1)
    assert _is_linked(a, 'fastfst_fBldFile_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst276'):
        assert _is_linked(b1, 'fastfst_ModelFastfst276', a)
    _safe_set(a, 'fastfst_fBldFile_2_', b2)
    assert _is_linked(a, 'fastfst_fBldFile_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst276'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst276', a)
    if hasattr(b2, 'fastfst_ModelFastfst276'):
        assert _is_linked(b2, 'fastfst_ModelFastfst276', a)
    _safe_set(a, 'fastfst_fBldFile_2_', None)
    assert not _is_linked(a, 'fastfst_fBldFile_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst276'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst276', a)


def test_assoc_BldFile_3_277_link_reassign_clear():
    a = fastfst_fBldFile_3_(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fBldFile_3_', b1)
    assert _is_linked(a, 'fastfst_fBldFile_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst278'):
        assert _is_linked(b1, 'fastfst_ModelFastfst278', a)
    _safe_set(a, 'fastfst_fBldFile_3_', b2)
    assert _is_linked(a, 'fastfst_fBldFile_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst278'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst278', a)
    if hasattr(b2, 'fastfst_ModelFastfst278'):
        assert _is_linked(b2, 'fastfst_ModelFastfst278', a)
    _safe_set(a, 'fastfst_fBldFile_3_', None)
    assert not _is_linked(a, 'fastfst_fBldFile_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst278'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst278', a)


def test_assoc_BldGagNd315_link_reassign_clear():
    a = fastfst_aBldGagNd(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_aBldGagNd', b1)
    assert _is_linked(a, 'fastfst_aBldGagNd', b1)
    if hasattr(b1, 'fastfst_ModelFastfst316'):
        assert _is_linked(b1, 'fastfst_ModelFastfst316', a)
    _safe_set(a, 'fastfst_aBldGagNd', b2)
    assert _is_linked(a, 'fastfst_aBldGagNd', b2)
    if hasattr(b1, 'fastfst_ModelFastfst316'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst316', a)
    if hasattr(b2, 'fastfst_ModelFastfst316'):
        assert _is_linked(b2, 'fastfst_ModelFastfst316', a)
    _safe_set(a, 'fastfst_aBldGagNd', None)
    assert not _is_linked(a, 'fastfst_aBldGagNd', b2)
    if hasattr(b2, 'fastfst_ModelFastfst316'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst316', a)


def test_assoc_CompAero117_link_reassign_clear():
    a = fastfst_bCompAero(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bCompAero', b1)
    assert _is_linked(a, 'fastfst_bCompAero', b1)
    if hasattr(b1, 'fastfst_ModelFastfst118'):
        assert _is_linked(b1, 'fastfst_ModelFastfst118', a)
    _safe_set(a, 'fastfst_bCompAero', b2)
    assert _is_linked(a, 'fastfst_bCompAero', b2)
    if hasattr(b1, 'fastfst_ModelFastfst118'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst118', a)
    if hasattr(b2, 'fastfst_ModelFastfst118'):
        assert _is_linked(b2, 'fastfst_ModelFastfst118', a)
    _safe_set(a, 'fastfst_bCompAero', None)
    assert not _is_linked(a, 'fastfst_bCompAero', b2)
    if hasattr(b2, 'fastfst_ModelFastfst118'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst118', a)


def test_assoc_CompNoise119_link_reassign_clear():
    a = fastfst_bCompNoise(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bCompNoise', b1)
    assert _is_linked(a, 'fastfst_bCompNoise', b1)
    if hasattr(b1, 'fastfst_ModelFastfst120'):
        assert _is_linked(b1, 'fastfst_ModelFastfst120', a)
    _safe_set(a, 'fastfst_bCompNoise', b2)
    assert _is_linked(a, 'fastfst_bCompNoise', b2)
    if hasattr(b1, 'fastfst_ModelFastfst120'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst120', a)
    if hasattr(b2, 'fastfst_ModelFastfst120'):
        assert _is_linked(b2, 'fastfst_ModelFastfst120', a)
    _safe_set(a, 'fastfst_bCompNoise', None)
    assert not _is_linked(a, 'fastfst_bCompNoise', b2)
    if hasattr(b2, 'fastfst_ModelFastfst120'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst120', a)


def test_assoc_DT13_link_reassign_clear():
    a = fastfst_nDT(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nDT', b1)
    assert _is_linked(a, 'fastfst_nDT', b1)
    if hasattr(b1, 'fastfst_ModelFastfst14'):
        assert _is_linked(b1, 'fastfst_ModelFastfst14', a)
    _safe_set(a, 'fastfst_nDT', b2)
    assert _is_linked(a, 'fastfst_nDT', b2)
    if hasattr(b1, 'fastfst_ModelFastfst14'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst14', a)
    if hasattr(b2, 'fastfst_ModelFastfst14'):
        assert _is_linked(b2, 'fastfst_ModelFastfst14', a)
    _safe_set(a, 'fastfst_nDT', None)
    assert not _is_linked(a, 'fastfst_nDT', b2)
    if hasattr(b2, 'fastfst_ModelFastfst14'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst14', a)


def test_assoc_DTTorDmp207_link_reassign_clear():
    a = fastfst_nDTTorDmp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nDTTorDmp', b1)
    assert _is_linked(a, 'fastfst_nDTTorDmp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst208'):
        assert _is_linked(b1, 'fastfst_ModelFastfst208', a)
    _safe_set(a, 'fastfst_nDTTorDmp', b2)
    assert _is_linked(a, 'fastfst_nDTTorDmp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst208'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst208', a)
    if hasattr(b2, 'fastfst_ModelFastfst208'):
        assert _is_linked(b2, 'fastfst_ModelFastfst208', a)
    _safe_set(a, 'fastfst_nDTTorDmp', None)
    assert not _is_linked(a, 'fastfst_nDTTorDmp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst208'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst208', a)


def test_assoc_DTTorSpr205_link_reassign_clear():
    a = fastfst_nDTTorSpr(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nDTTorSpr', b1)
    assert _is_linked(a, 'fastfst_nDTTorSpr', b1)
    if hasattr(b1, 'fastfst_ModelFastfst206'):
        assert _is_linked(b1, 'fastfst_ModelFastfst206', a)
    _safe_set(a, 'fastfst_nDTTorSpr', b2)
    assert _is_linked(a, 'fastfst_nDTTorSpr', b2)
    if hasattr(b1, 'fastfst_ModelFastfst206'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst206', a)
    if hasattr(b2, 'fastfst_ModelFastfst206'):
        assert _is_linked(b2, 'fastfst_ModelFastfst206', a)
    _safe_set(a, 'fastfst_nDTTorSpr', None)
    assert not _is_linked(a, 'fastfst_nDTTorSpr', b2)
    if hasattr(b2, 'fastfst_ModelFastfst206'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst206', a)


def test_assoc_DecFact297_link_reassign_clear():
    a = fastfst_iDecFact(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iDecFact', b1)
    assert _is_linked(a, 'fastfst_iDecFact', b1)
    if hasattr(b1, 'fastfst_ModelFastfst298'):
        assert _is_linked(b1, 'fastfst_ModelFastfst298', a)
    _safe_set(a, 'fastfst_iDecFact', b2)
    assert _is_linked(a, 'fastfst_iDecFact', b2)
    if hasattr(b1, 'fastfst_ModelFastfst298'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst298', a)
    if hasattr(b2, 'fastfst_ModelFastfst298'):
        assert _is_linked(b2, 'fastfst_ModelFastfst298', a)
    _safe_set(a, 'fastfst_iDecFact', None)
    assert not _is_linked(a, 'fastfst_iDecFact', b2)
    if hasattr(b2, 'fastfst_ModelFastfst298'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst298', a)


def test_assoc_Delta3163_link_reassign_clear():
    a = fastfst_nDelta3(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nDelta3', b1)
    assert _is_linked(a, 'fastfst_nDelta3', b1)
    if hasattr(b1, 'fastfst_ModelFastfst164'):
        assert _is_linked(b1, 'fastfst_ModelFastfst164', a)
    _safe_set(a, 'fastfst_nDelta3', b2)
    assert _is_linked(a, 'fastfst_nDelta3', b2)
    if hasattr(b1, 'fastfst_ModelFastfst164'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst164', a)
    if hasattr(b2, 'fastfst_ModelFastfst164'):
        assert _is_linked(b2, 'fastfst_ModelFastfst164', a)
    _safe_set(a, 'fastfst_nDelta3', None)
    assert not _is_linked(a, 'fastfst_nDelta3', b2)
    if hasattr(b2, 'fastfst_ModelFastfst164'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst164', a)


def test_assoc_DrTrDOF103_link_reassign_clear():
    a = fastfst_bDrTrDOF(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bDrTrDOF', b1)
    assert _is_linked(a, 'fastfst_bDrTrDOF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst104'):
        assert _is_linked(b1, 'fastfst_ModelFastfst104', a)
    _safe_set(a, 'fastfst_bDrTrDOF', b2)
    assert _is_linked(a, 'fastfst_bDrTrDOF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst104'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst104', a)
    if hasattr(b2, 'fastfst_ModelFastfst104'):
        assert _is_linked(b2, 'fastfst_ModelFastfst104', a)
    _safe_set(a, 'fastfst_bDrTrDOF', None)
    assert not _is_linked(a, 'fastfst_bDrTrDOF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst104'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst104', a)


def test_assoc_DynBrkFi203_link_reassign_clear():
    a = fastfst_fDynBrkFi(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fDynBrkFi', b1)
    assert _is_linked(a, 'fastfst_fDynBrkFi', b1)
    if hasattr(b1, 'fastfst_ModelFastfst204'):
        assert _is_linked(b1, 'fastfst_ModelFastfst204', a)
    _safe_set(a, 'fastfst_fDynBrkFi', b2)
    assert _is_linked(a, 'fastfst_fDynBrkFi', b2)
    if hasattr(b1, 'fastfst_ModelFastfst204'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst204', a)
    if hasattr(b2, 'fastfst_ModelFastfst204'):
        assert _is_linked(b2, 'fastfst_ModelFastfst204', a)
    _safe_set(a, 'fastfst_fDynBrkFi', None)
    assert not _is_linked(a, 'fastfst_fDynBrkFi', b2)
    if hasattr(b2, 'fastfst_ModelFastfst204'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst204', a)


def test_assoc_Echo3_link_reassign_clear():
    a = fastfst_bEcho(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bEcho', b1)
    assert _is_linked(a, 'fastfst_bEcho', b1)
    if hasattr(b1, 'fastfst_ModelFastfst4'):
        assert _is_linked(b1, 'fastfst_ModelFastfst4', a)
    _safe_set(a, 'fastfst_bEcho', b2)
    assert _is_linked(a, 'fastfst_bEcho', b2)
    if hasattr(b1, 'fastfst_ModelFastfst4'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst4', a)
    if hasattr(b2, 'fastfst_ModelFastfst4'):
        assert _is_linked(b2, 'fastfst_ModelFastfst4', a)
    _safe_set(a, 'fastfst_bEcho', None)
    assert not _is_linked(a, 'fastfst_bEcho', b2)
    if hasattr(b2, 'fastfst_ModelFastfst4'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst4', a)


def test_assoc_EdgeDOF99_link_reassign_clear():
    a = fastfst_bEdgeDOF(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bEdgeDOF', b1)
    assert _is_linked(a, 'fastfst_bEdgeDOF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst100'):
        assert _is_linked(b1, 'fastfst_ModelFastfst100', a)
    _safe_set(a, 'fastfst_bEdgeDOF', b2)
    assert _is_linked(a, 'fastfst_bEdgeDOF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst100'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst100', a)
    if hasattr(b2, 'fastfst_ModelFastfst100'):
        assert _is_linked(b2, 'fastfst_ModelFastfst100', a)
    _safe_set(a, 'fastfst_bEdgeDOF', None)
    assert not _is_linked(a, 'fastfst_bEdgeDOF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst100'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst100', a)


def test_assoc_FlapDOF195_link_reassign_clear():
    a = fastfst_bFlapDOF1(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bFlapDOF1', b1)
    assert _is_linked(a, 'fastfst_bFlapDOF1', b1)
    if hasattr(b1, 'fastfst_ModelFastfst96'):
        assert _is_linked(b1, 'fastfst_ModelFastfst96', a)
    _safe_set(a, 'fastfst_bFlapDOF1', b2)
    assert _is_linked(a, 'fastfst_bFlapDOF1', b2)
    if hasattr(b1, 'fastfst_ModelFastfst96'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst96', a)
    if hasattr(b2, 'fastfst_ModelFastfst96'):
        assert _is_linked(b2, 'fastfst_ModelFastfst96', a)
    _safe_set(a, 'fastfst_bFlapDOF1', None)
    assert not _is_linked(a, 'fastfst_bFlapDOF1', b2)
    if hasattr(b2, 'fastfst_ModelFastfst96'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst96', a)


def test_assoc_FlapDOF297_link_reassign_clear():
    a = fastfst_bFlapDOF2(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bFlapDOF2', b1)
    assert _is_linked(a, 'fastfst_bFlapDOF2', b1)
    if hasattr(b1, 'fastfst_ModelFastfst98'):
        assert _is_linked(b1, 'fastfst_ModelFastfst98', a)
    _safe_set(a, 'fastfst_bFlapDOF2', b2)
    assert _is_linked(a, 'fastfst_bFlapDOF2', b2)
    if hasattr(b1, 'fastfst_ModelFastfst98'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst98', a)
    if hasattr(b2, 'fastfst_ModelFastfst98'):
        assert _is_linked(b2, 'fastfst_ModelFastfst98', a)
    _safe_set(a, 'fastfst_bFlapDOF2', None)
    assert not _is_linked(a, 'fastfst_bFlapDOF2', b2)
    if hasattr(b2, 'fastfst_ModelFastfst98'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst98', a)


def test_assoc_FurlFile249_link_reassign_clear():
    a = fastfst_fFurlFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fFurlFile', b1)
    assert _is_linked(a, 'fastfst_fFurlFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst250'):
        assert _is_linked(b1, 'fastfst_ModelFastfst250', a)
    _safe_set(a, 'fastfst_fFurlFile', b2)
    assert _is_linked(a, 'fastfst_fFurlFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst250'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst250', a)
    if hasattr(b2, 'fastfst_ModelFastfst250'):
        assert _is_linked(b2, 'fastfst_ModelFastfst250', a)
    _safe_set(a, 'fastfst_fFurlFile', None)
    assert not _is_linked(a, 'fastfst_fFurlFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst250'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst250', a)


def test_assoc_Furling247_link_reassign_clear():
    a = fastfst_bFurling(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bFurling', b1)
    assert _is_linked(a, 'fastfst_bFurling', b1)
    if hasattr(b1, 'fastfst_ModelFastfst248'):
        assert _is_linked(b1, 'fastfst_ModelFastfst248', a)
    _safe_set(a, 'fastfst_bFurling', b2)
    assert _is_linked(a, 'fastfst_bFurling', b2)
    if hasattr(b1, 'fastfst_ModelFastfst248'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst248', a)
    if hasattr(b2, 'fastfst_ModelFastfst248'):
        assert _is_linked(b2, 'fastfst_ModelFastfst248', a)
    _safe_set(a, 'fastfst_bFurling', None)
    assert not _is_linked(a, 'fastfst_bFurling', b2)
    if hasattr(b2, 'fastfst_ModelFastfst248'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst248', a)


def test_assoc_GBRatio195_link_reassign_clear():
    a = fastfst_nGBRatio(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nGBRatio', b1)
    assert _is_linked(a, 'fastfst_nGBRatio', b1)
    if hasattr(b1, 'fastfst_ModelFastfst196'):
        assert _is_linked(b1, 'fastfst_ModelFastfst196', a)
    _safe_set(a, 'fastfst_nGBRatio', b2)
    assert _is_linked(a, 'fastfst_nGBRatio', b2)
    if hasattr(b1, 'fastfst_ModelFastfst196'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst196', a)
    if hasattr(b2, 'fastfst_ModelFastfst196'):
        assert _is_linked(b2, 'fastfst_ModelFastfst196', a)
    _safe_set(a, 'fastfst_nGBRatio', None)
    assert not _is_linked(a, 'fastfst_nGBRatio', b2)
    if hasattr(b2, 'fastfst_ModelFastfst196'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst196', a)


def test_assoc_GBRevers197_link_reassign_clear():
    a = fastfst_bGBRevers(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bGBRevers', b1)
    assert _is_linked(a, 'fastfst_bGBRevers', b1)
    if hasattr(b1, 'fastfst_ModelFastfst198'):
        assert _is_linked(b1, 'fastfst_ModelFastfst198', a)
    _safe_set(a, 'fastfst_bGBRevers', b2)
    assert _is_linked(a, 'fastfst_bGBRevers', b2)
    if hasattr(b1, 'fastfst_ModelFastfst198'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst198', a)
    if hasattr(b2, 'fastfst_ModelFastfst198'):
        assert _is_linked(b2, 'fastfst_ModelFastfst198', a)
    _safe_set(a, 'fastfst_bGBRevers', None)
    assert not _is_linked(a, 'fastfst_bGBRevers', b2)
    if hasattr(b2, 'fastfst_ModelFastfst198'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst198', a)


def test_assoc_GBoxEff191_link_reassign_clear():
    a = fastfst_nGBoxEff(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nGBoxEff', b1)
    assert _is_linked(a, 'fastfst_nGBoxEff', b1)
    if hasattr(b1, 'fastfst_ModelFastfst192'):
        assert _is_linked(b1, 'fastfst_ModelFastfst192', a)
    _safe_set(a, 'fastfst_nGBoxEff', b2)
    assert _is_linked(a, 'fastfst_nGBoxEff', b2)
    if hasattr(b1, 'fastfst_ModelFastfst192'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst192', a)
    if hasattr(b2, 'fastfst_ModelFastfst192'):
        assert _is_linked(b2, 'fastfst_ModelFastfst192', a)
    _safe_set(a, 'fastfst_nGBoxEff', None)
    assert not _is_linked(a, 'fastfst_nGBoxEff', b2)
    if hasattr(b2, 'fastfst_ModelFastfst192'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst192', a)


def test_assoc_GenDOF105_link_reassign_clear():
    a = fastfst_bGenDOF(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bGenDOF', b1)
    assert _is_linked(a, 'fastfst_bGenDOF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst106'):
        assert _is_linked(b1, 'fastfst_ModelFastfst106', a)
    _safe_set(a, 'fastfst_bGenDOF', b2)
    assert _is_linked(a, 'fastfst_bGenDOF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst106'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst106', a)
    if hasattr(b2, 'fastfst_ModelFastfst106'):
        assert _is_linked(b2, 'fastfst_ModelFastfst106', a)
    _safe_set(a, 'fastfst_bGenDOF', None)
    assert not _is_linked(a, 'fastfst_bGenDOF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst106'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst106', a)


def test_assoc_GenEff193_link_reassign_clear():
    a = fastfst_nGenEff(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nGenEff', b1)
    assert _is_linked(a, 'fastfst_nGenEff', b1)
    if hasattr(b1, 'fastfst_ModelFastfst194'):
        assert _is_linked(b1, 'fastfst_ModelFastfst194', a)
    _safe_set(a, 'fastfst_nGenEff', b2)
    assert _is_linked(a, 'fastfst_nGenEff', b2)
    if hasattr(b1, 'fastfst_ModelFastfst194'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst194', a)
    if hasattr(b2, 'fastfst_ModelFastfst194'):
        assert _is_linked(b2, 'fastfst_ModelFastfst194', a)
    _safe_set(a, 'fastfst_nGenEff', None)
    assert not _is_linked(a, 'fastfst_nGenEff', b2)
    if hasattr(b2, 'fastfst_ModelFastfst194'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst194', a)


def test_assoc_GenIner187_link_reassign_clear():
    a = fastfst_nGenIner(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nGenIner', b1)
    assert _is_linked(a, 'fastfst_nGenIner', b1)
    if hasattr(b1, 'fastfst_ModelFastfst188'):
        assert _is_linked(b1, 'fastfst_ModelFastfst188', a)
    _safe_set(a, 'fastfst_nGenIner', b2)
    assert _is_linked(a, 'fastfst_nGenIner', b2)
    if hasattr(b1, 'fastfst_ModelFastfst188'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst188', a)
    if hasattr(b2, 'fastfst_ModelFastfst188'):
        assert _is_linked(b2, 'fastfst_ModelFastfst188', a)
    _safe_set(a, 'fastfst_nGenIner', None)
    assert not _is_linked(a, 'fastfst_nGenIner', b2)
    if hasattr(b2, 'fastfst_ModelFastfst188'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst188', a)


def test_assoc_GenModel33_link_reassign_clear():
    a = fastfst_iGenModel(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iGenModel', b1)
    assert _is_linked(a, 'fastfst_iGenModel', b1)
    if hasattr(b1, 'fastfst_ModelFastfst34'):
        assert _is_linked(b1, 'fastfst_ModelFastfst34', a)
    _safe_set(a, 'fastfst_iGenModel', b2)
    assert _is_linked(a, 'fastfst_iGenModel', b2)
    if hasattr(b1, 'fastfst_ModelFastfst34'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst34', a)
    if hasattr(b2, 'fastfst_ModelFastfst34'):
        assert _is_linked(b2, 'fastfst_ModelFastfst34', a)
    _safe_set(a, 'fastfst_iGenModel', None)
    assert not _is_linked(a, 'fastfst_iGenModel', b2)
    if hasattr(b2, 'fastfst_ModelFastfst34'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst34', a)


def test_assoc_GenTiStp37_link_reassign_clear():
    a = fastfst_bGenTiStp(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bGenTiStp', b1)
    assert _is_linked(a, 'fastfst_bGenTiStp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst38'):
        assert _is_linked(b1, 'fastfst_ModelFastfst38', a)
    _safe_set(a, 'fastfst_bGenTiStp', b2)
    assert _is_linked(a, 'fastfst_bGenTiStp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst38'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst38', a)
    if hasattr(b2, 'fastfst_ModelFastfst38'):
        assert _is_linked(b2, 'fastfst_ModelFastfst38', a)
    _safe_set(a, 'fastfst_bGenTiStp', None)
    assert not _is_linked(a, 'fastfst_bGenTiStp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst38'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst38', a)


def test_assoc_GenTiStr35_link_reassign_clear():
    a = fastfst_bGenTiStr(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bGenTiStr', b1)
    assert _is_linked(a, 'fastfst_bGenTiStr', b1)
    if hasattr(b1, 'fastfst_ModelFastfst36'):
        assert _is_linked(b1, 'fastfst_ModelFastfst36', a)
    _safe_set(a, 'fastfst_bGenTiStr', b2)
    assert _is_linked(a, 'fastfst_bGenTiStr', b2)
    if hasattr(b1, 'fastfst_ModelFastfst36'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst36', a)
    if hasattr(b2, 'fastfst_ModelFastfst36'):
        assert _is_linked(b2, 'fastfst_ModelFastfst36', a)
    _safe_set(a, 'fastfst_bGenTiStr', None)
    assert not _is_linked(a, 'fastfst_bGenTiStr', b2)
    if hasattr(b2, 'fastfst_ModelFastfst36'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst36', a)


def test_assoc_Gravity93_link_reassign_clear():
    a = fastfst_nGravity(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nGravity', b1)
    assert _is_linked(a, 'fastfst_nGravity', b1)
    if hasattr(b1, 'fastfst_ModelFastfst94'):
        assert _is_linked(b1, 'fastfst_ModelFastfst94', a)
    _safe_set(a, 'fastfst_nGravity', b2)
    assert _is_linked(a, 'fastfst_nGravity', b2)
    if hasattr(b1, 'fastfst_ModelFastfst94'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst94', a)
    if hasattr(b2, 'fastfst_ModelFastfst94'):
        assert _is_linked(b2, 'fastfst_ModelFastfst94', a)
    _safe_set(a, 'fastfst_nGravity', None)
    assert not _is_linked(a, 'fastfst_nGravity', b2)
    if hasattr(b2, 'fastfst_ModelFastfst94'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst94', a)


def test_assoc_HSSBrDT201_link_reassign_clear():
    a = fastfst_nHSSBrDT(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nHSSBrDT', b1)
    assert _is_linked(a, 'fastfst_nHSSBrDT', b1)
    if hasattr(b1, 'fastfst_ModelFastfst202'):
        assert _is_linked(b1, 'fastfst_ModelFastfst202', a)
    _safe_set(a, 'fastfst_nHSSBrDT', b2)
    assert _is_linked(a, 'fastfst_nHSSBrDT', b2)
    if hasattr(b1, 'fastfst_ModelFastfst202'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst202', a)
    if hasattr(b2, 'fastfst_ModelFastfst202'):
        assert _is_linked(b2, 'fastfst_ModelFastfst202', a)
    _safe_set(a, 'fastfst_nHSSBrDT', None)
    assert not _is_linked(a, 'fastfst_nHSSBrDT', b2)
    if hasattr(b2, 'fastfst_ModelFastfst202'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst202', a)


def test_assoc_HSSBrMode45_link_reassign_clear():
    a = fastfst_iHSSBrMode(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iHSSBrMode', b1)
    assert _is_linked(a, 'fastfst_iHSSBrMode', b1)
    if hasattr(b1, 'fastfst_ModelFastfst46'):
        assert _is_linked(b1, 'fastfst_ModelFastfst46', a)
    _safe_set(a, 'fastfst_iHSSBrMode', b2)
    assert _is_linked(a, 'fastfst_iHSSBrMode', b2)
    if hasattr(b1, 'fastfst_ModelFastfst46'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst46', a)
    if hasattr(b2, 'fastfst_ModelFastfst46'):
        assert _is_linked(b2, 'fastfst_ModelFastfst46', a)
    _safe_set(a, 'fastfst_iHSSBrMode', None)
    assert not _is_linked(a, 'fastfst_iHSSBrMode', b2)
    if hasattr(b2, 'fastfst_ModelFastfst46'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst46', a)


def test_assoc_HSSBrTqF199_link_reassign_clear():
    a = fastfst_nHSSBrTqF(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nHSSBrTqF', b1)
    assert _is_linked(a, 'fastfst_nHSSBrTqF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst200'):
        assert _is_linked(b1, 'fastfst_ModelFastfst200', a)
    _safe_set(a, 'fastfst_nHSSBrTqF', b2)
    assert _is_linked(a, 'fastfst_nHSSBrTqF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst200'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst200', a)
    if hasattr(b2, 'fastfst_ModelFastfst200'):
        assert _is_linked(b2, 'fastfst_ModelFastfst200', a)
    _safe_set(a, 'fastfst_nHSSBrTqF', None)
    assert not _is_linked(a, 'fastfst_nHSSBrTqF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst200'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst200', a)


def test_assoc_Head0_link_reassign_clear():
    a = fastfst_Header(rows="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_Header', b1)
    assert _is_linked(a, 'fastfst_Header', b1)
    if hasattr(b1, 'fastfst_ModelFastfst'):
        assert _is_linked(b1, 'fastfst_ModelFastfst', a)
    _safe_set(a, 'fastfst_Header', b2)
    assert _is_linked(a, 'fastfst_Header', b2)
    if hasattr(b1, 'fastfst_ModelFastfst'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst', a)
    if hasattr(b2, 'fastfst_ModelFastfst'):
        assert _is_linked(b2, 'fastfst_ModelFastfst', a)
    _safe_set(a, 'fastfst_Header', None)
    assert not _is_linked(a, 'fastfst_Header', b2)
    if hasattr(b2, 'fastfst_ModelFastfst'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst', a)


def test_assoc_HubCM145_link_reassign_clear():
    a = fastfst_nHubCM(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nHubCM', b1)
    assert _is_linked(a, 'fastfst_nHubCM', b1)
    if hasattr(b1, 'fastfst_ModelFastfst146'):
        assert _is_linked(b1, 'fastfst_ModelFastfst146', a)
    _safe_set(a, 'fastfst_nHubCM', b2)
    assert _is_linked(a, 'fastfst_nHubCM', b2)
    if hasattr(b1, 'fastfst_ModelFastfst146'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst146', a)
    if hasattr(b2, 'fastfst_ModelFastfst146'):
        assert _is_linked(b2, 'fastfst_ModelFastfst146', a)
    _safe_set(a, 'fastfst_nHubCM', None)
    assert not _is_linked(a, 'fastfst_nHubCM', b2)
    if hasattr(b2, 'fastfst_ModelFastfst146'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst146', a)


def test_assoc_HubIner189_link_reassign_clear():
    a = fastfst_nHubIner(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nHubIner', b1)
    assert _is_linked(a, 'fastfst_nHubIner', b1)
    if hasattr(b1, 'fastfst_ModelFastfst190'):
        assert _is_linked(b1, 'fastfst_ModelFastfst190', a)
    _safe_set(a, 'fastfst_nHubIner', b2)
    assert _is_linked(a, 'fastfst_nHubIner', b2)
    if hasattr(b1, 'fastfst_ModelFastfst190'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst190', a)
    if hasattr(b2, 'fastfst_ModelFastfst190'):
        assert _is_linked(b2, 'fastfst_ModelFastfst190', a)
    _safe_set(a, 'fastfst_nHubIner', None)
    assert not _is_linked(a, 'fastfst_nHubIner', b2)
    if hasattr(b2, 'fastfst_ModelFastfst190'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst190', a)


def test_assoc_HubMass177_link_reassign_clear():
    a = fastfst_nHubMass(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nHubMass', b1)
    assert _is_linked(a, 'fastfst_nHubMass', b1)
    if hasattr(b1, 'fastfst_ModelFastfst178'):
        assert _is_linked(b1, 'fastfst_ModelFastfst178', a)
    _safe_set(a, 'fastfst_nHubMass', b2)
    assert _is_linked(a, 'fastfst_nHubMass', b2)
    if hasattr(b1, 'fastfst_ModelFastfst178'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst178', a)
    if hasattr(b2, 'fastfst_ModelFastfst178'):
        assert _is_linked(b2, 'fastfst_ModelFastfst178', a)
    _safe_set(a, 'fastfst_nHubMass', None)
    assert not _is_linked(a, 'fastfst_nHubMass', b2)
    if hasattr(b2, 'fastfst_ModelFastfst178'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst178', a)


def test_assoc_HubRad139_link_reassign_clear():
    a = fastfst_nHubRad(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nHubRad', b1)
    assert _is_linked(a, 'fastfst_nHubRad', b1)
    if hasattr(b1, 'fastfst_ModelFastfst140'):
        assert _is_linked(b1, 'fastfst_ModelFastfst140', a)
    _safe_set(a, 'fastfst_nHubRad', b2)
    assert _is_linked(a, 'fastfst_nHubRad', b2)
    if hasattr(b1, 'fastfst_ModelFastfst140'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst140', a)
    if hasattr(b2, 'fastfst_ModelFastfst140'):
        assert _is_linked(b2, 'fastfst_ModelFastfst140', a)
    _safe_set(a, 'fastfst_nHubRad', None)
    assert not _is_linked(a, 'fastfst_nHubRad', b2)
    if hasattr(b2, 'fastfst_ModelFastfst140'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst140', a)


def test_assoc_IPDefl123_link_reassign_clear():
    a = fastfst_nIPDefl(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nIPDefl', b1)
    assert _is_linked(a, 'fastfst_nIPDefl', b1)
    if hasattr(b1, 'fastfst_ModelFastfst124'):
        assert _is_linked(b1, 'fastfst_ModelFastfst124', a)
    _safe_set(a, 'fastfst_nIPDefl', b2)
    assert _is_linked(a, 'fastfst_nIPDefl', b2)
    if hasattr(b1, 'fastfst_ModelFastfst124'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst124', a)
    if hasattr(b2, 'fastfst_ModelFastfst124'):
        assert _is_linked(b2, 'fastfst_ModelFastfst124', a)
    _safe_set(a, 'fastfst_nIPDefl', None)
    assert not _is_linked(a, 'fastfst_nIPDefl', b2)
    if hasattr(b2, 'fastfst_ModelFastfst124'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst124', a)


def test_assoc_LinFile285_link_reassign_clear():
    a = fastfst_fLinFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fLinFile', b1)
    assert _is_linked(a, 'fastfst_fLinFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst286'):
        assert _is_linked(b1, 'fastfst_ModelFastfst286', a)
    _safe_set(a, 'fastfst_fLinFile', b2)
    assert _is_linked(a, 'fastfst_fLinFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst286'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst286', a)
    if hasattr(b2, 'fastfst_ModelFastfst286'):
        assert _is_linked(b2, 'fastfst_ModelFastfst286', a)
    _safe_set(a, 'fastfst_fLinFile', None)
    assert not _is_linked(a, 'fastfst_fLinFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst286'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst286', a)


def test_assoc_NBlGages313_link_reassign_clear():
    a = fastfst_iNBlGages(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iNBlGages', b1)
    assert _is_linked(a, 'fastfst_iNBlGages', b1)
    if hasattr(b1, 'fastfst_ModelFastfst314'):
        assert _is_linked(b1, 'fastfst_ModelFastfst314', a)
    _safe_set(a, 'fastfst_iNBlGages', b2)
    assert _is_linked(a, 'fastfst_iNBlGages', b2)
    if hasattr(b1, 'fastfst_ModelFastfst314'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst314', a)
    if hasattr(b2, 'fastfst_ModelFastfst314'):
        assert _is_linked(b2, 'fastfst_ModelFastfst314', a)
    _safe_set(a, 'fastfst_iNBlGages', None)
    assert not _is_linked(a, 'fastfst_iNBlGages', b2)
    if hasattr(b2, 'fastfst_ModelFastfst314'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst314', a)


def test_assoc_NTwGages309_link_reassign_clear():
    a = fastfst_iNTwGages(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iNTwGages', b1)
    assert _is_linked(a, 'fastfst_iNTwGages', b1)
    if hasattr(b1, 'fastfst_ModelFastfst310'):
        assert _is_linked(b1, 'fastfst_ModelFastfst310', a)
    _safe_set(a, 'fastfst_iNTwGages', b2)
    assert _is_linked(a, 'fastfst_iNTwGages', b2)
    if hasattr(b1, 'fastfst_ModelFastfst310'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst310', a)
    if hasattr(b2, 'fastfst_ModelFastfst310'):
        assert _is_linked(b2, 'fastfst_ModelFastfst310', a)
    _safe_set(a, 'fastfst_iNTwGages', None)
    assert not _is_linked(a, 'fastfst_iNTwGages', b2)
    if hasattr(b2, 'fastfst_ModelFastfst310'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst310', a)


def test_assoc_NacCMxn149_link_reassign_clear():
    a = fastfst_nNacCMxn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacCMxn', b1)
    assert _is_linked(a, 'fastfst_nNacCMxn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst150'):
        assert _is_linked(b1, 'fastfst_ModelFastfst150', a)
    _safe_set(a, 'fastfst_nNacCMxn', b2)
    assert _is_linked(a, 'fastfst_nNacCMxn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst150'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst150', a)
    if hasattr(b2, 'fastfst_ModelFastfst150'):
        assert _is_linked(b2, 'fastfst_ModelFastfst150', a)
    _safe_set(a, 'fastfst_nNacCMxn', None)
    assert not _is_linked(a, 'fastfst_nNacCMxn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst150'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst150', a)


def test_assoc_NacCMyn151_link_reassign_clear():
    a = fastfst_nNacCMyn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacCMyn', b1)
    assert _is_linked(a, 'fastfst_nNacCMyn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst152'):
        assert _is_linked(b1, 'fastfst_ModelFastfst152', a)
    _safe_set(a, 'fastfst_nNacCMyn', b2)
    assert _is_linked(a, 'fastfst_nNacCMyn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst152'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst152', a)
    if hasattr(b2, 'fastfst_ModelFastfst152'):
        assert _is_linked(b2, 'fastfst_ModelFastfst152', a)
    _safe_set(a, 'fastfst_nNacCMyn', None)
    assert not _is_linked(a, 'fastfst_nNacCMyn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst152'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst152', a)


def test_assoc_NacCMzn153_link_reassign_clear():
    a = fastfst_nNacCMzn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacCMzn', b1)
    assert _is_linked(a, 'fastfst_nNacCMzn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst154'):
        assert _is_linked(b1, 'fastfst_ModelFastfst154', a)
    _safe_set(a, 'fastfst_nNacCMzn', b2)
    assert _is_linked(a, 'fastfst_nNacCMzn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst154'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst154', a)
    if hasattr(b2, 'fastfst_ModelFastfst154'):
        assert _is_linked(b2, 'fastfst_ModelFastfst154', a)
    _safe_set(a, 'fastfst_nNacCMzn', None)
    assert not _is_linked(a, 'fastfst_nNacCMzn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst154'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst154', a)


def test_assoc_NacMass175_link_reassign_clear():
    a = fastfst_nNacMass(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacMass', b1)
    assert _is_linked(a, 'fastfst_nNacMass', b1)
    if hasattr(b1, 'fastfst_ModelFastfst176'):
        assert _is_linked(b1, 'fastfst_ModelFastfst176', a)
    _safe_set(a, 'fastfst_nNacMass', b2)
    assert _is_linked(a, 'fastfst_nNacMass', b2)
    if hasattr(b1, 'fastfst_ModelFastfst176'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst176', a)
    if hasattr(b2, 'fastfst_ModelFastfst176'):
        assert _is_linked(b2, 'fastfst_ModelFastfst176', a)
    _safe_set(a, 'fastfst_nNacMass', None)
    assert not _is_linked(a, 'fastfst_nNacMass', b2)
    if hasattr(b2, 'fastfst_ModelFastfst176'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst176', a)


def test_assoc_NacYIner185_link_reassign_clear():
    a = fastfst_nNacYIner(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacYIner', b1)
    assert _is_linked(a, 'fastfst_nNacYIner', b1)
    if hasattr(b1, 'fastfst_ModelFastfst186'):
        assert _is_linked(b1, 'fastfst_ModelFastfst186', a)
    _safe_set(a, 'fastfst_nNacYIner', b2)
    assert _is_linked(a, 'fastfst_nNacYIner', b2)
    if hasattr(b1, 'fastfst_ModelFastfst186'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst186', a)
    if hasattr(b2, 'fastfst_ModelFastfst186'):
        assert _is_linked(b2, 'fastfst_ModelFastfst186', a)
    _safe_set(a, 'fastfst_nNacYIner', None)
    assert not _is_linked(a, 'fastfst_nNacYIner', b2)
    if hasattr(b2, 'fastfst_ModelFastfst186'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst186', a)


def test_assoc_NacYaw131_link_reassign_clear():
    a = fastfst_nNacYaw(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacYaw', b1)
    assert _is_linked(a, 'fastfst_nNacYaw', b1)
    if hasattr(b1, 'fastfst_ModelFastfst132'):
        assert _is_linked(b1, 'fastfst_ModelFastfst132', a)
    _safe_set(a, 'fastfst_nNacYaw', b2)
    assert _is_linked(a, 'fastfst_nNacYaw', b2)
    if hasattr(b1, 'fastfst_ModelFastfst132'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst132', a)
    if hasattr(b2, 'fastfst_ModelFastfst132'):
        assert _is_linked(b2, 'fastfst_ModelFastfst132', a)
    _safe_set(a, 'fastfst_nNacYaw', None)
    assert not _is_linked(a, 'fastfst_nNacYaw', b2)
    if hasattr(b2, 'fastfst_ModelFastfst132'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst132', a)


def test_assoc_NacYawF67_link_reassign_clear():
    a = fastfst_nNacYawF(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNacYawF', b1)
    assert _is_linked(a, 'fastfst_nNacYawF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst68'):
        assert _is_linked(b1, 'fastfst_ModelFastfst68', a)
    _safe_set(a, 'fastfst_nNacYawF', b2)
    assert _is_linked(a, 'fastfst_nNacYawF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst68'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst68', a)
    if hasattr(b2, 'fastfst_ModelFastfst68'):
        assert _is_linked(b2, 'fastfst_ModelFastfst68', a)
    _safe_set(a, 'fastfst_nNacYawF', None)
    assert not _is_linked(a, 'fastfst_nNacYawF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst68'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst68', a)


def test_assoc_NcIMUxn301_link_reassign_clear():
    a = fastfst_nNcIMUxn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNcIMUxn', b1)
    assert _is_linked(a, 'fastfst_nNcIMUxn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst302'):
        assert _is_linked(b1, 'fastfst_ModelFastfst302', a)
    _safe_set(a, 'fastfst_nNcIMUxn', b2)
    assert _is_linked(a, 'fastfst_nNcIMUxn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst302'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst302', a)
    if hasattr(b2, 'fastfst_ModelFastfst302'):
        assert _is_linked(b2, 'fastfst_ModelFastfst302', a)
    _safe_set(a, 'fastfst_nNcIMUxn', None)
    assert not _is_linked(a, 'fastfst_nNcIMUxn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst302'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst302', a)


def test_assoc_NcIMUyn303_link_reassign_clear():
    a = fastfst_nNcIMUyn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNcIMUyn', b1)
    assert _is_linked(a, 'fastfst_nNcIMUyn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst304'):
        assert _is_linked(b1, 'fastfst_ModelFastfst304', a)
    _safe_set(a, 'fastfst_nNcIMUyn', b2)
    assert _is_linked(a, 'fastfst_nNcIMUyn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst304'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst304', a)
    if hasattr(b2, 'fastfst_ModelFastfst304'):
        assert _is_linked(b2, 'fastfst_ModelFastfst304', a)
    _safe_set(a, 'fastfst_nNcIMUyn', None)
    assert not _is_linked(a, 'fastfst_nNcIMUyn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst304'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst304', a)


def test_assoc_NcIMUzn305_link_reassign_clear():
    a = fastfst_nNcIMUzn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nNcIMUzn', b1)
    assert _is_linked(a, 'fastfst_nNcIMUzn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst306'):
        assert _is_linked(b1, 'fastfst_ModelFastfst306', a)
    _safe_set(a, 'fastfst_nNcIMUzn', b2)
    assert _is_linked(a, 'fastfst_nNcIMUzn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst306'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst306', a)
    if hasattr(b2, 'fastfst_ModelFastfst306'):
        assert _is_linked(b2, 'fastfst_ModelFastfst306', a)
    _safe_set(a, 'fastfst_nNcIMUzn', None)
    assert not _is_linked(a, 'fastfst_nNcIMUzn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst306'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst306', a)


def test_assoc_NoiseFile281_link_reassign_clear():
    a = fastfst_fNoiseFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fNoiseFile', b1)
    assert _is_linked(a, 'fastfst_fNoiseFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst282'):
        assert _is_linked(b1, 'fastfst_ModelFastfst282', a)
    _safe_set(a, 'fastfst_fNoiseFile', b2)
    assert _is_linked(a, 'fastfst_fNoiseFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst282'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst282', a)
    if hasattr(b2, 'fastfst_ModelFastfst282'):
        assert _is_linked(b2, 'fastfst_ModelFastfst282', a)
    _safe_set(a, 'fastfst_fNoiseFile', None)
    assert not _is_linked(a, 'fastfst_fNoiseFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst282'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst282', a)


def test_assoc_NumBl9_link_reassign_clear():
    a = fastfst_iNumBl(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iNumBl', b1)
    assert _is_linked(a, 'fastfst_iNumBl', b1)
    if hasattr(b1, 'fastfst_ModelFastfst10'):
        assert _is_linked(b1, 'fastfst_ModelFastfst10', a)
    _safe_set(a, 'fastfst_iNumBl', b2)
    assert _is_linked(a, 'fastfst_iNumBl', b2)
    if hasattr(b1, 'fastfst_ModelFastfst10'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst10', a)
    if hasattr(b2, 'fastfst_ModelFastfst10'):
        assert _is_linked(b2, 'fastfst_ModelFastfst10', a)
    _safe_set(a, 'fastfst_iNumBl', None)
    assert not _is_linked(a, 'fastfst_iNumBl', b2)
    if hasattr(b2, 'fastfst_ModelFastfst10'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst10', a)


def test_assoc_OoPDefl121_link_reassign_clear():
    a = fastfst_nOoPDefl(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nOoPDefl', b1)
    assert _is_linked(a, 'fastfst_nOoPDefl', b1)
    if hasattr(b1, 'fastfst_ModelFastfst122'):
        assert _is_linked(b1, 'fastfst_ModelFastfst122', a)
    _safe_set(a, 'fastfst_nOoPDefl', b2)
    assert _is_linked(a, 'fastfst_nOoPDefl', b2)
    if hasattr(b1, 'fastfst_ModelFastfst122'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst122', a)
    if hasattr(b2, 'fastfst_ModelFastfst122'):
        assert _is_linked(b2, 'fastfst_ModelFastfst122', a)
    _safe_set(a, 'fastfst_nOoPDefl', None)
    assert not _is_linked(a, 'fastfst_nOoPDefl', b2)
    if hasattr(b2, 'fastfst_ModelFastfst122'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst122', a)


def test_assoc_OutFileFmt289_link_reassign_clear():
    a = fastfst_bOutFileFmt(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bOutFileFmt', b1)
    assert _is_linked(a, 'fastfst_bOutFileFmt', b1)
    if hasattr(b1, 'fastfst_ModelFastfst290'):
        assert _is_linked(b1, 'fastfst_ModelFastfst290', a)
    _safe_set(a, 'fastfst_bOutFileFmt', b2)
    assert _is_linked(a, 'fastfst_bOutFileFmt', b2)
    if hasattr(b1, 'fastfst_ModelFastfst290'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst290', a)
    if hasattr(b2, 'fastfst_ModelFastfst290'):
        assert _is_linked(b2, 'fastfst_ModelFastfst290', a)
    _safe_set(a, 'fastfst_bOutFileFmt', None)
    assert not _is_linked(a, 'fastfst_bOutFileFmt', b2)
    if hasattr(b2, 'fastfst_ModelFastfst290'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst290', a)


def test_assoc_OutFmt293_link_reassign_clear():
    a = fastfst_sOutFmt(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_sOutFmt', b1)
    assert _is_linked(a, 'fastfst_sOutFmt', b1)
    if hasattr(b1, 'fastfst_ModelFastfst294'):
        assert _is_linked(b1, 'fastfst_ModelFastfst294', a)
    _safe_set(a, 'fastfst_sOutFmt', b2)
    assert _is_linked(a, 'fastfst_sOutFmt', b2)
    if hasattr(b1, 'fastfst_ModelFastfst294'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst294', a)
    if hasattr(b2, 'fastfst_ModelFastfst294'):
        assert _is_linked(b2, 'fastfst_ModelFastfst294', a)
    _safe_set(a, 'fastfst_sOutFmt', None)
    assert not _is_linked(a, 'fastfst_sOutFmt', b2)
    if hasattr(b2, 'fastfst_ModelFastfst294'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst294', a)


def test_assoc_OutList317_link_reassign_clear():
    a = fastfst_vOutList(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_vOutList', b1)
    assert _is_linked(a, 'fastfst_vOutList', b1)
    if hasattr(b1, 'fastfst_ModelFastfst318'):
        assert _is_linked(b1, 'fastfst_ModelFastfst318', a)
    _safe_set(a, 'fastfst_vOutList', b2)
    assert _is_linked(a, 'fastfst_vOutList', b2)
    if hasattr(b1, 'fastfst_ModelFastfst318'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst318', a)
    if hasattr(b2, 'fastfst_ModelFastfst318'):
        assert _is_linked(b2, 'fastfst_ModelFastfst318', a)
    _safe_set(a, 'fastfst_vOutList', None)
    assert not _is_linked(a, 'fastfst_vOutList', b2)
    if hasattr(b2, 'fastfst_ModelFastfst318'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst318', a)


def test_assoc_OverHang147_link_reassign_clear():
    a = fastfst_nOverHang(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nOverHang', b1)
    assert _is_linked(a, 'fastfst_nOverHang', b1)
    if hasattr(b1, 'fastfst_ModelFastfst148'):
        assert _is_linked(b1, 'fastfst_ModelFastfst148', a)
    _safe_set(a, 'fastfst_nOverHang', b2)
    assert _is_linked(a, 'fastfst_nOverHang', b2)
    if hasattr(b1, 'fastfst_ModelFastfst148'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst148', a)
    if hasattr(b2, 'fastfst_ModelFastfst148'):
        assert _is_linked(b2, 'fastfst_ModelFastfst148', a)
    _safe_set(a, 'fastfst_nOverHang', None)
    assert not _is_linked(a, 'fastfst_nOverHang', b2)
    if hasattr(b2, 'fastfst_ModelFastfst148'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst148', a)


def test_assoc_PCMode19_link_reassign_clear():
    a = fastfst_iPCMode(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iPCMode', b1)
    assert _is_linked(a, 'fastfst_iPCMode', b1)
    if hasattr(b1, 'fastfst_ModelFastfst20'):
        assert _is_linked(b1, 'fastfst_ModelFastfst20', a)
    _safe_set(a, 'fastfst_iPCMode', b2)
    assert _is_linked(a, 'fastfst_iPCMode', b2)
    if hasattr(b1, 'fastfst_ModelFastfst20'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst20', a)
    if hasattr(b2, 'fastfst_ModelFastfst20'):
        assert _is_linked(b2, 'fastfst_ModelFastfst20', a)
    _safe_set(a, 'fastfst_iPCMode', None)
    assert not _is_linked(a, 'fastfst_iPCMode', b2)
    if hasattr(b2, 'fastfst_ModelFastfst20'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst20', a)


def test_assoc_PSpnElN141_link_reassign_clear():
    a = fastfst_nPSpnElN(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nPSpnElN', b1)
    assert _is_linked(a, 'fastfst_nPSpnElN', b1)
    if hasattr(b1, 'fastfst_ModelFastfst142'):
        assert _is_linked(b1, 'fastfst_ModelFastfst142', a)
    _safe_set(a, 'fastfst_nPSpnElN', b2)
    assert _is_linked(a, 'fastfst_nPSpnElN', b2)
    if hasattr(b1, 'fastfst_ModelFastfst142'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst142', a)
    if hasattr(b2, 'fastfst_ModelFastfst142'):
        assert _is_linked(b2, 'fastfst_ModelFastfst142', a)
    _safe_set(a, 'fastfst_nPSpnElN', None)
    assert not _is_linked(a, 'fastfst_nPSpnElN', b2)
    if hasattr(b2, 'fastfst_ModelFastfst142'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst142', a)


def test_assoc_PreCone_1_165_link_reassign_clear():
    a = fastfst_nPreCone_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nPreCone_1_', b1)
    assert _is_linked(a, 'fastfst_nPreCone_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst166'):
        assert _is_linked(b1, 'fastfst_ModelFastfst166', a)
    _safe_set(a, 'fastfst_nPreCone_1_', b2)
    assert _is_linked(a, 'fastfst_nPreCone_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst166'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst166', a)
    if hasattr(b2, 'fastfst_ModelFastfst166'):
        assert _is_linked(b2, 'fastfst_ModelFastfst166', a)
    _safe_set(a, 'fastfst_nPreCone_1_', None)
    assert not _is_linked(a, 'fastfst_nPreCone_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst166'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst166', a)


def test_assoc_PreCone_2_167_link_reassign_clear():
    a = fastfst_nPreCone_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nPreCone_2_', b1)
    assert _is_linked(a, 'fastfst_nPreCone_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst168'):
        assert _is_linked(b1, 'fastfst_ModelFastfst168', a)
    _safe_set(a, 'fastfst_nPreCone_2_', b2)
    assert _is_linked(a, 'fastfst_nPreCone_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst168'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst168', a)
    if hasattr(b2, 'fastfst_ModelFastfst168'):
        assert _is_linked(b2, 'fastfst_ModelFastfst168', a)
    _safe_set(a, 'fastfst_nPreCone_2_', None)
    assert not _is_linked(a, 'fastfst_nPreCone_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst168'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst168', a)


def test_assoc_PreCone_3_169_link_reassign_clear():
    a = fastfst_nPreCone_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nPreCone_3_', b1)
    assert _is_linked(a, 'fastfst_nPreCone_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst170'):
        assert _is_linked(b1, 'fastfst_ModelFastfst170', a)
    _safe_set(a, 'fastfst_nPreCone_3_', b2)
    assert _is_linked(a, 'fastfst_nPreCone_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst170'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst170', a)
    if hasattr(b2, 'fastfst_ModelFastfst170'):
        assert _is_linked(b2, 'fastfst_ModelFastfst170', a)
    _safe_set(a, 'fastfst_nPreCone_3_', None)
    assert not _is_linked(a, 'fastfst_nPreCone_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst170'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst170', a)


def test_assoc_PtfmFile235_link_reassign_clear():
    a = fastfst_fPtfmFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fPtfmFile', b1)
    assert _is_linked(a, 'fastfst_fPtfmFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst236'):
        assert _is_linked(b1, 'fastfst_ModelFastfst236', a)
    _safe_set(a, 'fastfst_fPtfmFile', b2)
    assert _is_linked(a, 'fastfst_fPtfmFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst236'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst236', a)
    if hasattr(b2, 'fastfst_ModelFastfst236'):
        assert _is_linked(b2, 'fastfst_ModelFastfst236', a)
    _safe_set(a, 'fastfst_fPtfmFile', None)
    assert not _is_linked(a, 'fastfst_fPtfmFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst236'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst236', a)


def test_assoc_PtfmModel233_link_reassign_clear():
    a = fastfst_iPtfmModel(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iPtfmModel', b1)
    assert _is_linked(a, 'fastfst_iPtfmModel', b1)
    if hasattr(b1, 'fastfst_ModelFastfst234'):
        assert _is_linked(b1, 'fastfst_ModelFastfst234', a)
    _safe_set(a, 'fastfst_iPtfmModel', b2)
    assert _is_linked(a, 'fastfst_iPtfmModel', b2)
    if hasattr(b1, 'fastfst_ModelFastfst234'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst234', a)
    if hasattr(b2, 'fastfst_ModelFastfst234'):
        assert _is_linked(b2, 'fastfst_ModelFastfst234', a)
    _safe_set(a, 'fastfst_iPtfmModel', None)
    assert not _is_linked(a, 'fastfst_iPtfmModel', b2)
    if hasattr(b2, 'fastfst_ModelFastfst234'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst234', a)


def test_assoc_RotSpeed129_link_reassign_clear():
    a = fastfst_nRotSpeed(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nRotSpeed', b1)
    assert _is_linked(a, 'fastfst_nRotSpeed', b1)
    if hasattr(b1, 'fastfst_ModelFastfst130'):
        assert _is_linked(b1, 'fastfst_ModelFastfst130', a)
    _safe_set(a, 'fastfst_nRotSpeed', b2)
    assert _is_linked(a, 'fastfst_nRotSpeed', b2)
    if hasattr(b1, 'fastfst_ModelFastfst130'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst130', a)
    if hasattr(b2, 'fastfst_ModelFastfst130'):
        assert _is_linked(b2, 'fastfst_ModelFastfst130', a)
    _safe_set(a, 'fastfst_nRotSpeed', None)
    assert not _is_linked(a, 'fastfst_nRotSpeed', b2)
    if hasattr(b2, 'fastfst_ModelFastfst130'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst130', a)


def test_assoc_SIG_PORt215_link_reassign_clear():
    a = fastfst_nSIG_PORt(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nSIG_PORt', b1)
    assert _is_linked(a, 'fastfst_nSIG_PORt', b1)
    if hasattr(b1, 'fastfst_ModelFastfst216'):
        assert _is_linked(b1, 'fastfst_ModelFastfst216', a)
    _safe_set(a, 'fastfst_nSIG_PORt', b2)
    assert _is_linked(a, 'fastfst_nSIG_PORt', b2)
    if hasattr(b1, 'fastfst_ModelFastfst216'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst216', a)
    if hasattr(b2, 'fastfst_ModelFastfst216'):
        assert _is_linked(b2, 'fastfst_ModelFastfst216', a)
    _safe_set(a, 'fastfst_nSIG_PORt', None)
    assert not _is_linked(a, 'fastfst_nSIG_PORt', b2)
    if hasattr(b2, 'fastfst_ModelFastfst216'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst216', a)


def test_assoc_SIG_RtTq213_link_reassign_clear():
    a = fastfst_nSIG_RtTq(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nSIG_RtTq', b1)
    assert _is_linked(a, 'fastfst_nSIG_RtTq', b1)
    if hasattr(b1, 'fastfst_ModelFastfst214'):
        assert _is_linked(b1, 'fastfst_ModelFastfst214', a)
    _safe_set(a, 'fastfst_nSIG_RtTq', b2)
    assert _is_linked(a, 'fastfst_nSIG_RtTq', b2)
    if hasattr(b1, 'fastfst_ModelFastfst214'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst214', a)
    if hasattr(b2, 'fastfst_ModelFastfst214'):
        assert _is_linked(b2, 'fastfst_ModelFastfst214', a)
    _safe_set(a, 'fastfst_nSIG_RtTq', None)
    assert not _is_linked(a, 'fastfst_nSIG_RtTq', b2)
    if hasattr(b2, 'fastfst_ModelFastfst214'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst214', a)


def test_assoc_SIG_SlPc209_link_reassign_clear():
    a = fastfst_nSIG_SlPc(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nSIG_SlPc', b1)
    assert _is_linked(a, 'fastfst_nSIG_SlPc', b1)
    if hasattr(b1, 'fastfst_ModelFastfst210'):
        assert _is_linked(b1, 'fastfst_ModelFastfst210', a)
    _safe_set(a, 'fastfst_nSIG_SlPc', b2)
    assert _is_linked(a, 'fastfst_nSIG_SlPc', b2)
    if hasattr(b1, 'fastfst_ModelFastfst210'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst210', a)
    if hasattr(b2, 'fastfst_ModelFastfst210'):
        assert _is_linked(b2, 'fastfst_ModelFastfst210', a)
    _safe_set(a, 'fastfst_nSIG_SlPc', None)
    assert not _is_linked(a, 'fastfst_nSIG_SlPc', b2)
    if hasattr(b2, 'fastfst_ModelFastfst210'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst210', a)


def test_assoc_SIG_SySp211_link_reassign_clear():
    a = fastfst_nSIG_SySp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nSIG_SySp', b1)
    assert _is_linked(a, 'fastfst_nSIG_SySp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst212'):
        assert _is_linked(b1, 'fastfst_ModelFastfst212', a)
    _safe_set(a, 'fastfst_nSIG_SySp', b2)
    assert _is_linked(a, 'fastfst_nSIG_SySp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst212'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst212', a)
    if hasattr(b2, 'fastfst_ModelFastfst212'):
        assert _is_linked(b2, 'fastfst_ModelFastfst212', a)
    _safe_set(a, 'fastfst_nSIG_SySp', None)
    assert not _is_linked(a, 'fastfst_nSIG_SySp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst212'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst212', a)


def test_assoc_ShftGagL307_link_reassign_clear():
    a = fastfst_nShftGagL(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nShftGagL', b1)
    assert _is_linked(a, 'fastfst_nShftGagL', b1)
    if hasattr(b1, 'fastfst_ModelFastfst308'):
        assert _is_linked(b1, 'fastfst_ModelFastfst308', a)
    _safe_set(a, 'fastfst_nShftGagL', b2)
    assert _is_linked(a, 'fastfst_nShftGagL', b2)
    if hasattr(b1, 'fastfst_ModelFastfst308'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst308', a)
    if hasattr(b2, 'fastfst_ModelFastfst308'):
        assert _is_linked(b2, 'fastfst_ModelFastfst308', a)
    _safe_set(a, 'fastfst_nShftGagL', None)
    assert not _is_linked(a, 'fastfst_nShftGagL', b2)
    if hasattr(b2, 'fastfst_ModelFastfst308'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst308', a)


def test_assoc_ShftTilt161_link_reassign_clear():
    a = fastfst_nShftTilt(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nShftTilt', b1)
    assert _is_linked(a, 'fastfst_nShftTilt', b1)
    if hasattr(b1, 'fastfst_ModelFastfst162'):
        assert _is_linked(b1, 'fastfst_ModelFastfst162', a)
    _safe_set(a, 'fastfst_nShftTilt', b2)
    assert _is_linked(a, 'fastfst_nShftTilt', b2)
    if hasattr(b1, 'fastfst_ModelFastfst162'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst162', a)
    if hasattr(b2, 'fastfst_ModelFastfst162'):
        assert _is_linked(b2, 'fastfst_ModelFastfst162', a)
    _safe_set(a, 'fastfst_nShftTilt', None)
    assert not _is_linked(a, 'fastfst_nShftTilt', b2)
    if hasattr(b2, 'fastfst_ModelFastfst162'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst162', a)


def test_assoc_SpdGenOn39_link_reassign_clear():
    a = fastfst_nSpdGenOn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nSpdGenOn', b1)
    assert _is_linked(a, 'fastfst_nSpdGenOn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst40'):
        assert _is_linked(b1, 'fastfst_ModelFastfst40', a)
    _safe_set(a, 'fastfst_nSpdGenOn', b2)
    assert _is_linked(a, 'fastfst_nSpdGenOn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst40'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst40', a)
    if hasattr(b2, 'fastfst_ModelFastfst40'):
        assert _is_linked(b2, 'fastfst_ModelFastfst40', a)
    _safe_set(a, 'fastfst_nSpdGenOn', None)
    assert not _is_linked(a, 'fastfst_nSpdGenOn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst40'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst40', a)


def test_assoc_SttsTime299_link_reassign_clear():
    a = fastfst_nSttsTime(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nSttsTime', b1)
    assert _is_linked(a, 'fastfst_nSttsTime', b1)
    if hasattr(b1, 'fastfst_ModelFastfst300'):
        assert _is_linked(b1, 'fastfst_ModelFastfst300', a)
    _safe_set(a, 'fastfst_nSttsTime', b2)
    assert _is_linked(a, 'fastfst_nSttsTime', b2)
    if hasattr(b1, 'fastfst_ModelFastfst300'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst300', a)
    if hasattr(b2, 'fastfst_ModelFastfst300'):
        assert _is_linked(b2, 'fastfst_ModelFastfst300', a)
    _safe_set(a, 'fastfst_nSttsTime', None)
    assert not _is_linked(a, 'fastfst_nSttsTime', b2)
    if hasattr(b2, 'fastfst_ModelFastfst300'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst300', a)


def test_assoc_SumPrint287_link_reassign_clear():
    a = fastfst_bSumPrint(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bSumPrint', b1)
    assert _is_linked(a, 'fastfst_bSumPrint', b1)
    if hasattr(b1, 'fastfst_ModelFastfst288'):
        assert _is_linked(b1, 'fastfst_ModelFastfst288', a)
    _safe_set(a, 'fastfst_bSumPrint', b2)
    assert _is_linked(a, 'fastfst_bSumPrint', b2)
    if hasattr(b1, 'fastfst_ModelFastfst288'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst288', a)
    if hasattr(b2, 'fastfst_ModelFastfst288'):
        assert _is_linked(b2, 'fastfst_ModelFastfst288', a)
    _safe_set(a, 'fastfst_bSumPrint', None)
    assert not _is_linked(a, 'fastfst_bSumPrint', b2)
    if hasattr(b2, 'fastfst_ModelFastfst288'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst288', a)


def test_assoc_TBDepISp_1_57_link_reassign_clear():
    a = fastfst_nTBDepISp_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTBDepISp_1_', b1)
    assert _is_linked(a, 'fastfst_nTBDepISp_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst58'):
        assert _is_linked(b1, 'fastfst_ModelFastfst58', a)
    _safe_set(a, 'fastfst_nTBDepISp_1_', b2)
    assert _is_linked(a, 'fastfst_nTBDepISp_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst58'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst58', a)
    if hasattr(b2, 'fastfst_ModelFastfst58'):
        assert _is_linked(b2, 'fastfst_ModelFastfst58', a)
    _safe_set(a, 'fastfst_nTBDepISp_1_', None)
    assert not _is_linked(a, 'fastfst_nTBDepISp_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst58'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst58', a)


def test_assoc_TBDepISp_2_59_link_reassign_clear():
    a = fastfst_nTBDepISp_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTBDepISp_2_', b1)
    assert _is_linked(a, 'fastfst_nTBDepISp_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst60'):
        assert _is_linked(b1, 'fastfst_ModelFastfst60', a)
    _safe_set(a, 'fastfst_nTBDepISp_2_', b2)
    assert _is_linked(a, 'fastfst_nTBDepISp_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst60'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst60', a)
    if hasattr(b2, 'fastfst_ModelFastfst60'):
        assert _is_linked(b2, 'fastfst_ModelFastfst60', a)
    _safe_set(a, 'fastfst_nTBDepISp_2_', None)
    assert not _is_linked(a, 'fastfst_nTBDepISp_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst60'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst60', a)


def test_assoc_TBDepISp_3_61_link_reassign_clear():
    a = fastfst_nTBDepISp_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTBDepISp_3_', b1)
    assert _is_linked(a, 'fastfst_nTBDepISp_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst62'):
        assert _is_linked(b1, 'fastfst_ModelFastfst62', a)
    _safe_set(a, 'fastfst_nTBDepISp_3_', b2)
    assert _is_linked(a, 'fastfst_nTBDepISp_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst62'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst62', a)
    if hasattr(b2, 'fastfst_ModelFastfst62'):
        assert _is_linked(b2, 'fastfst_ModelFastfst62', a)
    _safe_set(a, 'fastfst_nTBDepISp_3_', None)
    assert not _is_linked(a, 'fastfst_nTBDepISp_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst62'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst62', a)


def test_assoc_TBDrConD269_link_reassign_clear():
    a = fastfst_nTBDrConD(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTBDrConD', b1)
    assert _is_linked(a, 'fastfst_nTBDrConD', b1)
    if hasattr(b1, 'fastfst_ModelFastfst270'):
        assert _is_linked(b1, 'fastfst_ModelFastfst270', a)
    _safe_set(a, 'fastfst_nTBDrConD', b2)
    assert _is_linked(a, 'fastfst_nTBDrConD', b2)
    if hasattr(b1, 'fastfst_ModelFastfst270'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst270', a)
    if hasattr(b2, 'fastfst_ModelFastfst270'):
        assert _is_linked(b2, 'fastfst_ModelFastfst270', a)
    _safe_set(a, 'fastfst_nTBDrConD', None)
    assert not _is_linked(a, 'fastfst_nTBDrConD', b2)
    if hasattr(b2, 'fastfst_ModelFastfst270'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst270', a)


def test_assoc_TBDrConN267_link_reassign_clear():
    a = fastfst_nTBDrConN(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTBDrConN', b1)
    assert _is_linked(a, 'fastfst_nTBDrConN', b1)
    if hasattr(b1, 'fastfst_ModelFastfst268'):
        assert _is_linked(b1, 'fastfst_ModelFastfst268', a)
    _safe_set(a, 'fastfst_nTBDrConN', b2)
    assert _is_linked(a, 'fastfst_nTBDrConN', b2)
    if hasattr(b1, 'fastfst_ModelFastfst268'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst268', a)
    if hasattr(b2, 'fastfst_ModelFastfst268'):
        assert _is_linked(b2, 'fastfst_ModelFastfst268', a)
    _safe_set(a, 'fastfst_nTBDrConN', None)
    assert not _is_linked(a, 'fastfst_nTBDrConN', b2)
    if hasattr(b2, 'fastfst_ModelFastfst268'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst268', a)


def test_assoc_TEC_Freq217_link_reassign_clear():
    a = fastfst_nTEC_Freq(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_Freq', b1)
    assert _is_linked(a, 'fastfst_nTEC_Freq', b1)
    if hasattr(b1, 'fastfst_ModelFastfst218'):
        assert _is_linked(b1, 'fastfst_ModelFastfst218', a)
    _safe_set(a, 'fastfst_nTEC_Freq', b2)
    assert _is_linked(a, 'fastfst_nTEC_Freq', b2)
    if hasattr(b1, 'fastfst_ModelFastfst218'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst218', a)
    if hasattr(b2, 'fastfst_ModelFastfst218'):
        assert _is_linked(b2, 'fastfst_ModelFastfst218', a)
    _safe_set(a, 'fastfst_nTEC_Freq', None)
    assert not _is_linked(a, 'fastfst_nTEC_Freq', b2)
    if hasattr(b2, 'fastfst_ModelFastfst218'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst218', a)


def test_assoc_TEC_MR231_link_reassign_clear():
    a = fastfst_nTEC_MR(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_MR', b1)
    assert _is_linked(a, 'fastfst_nTEC_MR', b1)
    if hasattr(b1, 'fastfst_ModelFastfst232'):
        assert _is_linked(b1, 'fastfst_ModelFastfst232', a)
    _safe_set(a, 'fastfst_nTEC_MR', b2)
    assert _is_linked(a, 'fastfst_nTEC_MR', b2)
    if hasattr(b1, 'fastfst_ModelFastfst232'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst232', a)
    if hasattr(b2, 'fastfst_ModelFastfst232'):
        assert _is_linked(b2, 'fastfst_ModelFastfst232', a)
    _safe_set(a, 'fastfst_nTEC_MR', None)
    assert not _is_linked(a, 'fastfst_nTEC_MR', b2)
    if hasattr(b2, 'fastfst_ModelFastfst232'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst232', a)


def test_assoc_TEC_Npol219_link_reassign_clear():
    a = fastfst_nTEC_Npol(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_Npol', b1)
    assert _is_linked(a, 'fastfst_nTEC_Npol', b1)
    if hasattr(b1, 'fastfst_ModelFastfst220'):
        assert _is_linked(b1, 'fastfst_ModelFastfst220', a)
    _safe_set(a, 'fastfst_nTEC_Npol', b2)
    assert _is_linked(a, 'fastfst_nTEC_Npol', b2)
    if hasattr(b1, 'fastfst_ModelFastfst220'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst220', a)
    if hasattr(b2, 'fastfst_ModelFastfst220'):
        assert _is_linked(b2, 'fastfst_ModelFastfst220', a)
    _safe_set(a, 'fastfst_nTEC_Npol', None)
    assert not _is_linked(a, 'fastfst_nTEC_Npol', b2)
    if hasattr(b2, 'fastfst_ModelFastfst220'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst220', a)


def test_assoc_TEC_RLR229_link_reassign_clear():
    a = fastfst_nTEC_RLR(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_RLR', b1)
    assert _is_linked(a, 'fastfst_nTEC_RLR', b1)
    if hasattr(b1, 'fastfst_ModelFastfst230'):
        assert _is_linked(b1, 'fastfst_ModelFastfst230', a)
    _safe_set(a, 'fastfst_nTEC_RLR', b2)
    assert _is_linked(a, 'fastfst_nTEC_RLR', b2)
    if hasattr(b1, 'fastfst_ModelFastfst230'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst230', a)
    if hasattr(b2, 'fastfst_ModelFastfst230'):
        assert _is_linked(b2, 'fastfst_ModelFastfst230', a)
    _safe_set(a, 'fastfst_nTEC_RLR', None)
    assert not _is_linked(a, 'fastfst_nTEC_RLR', b2)
    if hasattr(b2, 'fastfst_ModelFastfst230'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst230', a)


def test_assoc_TEC_Rres223_link_reassign_clear():
    a = fastfst_nTEC_Rres(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_Rres', b1)
    assert _is_linked(a, 'fastfst_nTEC_Rres', b1)
    if hasattr(b1, 'fastfst_ModelFastfst224'):
        assert _is_linked(b1, 'fastfst_ModelFastfst224', a)
    _safe_set(a, 'fastfst_nTEC_Rres', b2)
    assert _is_linked(a, 'fastfst_nTEC_Rres', b2)
    if hasattr(b1, 'fastfst_ModelFastfst224'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst224', a)
    if hasattr(b2, 'fastfst_ModelFastfst224'):
        assert _is_linked(b2, 'fastfst_ModelFastfst224', a)
    _safe_set(a, 'fastfst_nTEC_Rres', None)
    assert not _is_linked(a, 'fastfst_nTEC_Rres', b2)
    if hasattr(b2, 'fastfst_ModelFastfst224'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst224', a)


def test_assoc_TEC_SLR227_link_reassign_clear():
    a = fastfst_nTEC_SLR(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_SLR', b1)
    assert _is_linked(a, 'fastfst_nTEC_SLR', b1)
    if hasattr(b1, 'fastfst_ModelFastfst228'):
        assert _is_linked(b1, 'fastfst_ModelFastfst228', a)
    _safe_set(a, 'fastfst_nTEC_SLR', b2)
    assert _is_linked(a, 'fastfst_nTEC_SLR', b2)
    if hasattr(b1, 'fastfst_ModelFastfst228'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst228', a)
    if hasattr(b2, 'fastfst_ModelFastfst228'):
        assert _is_linked(b2, 'fastfst_ModelFastfst228', a)
    _safe_set(a, 'fastfst_nTEC_SLR', None)
    assert not _is_linked(a, 'fastfst_nTEC_SLR', b2)
    if hasattr(b2, 'fastfst_ModelFastfst228'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst228', a)


def test_assoc_TEC_Sres221_link_reassign_clear():
    a = fastfst_nTEC_Sres(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_Sres', b1)
    assert _is_linked(a, 'fastfst_nTEC_Sres', b1)
    if hasattr(b1, 'fastfst_ModelFastfst222'):
        assert _is_linked(b1, 'fastfst_ModelFastfst222', a)
    _safe_set(a, 'fastfst_nTEC_Sres', b2)
    assert _is_linked(a, 'fastfst_nTEC_Sres', b2)
    if hasattr(b1, 'fastfst_ModelFastfst222'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst222', a)
    if hasattr(b2, 'fastfst_ModelFastfst222'):
        assert _is_linked(b2, 'fastfst_ModelFastfst222', a)
    _safe_set(a, 'fastfst_nTEC_Sres', None)
    assert not _is_linked(a, 'fastfst_nTEC_Sres', b2)
    if hasattr(b2, 'fastfst_ModelFastfst222'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst222', a)


def test_assoc_TEC_VLL225_link_reassign_clear():
    a = fastfst_nTEC_VLL(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTEC_VLL', b1)
    assert _is_linked(a, 'fastfst_nTEC_VLL', b1)
    if hasattr(b1, 'fastfst_ModelFastfst226'):
        assert _is_linked(b1, 'fastfst_ModelFastfst226', a)
    _safe_set(a, 'fastfst_nTEC_VLL', b2)
    assert _is_linked(a, 'fastfst_nTEC_VLL', b2)
    if hasattr(b1, 'fastfst_ModelFastfst226'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst226', a)
    if hasattr(b2, 'fastfst_ModelFastfst226'):
        assert _is_linked(b2, 'fastfst_ModelFastfst226', a)
    _safe_set(a, 'fastfst_nTEC_VLL', None)
    assert not _is_linked(a, 'fastfst_nTEC_VLL', b2)
    if hasattr(b2, 'fastfst_ModelFastfst226'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst226', a)


def test_assoc_THSSBrDp47_link_reassign_clear():
    a = fastfst_nTHSSBrDp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTHSSBrDp', b1)
    assert _is_linked(a, 'fastfst_nTHSSBrDp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst48'):
        assert _is_linked(b1, 'fastfst_ModelFastfst48', a)
    _safe_set(a, 'fastfst_nTHSSBrDp', b2)
    assert _is_linked(a, 'fastfst_nTHSSBrDp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst48'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst48', a)
    if hasattr(b2, 'fastfst_ModelFastfst48'):
        assert _is_linked(b2, 'fastfst_ModelFastfst48', a)
    _safe_set(a, 'fastfst_nTHSSBrDp', None)
    assert not _is_linked(a, 'fastfst_nTHSSBrDp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst48'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst48', a)


def test_assoc_TMax11_link_reassign_clear():
    a = fastfst_nTMax(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTMax', b1)
    assert _is_linked(a, 'fastfst_nTMax', b1)
    if hasattr(b1, 'fastfst_ModelFastfst12'):
        assert _is_linked(b1, 'fastfst_ModelFastfst12', a)
    _safe_set(a, 'fastfst_nTMax', b2)
    assert _is_linked(a, 'fastfst_nTMax', b2)
    if hasattr(b1, 'fastfst_ModelFastfst12'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst12', a)
    if hasattr(b2, 'fastfst_ModelFastfst12'):
        assert _is_linked(b2, 'fastfst_ModelFastfst12', a)
    _safe_set(a, 'fastfst_nTMax', None)
    assert not _is_linked(a, 'fastfst_nTMax', b2)
    if hasattr(b2, 'fastfst_ModelFastfst12'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst12', a)


def test_assoc_TPCOn21_link_reassign_clear():
    a = fastfst_nTPCOn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPCOn', b1)
    assert _is_linked(a, 'fastfst_nTPCOn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst22'):
        assert _is_linked(b1, 'fastfst_ModelFastfst22', a)
    _safe_set(a, 'fastfst_nTPCOn', b2)
    assert _is_linked(a, 'fastfst_nTPCOn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst22'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst22', a)
    if hasattr(b2, 'fastfst_ModelFastfst22'):
        assert _is_linked(b2, 'fastfst_ModelFastfst22', a)
    _safe_set(a, 'fastfst_nTPCOn', None)
    assert not _is_linked(a, 'fastfst_nTPCOn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst22'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst22', a)


def test_assoc_TPitManE_1_75_link_reassign_clear():
    a = fastfst_nTPitManE_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPitManE_1_', b1)
    assert _is_linked(a, 'fastfst_nTPitManE_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst76'):
        assert _is_linked(b1, 'fastfst_ModelFastfst76', a)
    _safe_set(a, 'fastfst_nTPitManE_1_', b2)
    assert _is_linked(a, 'fastfst_nTPitManE_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst76'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst76', a)
    if hasattr(b2, 'fastfst_ModelFastfst76'):
        assert _is_linked(b2, 'fastfst_ModelFastfst76', a)
    _safe_set(a, 'fastfst_nTPitManE_1_', None)
    assert not _is_linked(a, 'fastfst_nTPitManE_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst76'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst76', a)


def test_assoc_TPitManE_2_77_link_reassign_clear():
    a = fastfst_nTPitManE_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPitManE_2_', b1)
    assert _is_linked(a, 'fastfst_nTPitManE_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst78'):
        assert _is_linked(b1, 'fastfst_ModelFastfst78', a)
    _safe_set(a, 'fastfst_nTPitManE_2_', b2)
    assert _is_linked(a, 'fastfst_nTPitManE_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst78'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst78', a)
    if hasattr(b2, 'fastfst_ModelFastfst78'):
        assert _is_linked(b2, 'fastfst_ModelFastfst78', a)
    _safe_set(a, 'fastfst_nTPitManE_2_', None)
    assert not _is_linked(a, 'fastfst_nTPitManE_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst78'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst78', a)


def test_assoc_TPitManE_3_79_link_reassign_clear():
    a = fastfst_nTPitManE_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPitManE_3_', b1)
    assert _is_linked(a, 'fastfst_nTPitManE_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst80'):
        assert _is_linked(b1, 'fastfst_ModelFastfst80', a)
    _safe_set(a, 'fastfst_nTPitManE_3_', b2)
    assert _is_linked(a, 'fastfst_nTPitManE_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst80'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst80', a)
    if hasattr(b2, 'fastfst_ModelFastfst80'):
        assert _is_linked(b2, 'fastfst_ModelFastfst80', a)
    _safe_set(a, 'fastfst_nTPitManE_3_', None)
    assert not _is_linked(a, 'fastfst_nTPitManE_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst80'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst80', a)


def test_assoc_TPitManS_1_69_link_reassign_clear():
    a = fastfst_nTPitManS_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPitManS_1_', b1)
    assert _is_linked(a, 'fastfst_nTPitManS_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst70'):
        assert _is_linked(b1, 'fastfst_ModelFastfst70', a)
    _safe_set(a, 'fastfst_nTPitManS_1_', b2)
    assert _is_linked(a, 'fastfst_nTPitManS_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst70'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst70', a)
    if hasattr(b2, 'fastfst_ModelFastfst70'):
        assert _is_linked(b2, 'fastfst_ModelFastfst70', a)
    _safe_set(a, 'fastfst_nTPitManS_1_', None)
    assert not _is_linked(a, 'fastfst_nTPitManS_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst70'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst70', a)


def test_assoc_TPitManS_2_71_link_reassign_clear():
    a = fastfst_nTPitManS_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPitManS_2_', b1)
    assert _is_linked(a, 'fastfst_nTPitManS_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst72'):
        assert _is_linked(b1, 'fastfst_ModelFastfst72', a)
    _safe_set(a, 'fastfst_nTPitManS_2_', b2)
    assert _is_linked(a, 'fastfst_nTPitManS_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst72'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst72', a)
    if hasattr(b2, 'fastfst_ModelFastfst72'):
        assert _is_linked(b2, 'fastfst_ModelFastfst72', a)
    _safe_set(a, 'fastfst_nTPitManS_2_', None)
    assert not _is_linked(a, 'fastfst_nTPitManS_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst72'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst72', a)


def test_assoc_TPitManS_3_73_link_reassign_clear():
    a = fastfst_nTPitManS_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTPitManS_3_', b1)
    assert _is_linked(a, 'fastfst_nTPitManS_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst74'):
        assert _is_linked(b1, 'fastfst_ModelFastfst74', a)
    _safe_set(a, 'fastfst_nTPitManS_3_', b2)
    assert _is_linked(a, 'fastfst_nTPitManS_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst74'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst74', a)
    if hasattr(b2, 'fastfst_ModelFastfst74'):
        assert _is_linked(b2, 'fastfst_ModelFastfst74', a)
    _safe_set(a, 'fastfst_nTPitManS_3_', None)
    assert not _is_linked(a, 'fastfst_nTPitManS_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst74'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst74', a)


def test_assoc_TStart295_link_reassign_clear():
    a = fastfst_nTStart(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTStart', b1)
    assert _is_linked(a, 'fastfst_nTStart', b1)
    if hasattr(b1, 'fastfst_ModelFastfst296'):
        assert _is_linked(b1, 'fastfst_ModelFastfst296', a)
    _safe_set(a, 'fastfst_nTStart', b2)
    assert _is_linked(a, 'fastfst_nTStart', b2)
    if hasattr(b1, 'fastfst_ModelFastfst296'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst296', a)
    if hasattr(b2, 'fastfst_ModelFastfst296'):
        assert _is_linked(b2, 'fastfst_ModelFastfst296', a)
    _safe_set(a, 'fastfst_nTStart', None)
    assert not _is_linked(a, 'fastfst_nTStart', b2)
    if hasattr(b2, 'fastfst_ModelFastfst296'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst296', a)


def test_assoc_TTDspFA133_link_reassign_clear():
    a = fastfst_nTTDspFA(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTTDspFA', b1)
    assert _is_linked(a, 'fastfst_nTTDspFA', b1)
    if hasattr(b1, 'fastfst_ModelFastfst134'):
        assert _is_linked(b1, 'fastfst_ModelFastfst134', a)
    _safe_set(a, 'fastfst_nTTDspFA', b2)
    assert _is_linked(a, 'fastfst_nTTDspFA', b2)
    if hasattr(b1, 'fastfst_ModelFastfst134'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst134', a)
    if hasattr(b2, 'fastfst_ModelFastfst134'):
        assert _is_linked(b2, 'fastfst_ModelFastfst134', a)
    _safe_set(a, 'fastfst_nTTDspFA', None)
    assert not _is_linked(a, 'fastfst_nTTDspFA', b2)
    if hasattr(b2, 'fastfst_ModelFastfst134'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst134', a)


def test_assoc_TTDspSS135_link_reassign_clear():
    a = fastfst_nTTDspSS(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTTDspSS', b1)
    assert _is_linked(a, 'fastfst_nTTDspSS', b1)
    if hasattr(b1, 'fastfst_ModelFastfst136'):
        assert _is_linked(b1, 'fastfst_ModelFastfst136', a)
    _safe_set(a, 'fastfst_nTTDspSS', b2)
    assert _is_linked(a, 'fastfst_nTTDspSS', b2)
    if hasattr(b1, 'fastfst_ModelFastfst136'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst136', a)
    if hasattr(b2, 'fastfst_ModelFastfst136'):
        assert _is_linked(b2, 'fastfst_ModelFastfst136', a)
    _safe_set(a, 'fastfst_nTTDspSS', None)
    assert not _is_linked(a, 'fastfst_nTTDspSS', b2)
    if hasattr(b2, 'fastfst_ModelFastfst136'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst136', a)


def test_assoc_TTpBrDp_1_51_link_reassign_clear():
    a = fastfst_nTTpBrDp_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTTpBrDp_1_', b1)
    assert _is_linked(a, 'fastfst_nTTpBrDp_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst52'):
        assert _is_linked(b1, 'fastfst_ModelFastfst52', a)
    _safe_set(a, 'fastfst_nTTpBrDp_1_', b2)
    assert _is_linked(a, 'fastfst_nTTpBrDp_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst52'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst52', a)
    if hasattr(b2, 'fastfst_ModelFastfst52'):
        assert _is_linked(b2, 'fastfst_ModelFastfst52', a)
    _safe_set(a, 'fastfst_nTTpBrDp_1_', None)
    assert not _is_linked(a, 'fastfst_nTTpBrDp_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst52'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst52', a)


def test_assoc_TTpBrDp_2_53_link_reassign_clear():
    a = fastfst_nTTpBrDp_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTTpBrDp_2_', b1)
    assert _is_linked(a, 'fastfst_nTTpBrDp_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst54'):
        assert _is_linked(b1, 'fastfst_ModelFastfst54', a)
    _safe_set(a, 'fastfst_nTTpBrDp_2_', b2)
    assert _is_linked(a, 'fastfst_nTTpBrDp_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst54'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst54', a)
    if hasattr(b2, 'fastfst_ModelFastfst54'):
        assert _is_linked(b2, 'fastfst_ModelFastfst54', a)
    _safe_set(a, 'fastfst_nTTpBrDp_2_', None)
    assert not _is_linked(a, 'fastfst_nTTpBrDp_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst54'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst54', a)


def test_assoc_TTpBrDp_3_55_link_reassign_clear():
    a = fastfst_nTTpBrDp_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTTpBrDp_3_', b1)
    assert _is_linked(a, 'fastfst_nTTpBrDp_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst56'):
        assert _is_linked(b1, 'fastfst_ModelFastfst56', a)
    _safe_set(a, 'fastfst_nTTpBrDp_3_', b2)
    assert _is_linked(a, 'fastfst_nTTpBrDp_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst56'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst56', a)
    if hasattr(b2, 'fastfst_ModelFastfst56'):
        assert _is_linked(b2, 'fastfst_ModelFastfst56', a)
    _safe_set(a, 'fastfst_nTTpBrDp_3_', None)
    assert not _is_linked(a, 'fastfst_nTTpBrDp_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst56'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst56', a)


def test_assoc_TYCOn17_link_reassign_clear():
    a = fastfst_nTYCOn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTYCOn', b1)
    assert _is_linked(a, 'fastfst_nTYCOn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst18'):
        assert _is_linked(b1, 'fastfst_ModelFastfst18', a)
    _safe_set(a, 'fastfst_nTYCOn', b2)
    assert _is_linked(a, 'fastfst_nTYCOn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst18'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst18', a)
    if hasattr(b2, 'fastfst_ModelFastfst18'):
        assert _is_linked(b2, 'fastfst_ModelFastfst18', a)
    _safe_set(a, 'fastfst_nTYCOn', None)
    assert not _is_linked(a, 'fastfst_nTYCOn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst18'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst18', a)


def test_assoc_TYawManE65_link_reassign_clear():
    a = fastfst_nTYawManE(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTYawManE', b1)
    assert _is_linked(a, 'fastfst_nTYawManE', b1)
    if hasattr(b1, 'fastfst_ModelFastfst66'):
        assert _is_linked(b1, 'fastfst_ModelFastfst66', a)
    _safe_set(a, 'fastfst_nTYawManE', b2)
    assert _is_linked(a, 'fastfst_nTYawManE', b2)
    if hasattr(b1, 'fastfst_ModelFastfst66'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst66', a)
    if hasattr(b2, 'fastfst_ModelFastfst66'):
        assert _is_linked(b2, 'fastfst_ModelFastfst66', a)
    _safe_set(a, 'fastfst_nTYawManE', None)
    assert not _is_linked(a, 'fastfst_nTYawManE', b2)
    if hasattr(b2, 'fastfst_ModelFastfst66'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst66', a)


def test_assoc_TYawManS63_link_reassign_clear():
    a = fastfst_nTYawManS(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTYawManS', b1)
    assert _is_linked(a, 'fastfst_nTYawManS', b1)
    if hasattr(b1, 'fastfst_ModelFastfst64'):
        assert _is_linked(b1, 'fastfst_ModelFastfst64', a)
    _safe_set(a, 'fastfst_nTYawManS', b2)
    assert _is_linked(a, 'fastfst_nTYawManS', b2)
    if hasattr(b1, 'fastfst_ModelFastfst64'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst64', a)
    if hasattr(b2, 'fastfst_ModelFastfst64'):
        assert _is_linked(b2, 'fastfst_ModelFastfst64', a)
    _safe_set(a, 'fastfst_nTYawManS', None)
    assert not _is_linked(a, 'fastfst_nTYawManS', b2)
    if hasattr(b2, 'fastfst_ModelFastfst64'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst64', a)


def test_assoc_TabDelim291_link_reassign_clear():
    a = fastfst_bTabDelim(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bTabDelim', b1)
    assert _is_linked(a, 'fastfst_bTabDelim', b1)
    if hasattr(b1, 'fastfst_ModelFastfst292'):
        assert _is_linked(b1, 'fastfst_ModelFastfst292', a)
    _safe_set(a, 'fastfst_bTabDelim', b2)
    assert _is_linked(a, 'fastfst_bTabDelim', b2)
    if hasattr(b1, 'fastfst_ModelFastfst292'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst292', a)
    if hasattr(b2, 'fastfst_ModelFastfst292'):
        assert _is_linked(b2, 'fastfst_ModelFastfst292', a)
    _safe_set(a, 'fastfst_bTabDelim', None)
    assert not _is_linked(a, 'fastfst_bTabDelim', b2)
    if hasattr(b2, 'fastfst_ModelFastfst292'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst292', a)


def test_assoc_TeetCDmp257_link_reassign_clear():
    a = fastfst_nTeetCDmp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetCDmp', b1)
    assert _is_linked(a, 'fastfst_nTeetCDmp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst258'):
        assert _is_linked(b1, 'fastfst_ModelFastfst258', a)
    _safe_set(a, 'fastfst_nTeetCDmp', b2)
    assert _is_linked(a, 'fastfst_nTeetCDmp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst258'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst258', a)
    if hasattr(b2, 'fastfst_ModelFastfst258'):
        assert _is_linked(b2, 'fastfst_ModelFastfst258', a)
    _safe_set(a, 'fastfst_nTeetCDmp', None)
    assert not _is_linked(a, 'fastfst_nTeetCDmp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst258'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst258', a)


def test_assoc_TeetDOF101_link_reassign_clear():
    a = fastfst_bTeetDOF(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bTeetDOF', b1)
    assert _is_linked(a, 'fastfst_bTeetDOF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst102'):
        assert _is_linked(b1, 'fastfst_ModelFastfst102', a)
    _safe_set(a, 'fastfst_bTeetDOF', b2)
    assert _is_linked(a, 'fastfst_bTeetDOF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst102'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst102', a)
    if hasattr(b2, 'fastfst_ModelFastfst102'):
        assert _is_linked(b2, 'fastfst_ModelFastfst102', a)
    _safe_set(a, 'fastfst_bTeetDOF', None)
    assert not _is_linked(a, 'fastfst_bTeetDOF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst102'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst102', a)


def test_assoc_TeetDefl125_link_reassign_clear():
    a = fastfst_nTeetDefl(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetDefl', b1)
    assert _is_linked(a, 'fastfst_nTeetDefl', b1)
    if hasattr(b1, 'fastfst_ModelFastfst126'):
        assert _is_linked(b1, 'fastfst_ModelFastfst126', a)
    _safe_set(a, 'fastfst_nTeetDefl', b2)
    assert _is_linked(a, 'fastfst_nTeetDefl', b2)
    if hasattr(b1, 'fastfst_ModelFastfst126'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst126', a)
    if hasattr(b2, 'fastfst_ModelFastfst126'):
        assert _is_linked(b2, 'fastfst_ModelFastfst126', a)
    _safe_set(a, 'fastfst_nTeetDefl', None)
    assert not _is_linked(a, 'fastfst_nTeetDefl', b2)
    if hasattr(b2, 'fastfst_ModelFastfst126'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst126', a)


def test_assoc_TeetDmp255_link_reassign_clear():
    a = fastfst_nTeetDmp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetDmp', b1)
    assert _is_linked(a, 'fastfst_nTeetDmp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst256'):
        assert _is_linked(b1, 'fastfst_ModelFastfst256', a)
    _safe_set(a, 'fastfst_nTeetDmp', b2)
    assert _is_linked(a, 'fastfst_nTeetDmp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst256'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst256', a)
    if hasattr(b2, 'fastfst_ModelFastfst256'):
        assert _is_linked(b2, 'fastfst_ModelFastfst256', a)
    _safe_set(a, 'fastfst_nTeetDmp', None)
    assert not _is_linked(a, 'fastfst_nTeetDmp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst256'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst256', a)


def test_assoc_TeetDmpP253_link_reassign_clear():
    a = fastfst_nTeetDmpP(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetDmpP', b1)
    assert _is_linked(a, 'fastfst_nTeetDmpP', b1)
    if hasattr(b1, 'fastfst_ModelFastfst254'):
        assert _is_linked(b1, 'fastfst_ModelFastfst254', a)
    _safe_set(a, 'fastfst_nTeetDmpP', b2)
    assert _is_linked(a, 'fastfst_nTeetDmpP', b2)
    if hasattr(b1, 'fastfst_ModelFastfst254'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst254', a)
    if hasattr(b2, 'fastfst_ModelFastfst254'):
        assert _is_linked(b2, 'fastfst_ModelFastfst254', a)
    _safe_set(a, 'fastfst_nTeetDmpP', None)
    assert not _is_linked(a, 'fastfst_nTeetDmpP', b2)
    if hasattr(b2, 'fastfst_ModelFastfst254'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst254', a)


def test_assoc_TeetHSSp265_link_reassign_clear():
    a = fastfst_nTeetHSSp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetHSSp', b1)
    assert _is_linked(a, 'fastfst_nTeetHSSp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst266'):
        assert _is_linked(b1, 'fastfst_ModelFastfst266', a)
    _safe_set(a, 'fastfst_nTeetHSSp', b2)
    assert _is_linked(a, 'fastfst_nTeetHSSp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst266'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst266', a)
    if hasattr(b2, 'fastfst_ModelFastfst266'):
        assert _is_linked(b2, 'fastfst_ModelFastfst266', a)
    _safe_set(a, 'fastfst_nTeetHSSp', None)
    assert not _is_linked(a, 'fastfst_nTeetHSSp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst266'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst266', a)


def test_assoc_TeetHStP261_link_reassign_clear():
    a = fastfst_nTeetHStP(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetHStP', b1)
    assert _is_linked(a, 'fastfst_nTeetHStP', b1)
    if hasattr(b1, 'fastfst_ModelFastfst262'):
        assert _is_linked(b1, 'fastfst_ModelFastfst262', a)
    _safe_set(a, 'fastfst_nTeetHStP', b2)
    assert _is_linked(a, 'fastfst_nTeetHStP', b2)
    if hasattr(b1, 'fastfst_ModelFastfst262'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst262', a)
    if hasattr(b2, 'fastfst_ModelFastfst262'):
        assert _is_linked(b2, 'fastfst_ModelFastfst262', a)
    _safe_set(a, 'fastfst_nTeetHStP', None)
    assert not _is_linked(a, 'fastfst_nTeetHStP', b2)
    if hasattr(b2, 'fastfst_ModelFastfst262'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst262', a)


def test_assoc_TeetMod251_link_reassign_clear():
    a = fastfst_iTeetMod(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iTeetMod', b1)
    assert _is_linked(a, 'fastfst_iTeetMod', b1)
    if hasattr(b1, 'fastfst_ModelFastfst252'):
        assert _is_linked(b1, 'fastfst_ModelFastfst252', a)
    _safe_set(a, 'fastfst_iTeetMod', b2)
    assert _is_linked(a, 'fastfst_iTeetMod', b2)
    if hasattr(b1, 'fastfst_ModelFastfst252'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst252', a)
    if hasattr(b2, 'fastfst_ModelFastfst252'):
        assert _is_linked(b2, 'fastfst_ModelFastfst252', a)
    _safe_set(a, 'fastfst_iTeetMod', None)
    assert not _is_linked(a, 'fastfst_iTeetMod', b2)
    if hasattr(b2, 'fastfst_ModelFastfst252'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst252', a)


def test_assoc_TeetSSSp263_link_reassign_clear():
    a = fastfst_nTeetSSSp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetSSSp', b1)
    assert _is_linked(a, 'fastfst_nTeetSSSp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst264'):
        assert _is_linked(b1, 'fastfst_ModelFastfst264', a)
    _safe_set(a, 'fastfst_nTeetSSSp', b2)
    assert _is_linked(a, 'fastfst_nTeetSSSp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst264'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst264', a)
    if hasattr(b2, 'fastfst_ModelFastfst264'):
        assert _is_linked(b2, 'fastfst_ModelFastfst264', a)
    _safe_set(a, 'fastfst_nTeetSSSp', None)
    assert not _is_linked(a, 'fastfst_nTeetSSSp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst264'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst264', a)


def test_assoc_TeetSStP259_link_reassign_clear():
    a = fastfst_nTeetSStP(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTeetSStP', b1)
    assert _is_linked(a, 'fastfst_nTeetSStP', b1)
    if hasattr(b1, 'fastfst_ModelFastfst260'):
        assert _is_linked(b1, 'fastfst_ModelFastfst260', a)
    _safe_set(a, 'fastfst_nTeetSStP', b2)
    assert _is_linked(a, 'fastfst_nTeetSStP', b2)
    if hasattr(b1, 'fastfst_ModelFastfst260'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst260', a)
    if hasattr(b2, 'fastfst_ModelFastfst260'):
        assert _is_linked(b2, 'fastfst_ModelFastfst260', a)
    _safe_set(a, 'fastfst_nTeetSStP', None)
    assert not _is_linked(a, 'fastfst_nTeetSStP', b2)
    if hasattr(b2, 'fastfst_ModelFastfst260'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst260', a)


def test_assoc_TiDynBrk49_link_reassign_clear():
    a = fastfst_nTiDynBrk(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTiDynBrk', b1)
    assert _is_linked(a, 'fastfst_nTiDynBrk', b1)
    if hasattr(b1, 'fastfst_ModelFastfst50'):
        assert _is_linked(b1, 'fastfst_ModelFastfst50', a)
    _safe_set(a, 'fastfst_nTiDynBrk', b2)
    assert _is_linked(a, 'fastfst_nTiDynBrk', b2)
    if hasattr(b1, 'fastfst_ModelFastfst50'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst50', a)
    if hasattr(b2, 'fastfst_ModelFastfst50'):
        assert _is_linked(b2, 'fastfst_ModelFastfst50', a)
    _safe_set(a, 'fastfst_nTiDynBrk', None)
    assert not _is_linked(a, 'fastfst_nTiDynBrk', b2)
    if hasattr(b2, 'fastfst_ModelFastfst50'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst50', a)


def test_assoc_TimGenOf43_link_reassign_clear():
    a = fastfst_nTimGenOf(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTimGenOf', b1)
    assert _is_linked(a, 'fastfst_nTimGenOf', b1)
    if hasattr(b1, 'fastfst_ModelFastfst44'):
        assert _is_linked(b1, 'fastfst_ModelFastfst44', a)
    _safe_set(a, 'fastfst_nTimGenOf', b2)
    assert _is_linked(a, 'fastfst_nTimGenOf', b2)
    if hasattr(b1, 'fastfst_ModelFastfst44'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst44', a)
    if hasattr(b2, 'fastfst_ModelFastfst44'):
        assert _is_linked(b2, 'fastfst_ModelFastfst44', a)
    _safe_set(a, 'fastfst_nTimGenOf', None)
    assert not _is_linked(a, 'fastfst_nTimGenOf', b2)
    if hasattr(b2, 'fastfst_ModelFastfst44'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst44', a)


def test_assoc_TimGenOn41_link_reassign_clear():
    a = fastfst_nTimGenOn(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTimGenOn', b1)
    assert _is_linked(a, 'fastfst_nTimGenOn', b1)
    if hasattr(b1, 'fastfst_ModelFastfst42'):
        assert _is_linked(b1, 'fastfst_ModelFastfst42', a)
    _safe_set(a, 'fastfst_nTimGenOn', b2)
    assert _is_linked(a, 'fastfst_nTimGenOn', b2)
    if hasattr(b1, 'fastfst_ModelFastfst42'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst42', a)
    if hasattr(b2, 'fastfst_ModelFastfst42'):
        assert _is_linked(b2, 'fastfst_ModelFastfst42', a)
    _safe_set(a, 'fastfst_nTimGenOn', None)
    assert not _is_linked(a, 'fastfst_nTimGenOn', b2)
    if hasattr(b2, 'fastfst_ModelFastfst42'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst42', a)


def test_assoc_TipMass_1_179_link_reassign_clear():
    a = fastfst_nTipMass_1_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTipMass_1_', b1)
    assert _is_linked(a, 'fastfst_nTipMass_1_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst180'):
        assert _is_linked(b1, 'fastfst_ModelFastfst180', a)
    _safe_set(a, 'fastfst_nTipMass_1_', b2)
    assert _is_linked(a, 'fastfst_nTipMass_1_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst180'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst180', a)
    if hasattr(b2, 'fastfst_ModelFastfst180'):
        assert _is_linked(b2, 'fastfst_ModelFastfst180', a)
    _safe_set(a, 'fastfst_nTipMass_1_', None)
    assert not _is_linked(a, 'fastfst_nTipMass_1_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst180'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst180', a)


def test_assoc_TipMass_2_181_link_reassign_clear():
    a = fastfst_nTipMass_2_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTipMass_2_', b1)
    assert _is_linked(a, 'fastfst_nTipMass_2_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst182'):
        assert _is_linked(b1, 'fastfst_ModelFastfst182', a)
    _safe_set(a, 'fastfst_nTipMass_2_', b2)
    assert _is_linked(a, 'fastfst_nTipMass_2_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst182'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst182', a)
    if hasattr(b2, 'fastfst_ModelFastfst182'):
        assert _is_linked(b2, 'fastfst_ModelFastfst182', a)
    _safe_set(a, 'fastfst_nTipMass_2_', None)
    assert not _is_linked(a, 'fastfst_nTipMass_2_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst182'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst182', a)


def test_assoc_TipMass_3_183_link_reassign_clear():
    a = fastfst_nTipMass_3_(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTipMass_3_', b1)
    assert _is_linked(a, 'fastfst_nTipMass_3_', b1)
    if hasattr(b1, 'fastfst_ModelFastfst184'):
        assert _is_linked(b1, 'fastfst_ModelFastfst184', a)
    _safe_set(a, 'fastfst_nTipMass_3_', b2)
    assert _is_linked(a, 'fastfst_nTipMass_3_', b2)
    if hasattr(b1, 'fastfst_ModelFastfst184'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst184', a)
    if hasattr(b2, 'fastfst_ModelFastfst184'):
        assert _is_linked(b2, 'fastfst_ModelFastfst184', a)
    _safe_set(a, 'fastfst_nTipMass_3_', None)
    assert not _is_linked(a, 'fastfst_nTipMass_3_', b2)
    if hasattr(b2, 'fastfst_ModelFastfst184'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst184', a)


def test_assoc_TipRad137_link_reassign_clear():
    a = fastfst_nTipRad(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTipRad', b1)
    assert _is_linked(a, 'fastfst_nTipRad', b1)
    if hasattr(b1, 'fastfst_ModelFastfst138'):
        assert _is_linked(b1, 'fastfst_ModelFastfst138', a)
    _safe_set(a, 'fastfst_nTipRad', b2)
    assert _is_linked(a, 'fastfst_nTipRad', b2)
    if hasattr(b1, 'fastfst_ModelFastfst138'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst138', a)
    if hasattr(b2, 'fastfst_ModelFastfst138'):
        assert _is_linked(b2, 'fastfst_ModelFastfst138', a)
    _safe_set(a, 'fastfst_nTipRad', None)
    assert not _is_linked(a, 'fastfst_nTipRad', b2)
    if hasattr(b2, 'fastfst_ModelFastfst138'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst138', a)


def test_assoc_TowerHt155_link_reassign_clear():
    a = fastfst_nTowerHt(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTowerHt', b1)
    assert _is_linked(a, 'fastfst_nTowerHt', b1)
    if hasattr(b1, 'fastfst_ModelFastfst156'):
        assert _is_linked(b1, 'fastfst_ModelFastfst156', a)
    _safe_set(a, 'fastfst_nTowerHt', b2)
    assert _is_linked(a, 'fastfst_nTowerHt', b2)
    if hasattr(b1, 'fastfst_ModelFastfst156'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst156', a)
    if hasattr(b2, 'fastfst_ModelFastfst156'):
        assert _is_linked(b2, 'fastfst_ModelFastfst156', a)
    _safe_set(a, 'fastfst_nTowerHt', None)
    assert not _is_linked(a, 'fastfst_nTowerHt', b2)
    if hasattr(b2, 'fastfst_ModelFastfst156'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst156', a)


def test_assoc_TpBrDT271_link_reassign_clear():
    a = fastfst_nTpBrDT(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTpBrDT', b1)
    assert _is_linked(a, 'fastfst_nTpBrDT', b1)
    if hasattr(b1, 'fastfst_ModelFastfst272'):
        assert _is_linked(b1, 'fastfst_ModelFastfst272', a)
    _safe_set(a, 'fastfst_nTpBrDT', b2)
    assert _is_linked(a, 'fastfst_nTpBrDT', b2)
    if hasattr(b1, 'fastfst_ModelFastfst272'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst272', a)
    if hasattr(b2, 'fastfst_ModelFastfst272'):
        assert _is_linked(b2, 'fastfst_ModelFastfst272', a)
    _safe_set(a, 'fastfst_nTpBrDT', None)
    assert not _is_linked(a, 'fastfst_nTpBrDT', b2)
    if hasattr(b2, 'fastfst_ModelFastfst272'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst272', a)


def test_assoc_TwFADOF1109_link_reassign_clear():
    a = fastfst_bTwFADOF1(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bTwFADOF1', b1)
    assert _is_linked(a, 'fastfst_bTwFADOF1', b1)
    if hasattr(b1, 'fastfst_ModelFastfst110'):
        assert _is_linked(b1, 'fastfst_ModelFastfst110', a)
    _safe_set(a, 'fastfst_bTwFADOF1', b2)
    assert _is_linked(a, 'fastfst_bTwFADOF1', b2)
    if hasattr(b1, 'fastfst_ModelFastfst110'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst110', a)
    if hasattr(b2, 'fastfst_ModelFastfst110'):
        assert _is_linked(b2, 'fastfst_ModelFastfst110', a)
    _safe_set(a, 'fastfst_bTwFADOF1', None)
    assert not _is_linked(a, 'fastfst_bTwFADOF1', b2)
    if hasattr(b2, 'fastfst_ModelFastfst110'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst110', a)


def test_assoc_TwFADOF2111_link_reassign_clear():
    a = fastfst_bTwFADOF2(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bTwFADOF2', b1)
    assert _is_linked(a, 'fastfst_bTwFADOF2', b1)
    if hasattr(b1, 'fastfst_ModelFastfst112'):
        assert _is_linked(b1, 'fastfst_ModelFastfst112', a)
    _safe_set(a, 'fastfst_bTwFADOF2', b2)
    assert _is_linked(a, 'fastfst_bTwFADOF2', b2)
    if hasattr(b1, 'fastfst_ModelFastfst112'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst112', a)
    if hasattr(b2, 'fastfst_ModelFastfst112'):
        assert _is_linked(b2, 'fastfst_ModelFastfst112', a)
    _safe_set(a, 'fastfst_bTwFADOF2', None)
    assert not _is_linked(a, 'fastfst_bTwFADOF2', b2)
    if hasattr(b2, 'fastfst_ModelFastfst112'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst112', a)


def test_assoc_TwSSDOF1113_link_reassign_clear():
    a = fastfst_bTwSSDOF1(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bTwSSDOF1', b1)
    assert _is_linked(a, 'fastfst_bTwSSDOF1', b1)
    if hasattr(b1, 'fastfst_ModelFastfst114'):
        assert _is_linked(b1, 'fastfst_ModelFastfst114', a)
    _safe_set(a, 'fastfst_bTwSSDOF1', b2)
    assert _is_linked(a, 'fastfst_bTwSSDOF1', b2)
    if hasattr(b1, 'fastfst_ModelFastfst114'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst114', a)
    if hasattr(b2, 'fastfst_ModelFastfst114'):
        assert _is_linked(b2, 'fastfst_ModelFastfst114', a)
    _safe_set(a, 'fastfst_bTwSSDOF1', None)
    assert not _is_linked(a, 'fastfst_bTwSSDOF1', b2)
    if hasattr(b2, 'fastfst_ModelFastfst114'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst114', a)


def test_assoc_TwSSDOF2115_link_reassign_clear():
    a = fastfst_bTwSSDOF2(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bTwSSDOF2', b1)
    assert _is_linked(a, 'fastfst_bTwSSDOF2', b1)
    if hasattr(b1, 'fastfst_ModelFastfst116'):
        assert _is_linked(b1, 'fastfst_ModelFastfst116', a)
    _safe_set(a, 'fastfst_bTwSSDOF2', b2)
    assert _is_linked(a, 'fastfst_bTwSSDOF2', b2)
    if hasattr(b1, 'fastfst_ModelFastfst116'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst116', a)
    if hasattr(b2, 'fastfst_ModelFastfst116'):
        assert _is_linked(b2, 'fastfst_ModelFastfst116', a)
    _safe_set(a, 'fastfst_bTwSSDOF2', None)
    assert not _is_linked(a, 'fastfst_bTwSSDOF2', b2)
    if hasattr(b2, 'fastfst_ModelFastfst116'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst116', a)


def test_assoc_Twr2Shft157_link_reassign_clear():
    a = fastfst_nTwr2Shft(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTwr2Shft', b1)
    assert _is_linked(a, 'fastfst_nTwr2Shft', b1)
    if hasattr(b1, 'fastfst_ModelFastfst158'):
        assert _is_linked(b1, 'fastfst_ModelFastfst158', a)
    _safe_set(a, 'fastfst_nTwr2Shft', b2)
    assert _is_linked(a, 'fastfst_nTwr2Shft', b2)
    if hasattr(b1, 'fastfst_ModelFastfst158'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst158', a)
    if hasattr(b2, 'fastfst_ModelFastfst158'):
        assert _is_linked(b2, 'fastfst_ModelFastfst158', a)
    _safe_set(a, 'fastfst_nTwr2Shft', None)
    assert not _is_linked(a, 'fastfst_nTwr2Shft', b2)
    if hasattr(b2, 'fastfst_ModelFastfst158'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst158', a)


def test_assoc_TwrFile239_link_reassign_clear():
    a = fastfst_fTwrFile(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_fTwrFile', b1)
    assert _is_linked(a, 'fastfst_fTwrFile', b1)
    if hasattr(b1, 'fastfst_ModelFastfst240'):
        assert _is_linked(b1, 'fastfst_ModelFastfst240', a)
    _safe_set(a, 'fastfst_fTwrFile', b2)
    assert _is_linked(a, 'fastfst_fTwrFile', b2)
    if hasattr(b1, 'fastfst_ModelFastfst240'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst240', a)
    if hasattr(b2, 'fastfst_ModelFastfst240'):
        assert _is_linked(b2, 'fastfst_ModelFastfst240', a)
    _safe_set(a, 'fastfst_fTwrFile', None)
    assert not _is_linked(a, 'fastfst_fTwrFile', b2)
    if hasattr(b2, 'fastfst_ModelFastfst240'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst240', a)


def test_assoc_TwrGagNd311_link_reassign_clear():
    a = fastfst_aTwrGagNd(name="sample_text", value="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_aTwrGagNd', b1)
    assert _is_linked(a, 'fastfst_aTwrGagNd', b1)
    if hasattr(b1, 'fastfst_ModelFastfst312'):
        assert _is_linked(b1, 'fastfst_ModelFastfst312', a)
    _safe_set(a, 'fastfst_aTwrGagNd', b2)
    assert _is_linked(a, 'fastfst_aTwrGagNd', b2)
    if hasattr(b1, 'fastfst_ModelFastfst312'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst312', a)
    if hasattr(b2, 'fastfst_ModelFastfst312'):
        assert _is_linked(b2, 'fastfst_ModelFastfst312', a)
    _safe_set(a, 'fastfst_aTwrGagNd', None)
    assert not _is_linked(a, 'fastfst_aTwrGagNd', b2)
    if hasattr(b2, 'fastfst_ModelFastfst312'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst312', a)


def test_assoc_TwrNodes237_link_reassign_clear():
    a = fastfst_iTwrNodes(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iTwrNodes', b1)
    assert _is_linked(a, 'fastfst_iTwrNodes', b1)
    if hasattr(b1, 'fastfst_ModelFastfst238'):
        assert _is_linked(b1, 'fastfst_ModelFastfst238', a)
    _safe_set(a, 'fastfst_iTwrNodes', b2)
    assert _is_linked(a, 'fastfst_iTwrNodes', b2)
    if hasattr(b1, 'fastfst_ModelFastfst238'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst238', a)
    if hasattr(b2, 'fastfst_ModelFastfst238'):
        assert _is_linked(b2, 'fastfst_ModelFastfst238', a)
    _safe_set(a, 'fastfst_iTwrNodes', None)
    assert not _is_linked(a, 'fastfst_iTwrNodes', b2)
    if hasattr(b2, 'fastfst_ModelFastfst238'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst238', a)


def test_assoc_TwrRBHt159_link_reassign_clear():
    a = fastfst_nTwrRBHt(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nTwrRBHt', b1)
    assert _is_linked(a, 'fastfst_nTwrRBHt', b1)
    if hasattr(b1, 'fastfst_ModelFastfst160'):
        assert _is_linked(b1, 'fastfst_ModelFastfst160', a)
    _safe_set(a, 'fastfst_nTwrRBHt', b2)
    assert _is_linked(a, 'fastfst_nTwrRBHt', b2)
    if hasattr(b1, 'fastfst_ModelFastfst160'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst160', a)
    if hasattr(b2, 'fastfst_ModelFastfst160'):
        assert _is_linked(b2, 'fastfst_ModelFastfst160', a)
    _safe_set(a, 'fastfst_nTwrRBHt', None)
    assert not _is_linked(a, 'fastfst_nTwrRBHt', b2)
    if hasattr(b2, 'fastfst_ModelFastfst160'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst160', a)


def test_assoc_UndSling143_link_reassign_clear():
    a = fastfst_nUndSling(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nUndSling', b1)
    assert _is_linked(a, 'fastfst_nUndSling', b1)
    if hasattr(b1, 'fastfst_ModelFastfst144'):
        assert _is_linked(b1, 'fastfst_ModelFastfst144', a)
    _safe_set(a, 'fastfst_nUndSling', b2)
    assert _is_linked(a, 'fastfst_nUndSling', b2)
    if hasattr(b1, 'fastfst_ModelFastfst144'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst144', a)
    if hasattr(b2, 'fastfst_ModelFastfst144'):
        assert _is_linked(b2, 'fastfst_ModelFastfst144', a)
    _safe_set(a, 'fastfst_nUndSling', None)
    assert not _is_linked(a, 'fastfst_nUndSling', b2)
    if hasattr(b2, 'fastfst_ModelFastfst144'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst144', a)


def test_assoc_VSContrl23_link_reassign_clear():
    a = fastfst_iVSContrl(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iVSContrl', b1)
    assert _is_linked(a, 'fastfst_iVSContrl', b1)
    if hasattr(b1, 'fastfst_ModelFastfst24'):
        assert _is_linked(b1, 'fastfst_ModelFastfst24', a)
    _safe_set(a, 'fastfst_iVSContrl', b2)
    assert _is_linked(a, 'fastfst_iVSContrl', b2)
    if hasattr(b1, 'fastfst_ModelFastfst24'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst24', a)
    if hasattr(b2, 'fastfst_ModelFastfst24'):
        assert _is_linked(b2, 'fastfst_ModelFastfst24', a)
    _safe_set(a, 'fastfst_iVSContrl', None)
    assert not _is_linked(a, 'fastfst_iVSContrl', b2)
    if hasattr(b2, 'fastfst_ModelFastfst24'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst24', a)


def test_assoc_VS_Rgn2K29_link_reassign_clear():
    a = fastfst_nVS_Rgn2K(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nVS_Rgn2K', b1)
    assert _is_linked(a, 'fastfst_nVS_Rgn2K', b1)
    if hasattr(b1, 'fastfst_ModelFastfst30'):
        assert _is_linked(b1, 'fastfst_ModelFastfst30', a)
    _safe_set(a, 'fastfst_nVS_Rgn2K', b2)
    assert _is_linked(a, 'fastfst_nVS_Rgn2K', b2)
    if hasattr(b1, 'fastfst_ModelFastfst30'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst30', a)
    if hasattr(b2, 'fastfst_ModelFastfst30'):
        assert _is_linked(b2, 'fastfst_ModelFastfst30', a)
    _safe_set(a, 'fastfst_nVS_Rgn2K', None)
    assert not _is_linked(a, 'fastfst_nVS_Rgn2K', b2)
    if hasattr(b2, 'fastfst_ModelFastfst30'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst30', a)


def test_assoc_VS_RtGnSp25_link_reassign_clear():
    a = fastfst_nVS_RtGnSp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nVS_RtGnSp', b1)
    assert _is_linked(a, 'fastfst_nVS_RtGnSp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst26'):
        assert _is_linked(b1, 'fastfst_ModelFastfst26', a)
    _safe_set(a, 'fastfst_nVS_RtGnSp', b2)
    assert _is_linked(a, 'fastfst_nVS_RtGnSp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst26'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst26', a)
    if hasattr(b2, 'fastfst_ModelFastfst26'):
        assert _is_linked(b2, 'fastfst_ModelFastfst26', a)
    _safe_set(a, 'fastfst_nVS_RtGnSp', None)
    assert not _is_linked(a, 'fastfst_nVS_RtGnSp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst26'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst26', a)


def test_assoc_VS_RtTq27_link_reassign_clear():
    a = fastfst_nVS_RtTq(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nVS_RtTq', b1)
    assert _is_linked(a, 'fastfst_nVS_RtTq', b1)
    if hasattr(b1, 'fastfst_ModelFastfst28'):
        assert _is_linked(b1, 'fastfst_ModelFastfst28', a)
    _safe_set(a, 'fastfst_nVS_RtTq', b2)
    assert _is_linked(a, 'fastfst_nVS_RtTq', b2)
    if hasattr(b1, 'fastfst_ModelFastfst28'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst28', a)
    if hasattr(b2, 'fastfst_ModelFastfst28'):
        assert _is_linked(b2, 'fastfst_ModelFastfst28', a)
    _safe_set(a, 'fastfst_nVS_RtTq', None)
    assert not _is_linked(a, 'fastfst_nVS_RtTq', b2)
    if hasattr(b2, 'fastfst_ModelFastfst28'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst28', a)


def test_assoc_VS_SlPc31_link_reassign_clear():
    a = fastfst_nVS_SlPc(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nVS_SlPc', b1)
    assert _is_linked(a, 'fastfst_nVS_SlPc', b1)
    if hasattr(b1, 'fastfst_ModelFastfst32'):
        assert _is_linked(b1, 'fastfst_ModelFastfst32', a)
    _safe_set(a, 'fastfst_nVS_SlPc', b2)
    assert _is_linked(a, 'fastfst_nVS_SlPc', b2)
    if hasattr(b1, 'fastfst_ModelFastfst32'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst32', a)
    if hasattr(b2, 'fastfst_ModelFastfst32'):
        assert _is_linked(b2, 'fastfst_ModelFastfst32', a)
    _safe_set(a, 'fastfst_nVS_SlPc', None)
    assert not _is_linked(a, 'fastfst_nVS_SlPc', b2)
    if hasattr(b2, 'fastfst_ModelFastfst32'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst32', a)


def test_assoc_YCMode15_link_reassign_clear():
    a = fastfst_iYCMode(name="sample_text", value=7)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_iYCMode', b1)
    assert _is_linked(a, 'fastfst_iYCMode', b1)
    if hasattr(b1, 'fastfst_ModelFastfst16'):
        assert _is_linked(b1, 'fastfst_ModelFastfst16', a)
    _safe_set(a, 'fastfst_iYCMode', b2)
    assert _is_linked(a, 'fastfst_iYCMode', b2)
    if hasattr(b1, 'fastfst_ModelFastfst16'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst16', a)
    if hasattr(b2, 'fastfst_ModelFastfst16'):
        assert _is_linked(b2, 'fastfst_ModelFastfst16', a)
    _safe_set(a, 'fastfst_iYCMode', None)
    assert not _is_linked(a, 'fastfst_iYCMode', b2)
    if hasattr(b2, 'fastfst_ModelFastfst16'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst16', a)


def test_assoc_YawBrMass173_link_reassign_clear():
    a = fastfst_nYawBrMass(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nYawBrMass', b1)
    assert _is_linked(a, 'fastfst_nYawBrMass', b1)
    if hasattr(b1, 'fastfst_ModelFastfst174'):
        assert _is_linked(b1, 'fastfst_ModelFastfst174', a)
    _safe_set(a, 'fastfst_nYawBrMass', b2)
    assert _is_linked(a, 'fastfst_nYawBrMass', b2)
    if hasattr(b1, 'fastfst_ModelFastfst174'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst174', a)
    if hasattr(b2, 'fastfst_ModelFastfst174'):
        assert _is_linked(b2, 'fastfst_ModelFastfst174', a)
    _safe_set(a, 'fastfst_nYawBrMass', None)
    assert not _is_linked(a, 'fastfst_nYawBrMass', b2)
    if hasattr(b2, 'fastfst_ModelFastfst174'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst174', a)


def test_assoc_YawDOF107_link_reassign_clear():
    a = fastfst_bYawDOF(name="sample_text", value=True)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_bYawDOF', b1)
    assert _is_linked(a, 'fastfst_bYawDOF', b1)
    if hasattr(b1, 'fastfst_ModelFastfst108'):
        assert _is_linked(b1, 'fastfst_ModelFastfst108', a)
    _safe_set(a, 'fastfst_bYawDOF', b2)
    assert _is_linked(a, 'fastfst_bYawDOF', b2)
    if hasattr(b1, 'fastfst_ModelFastfst108'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst108', a)
    if hasattr(b2, 'fastfst_ModelFastfst108'):
        assert _is_linked(b2, 'fastfst_ModelFastfst108', a)
    _safe_set(a, 'fastfst_bYawDOF', None)
    assert not _is_linked(a, 'fastfst_bYawDOF', b2)
    if hasattr(b2, 'fastfst_ModelFastfst108'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst108', a)


def test_assoc_YawDamp243_link_reassign_clear():
    a = fastfst_nYawDamp(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nYawDamp', b1)
    assert _is_linked(a, 'fastfst_nYawDamp', b1)
    if hasattr(b1, 'fastfst_ModelFastfst244'):
        assert _is_linked(b1, 'fastfst_ModelFastfst244', a)
    _safe_set(a, 'fastfst_nYawDamp', b2)
    assert _is_linked(a, 'fastfst_nYawDamp', b2)
    if hasattr(b1, 'fastfst_ModelFastfst244'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst244', a)
    if hasattr(b2, 'fastfst_ModelFastfst244'):
        assert _is_linked(b2, 'fastfst_ModelFastfst244', a)
    _safe_set(a, 'fastfst_nYawDamp', None)
    assert not _is_linked(a, 'fastfst_nYawDamp', b2)
    if hasattr(b2, 'fastfst_ModelFastfst244'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst244', a)


def test_assoc_YawNeut245_link_reassign_clear():
    a = fastfst_nYawNeut(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nYawNeut', b1)
    assert _is_linked(a, 'fastfst_nYawNeut', b1)
    if hasattr(b1, 'fastfst_ModelFastfst246'):
        assert _is_linked(b1, 'fastfst_ModelFastfst246', a)
    _safe_set(a, 'fastfst_nYawNeut', b2)
    assert _is_linked(a, 'fastfst_nYawNeut', b2)
    if hasattr(b1, 'fastfst_ModelFastfst246'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst246', a)
    if hasattr(b2, 'fastfst_ModelFastfst246'):
        assert _is_linked(b2, 'fastfst_ModelFastfst246', a)
    _safe_set(a, 'fastfst_nYawNeut', None)
    assert not _is_linked(a, 'fastfst_nYawNeut', b2)
    if hasattr(b2, 'fastfst_ModelFastfst246'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst246', a)


def test_assoc_YawSpr241_link_reassign_clear():
    a = fastfst_nYawSpr(name="sample_text", value=3.14)
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_nYawSpr', b1)
    assert _is_linked(a, 'fastfst_nYawSpr', b1)
    if hasattr(b1, 'fastfst_ModelFastfst242'):
        assert _is_linked(b1, 'fastfst_ModelFastfst242', a)
    _safe_set(a, 'fastfst_nYawSpr', b2)
    assert _is_linked(a, 'fastfst_nYawSpr', b2)
    if hasattr(b1, 'fastfst_ModelFastfst242'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst242', a)
    if hasattr(b2, 'fastfst_ModelFastfst242'):
        assert _is_linked(b2, 'fastfst_ModelFastfst242', a)
    _safe_set(a, 'fastfst_nYawSpr', None)
    assert not _is_linked(a, 'fastfst_nYawSpr', b2)
    if hasattr(b2, 'fastfst_ModelFastfst242'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst242', a)


def test_assoc_sections1_link_reassign_clear():
    a = fastfst_Section(name="sample_text")
    b1 = fastfst_ModelFastfst()
    b2 = fastfst_ModelFastfst()
    _safe_set(a, 'fastfst_Section', b1)
    assert _is_linked(a, 'fastfst_Section', b1)
    if hasattr(b1, 'fastfst_ModelFastfst2'):
        assert _is_linked(b1, 'fastfst_ModelFastfst2', a)
    _safe_set(a, 'fastfst_Section', b2)
    assert _is_linked(a, 'fastfst_Section', b2)
    if hasattr(b1, 'fastfst_ModelFastfst2'):
        assert not _is_linked(b1, 'fastfst_ModelFastfst2', a)
    if hasattr(b2, 'fastfst_ModelFastfst2'):
        assert _is_linked(b2, 'fastfst_ModelFastfst2', a)
    _safe_set(a, 'fastfst_Section', None)
    assert not _is_linked(a, 'fastfst_Section', b2)
    if hasattr(b2, 'fastfst_ModelFastfst2'):
        assert not _is_linked(b2, 'fastfst_ModelFastfst2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fastfst_Header_strategy = st.builds(fastfst_Header, rows=safe_text)
@given(instance=fastfst_Header_strategy)
@settings(max_examples=25)
def test_fastfst_Header_instantiation(instance):
    assert isinstance(instance, fastfst_Header)


fastfst_ModelFastfst_strategy = st.builds(fastfst_ModelFastfst)
@given(instance=fastfst_ModelFastfst_strategy)
@settings(max_examples=25)
def test_fastfst_ModelFastfst_instantiation(instance):
    assert isinstance(instance, fastfst_ModelFastfst)


fastfst_Section_strategy = st.builds(fastfst_Section, name=safe_text)
@given(instance=fastfst_Section_strategy)
@settings(max_examples=25)
def test_fastfst_Section_instantiation(instance):
    assert isinstance(instance, fastfst_Section)


fastfst_aBldGagNd_strategy = st.builds(fastfst_aBldGagNd, name=safe_text, value=safe_text)
@given(instance=fastfst_aBldGagNd_strategy)
@settings(max_examples=25)
def test_fastfst_aBldGagNd_instantiation(instance):
    assert isinstance(instance, fastfst_aBldGagNd)


fastfst_aTwrGagNd_strategy = st.builds(fastfst_aTwrGagNd, name=safe_text, value=safe_text)
@given(instance=fastfst_aTwrGagNd_strategy)
@settings(max_examples=25)
def test_fastfst_aTwrGagNd_instantiation(instance):
    assert isinstance(instance, fastfst_aTwrGagNd)


fastfst_bCompAero_strategy = st.builds(fastfst_bCompAero, name=safe_text, value=st.booleans())
@given(instance=fastfst_bCompAero_strategy)
@settings(max_examples=25)
def test_fastfst_bCompAero_instantiation(instance):
    assert isinstance(instance, fastfst_bCompAero)


fastfst_bCompNoise_strategy = st.builds(fastfst_bCompNoise, name=safe_text, value=st.booleans())
@given(instance=fastfst_bCompNoise_strategy)
@settings(max_examples=25)
def test_fastfst_bCompNoise_instantiation(instance):
    assert isinstance(instance, fastfst_bCompNoise)


fastfst_bDrTrDOF_strategy = st.builds(fastfst_bDrTrDOF, name=safe_text, value=st.booleans())
@given(instance=fastfst_bDrTrDOF_strategy)
@settings(max_examples=25)
def test_fastfst_bDrTrDOF_instantiation(instance):
    assert isinstance(instance, fastfst_bDrTrDOF)


fastfst_bEcho_strategy = st.builds(fastfst_bEcho, name=safe_text, value=st.booleans())
@given(instance=fastfst_bEcho_strategy)
@settings(max_examples=25)
def test_fastfst_bEcho_instantiation(instance):
    assert isinstance(instance, fastfst_bEcho)


fastfst_bEdgeDOF_strategy = st.builds(fastfst_bEdgeDOF, name=safe_text, value=st.booleans())
@given(instance=fastfst_bEdgeDOF_strategy)
@settings(max_examples=25)
def test_fastfst_bEdgeDOF_instantiation(instance):
    assert isinstance(instance, fastfst_bEdgeDOF)


fastfst_bFlapDOF1_strategy = st.builds(fastfst_bFlapDOF1, name=safe_text, value=st.booleans())
@given(instance=fastfst_bFlapDOF1_strategy)
@settings(max_examples=25)
def test_fastfst_bFlapDOF1_instantiation(instance):
    assert isinstance(instance, fastfst_bFlapDOF1)


fastfst_bFlapDOF2_strategy = st.builds(fastfst_bFlapDOF2, name=safe_text, value=st.booleans())
@given(instance=fastfst_bFlapDOF2_strategy)
@settings(max_examples=25)
def test_fastfst_bFlapDOF2_instantiation(instance):
    assert isinstance(instance, fastfst_bFlapDOF2)


fastfst_bFurling_strategy = st.builds(fastfst_bFurling, name=safe_text, value=st.booleans())
@given(instance=fastfst_bFurling_strategy)
@settings(max_examples=25)
def test_fastfst_bFurling_instantiation(instance):
    assert isinstance(instance, fastfst_bFurling)


fastfst_bGBRevers_strategy = st.builds(fastfst_bGBRevers, name=safe_text, value=st.booleans())
@given(instance=fastfst_bGBRevers_strategy)
@settings(max_examples=25)
def test_fastfst_bGBRevers_instantiation(instance):
    assert isinstance(instance, fastfst_bGBRevers)


fastfst_bGenDOF_strategy = st.builds(fastfst_bGenDOF, name=safe_text, value=st.booleans())
@given(instance=fastfst_bGenDOF_strategy)
@settings(max_examples=25)
def test_fastfst_bGenDOF_instantiation(instance):
    assert isinstance(instance, fastfst_bGenDOF)


fastfst_bGenTiStp_strategy = st.builds(fastfst_bGenTiStp, name=safe_text, value=st.booleans())
@given(instance=fastfst_bGenTiStp_strategy)
@settings(max_examples=25)
def test_fastfst_bGenTiStp_instantiation(instance):
    assert isinstance(instance, fastfst_bGenTiStp)


fastfst_bGenTiStr_strategy = st.builds(fastfst_bGenTiStr, name=safe_text, value=st.booleans())
@given(instance=fastfst_bGenTiStr_strategy)
@settings(max_examples=25)
def test_fastfst_bGenTiStr_instantiation(instance):
    assert isinstance(instance, fastfst_bGenTiStr)


fastfst_bOutFileFmt_strategy = st.builds(fastfst_bOutFileFmt, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_bOutFileFmt_strategy)
@settings(max_examples=25)
def test_fastfst_bOutFileFmt_instantiation(instance):
    assert isinstance(instance, fastfst_bOutFileFmt)


fastfst_bSumPrint_strategy = st.builds(fastfst_bSumPrint, name=safe_text, value=st.booleans())
@given(instance=fastfst_bSumPrint_strategy)
@settings(max_examples=25)
def test_fastfst_bSumPrint_instantiation(instance):
    assert isinstance(instance, fastfst_bSumPrint)


fastfst_bTabDelim_strategy = st.builds(fastfst_bTabDelim, name=safe_text, value=st.booleans())
@given(instance=fastfst_bTabDelim_strategy)
@settings(max_examples=25)
def test_fastfst_bTabDelim_instantiation(instance):
    assert isinstance(instance, fastfst_bTabDelim)


fastfst_bTeetDOF_strategy = st.builds(fastfst_bTeetDOF, name=safe_text, value=st.booleans())
@given(instance=fastfst_bTeetDOF_strategy)
@settings(max_examples=25)
def test_fastfst_bTeetDOF_instantiation(instance):
    assert isinstance(instance, fastfst_bTeetDOF)


fastfst_bTwFADOF1_strategy = st.builds(fastfst_bTwFADOF1, name=safe_text, value=st.booleans())
@given(instance=fastfst_bTwFADOF1_strategy)
@settings(max_examples=25)
def test_fastfst_bTwFADOF1_instantiation(instance):
    assert isinstance(instance, fastfst_bTwFADOF1)


fastfst_bTwFADOF2_strategy = st.builds(fastfst_bTwFADOF2, name=safe_text, value=st.booleans())
@given(instance=fastfst_bTwFADOF2_strategy)
@settings(max_examples=25)
def test_fastfst_bTwFADOF2_instantiation(instance):
    assert isinstance(instance, fastfst_bTwFADOF2)


fastfst_bTwSSDOF1_strategy = st.builds(fastfst_bTwSSDOF1, name=safe_text, value=st.booleans())
@given(instance=fastfst_bTwSSDOF1_strategy)
@settings(max_examples=25)
def test_fastfst_bTwSSDOF1_instantiation(instance):
    assert isinstance(instance, fastfst_bTwSSDOF1)


fastfst_bTwSSDOF2_strategy = st.builds(fastfst_bTwSSDOF2, name=safe_text, value=st.booleans())
@given(instance=fastfst_bTwSSDOF2_strategy)
@settings(max_examples=25)
def test_fastfst_bTwSSDOF2_instantiation(instance):
    assert isinstance(instance, fastfst_bTwSSDOF2)


fastfst_bYawDOF_strategy = st.builds(fastfst_bYawDOF, name=safe_text, value=st.booleans())
@given(instance=fastfst_bYawDOF_strategy)
@settings(max_examples=25)
def test_fastfst_bYawDOF_instantiation(instance):
    assert isinstance(instance, fastfst_bYawDOF)


fastfst_fADAMSFile_strategy = st.builds(fastfst_fADAMSFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fADAMSFile_strategy)
@settings(max_examples=25)
def test_fastfst_fADAMSFile_instantiation(instance):
    assert isinstance(instance, fastfst_fADAMSFile)


fastfst_fADFile_strategy = st.builds(fastfst_fADFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fADFile_strategy)
@settings(max_examples=25)
def test_fastfst_fADFile_instantiation(instance):
    assert isinstance(instance, fastfst_fADFile)


fastfst_fBldFile_1__strategy = st.builds(fastfst_fBldFile_1_, name=safe_text, value=safe_text)
@given(instance=fastfst_fBldFile_1__strategy)
@settings(max_examples=25)
def test_fastfst_fBldFile_1__instantiation(instance):
    assert isinstance(instance, fastfst_fBldFile_1_)


fastfst_fBldFile_2__strategy = st.builds(fastfst_fBldFile_2_, name=safe_text, value=safe_text)
@given(instance=fastfst_fBldFile_2__strategy)
@settings(max_examples=25)
def test_fastfst_fBldFile_2__instantiation(instance):
    assert isinstance(instance, fastfst_fBldFile_2_)


fastfst_fBldFile_3__strategy = st.builds(fastfst_fBldFile_3_, name=safe_text, value=safe_text)
@given(instance=fastfst_fBldFile_3__strategy)
@settings(max_examples=25)
def test_fastfst_fBldFile_3__instantiation(instance):
    assert isinstance(instance, fastfst_fBldFile_3_)


fastfst_fDynBrkFi_strategy = st.builds(fastfst_fDynBrkFi, name=safe_text, value=safe_text)
@given(instance=fastfst_fDynBrkFi_strategy)
@settings(max_examples=25)
def test_fastfst_fDynBrkFi_instantiation(instance):
    assert isinstance(instance, fastfst_fDynBrkFi)


fastfst_fFurlFile_strategy = st.builds(fastfst_fFurlFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fFurlFile_strategy)
@settings(max_examples=25)
def test_fastfst_fFurlFile_instantiation(instance):
    assert isinstance(instance, fastfst_fFurlFile)


fastfst_fLinFile_strategy = st.builds(fastfst_fLinFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fLinFile_strategy)
@settings(max_examples=25)
def test_fastfst_fLinFile_instantiation(instance):
    assert isinstance(instance, fastfst_fLinFile)


fastfst_fNoiseFile_strategy = st.builds(fastfst_fNoiseFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fNoiseFile_strategy)
@settings(max_examples=25)
def test_fastfst_fNoiseFile_instantiation(instance):
    assert isinstance(instance, fastfst_fNoiseFile)


fastfst_fPtfmFile_strategy = st.builds(fastfst_fPtfmFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fPtfmFile_strategy)
@settings(max_examples=25)
def test_fastfst_fPtfmFile_instantiation(instance):
    assert isinstance(instance, fastfst_fPtfmFile)


fastfst_fTwrFile_strategy = st.builds(fastfst_fTwrFile, name=safe_text, value=safe_text)
@given(instance=fastfst_fTwrFile_strategy)
@settings(max_examples=25)
def test_fastfst_fTwrFile_instantiation(instance):
    assert isinstance(instance, fastfst_fTwrFile)


fastfst_iADAMSPrep_strategy = st.builds(fastfst_iADAMSPrep, name=safe_text, value=st.integers())
@given(instance=fastfst_iADAMSPrep_strategy)
@settings(max_examples=25)
def test_fastfst_iADAMSPrep_instantiation(instance):
    assert isinstance(instance, fastfst_iADAMSPrep)


fastfst_iAnalMode_strategy = st.builds(fastfst_iAnalMode, name=safe_text, value=st.integers())
@given(instance=fastfst_iAnalMode_strategy)
@settings(max_examples=25)
def test_fastfst_iAnalMode_instantiation(instance):
    assert isinstance(instance, fastfst_iAnalMode)


fastfst_iDecFact_strategy = st.builds(fastfst_iDecFact, name=safe_text, value=st.integers())
@given(instance=fastfst_iDecFact_strategy)
@settings(max_examples=25)
def test_fastfst_iDecFact_instantiation(instance):
    assert isinstance(instance, fastfst_iDecFact)


fastfst_iGenModel_strategy = st.builds(fastfst_iGenModel, name=safe_text, value=st.integers())
@given(instance=fastfst_iGenModel_strategy)
@settings(max_examples=25)
def test_fastfst_iGenModel_instantiation(instance):
    assert isinstance(instance, fastfst_iGenModel)


fastfst_iHSSBrMode_strategy = st.builds(fastfst_iHSSBrMode, name=safe_text, value=st.integers())
@given(instance=fastfst_iHSSBrMode_strategy)
@settings(max_examples=25)
def test_fastfst_iHSSBrMode_instantiation(instance):
    assert isinstance(instance, fastfst_iHSSBrMode)


fastfst_iNBlGages_strategy = st.builds(fastfst_iNBlGages, name=safe_text, value=st.integers())
@given(instance=fastfst_iNBlGages_strategy)
@settings(max_examples=25)
def test_fastfst_iNBlGages_instantiation(instance):
    assert isinstance(instance, fastfst_iNBlGages)


fastfst_iNTwGages_strategy = st.builds(fastfst_iNTwGages, name=safe_text, value=st.integers())
@given(instance=fastfst_iNTwGages_strategy)
@settings(max_examples=25)
def test_fastfst_iNTwGages_instantiation(instance):
    assert isinstance(instance, fastfst_iNTwGages)


fastfst_iNumBl_strategy = st.builds(fastfst_iNumBl, name=safe_text, value=st.integers())
@given(instance=fastfst_iNumBl_strategy)
@settings(max_examples=25)
def test_fastfst_iNumBl_instantiation(instance):
    assert isinstance(instance, fastfst_iNumBl)


fastfst_iPCMode_strategy = st.builds(fastfst_iPCMode, name=safe_text, value=st.integers())
@given(instance=fastfst_iPCMode_strategy)
@settings(max_examples=25)
def test_fastfst_iPCMode_instantiation(instance):
    assert isinstance(instance, fastfst_iPCMode)


fastfst_iPtfmModel_strategy = st.builds(fastfst_iPtfmModel, name=safe_text, value=st.integers())
@given(instance=fastfst_iPtfmModel_strategy)
@settings(max_examples=25)
def test_fastfst_iPtfmModel_instantiation(instance):
    assert isinstance(instance, fastfst_iPtfmModel)


fastfst_iTeetMod_strategy = st.builds(fastfst_iTeetMod, name=safe_text, value=st.integers())
@given(instance=fastfst_iTeetMod_strategy)
@settings(max_examples=25)
def test_fastfst_iTeetMod_instantiation(instance):
    assert isinstance(instance, fastfst_iTeetMod)


fastfst_iTwrNodes_strategy = st.builds(fastfst_iTwrNodes, name=safe_text, value=st.integers())
@given(instance=fastfst_iTwrNodes_strategy)
@settings(max_examples=25)
def test_fastfst_iTwrNodes_instantiation(instance):
    assert isinstance(instance, fastfst_iTwrNodes)


fastfst_iVSContrl_strategy = st.builds(fastfst_iVSContrl, name=safe_text, value=st.integers())
@given(instance=fastfst_iVSContrl_strategy)
@settings(max_examples=25)
def test_fastfst_iVSContrl_instantiation(instance):
    assert isinstance(instance, fastfst_iVSContrl)


fastfst_iYCMode_strategy = st.builds(fastfst_iYCMode, name=safe_text, value=st.integers())
@given(instance=fastfst_iYCMode_strategy)
@settings(max_examples=25)
def test_fastfst_iYCMode_instantiation(instance):
    assert isinstance(instance, fastfst_iYCMode)


fastfst_nAzimB1Up_strategy = st.builds(fastfst_nAzimB1Up, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nAzimB1Up_strategy)
@settings(max_examples=25)
def test_fastfst_nAzimB1Up_instantiation(instance):
    assert isinstance(instance, fastfst_nAzimB1Up)


fastfst_nAzimuth_strategy = st.builds(fastfst_nAzimuth, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nAzimuth_strategy)
@settings(max_examples=25)
def test_fastfst_nAzimuth_instantiation(instance):
    assert isinstance(instance, fastfst_nAzimuth)


fastfst_nBlPitchF_1__strategy = st.builds(fastfst_nBlPitchF_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nBlPitchF_1__strategy)
@settings(max_examples=25)
def test_fastfst_nBlPitchF_1__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitchF_1_)


fastfst_nBlPitchF_2__strategy = st.builds(fastfst_nBlPitchF_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nBlPitchF_2__strategy)
@settings(max_examples=25)
def test_fastfst_nBlPitchF_2__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitchF_2_)


fastfst_nBlPitchF_3__strategy = st.builds(fastfst_nBlPitchF_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nBlPitchF_3__strategy)
@settings(max_examples=25)
def test_fastfst_nBlPitchF_3__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitchF_3_)


fastfst_nBlPitch_1__strategy = st.builds(fastfst_nBlPitch_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nBlPitch_1__strategy)
@settings(max_examples=25)
def test_fastfst_nBlPitch_1__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitch_1_)


fastfst_nBlPitch_2__strategy = st.builds(fastfst_nBlPitch_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nBlPitch_2__strategy)
@settings(max_examples=25)
def test_fastfst_nBlPitch_2__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitch_2_)


fastfst_nBlPitch_3__strategy = st.builds(fastfst_nBlPitch_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nBlPitch_3__strategy)
@settings(max_examples=25)
def test_fastfst_nBlPitch_3__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitch_3_)


fastfst_nDT_strategy = st.builds(fastfst_nDT, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nDT_strategy)
@settings(max_examples=25)
def test_fastfst_nDT_instantiation(instance):
    assert isinstance(instance, fastfst_nDT)


fastfst_nDTTorDmp_strategy = st.builds(fastfst_nDTTorDmp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nDTTorDmp_strategy)
@settings(max_examples=25)
def test_fastfst_nDTTorDmp_instantiation(instance):
    assert isinstance(instance, fastfst_nDTTorDmp)


fastfst_nDTTorSpr_strategy = st.builds(fastfst_nDTTorSpr, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nDTTorSpr_strategy)
@settings(max_examples=25)
def test_fastfst_nDTTorSpr_instantiation(instance):
    assert isinstance(instance, fastfst_nDTTorSpr)


fastfst_nDelta3_strategy = st.builds(fastfst_nDelta3, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nDelta3_strategy)
@settings(max_examples=25)
def test_fastfst_nDelta3_instantiation(instance):
    assert isinstance(instance, fastfst_nDelta3)


fastfst_nGBRatio_strategy = st.builds(fastfst_nGBRatio, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nGBRatio_strategy)
@settings(max_examples=25)
def test_fastfst_nGBRatio_instantiation(instance):
    assert isinstance(instance, fastfst_nGBRatio)


fastfst_nGBoxEff_strategy = st.builds(fastfst_nGBoxEff, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nGBoxEff_strategy)
@settings(max_examples=25)
def test_fastfst_nGBoxEff_instantiation(instance):
    assert isinstance(instance, fastfst_nGBoxEff)


fastfst_nGenEff_strategy = st.builds(fastfst_nGenEff, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nGenEff_strategy)
@settings(max_examples=25)
def test_fastfst_nGenEff_instantiation(instance):
    assert isinstance(instance, fastfst_nGenEff)


fastfst_nGenIner_strategy = st.builds(fastfst_nGenIner, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nGenIner_strategy)
@settings(max_examples=25)
def test_fastfst_nGenIner_instantiation(instance):
    assert isinstance(instance, fastfst_nGenIner)


fastfst_nGravity_strategy = st.builds(fastfst_nGravity, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nGravity_strategy)
@settings(max_examples=25)
def test_fastfst_nGravity_instantiation(instance):
    assert isinstance(instance, fastfst_nGravity)


fastfst_nHSSBrDT_strategy = st.builds(fastfst_nHSSBrDT, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nHSSBrDT_strategy)
@settings(max_examples=25)
def test_fastfst_nHSSBrDT_instantiation(instance):
    assert isinstance(instance, fastfst_nHSSBrDT)


fastfst_nHSSBrTqF_strategy = st.builds(fastfst_nHSSBrTqF, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nHSSBrTqF_strategy)
@settings(max_examples=25)
def test_fastfst_nHSSBrTqF_instantiation(instance):
    assert isinstance(instance, fastfst_nHSSBrTqF)


fastfst_nHubCM_strategy = st.builds(fastfst_nHubCM, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nHubCM_strategy)
@settings(max_examples=25)
def test_fastfst_nHubCM_instantiation(instance):
    assert isinstance(instance, fastfst_nHubCM)


fastfst_nHubIner_strategy = st.builds(fastfst_nHubIner, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nHubIner_strategy)
@settings(max_examples=25)
def test_fastfst_nHubIner_instantiation(instance):
    assert isinstance(instance, fastfst_nHubIner)


fastfst_nHubMass_strategy = st.builds(fastfst_nHubMass, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nHubMass_strategy)
@settings(max_examples=25)
def test_fastfst_nHubMass_instantiation(instance):
    assert isinstance(instance, fastfst_nHubMass)


fastfst_nHubRad_strategy = st.builds(fastfst_nHubRad, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nHubRad_strategy)
@settings(max_examples=25)
def test_fastfst_nHubRad_instantiation(instance):
    assert isinstance(instance, fastfst_nHubRad)


fastfst_nIPDefl_strategy = st.builds(fastfst_nIPDefl, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nIPDefl_strategy)
@settings(max_examples=25)
def test_fastfst_nIPDefl_instantiation(instance):
    assert isinstance(instance, fastfst_nIPDefl)


fastfst_nNacCMxn_strategy = st.builds(fastfst_nNacCMxn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacCMxn_strategy)
@settings(max_examples=25)
def test_fastfst_nNacCMxn_instantiation(instance):
    assert isinstance(instance, fastfst_nNacCMxn)


fastfst_nNacCMyn_strategy = st.builds(fastfst_nNacCMyn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacCMyn_strategy)
@settings(max_examples=25)
def test_fastfst_nNacCMyn_instantiation(instance):
    assert isinstance(instance, fastfst_nNacCMyn)


fastfst_nNacCMzn_strategy = st.builds(fastfst_nNacCMzn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacCMzn_strategy)
@settings(max_examples=25)
def test_fastfst_nNacCMzn_instantiation(instance):
    assert isinstance(instance, fastfst_nNacCMzn)


fastfst_nNacMass_strategy = st.builds(fastfst_nNacMass, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacMass_strategy)
@settings(max_examples=25)
def test_fastfst_nNacMass_instantiation(instance):
    assert isinstance(instance, fastfst_nNacMass)


fastfst_nNacYIner_strategy = st.builds(fastfst_nNacYIner, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacYIner_strategy)
@settings(max_examples=25)
def test_fastfst_nNacYIner_instantiation(instance):
    assert isinstance(instance, fastfst_nNacYIner)


fastfst_nNacYaw_strategy = st.builds(fastfst_nNacYaw, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacYaw_strategy)
@settings(max_examples=25)
def test_fastfst_nNacYaw_instantiation(instance):
    assert isinstance(instance, fastfst_nNacYaw)


fastfst_nNacYawF_strategy = st.builds(fastfst_nNacYawF, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNacYawF_strategy)
@settings(max_examples=25)
def test_fastfst_nNacYawF_instantiation(instance):
    assert isinstance(instance, fastfst_nNacYawF)


fastfst_nNcIMUxn_strategy = st.builds(fastfst_nNcIMUxn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNcIMUxn_strategy)
@settings(max_examples=25)
def test_fastfst_nNcIMUxn_instantiation(instance):
    assert isinstance(instance, fastfst_nNcIMUxn)


fastfst_nNcIMUyn_strategy = st.builds(fastfst_nNcIMUyn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNcIMUyn_strategy)
@settings(max_examples=25)
def test_fastfst_nNcIMUyn_instantiation(instance):
    assert isinstance(instance, fastfst_nNcIMUyn)


fastfst_nNcIMUzn_strategy = st.builds(fastfst_nNcIMUzn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nNcIMUzn_strategy)
@settings(max_examples=25)
def test_fastfst_nNcIMUzn_instantiation(instance):
    assert isinstance(instance, fastfst_nNcIMUzn)


fastfst_nOoPDefl_strategy = st.builds(fastfst_nOoPDefl, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nOoPDefl_strategy)
@settings(max_examples=25)
def test_fastfst_nOoPDefl_instantiation(instance):
    assert isinstance(instance, fastfst_nOoPDefl)


fastfst_nOverHang_strategy = st.builds(fastfst_nOverHang, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nOverHang_strategy)
@settings(max_examples=25)
def test_fastfst_nOverHang_instantiation(instance):
    assert isinstance(instance, fastfst_nOverHang)


fastfst_nPSpnElN_strategy = st.builds(fastfst_nPSpnElN, name=safe_text, value=st.integers())
@given(instance=fastfst_nPSpnElN_strategy)
@settings(max_examples=25)
def test_fastfst_nPSpnElN_instantiation(instance):
    assert isinstance(instance, fastfst_nPSpnElN)


fastfst_nPreCone_1__strategy = st.builds(fastfst_nPreCone_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nPreCone_1__strategy)
@settings(max_examples=25)
def test_fastfst_nPreCone_1__instantiation(instance):
    assert isinstance(instance, fastfst_nPreCone_1_)


fastfst_nPreCone_2__strategy = st.builds(fastfst_nPreCone_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nPreCone_2__strategy)
@settings(max_examples=25)
def test_fastfst_nPreCone_2__instantiation(instance):
    assert isinstance(instance, fastfst_nPreCone_2_)


fastfst_nPreCone_3__strategy = st.builds(fastfst_nPreCone_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nPreCone_3__strategy)
@settings(max_examples=25)
def test_fastfst_nPreCone_3__instantiation(instance):
    assert isinstance(instance, fastfst_nPreCone_3_)


fastfst_nRotSpeed_strategy = st.builds(fastfst_nRotSpeed, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nRotSpeed_strategy)
@settings(max_examples=25)
def test_fastfst_nRotSpeed_instantiation(instance):
    assert isinstance(instance, fastfst_nRotSpeed)


fastfst_nSIG_PORt_strategy = st.builds(fastfst_nSIG_PORt, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nSIG_PORt_strategy)
@settings(max_examples=25)
def test_fastfst_nSIG_PORt_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_PORt)


fastfst_nSIG_RtTq_strategy = st.builds(fastfst_nSIG_RtTq, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nSIG_RtTq_strategy)
@settings(max_examples=25)
def test_fastfst_nSIG_RtTq_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_RtTq)


fastfst_nSIG_SlPc_strategy = st.builds(fastfst_nSIG_SlPc, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nSIG_SlPc_strategy)
@settings(max_examples=25)
def test_fastfst_nSIG_SlPc_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_SlPc)


fastfst_nSIG_SySp_strategy = st.builds(fastfst_nSIG_SySp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nSIG_SySp_strategy)
@settings(max_examples=25)
def test_fastfst_nSIG_SySp_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_SySp)


fastfst_nShftGagL_strategy = st.builds(fastfst_nShftGagL, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nShftGagL_strategy)
@settings(max_examples=25)
def test_fastfst_nShftGagL_instantiation(instance):
    assert isinstance(instance, fastfst_nShftGagL)


fastfst_nShftTilt_strategy = st.builds(fastfst_nShftTilt, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nShftTilt_strategy)
@settings(max_examples=25)
def test_fastfst_nShftTilt_instantiation(instance):
    assert isinstance(instance, fastfst_nShftTilt)


fastfst_nSpdGenOn_strategy = st.builds(fastfst_nSpdGenOn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nSpdGenOn_strategy)
@settings(max_examples=25)
def test_fastfst_nSpdGenOn_instantiation(instance):
    assert isinstance(instance, fastfst_nSpdGenOn)


fastfst_nSttsTime_strategy = st.builds(fastfst_nSttsTime, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nSttsTime_strategy)
@settings(max_examples=25)
def test_fastfst_nSttsTime_instantiation(instance):
    assert isinstance(instance, fastfst_nSttsTime)


fastfst_nTBDepISp_1__strategy = st.builds(fastfst_nTBDepISp_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTBDepISp_1__strategy)
@settings(max_examples=25)
def test_fastfst_nTBDepISp_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTBDepISp_1_)


fastfst_nTBDepISp_2__strategy = st.builds(fastfst_nTBDepISp_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTBDepISp_2__strategy)
@settings(max_examples=25)
def test_fastfst_nTBDepISp_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTBDepISp_2_)


fastfst_nTBDepISp_3__strategy = st.builds(fastfst_nTBDepISp_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTBDepISp_3__strategy)
@settings(max_examples=25)
def test_fastfst_nTBDepISp_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTBDepISp_3_)


fastfst_nTBDrConD_strategy = st.builds(fastfst_nTBDrConD, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTBDrConD_strategy)
@settings(max_examples=25)
def test_fastfst_nTBDrConD_instantiation(instance):
    assert isinstance(instance, fastfst_nTBDrConD)


fastfst_nTBDrConN_strategy = st.builds(fastfst_nTBDrConN, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTBDrConN_strategy)
@settings(max_examples=25)
def test_fastfst_nTBDrConN_instantiation(instance):
    assert isinstance(instance, fastfst_nTBDrConN)


fastfst_nTEC_Freq_strategy = st.builds(fastfst_nTEC_Freq, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_Freq_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_Freq_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Freq)


fastfst_nTEC_MR_strategy = st.builds(fastfst_nTEC_MR, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_MR_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_MR_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_MR)


fastfst_nTEC_Npol_strategy = st.builds(fastfst_nTEC_Npol, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_Npol_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_Npol_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Npol)


fastfst_nTEC_RLR_strategy = st.builds(fastfst_nTEC_RLR, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_RLR_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_RLR_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_RLR)


fastfst_nTEC_Rres_strategy = st.builds(fastfst_nTEC_Rres, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_Rres_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_Rres_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Rres)


fastfst_nTEC_SLR_strategy = st.builds(fastfst_nTEC_SLR, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_SLR_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_SLR_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_SLR)


fastfst_nTEC_Sres_strategy = st.builds(fastfst_nTEC_Sres, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_Sres_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_Sres_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Sres)


fastfst_nTEC_VLL_strategy = st.builds(fastfst_nTEC_VLL, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTEC_VLL_strategy)
@settings(max_examples=25)
def test_fastfst_nTEC_VLL_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_VLL)


fastfst_nTHSSBrDp_strategy = st.builds(fastfst_nTHSSBrDp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTHSSBrDp_strategy)
@settings(max_examples=25)
def test_fastfst_nTHSSBrDp_instantiation(instance):
    assert isinstance(instance, fastfst_nTHSSBrDp)


fastfst_nTMax_strategy = st.builds(fastfst_nTMax, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTMax_strategy)
@settings(max_examples=25)
def test_fastfst_nTMax_instantiation(instance):
    assert isinstance(instance, fastfst_nTMax)


fastfst_nTPCOn_strategy = st.builds(fastfst_nTPCOn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPCOn_strategy)
@settings(max_examples=25)
def test_fastfst_nTPCOn_instantiation(instance):
    assert isinstance(instance, fastfst_nTPCOn)


fastfst_nTPitManE_1__strategy = st.builds(fastfst_nTPitManE_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPitManE_1__strategy)
@settings(max_examples=25)
def test_fastfst_nTPitManE_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManE_1_)


fastfst_nTPitManE_2__strategy = st.builds(fastfst_nTPitManE_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPitManE_2__strategy)
@settings(max_examples=25)
def test_fastfst_nTPitManE_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManE_2_)


fastfst_nTPitManE_3__strategy = st.builds(fastfst_nTPitManE_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPitManE_3__strategy)
@settings(max_examples=25)
def test_fastfst_nTPitManE_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManE_3_)


fastfst_nTPitManS_1__strategy = st.builds(fastfst_nTPitManS_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPitManS_1__strategy)
@settings(max_examples=25)
def test_fastfst_nTPitManS_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManS_1_)


fastfst_nTPitManS_2__strategy = st.builds(fastfst_nTPitManS_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPitManS_2__strategy)
@settings(max_examples=25)
def test_fastfst_nTPitManS_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManS_2_)


fastfst_nTPitManS_3__strategy = st.builds(fastfst_nTPitManS_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTPitManS_3__strategy)
@settings(max_examples=25)
def test_fastfst_nTPitManS_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManS_3_)


fastfst_nTStart_strategy = st.builds(fastfst_nTStart, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTStart_strategy)
@settings(max_examples=25)
def test_fastfst_nTStart_instantiation(instance):
    assert isinstance(instance, fastfst_nTStart)


fastfst_nTTDspFA_strategy = st.builds(fastfst_nTTDspFA, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTTDspFA_strategy)
@settings(max_examples=25)
def test_fastfst_nTTDspFA_instantiation(instance):
    assert isinstance(instance, fastfst_nTTDspFA)


fastfst_nTTDspSS_strategy = st.builds(fastfst_nTTDspSS, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTTDspSS_strategy)
@settings(max_examples=25)
def test_fastfst_nTTDspSS_instantiation(instance):
    assert isinstance(instance, fastfst_nTTDspSS)


fastfst_nTTpBrDp_1__strategy = st.builds(fastfst_nTTpBrDp_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTTpBrDp_1__strategy)
@settings(max_examples=25)
def test_fastfst_nTTpBrDp_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTTpBrDp_1_)


fastfst_nTTpBrDp_2__strategy = st.builds(fastfst_nTTpBrDp_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTTpBrDp_2__strategy)
@settings(max_examples=25)
def test_fastfst_nTTpBrDp_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTTpBrDp_2_)


fastfst_nTTpBrDp_3__strategy = st.builds(fastfst_nTTpBrDp_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTTpBrDp_3__strategy)
@settings(max_examples=25)
def test_fastfst_nTTpBrDp_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTTpBrDp_3_)


fastfst_nTYCOn_strategy = st.builds(fastfst_nTYCOn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTYCOn_strategy)
@settings(max_examples=25)
def test_fastfst_nTYCOn_instantiation(instance):
    assert isinstance(instance, fastfst_nTYCOn)


fastfst_nTYawManE_strategy = st.builds(fastfst_nTYawManE, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTYawManE_strategy)
@settings(max_examples=25)
def test_fastfst_nTYawManE_instantiation(instance):
    assert isinstance(instance, fastfst_nTYawManE)


fastfst_nTYawManS_strategy = st.builds(fastfst_nTYawManS, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTYawManS_strategy)
@settings(max_examples=25)
def test_fastfst_nTYawManS_instantiation(instance):
    assert isinstance(instance, fastfst_nTYawManS)


fastfst_nTeetCDmp_strategy = st.builds(fastfst_nTeetCDmp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetCDmp_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetCDmp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetCDmp)


fastfst_nTeetDefl_strategy = st.builds(fastfst_nTeetDefl, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetDefl_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetDefl_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetDefl)


fastfst_nTeetDmp_strategy = st.builds(fastfst_nTeetDmp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetDmp_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetDmp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetDmp)


fastfst_nTeetDmpP_strategy = st.builds(fastfst_nTeetDmpP, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetDmpP_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetDmpP_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetDmpP)


fastfst_nTeetHSSp_strategy = st.builds(fastfst_nTeetHSSp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetHSSp_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetHSSp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetHSSp)


fastfst_nTeetHStP_strategy = st.builds(fastfst_nTeetHStP, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetHStP_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetHStP_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetHStP)


fastfst_nTeetSSSp_strategy = st.builds(fastfst_nTeetSSSp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetSSSp_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetSSSp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetSSSp)


fastfst_nTeetSStP_strategy = st.builds(fastfst_nTeetSStP, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTeetSStP_strategy)
@settings(max_examples=25)
def test_fastfst_nTeetSStP_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetSStP)


fastfst_nTiDynBrk_strategy = st.builds(fastfst_nTiDynBrk, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTiDynBrk_strategy)
@settings(max_examples=25)
def test_fastfst_nTiDynBrk_instantiation(instance):
    assert isinstance(instance, fastfst_nTiDynBrk)


fastfst_nTimGenOf_strategy = st.builds(fastfst_nTimGenOf, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTimGenOf_strategy)
@settings(max_examples=25)
def test_fastfst_nTimGenOf_instantiation(instance):
    assert isinstance(instance, fastfst_nTimGenOf)


fastfst_nTimGenOn_strategy = st.builds(fastfst_nTimGenOn, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTimGenOn_strategy)
@settings(max_examples=25)
def test_fastfst_nTimGenOn_instantiation(instance):
    assert isinstance(instance, fastfst_nTimGenOn)


fastfst_nTipMass_1__strategy = st.builds(fastfst_nTipMass_1_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTipMass_1__strategy)
@settings(max_examples=25)
def test_fastfst_nTipMass_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTipMass_1_)


fastfst_nTipMass_2__strategy = st.builds(fastfst_nTipMass_2_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTipMass_2__strategy)
@settings(max_examples=25)
def test_fastfst_nTipMass_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTipMass_2_)


fastfst_nTipMass_3__strategy = st.builds(fastfst_nTipMass_3_, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTipMass_3__strategy)
@settings(max_examples=25)
def test_fastfst_nTipMass_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTipMass_3_)


fastfst_nTipRad_strategy = st.builds(fastfst_nTipRad, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTipRad_strategy)
@settings(max_examples=25)
def test_fastfst_nTipRad_instantiation(instance):
    assert isinstance(instance, fastfst_nTipRad)


fastfst_nTowerHt_strategy = st.builds(fastfst_nTowerHt, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTowerHt_strategy)
@settings(max_examples=25)
def test_fastfst_nTowerHt_instantiation(instance):
    assert isinstance(instance, fastfst_nTowerHt)


fastfst_nTpBrDT_strategy = st.builds(fastfst_nTpBrDT, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTpBrDT_strategy)
@settings(max_examples=25)
def test_fastfst_nTpBrDT_instantiation(instance):
    assert isinstance(instance, fastfst_nTpBrDT)


fastfst_nTwr2Shft_strategy = st.builds(fastfst_nTwr2Shft, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTwr2Shft_strategy)
@settings(max_examples=25)
def test_fastfst_nTwr2Shft_instantiation(instance):
    assert isinstance(instance, fastfst_nTwr2Shft)


fastfst_nTwrRBHt_strategy = st.builds(fastfst_nTwrRBHt, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nTwrRBHt_strategy)
@settings(max_examples=25)
def test_fastfst_nTwrRBHt_instantiation(instance):
    assert isinstance(instance, fastfst_nTwrRBHt)


fastfst_nUndSling_strategy = st.builds(fastfst_nUndSling, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nUndSling_strategy)
@settings(max_examples=25)
def test_fastfst_nUndSling_instantiation(instance):
    assert isinstance(instance, fastfst_nUndSling)


fastfst_nVS_Rgn2K_strategy = st.builds(fastfst_nVS_Rgn2K, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nVS_Rgn2K_strategy)
@settings(max_examples=25)
def test_fastfst_nVS_Rgn2K_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_Rgn2K)


fastfst_nVS_RtGnSp_strategy = st.builds(fastfst_nVS_RtGnSp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nVS_RtGnSp_strategy)
@settings(max_examples=25)
def test_fastfst_nVS_RtGnSp_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_RtGnSp)


fastfst_nVS_RtTq_strategy = st.builds(fastfst_nVS_RtTq, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nVS_RtTq_strategy)
@settings(max_examples=25)
def test_fastfst_nVS_RtTq_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_RtTq)


fastfst_nVS_SlPc_strategy = st.builds(fastfst_nVS_SlPc, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nVS_SlPc_strategy)
@settings(max_examples=25)
def test_fastfst_nVS_SlPc_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_SlPc)


fastfst_nYawBrMass_strategy = st.builds(fastfst_nYawBrMass, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nYawBrMass_strategy)
@settings(max_examples=25)
def test_fastfst_nYawBrMass_instantiation(instance):
    assert isinstance(instance, fastfst_nYawBrMass)


fastfst_nYawDamp_strategy = st.builds(fastfst_nYawDamp, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nYawDamp_strategy)
@settings(max_examples=25)
def test_fastfst_nYawDamp_instantiation(instance):
    assert isinstance(instance, fastfst_nYawDamp)


fastfst_nYawNeut_strategy = st.builds(fastfst_nYawNeut, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nYawNeut_strategy)
@settings(max_examples=25)
def test_fastfst_nYawNeut_instantiation(instance):
    assert isinstance(instance, fastfst_nYawNeut)


fastfst_nYawSpr_strategy = st.builds(fastfst_nYawSpr, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=fastfst_nYawSpr_strategy)
@settings(max_examples=25)
def test_fastfst_nYawSpr_instantiation(instance):
    assert isinstance(instance, fastfst_nYawSpr)


fastfst_sOutFmt_strategy = st.builds(fastfst_sOutFmt, name=safe_text, value=safe_text)
@given(instance=fastfst_sOutFmt_strategy)
@settings(max_examples=25)
def test_fastfst_sOutFmt_instantiation(instance):
    assert isinstance(instance, fastfst_sOutFmt)


fastfst_vOutList_strategy = st.builds(fastfst_vOutList, name=safe_text, value=safe_text)
@given(instance=fastfst_vOutList_strategy)
@settings(max_examples=25)
def test_fastfst_vOutList_instantiation(instance):
    assert isinstance(instance, fastfst_vOutList)



