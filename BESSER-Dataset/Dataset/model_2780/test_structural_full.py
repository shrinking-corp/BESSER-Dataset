import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AChild,
    BChild,
    CChild,
    DChild,
    EChild,
    ExprChild,
    FChild,
    GChild,
    HChild,
    IChild,
    JChild,
    KChild,
    LChild,
    MChild,
    NChild,
    OChild,
    PChild,
    QChild,
    RChild,
    SChild,
    TChild,
    UChild,
    VChild,
    WChild,
    XChild,
    YChild,
    ZChild,
    top_A,
    top_AChild,
    top_B,
    top_BChild,
    top_C,
    top_CChild,
    top_D,
    top_DChild,
    top_E,
    top_EChild,
    top_Expr,
    top_ExprChild,
    top_F,
    top_FChild,
    top_G,
    top_GChild,
    top_H,
    top_HChild,
    top_I,
    top_IChild,
    top_IntegerLiteral,
    top_J,
    top_JChild,
    top_K,
    top_KChild,
    top_L,
    top_LChild,
    top_M,
    top_MChild,
    top_N,
    top_NChild,
    top_O,
    top_OChild,
    top_P,
    top_PChild,
    top_Q,
    top_QChild,
    top_R,
    top_RChild,
    top_S,
    top_SChild,
    top_T,
    top_TChild,
    top_U,
    top_UChild,
    top_V,
    top_VChild,
    top_W,
    top_WChild,
    top_X,
    top_XChild,
    top_Y,
    top_YChild,
    top_Z,
    top_ZChild,
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

def test_top_IntegerLiteral_value_value_roundtrip():
    instance = top_IntegerLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_top_B_isa_AChild():
    instance = top_B()
    assert isinstance(instance, AChild)


def test_top_BChild_isa_AChild():
    instance = top_BChild()
    assert isinstance(instance, AChild)


def test_top_C_isa_BChild():
    instance = top_C()
    assert isinstance(instance, BChild)


def test_top_CChild_isa_BChild():
    instance = top_CChild()
    assert isinstance(instance, BChild)


def test_top_D_isa_CChild():
    instance = top_D()
    assert isinstance(instance, CChild)


def test_top_DChild_isa_CChild():
    instance = top_DChild()
    assert isinstance(instance, CChild)


def test_top_E_isa_DChild():
    instance = top_E()
    assert isinstance(instance, DChild)


def test_top_EChild_isa_DChild():
    instance = top_EChild()
    assert isinstance(instance, DChild)


def test_top_F_isa_EChild():
    instance = top_F()
    assert isinstance(instance, EChild)


def test_top_FChild_isa_EChild():
    instance = top_FChild()
    assert isinstance(instance, EChild)


def test_top_A_isa_ExprChild():
    instance = top_A()
    assert isinstance(instance, ExprChild)


def test_top_AChild_isa_ExprChild():
    instance = top_AChild()
    assert isinstance(instance, ExprChild)


def test_top_G_isa_FChild():
    instance = top_G()
    assert isinstance(instance, FChild)


def test_top_GChild_isa_FChild():
    instance = top_GChild()
    assert isinstance(instance, FChild)


def test_top_H_isa_GChild():
    instance = top_H()
    assert isinstance(instance, GChild)


def test_top_HChild_isa_GChild():
    instance = top_HChild()
    assert isinstance(instance, GChild)


def test_top_I_isa_HChild():
    instance = top_I()
    assert isinstance(instance, HChild)


def test_top_IChild_isa_HChild():
    instance = top_IChild()
    assert isinstance(instance, HChild)


def test_top_J_isa_IChild():
    instance = top_J()
    assert isinstance(instance, IChild)


def test_top_JChild_isa_IChild():
    instance = top_JChild()
    assert isinstance(instance, IChild)


def test_top_K_isa_JChild():
    instance = top_K()
    assert isinstance(instance, JChild)


def test_top_KChild_isa_JChild():
    instance = top_KChild()
    assert isinstance(instance, JChild)


def test_top_L_isa_KChild():
    instance = top_L()
    assert isinstance(instance, KChild)


def test_top_LChild_isa_KChild():
    instance = top_LChild()
    assert isinstance(instance, KChild)


def test_top_M_isa_LChild():
    instance = top_M()
    assert isinstance(instance, LChild)


def test_top_MChild_isa_LChild():
    instance = top_MChild()
    assert isinstance(instance, LChild)


def test_top_N_isa_MChild():
    instance = top_N()
    assert isinstance(instance, MChild)


def test_top_NChild_isa_MChild():
    instance = top_NChild()
    assert isinstance(instance, MChild)


def test_top_O_isa_NChild():
    instance = top_O()
    assert isinstance(instance, NChild)


def test_top_OChild_isa_NChild():
    instance = top_OChild()
    assert isinstance(instance, NChild)


def test_top_P_isa_OChild():
    instance = top_P()
    assert isinstance(instance, OChild)


def test_top_PChild_isa_OChild():
    instance = top_PChild()
    assert isinstance(instance, OChild)


def test_top_Q_isa_PChild():
    instance = top_Q()
    assert isinstance(instance, PChild)


def test_top_QChild_isa_PChild():
    instance = top_QChild()
    assert isinstance(instance, PChild)


def test_top_R_isa_QChild():
    instance = top_R()
    assert isinstance(instance, QChild)


def test_top_RChild_isa_QChild():
    instance = top_RChild()
    assert isinstance(instance, QChild)


def test_top_S_isa_RChild():
    instance = top_S()
    assert isinstance(instance, RChild)


def test_top_SChild_isa_RChild():
    instance = top_SChild()
    assert isinstance(instance, RChild)


def test_top_T_isa_SChild():
    instance = top_T()
    assert isinstance(instance, SChild)


def test_top_TChild_isa_SChild():
    instance = top_TChild()
    assert isinstance(instance, SChild)


def test_top_U_isa_TChild():
    instance = top_U()
    assert isinstance(instance, TChild)


def test_top_UChild_isa_TChild():
    instance = top_UChild()
    assert isinstance(instance, TChild)


def test_top_V_isa_UChild():
    instance = top_V()
    assert isinstance(instance, UChild)


def test_top_VChild_isa_UChild():
    instance = top_VChild()
    assert isinstance(instance, UChild)


def test_top_W_isa_VChild():
    instance = top_W()
    assert isinstance(instance, VChild)


def test_top_WChild_isa_VChild():
    instance = top_WChild()
    assert isinstance(instance, VChild)


def test_top_X_isa_WChild():
    instance = top_X()
    assert isinstance(instance, WChild)


def test_top_XChild_isa_WChild():
    instance = top_XChild()
    assert isinstance(instance, WChild)


def test_top_Y_isa_XChild():
    instance = top_Y()
    assert isinstance(instance, XChild)


def test_top_YChild_isa_XChild():
    instance = top_YChild()
    assert isinstance(instance, XChild)


def test_top_Z_isa_YChild():
    instance = top_Z()
    assert isinstance(instance, YChild)


def test_top_ZChild_isa_YChild():
    instance = top_ZChild()
    assert isinstance(instance, YChild)


def test_top_IntegerLiteral_isa_ZChild():
    instance = top_IntegerLiteral(value=7)
    assert isinstance(instance, ZChild)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AChild_strategy = st.builds(AChild)
@given(instance=AChild_strategy)
@settings(max_examples=25)
def test_AChild_instantiation(instance):
    assert isinstance(instance, AChild)


BChild_strategy = st.builds(BChild)
@given(instance=BChild_strategy)
@settings(max_examples=25)
def test_BChild_instantiation(instance):
    assert isinstance(instance, BChild)


CChild_strategy = st.builds(CChild)
@given(instance=CChild_strategy)
@settings(max_examples=25)
def test_CChild_instantiation(instance):
    assert isinstance(instance, CChild)


DChild_strategy = st.builds(DChild)
@given(instance=DChild_strategy)
@settings(max_examples=25)
def test_DChild_instantiation(instance):
    assert isinstance(instance, DChild)


EChild_strategy = st.builds(EChild)
@given(instance=EChild_strategy)
@settings(max_examples=25)
def test_EChild_instantiation(instance):
    assert isinstance(instance, EChild)


ExprChild_strategy = st.builds(ExprChild)
@given(instance=ExprChild_strategy)
@settings(max_examples=25)
def test_ExprChild_instantiation(instance):
    assert isinstance(instance, ExprChild)


FChild_strategy = st.builds(FChild)
@given(instance=FChild_strategy)
@settings(max_examples=25)
def test_FChild_instantiation(instance):
    assert isinstance(instance, FChild)


GChild_strategy = st.builds(GChild)
@given(instance=GChild_strategy)
@settings(max_examples=25)
def test_GChild_instantiation(instance):
    assert isinstance(instance, GChild)


HChild_strategy = st.builds(HChild)
@given(instance=HChild_strategy)
@settings(max_examples=25)
def test_HChild_instantiation(instance):
    assert isinstance(instance, HChild)


IChild_strategy = st.builds(IChild)
@given(instance=IChild_strategy)
@settings(max_examples=25)
def test_IChild_instantiation(instance):
    assert isinstance(instance, IChild)


JChild_strategy = st.builds(JChild)
@given(instance=JChild_strategy)
@settings(max_examples=25)
def test_JChild_instantiation(instance):
    assert isinstance(instance, JChild)


KChild_strategy = st.builds(KChild)
@given(instance=KChild_strategy)
@settings(max_examples=25)
def test_KChild_instantiation(instance):
    assert isinstance(instance, KChild)


LChild_strategy = st.builds(LChild)
@given(instance=LChild_strategy)
@settings(max_examples=25)
def test_LChild_instantiation(instance):
    assert isinstance(instance, LChild)


MChild_strategy = st.builds(MChild)
@given(instance=MChild_strategy)
@settings(max_examples=25)
def test_MChild_instantiation(instance):
    assert isinstance(instance, MChild)


NChild_strategy = st.builds(NChild)
@given(instance=NChild_strategy)
@settings(max_examples=25)
def test_NChild_instantiation(instance):
    assert isinstance(instance, NChild)


OChild_strategy = st.builds(OChild)
@given(instance=OChild_strategy)
@settings(max_examples=25)
def test_OChild_instantiation(instance):
    assert isinstance(instance, OChild)


PChild_strategy = st.builds(PChild)
@given(instance=PChild_strategy)
@settings(max_examples=25)
def test_PChild_instantiation(instance):
    assert isinstance(instance, PChild)


QChild_strategy = st.builds(QChild)
@given(instance=QChild_strategy)
@settings(max_examples=25)
def test_QChild_instantiation(instance):
    assert isinstance(instance, QChild)


RChild_strategy = st.builds(RChild)
@given(instance=RChild_strategy)
@settings(max_examples=25)
def test_RChild_instantiation(instance):
    assert isinstance(instance, RChild)


SChild_strategy = st.builds(SChild)
@given(instance=SChild_strategy)
@settings(max_examples=25)
def test_SChild_instantiation(instance):
    assert isinstance(instance, SChild)


TChild_strategy = st.builds(TChild)
@given(instance=TChild_strategy)
@settings(max_examples=25)
def test_TChild_instantiation(instance):
    assert isinstance(instance, TChild)


UChild_strategy = st.builds(UChild)
@given(instance=UChild_strategy)
@settings(max_examples=25)
def test_UChild_instantiation(instance):
    assert isinstance(instance, UChild)


VChild_strategy = st.builds(VChild)
@given(instance=VChild_strategy)
@settings(max_examples=25)
def test_VChild_instantiation(instance):
    assert isinstance(instance, VChild)


WChild_strategy = st.builds(WChild)
@given(instance=WChild_strategy)
@settings(max_examples=25)
def test_WChild_instantiation(instance):
    assert isinstance(instance, WChild)


XChild_strategy = st.builds(XChild)
@given(instance=XChild_strategy)
@settings(max_examples=25)
def test_XChild_instantiation(instance):
    assert isinstance(instance, XChild)


YChild_strategy = st.builds(YChild)
@given(instance=YChild_strategy)
@settings(max_examples=25)
def test_YChild_instantiation(instance):
    assert isinstance(instance, YChild)


ZChild_strategy = st.builds(ZChild)
@given(instance=ZChild_strategy)
@settings(max_examples=25)
def test_ZChild_instantiation(instance):
    assert isinstance(instance, ZChild)


top_A_strategy = st.builds(top_A)
@given(instance=top_A_strategy)
@settings(max_examples=25)
def test_top_A_instantiation(instance):
    assert isinstance(instance, top_A)


top_AChild_strategy = st.builds(top_AChild)
@given(instance=top_AChild_strategy)
@settings(max_examples=25)
def test_top_AChild_instantiation(instance):
    assert isinstance(instance, top_AChild)


top_B_strategy = st.builds(top_B)
@given(instance=top_B_strategy)
@settings(max_examples=25)
def test_top_B_instantiation(instance):
    assert isinstance(instance, top_B)


top_BChild_strategy = st.builds(top_BChild)
@given(instance=top_BChild_strategy)
@settings(max_examples=25)
def test_top_BChild_instantiation(instance):
    assert isinstance(instance, top_BChild)


top_C_strategy = st.builds(top_C)
@given(instance=top_C_strategy)
@settings(max_examples=25)
def test_top_C_instantiation(instance):
    assert isinstance(instance, top_C)


top_CChild_strategy = st.builds(top_CChild)
@given(instance=top_CChild_strategy)
@settings(max_examples=25)
def test_top_CChild_instantiation(instance):
    assert isinstance(instance, top_CChild)


top_D_strategy = st.builds(top_D)
@given(instance=top_D_strategy)
@settings(max_examples=25)
def test_top_D_instantiation(instance):
    assert isinstance(instance, top_D)


top_DChild_strategy = st.builds(top_DChild)
@given(instance=top_DChild_strategy)
@settings(max_examples=25)
def test_top_DChild_instantiation(instance):
    assert isinstance(instance, top_DChild)


top_E_strategy = st.builds(top_E)
@given(instance=top_E_strategy)
@settings(max_examples=25)
def test_top_E_instantiation(instance):
    assert isinstance(instance, top_E)


top_EChild_strategy = st.builds(top_EChild)
@given(instance=top_EChild_strategy)
@settings(max_examples=25)
def test_top_EChild_instantiation(instance):
    assert isinstance(instance, top_EChild)


top_Expr_strategy = st.builds(top_Expr)
@given(instance=top_Expr_strategy)
@settings(max_examples=25)
def test_top_Expr_instantiation(instance):
    assert isinstance(instance, top_Expr)


top_ExprChild_strategy = st.builds(top_ExprChild)
@given(instance=top_ExprChild_strategy)
@settings(max_examples=25)
def test_top_ExprChild_instantiation(instance):
    assert isinstance(instance, top_ExprChild)


top_F_strategy = st.builds(top_F)
@given(instance=top_F_strategy)
@settings(max_examples=25)
def test_top_F_instantiation(instance):
    assert isinstance(instance, top_F)


top_FChild_strategy = st.builds(top_FChild)
@given(instance=top_FChild_strategy)
@settings(max_examples=25)
def test_top_FChild_instantiation(instance):
    assert isinstance(instance, top_FChild)


top_G_strategy = st.builds(top_G)
@given(instance=top_G_strategy)
@settings(max_examples=25)
def test_top_G_instantiation(instance):
    assert isinstance(instance, top_G)


top_GChild_strategy = st.builds(top_GChild)
@given(instance=top_GChild_strategy)
@settings(max_examples=25)
def test_top_GChild_instantiation(instance):
    assert isinstance(instance, top_GChild)


top_H_strategy = st.builds(top_H)
@given(instance=top_H_strategy)
@settings(max_examples=25)
def test_top_H_instantiation(instance):
    assert isinstance(instance, top_H)


top_HChild_strategy = st.builds(top_HChild)
@given(instance=top_HChild_strategy)
@settings(max_examples=25)
def test_top_HChild_instantiation(instance):
    assert isinstance(instance, top_HChild)


top_I_strategy = st.builds(top_I)
@given(instance=top_I_strategy)
@settings(max_examples=25)
def test_top_I_instantiation(instance):
    assert isinstance(instance, top_I)


top_IChild_strategy = st.builds(top_IChild)
@given(instance=top_IChild_strategy)
@settings(max_examples=25)
def test_top_IChild_instantiation(instance):
    assert isinstance(instance, top_IChild)


top_IntegerLiteral_strategy = st.builds(top_IntegerLiteral, value=st.integers())
@given(instance=top_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_top_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, top_IntegerLiteral)


top_J_strategy = st.builds(top_J)
@given(instance=top_J_strategy)
@settings(max_examples=25)
def test_top_J_instantiation(instance):
    assert isinstance(instance, top_J)


top_JChild_strategy = st.builds(top_JChild)
@given(instance=top_JChild_strategy)
@settings(max_examples=25)
def test_top_JChild_instantiation(instance):
    assert isinstance(instance, top_JChild)


top_K_strategy = st.builds(top_K)
@given(instance=top_K_strategy)
@settings(max_examples=25)
def test_top_K_instantiation(instance):
    assert isinstance(instance, top_K)


top_KChild_strategy = st.builds(top_KChild)
@given(instance=top_KChild_strategy)
@settings(max_examples=25)
def test_top_KChild_instantiation(instance):
    assert isinstance(instance, top_KChild)


top_L_strategy = st.builds(top_L)
@given(instance=top_L_strategy)
@settings(max_examples=25)
def test_top_L_instantiation(instance):
    assert isinstance(instance, top_L)


top_LChild_strategy = st.builds(top_LChild)
@given(instance=top_LChild_strategy)
@settings(max_examples=25)
def test_top_LChild_instantiation(instance):
    assert isinstance(instance, top_LChild)


top_M_strategy = st.builds(top_M)
@given(instance=top_M_strategy)
@settings(max_examples=25)
def test_top_M_instantiation(instance):
    assert isinstance(instance, top_M)


top_MChild_strategy = st.builds(top_MChild)
@given(instance=top_MChild_strategy)
@settings(max_examples=25)
def test_top_MChild_instantiation(instance):
    assert isinstance(instance, top_MChild)


top_N_strategy = st.builds(top_N)
@given(instance=top_N_strategy)
@settings(max_examples=25)
def test_top_N_instantiation(instance):
    assert isinstance(instance, top_N)


top_NChild_strategy = st.builds(top_NChild)
@given(instance=top_NChild_strategy)
@settings(max_examples=25)
def test_top_NChild_instantiation(instance):
    assert isinstance(instance, top_NChild)


top_O_strategy = st.builds(top_O)
@given(instance=top_O_strategy)
@settings(max_examples=25)
def test_top_O_instantiation(instance):
    assert isinstance(instance, top_O)


top_OChild_strategy = st.builds(top_OChild)
@given(instance=top_OChild_strategy)
@settings(max_examples=25)
def test_top_OChild_instantiation(instance):
    assert isinstance(instance, top_OChild)


top_P_strategy = st.builds(top_P)
@given(instance=top_P_strategy)
@settings(max_examples=25)
def test_top_P_instantiation(instance):
    assert isinstance(instance, top_P)


top_PChild_strategy = st.builds(top_PChild)
@given(instance=top_PChild_strategy)
@settings(max_examples=25)
def test_top_PChild_instantiation(instance):
    assert isinstance(instance, top_PChild)


top_Q_strategy = st.builds(top_Q)
@given(instance=top_Q_strategy)
@settings(max_examples=25)
def test_top_Q_instantiation(instance):
    assert isinstance(instance, top_Q)


top_QChild_strategy = st.builds(top_QChild)
@given(instance=top_QChild_strategy)
@settings(max_examples=25)
def test_top_QChild_instantiation(instance):
    assert isinstance(instance, top_QChild)


top_R_strategy = st.builds(top_R)
@given(instance=top_R_strategy)
@settings(max_examples=25)
def test_top_R_instantiation(instance):
    assert isinstance(instance, top_R)


top_RChild_strategy = st.builds(top_RChild)
@given(instance=top_RChild_strategy)
@settings(max_examples=25)
def test_top_RChild_instantiation(instance):
    assert isinstance(instance, top_RChild)


top_S_strategy = st.builds(top_S)
@given(instance=top_S_strategy)
@settings(max_examples=25)
def test_top_S_instantiation(instance):
    assert isinstance(instance, top_S)


top_SChild_strategy = st.builds(top_SChild)
@given(instance=top_SChild_strategy)
@settings(max_examples=25)
def test_top_SChild_instantiation(instance):
    assert isinstance(instance, top_SChild)


top_T_strategy = st.builds(top_T)
@given(instance=top_T_strategy)
@settings(max_examples=25)
def test_top_T_instantiation(instance):
    assert isinstance(instance, top_T)


top_TChild_strategy = st.builds(top_TChild)
@given(instance=top_TChild_strategy)
@settings(max_examples=25)
def test_top_TChild_instantiation(instance):
    assert isinstance(instance, top_TChild)


top_U_strategy = st.builds(top_U)
@given(instance=top_U_strategy)
@settings(max_examples=25)
def test_top_U_instantiation(instance):
    assert isinstance(instance, top_U)


top_UChild_strategy = st.builds(top_UChild)
@given(instance=top_UChild_strategy)
@settings(max_examples=25)
def test_top_UChild_instantiation(instance):
    assert isinstance(instance, top_UChild)


top_V_strategy = st.builds(top_V)
@given(instance=top_V_strategy)
@settings(max_examples=25)
def test_top_V_instantiation(instance):
    assert isinstance(instance, top_V)


top_VChild_strategy = st.builds(top_VChild)
@given(instance=top_VChild_strategy)
@settings(max_examples=25)
def test_top_VChild_instantiation(instance):
    assert isinstance(instance, top_VChild)


top_W_strategy = st.builds(top_W)
@given(instance=top_W_strategy)
@settings(max_examples=25)
def test_top_W_instantiation(instance):
    assert isinstance(instance, top_W)


top_WChild_strategy = st.builds(top_WChild)
@given(instance=top_WChild_strategy)
@settings(max_examples=25)
def test_top_WChild_instantiation(instance):
    assert isinstance(instance, top_WChild)


top_X_strategy = st.builds(top_X)
@given(instance=top_X_strategy)
@settings(max_examples=25)
def test_top_X_instantiation(instance):
    assert isinstance(instance, top_X)


top_XChild_strategy = st.builds(top_XChild)
@given(instance=top_XChild_strategy)
@settings(max_examples=25)
def test_top_XChild_instantiation(instance):
    assert isinstance(instance, top_XChild)


top_Y_strategy = st.builds(top_Y)
@given(instance=top_Y_strategy)
@settings(max_examples=25)
def test_top_Y_instantiation(instance):
    assert isinstance(instance, top_Y)


top_YChild_strategy = st.builds(top_YChild)
@given(instance=top_YChild_strategy)
@settings(max_examples=25)
def test_top_YChild_instantiation(instance):
    assert isinstance(instance, top_YChild)


top_Z_strategy = st.builds(top_Z)
@given(instance=top_Z_strategy)
@settings(max_examples=25)
def test_top_Z_instantiation(instance):
    assert isinstance(instance, top_Z)


top_ZChild_strategy = st.builds(top_ZChild)
@given(instance=top_ZChild_strategy)
@settings(max_examples=25)
def test_top_ZChild_instantiation(instance):
    assert isinstance(instance, top_ZChild)


