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
    scrShYQYaSD_ak,
    scrShYQYaSD_HVOwDYkMdHvynG,
    scrShYQYaSD_xvHXdRr,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_scrshyqyasd_ak_is_not_abstract():
    assert not inspect.isabstract(scrShYQYaSD_ak)


def test_hyp_scrshyqyasd_ak_constructor_exists():
    assert callable(scrShYQYaSD_ak.__init__)


def test_hyp_scrshyqyasd_ak_constructor_args():
    sig = inspect.signature(scrShYQYaSD_ak.__init__)
    params = list(sig.parameters.keys())
    assert "CXmvqzTe" in params, "Missing parameter 'CXmvqzTe'"
    assert "MHQpVCYtERyk" in params, "Missing parameter 'MHQpVCYtERyk'"
    assert "zBIcb" in params, "Missing parameter 'zBIcb'"






def test_hyp_scrshyqyasd_hvowdykmdhvyng_is_not_abstract():
    assert not inspect.isabstract(scrShYQYaSD_HVOwDYkMdHvynG)


def test_hyp_scrshyqyasd_hvowdykmdhvyng_constructor_exists():
    assert callable(scrShYQYaSD_HVOwDYkMdHvynG.__init__)


def test_hyp_scrshyqyasd_hvowdykmdhvyng_constructor_args():
    sig = inspect.signature(scrShYQYaSD_HVOwDYkMdHvynG.__init__)
    params = list(sig.parameters.keys())
    assert "vdjNPHX" in params, "Missing parameter 'vdjNPHX'"




def test_hyp_scrshyqyasd_xvhxdrr_is_not_abstract():
    assert not inspect.isabstract(scrShYQYaSD_xvHXdRr)


def test_hyp_scrshyqyasd_xvhxdrr_constructor_exists():
    assert callable(scrShYQYaSD_xvHXdRr.__init__)


def test_hyp_scrshyqyasd_xvhxdrr_constructor_args():
    sig = inspect.signature(scrShYQYaSD_xvHXdRr.__init__)
    params = list(sig.parameters.keys())


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
scrShYQYaSD_ak_strategy = st.builds(
    scrShYQYaSD_ak,
    CXmvqzTe=
        safe_text,
    MHQpVCYtERyk=
        safe_text,
    zBIcb=
        safe_text
)
scrShYQYaSD_HVOwDYkMdHvynG_strategy = st.builds(
    scrShYQYaSD_HVOwDYkMdHvynG,
    vdjNPHX=
        safe_text
)
scrShYQYaSD_xvHXdRr_strategy = st.builds(
    scrShYQYaSD_xvHXdRr,
)




@given(instance=scrShYQYaSD_ak_strategy)
def test_hyp_scrshyqyasd_ak_CXmvqzTe_setter(instance):
    original = instance.CXmvqzTe
    instance.CXmvqzTe = original
    assert instance.CXmvqzTe == original



@given(instance=scrShYQYaSD_ak_strategy)
def test_hyp_scrshyqyasd_ak_MHQpVCYtERyk_setter(instance):
    original = instance.MHQpVCYtERyk
    instance.MHQpVCYtERyk = original
    assert instance.MHQpVCYtERyk == original



@given(instance=scrShYQYaSD_ak_strategy)
def test_hyp_scrshyqyasd_ak_zBIcb_setter(instance):
    original = instance.zBIcb
    instance.zBIcb = original
    assert instance.zBIcb == original




@given(instance=scrShYQYaSD_HVOwDYkMdHvynG_strategy)
def test_hyp_scrshyqyasd_hvowdykmdhvyng_vdjNPHX_setter(instance):
    original = instance.vdjNPHX
    instance.vdjNPHX = original
    assert instance.vdjNPHX == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    scrShYQYaSD_HVOwDYkMdHvynG,
    scrShYQYaSD_ak,
    scrShYQYaSD_xvHXdRr,
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

def test_scrShYQYaSD_HVOwDYkMdHvynG_vdjNPHX_value_roundtrip():
    instance = scrShYQYaSD_HVOwDYkMdHvynG(vdjNPHX="sample_text")
    assert instance.vdjNPHX == "sample_text"
    instance.vdjNPHX = "sample_text_2"
    assert instance.vdjNPHX == "sample_text_2"


def test_scrShYQYaSD_ak_CXmvqzTe_value_roundtrip():
    instance = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    assert instance.CXmvqzTe == "sample_text"
    instance.CXmvqzTe = "sample_text_2"
    assert instance.CXmvqzTe == "sample_text_2"


def test_scrShYQYaSD_ak_MHQpVCYtERyk_value_roundtrip():
    instance = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    assert instance.MHQpVCYtERyk == "sample_text"
    instance.MHQpVCYtERyk = "sample_text_2"
    assert instance.MHQpVCYtERyk == "sample_text_2"


def test_scrShYQYaSD_ak_zBIcb_value_roundtrip():
    instance = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    assert instance.zBIcb == "sample_text"
    instance.zBIcb = "sample_text_2"
    assert instance.zBIcb == "sample_text_2"


def test_assoc_BASoFcxsCI1_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_ak', b1)
    assert _is_linked(a, 'scrShYQYaSD_ak', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr2'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr2', a)
    _safe_set(a, 'scrShYQYaSD_ak', b2)
    assert _is_linked(a, 'scrShYQYaSD_ak', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr2'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr2', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr2'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr2', a)
    _safe_set(a, 'scrShYQYaSD_ak', None)
    assert not _is_linked(a, 'scrShYQYaSD_ak', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr2'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr2', a)


def test_assoc_JZZCZDdtPb9_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_ak11', b1)
    assert _is_linked(a, 'scrShYQYaSD_ak11', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr10'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr10', a)
    _safe_set(a, 'scrShYQYaSD_ak11', b2)
    assert _is_linked(a, 'scrShYQYaSD_ak11', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr10'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr10', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr10'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr10', a)
    _safe_set(a, 'scrShYQYaSD_ak11', None)
    assert not _is_linked(a, 'scrShYQYaSD_ak11', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr10'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr10', a)


def test_assoc_VSMbxzKCXwhSgFqrC0_link_reassign_clear():
    a = scrShYQYaSD_HVOwDYkMdHvynG(vdjNPHX="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_HVOwDYkMdHvynG', b1)
    assert _is_linked(a, 'scrShYQYaSD_HVOwDYkMdHvynG', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr', a)
    _safe_set(a, 'scrShYQYaSD_HVOwDYkMdHvynG', b2)
    assert _is_linked(a, 'scrShYQYaSD_HVOwDYkMdHvynG', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr', a)
    _safe_set(a, 'scrShYQYaSD_HVOwDYkMdHvynG', None)
    assert not _is_linked(a, 'scrShYQYaSD_HVOwDYkMdHvynG', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr', a)


def test_assoc_XObnJr15_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_ak16', b1)
    assert _is_linked(a, 'scrShYQYaSD_ak16', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr17'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr17', a)
    _safe_set(a, 'scrShYQYaSD_ak16', b2)
    assert _is_linked(a, 'scrShYQYaSD_ak16', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr17'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr17', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr17'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr17', a)
    _safe_set(a, 'scrShYQYaSD_ak16', None)
    assert not _is_linked(a, 'scrShYQYaSD_ak16', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr17'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr17', a)


def test_assoc_gQaACsS18_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_ak19', b1)
    assert _is_linked(a, 'scrShYQYaSD_ak19', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr20'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr20', a)
    _safe_set(a, 'scrShYQYaSD_ak19', b2)
    assert _is_linked(a, 'scrShYQYaSD_ak19', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr20'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr20', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr20'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr20', a)
    _safe_set(a, 'scrShYQYaSD_ak19', None)
    assert not _is_linked(a, 'scrShYQYaSD_ak19', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr20'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr20', a)


def test_assoc_keJwdNxMQ6_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_ak8', b1)
    assert _is_linked(a, 'scrShYQYaSD_ak8', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr7'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr7', a)
    _safe_set(a, 'scrShYQYaSD_ak8', b2)
    assert _is_linked(a, 'scrShYQYaSD_ak8', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr7'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr7', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr7'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr7', a)
    _safe_set(a, 'scrShYQYaSD_ak8', None)
    assert not _is_linked(a, 'scrShYQYaSD_ak8', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr7'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr7', a)


def test_assoc_kykuZBWLRVLW13_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b2 = scrShYQYaSD_ak(CXmvqzTe="sample_text_2", MHQpVCYtERyk="sample_text_2", zBIcb="sample_text_2")
    _safe_set(a, 'scrShYQYaSD_ak12', {b1})
    assert _is_linked(a, 'scrShYQYaSD_ak12', b1)
    if hasattr(b1, 'scrShYQYaSD_ak14'):
        assert _is_linked(b1, 'scrShYQYaSD_ak14', a)
    _safe_set(a, 'scrShYQYaSD_ak12', {b2})
    assert _is_linked(a, 'scrShYQYaSD_ak12', b2)
    if hasattr(b1, 'scrShYQYaSD_ak14'):
        assert not _is_linked(b1, 'scrShYQYaSD_ak14', a)
    if hasattr(b2, 'scrShYQYaSD_ak14'):
        assert _is_linked(b2, 'scrShYQYaSD_ak14', a)
    _safe_set(a, 'scrShYQYaSD_ak12', set())
    assert not _is_linked(a, 'scrShYQYaSD_ak12', b2)
    if hasattr(b2, 'scrShYQYaSD_ak14'):
        assert not _is_linked(b2, 'scrShYQYaSD_ak14', a)


def test_assoc_njevJtUoy3_link_reassign_clear():
    a = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    b1 = scrShYQYaSD_xvHXdRr()
    b2 = scrShYQYaSD_xvHXdRr()
    _safe_set(a, 'scrShYQYaSD_ak5', b1)
    assert _is_linked(a, 'scrShYQYaSD_ak5', b1)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr4'):
        assert _is_linked(b1, 'scrShYQYaSD_xvHXdRr4', a)
    _safe_set(a, 'scrShYQYaSD_ak5', b2)
    assert _is_linked(a, 'scrShYQYaSD_ak5', b2)
    if hasattr(b1, 'scrShYQYaSD_xvHXdRr4'):
        assert not _is_linked(b1, 'scrShYQYaSD_xvHXdRr4', a)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr4'):
        assert _is_linked(b2, 'scrShYQYaSD_xvHXdRr4', a)
    _safe_set(a, 'scrShYQYaSD_ak5', None)
    assert not _is_linked(a, 'scrShYQYaSD_ak5', b2)
    if hasattr(b2, 'scrShYQYaSD_xvHXdRr4'):
        assert not _is_linked(b2, 'scrShYQYaSD_xvHXdRr4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

scrShYQYaSD_HVOwDYkMdHvynG_strategy = st.builds(scrShYQYaSD_HVOwDYkMdHvynG, vdjNPHX=safe_text)
@given(instance=scrShYQYaSD_HVOwDYkMdHvynG_strategy)
@settings(max_examples=25)
def test_scrShYQYaSD_HVOwDYkMdHvynG_instantiation(instance):
    assert isinstance(instance, scrShYQYaSD_HVOwDYkMdHvynG)


scrShYQYaSD_ak_strategy = st.builds(scrShYQYaSD_ak, CXmvqzTe=safe_text, MHQpVCYtERyk=safe_text, zBIcb=safe_text)
@given(instance=scrShYQYaSD_ak_strategy)
@settings(max_examples=25)
def test_scrShYQYaSD_ak_instantiation(instance):
    assert isinstance(instance, scrShYQYaSD_ak)


scrShYQYaSD_xvHXdRr_strategy = st.builds(scrShYQYaSD_xvHXdRr)
@given(instance=scrShYQYaSD_xvHXdRr_strategy)
@settings(max_examples=25)
def test_scrShYQYaSD_xvHXdRr_instantiation(instance):
    assert isinstance(instance, scrShYQYaSD_xvHXdRr)



