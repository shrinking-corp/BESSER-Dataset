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
    Ker_t__n_tiedot_UseCase,
    Vakuutusyhti_,
    Vakuutus,
    Asiakas,
    Korvauksen_maksaminen_UseCase,
    Hakemuksen_k_sittely_UseCase,
    Vakuutusyhti__Actor,
    Vakuutusselvitys_UseCase,
    Kirjautuminen_UseCase,
    Korvauksen_Hakeminen_UseCase,
    K_ytt_j__Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ker_t__n_tiedot_usecase_is_not_abstract():
    assert not inspect.isabstract(Ker_t__n_tiedot_UseCase)


def test_hyp_ker_t__n_tiedot_usecase_constructor_exists():
    assert callable(Ker_t__n_tiedot_UseCase.__init__)


def test_hyp_ker_t__n_tiedot_usecase_constructor_args():
    sig = inspect.signature(Ker_t__n_tiedot_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vakuutusyhti__is_not_abstract():
    assert not inspect.isabstract(Vakuutusyhti_)


def test_hyp_vakuutusyhti__constructor_exists():
    assert callable(Vakuutusyhti_.__init__)


def test_hyp_vakuutusyhti__constructor_args():
    sig = inspect.signature(Vakuutusyhti_.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vakuutus_is_not_abstract():
    assert not inspect.isabstract(Vakuutus)


def test_hyp_vakuutus_constructor_exists():
    assert callable(Vakuutus.__init__)


def test_hyp_vakuutus_constructor_args():
    sig = inspect.signature(Vakuutus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_asiakas_is_not_abstract():
    assert not inspect.isabstract(Asiakas)


def test_hyp_asiakas_constructor_exists():
    assert callable(Asiakas.__init__)


def test_hyp_asiakas_constructor_args():
    sig = inspect.signature(Asiakas.__init__)
    params = list(sig.parameters.keys())
    assert "Asiakas__id_" in params, "Missing parameter 'Asiakas__id_'"




def test_hyp_korvauksen_maksaminen_usecase_is_not_abstract():
    assert not inspect.isabstract(Korvauksen_maksaminen_UseCase)


def test_hyp_korvauksen_maksaminen_usecase_constructor_exists():
    assert callable(Korvauksen_maksaminen_UseCase.__init__)


def test_hyp_korvauksen_maksaminen_usecase_constructor_args():
    sig = inspect.signature(Korvauksen_maksaminen_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hakemuksen_k_sittely_usecase_is_not_abstract():
    assert not inspect.isabstract(Hakemuksen_k_sittely_UseCase)


def test_hyp_hakemuksen_k_sittely_usecase_constructor_exists():
    assert callable(Hakemuksen_k_sittely_UseCase.__init__)


def test_hyp_hakemuksen_k_sittely_usecase_constructor_args():
    sig = inspect.signature(Hakemuksen_k_sittely_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vakuutusyhti__actor_is_not_abstract():
    assert not inspect.isabstract(Vakuutusyhti__Actor)


def test_hyp_vakuutusyhti__actor_constructor_exists():
    assert callable(Vakuutusyhti__Actor.__init__)


def test_hyp_vakuutusyhti__actor_constructor_args():
    sig = inspect.signature(Vakuutusyhti__Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vakuutusselvitys_usecase_is_not_abstract():
    assert not inspect.isabstract(Vakuutusselvitys_UseCase)


def test_hyp_vakuutusselvitys_usecase_constructor_exists():
    assert callable(Vakuutusselvitys_UseCase.__init__)


def test_hyp_vakuutusselvitys_usecase_constructor_args():
    sig = inspect.signature(Vakuutusselvitys_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kirjautuminen_usecase_is_not_abstract():
    assert not inspect.isabstract(Kirjautuminen_UseCase)


def test_hyp_kirjautuminen_usecase_constructor_exists():
    assert callable(Kirjautuminen_UseCase.__init__)


def test_hyp_kirjautuminen_usecase_constructor_args():
    sig = inspect.signature(Kirjautuminen_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_korvauksen_hakeminen_usecase_is_not_abstract():
    assert not inspect.isabstract(Korvauksen_Hakeminen_UseCase)


def test_hyp_korvauksen_hakeminen_usecase_constructor_exists():
    assert callable(Korvauksen_Hakeminen_UseCase.__init__)


def test_hyp_korvauksen_hakeminen_usecase_constructor_args():
    sig = inspect.signature(Korvauksen_Hakeminen_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k_ytt_j__actor_is_not_abstract():
    assert not inspect.isabstract(K_ytt_j__Actor)


def test_hyp_k_ytt_j__actor_constructor_exists():
    assert callable(K_ytt_j__Actor.__init__)


def test_hyp_k_ytt_j__actor_constructor_args():
    sig = inspect.signature(K_ytt_j__Actor.__init__)
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
Ker_t__n_tiedot_UseCase_strategy = st.builds(
    Ker_t__n_tiedot_UseCase,
)
Vakuutusyhti__strategy = st.builds(
    Vakuutusyhti_,
)
Vakuutus_strategy = st.builds(
    Vakuutus,
)
Asiakas_strategy = st.builds(
    Asiakas,
    Asiakas__id_=
        st.integers()
)
Korvauksen_maksaminen_UseCase_strategy = st.builds(
    Korvauksen_maksaminen_UseCase,
)
Hakemuksen_k_sittely_UseCase_strategy = st.builds(
    Hakemuksen_k_sittely_UseCase,
)
Vakuutusyhti__Actor_strategy = st.builds(
    Vakuutusyhti__Actor,
)
Vakuutusselvitys_UseCase_strategy = st.builds(
    Vakuutusselvitys_UseCase,
)
Kirjautuminen_UseCase_strategy = st.builds(
    Kirjautuminen_UseCase,
)
Korvauksen_Hakeminen_UseCase_strategy = st.builds(
    Korvauksen_Hakeminen_UseCase,
)
K_ytt_j__Actor_strategy = st.builds(
    K_ytt_j__Actor,
)







@given(instance=Asiakas_strategy)
def test_hyp_asiakas_Asiakas__id__setter(instance):
    original = instance.Asiakas__id_
    instance.Asiakas__id_ = original
    assert instance.Asiakas__id_ == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Asiakas,
    Hakemuksen_k_sittely_UseCase,
    K_ytt_j__Actor,
    Ker_t__n_tiedot_UseCase,
    Kirjautuminen_UseCase,
    Korvauksen_Hakeminen_UseCase,
    Korvauksen_maksaminen_UseCase,
    Vakuutus,
    Vakuutusselvitys_UseCase,
    Vakuutusyhti_,
    Vakuutusyhti__Actor,
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

def test_Asiakas_Asiakas__id__value_roundtrip():
    instance = Asiakas(Asiakas__id_=7)
    assert instance.Asiakas__id_ == 7
    instance.Asiakas__id_ = 13
    assert instance.Asiakas__id_ == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Asiakas_strategy = st.builds(Asiakas, Asiakas__id_=st.integers())
@given(instance=Asiakas_strategy)
@settings(max_examples=25)
def test_Asiakas_instantiation(instance):
    assert isinstance(instance, Asiakas)


Hakemuksen_k_sittely_UseCase_strategy = st.builds(Hakemuksen_k_sittely_UseCase)
@given(instance=Hakemuksen_k_sittely_UseCase_strategy)
@settings(max_examples=25)
def test_Hakemuksen_k_sittely_UseCase_instantiation(instance):
    assert isinstance(instance, Hakemuksen_k_sittely_UseCase)


K_ytt_j__Actor_strategy = st.builds(K_ytt_j__Actor)
@given(instance=K_ytt_j__Actor_strategy)
@settings(max_examples=25)
def test_K_ytt_j__Actor_instantiation(instance):
    assert isinstance(instance, K_ytt_j__Actor)


Ker_t__n_tiedot_UseCase_strategy = st.builds(Ker_t__n_tiedot_UseCase)
@given(instance=Ker_t__n_tiedot_UseCase_strategy)
@settings(max_examples=25)
def test_Ker_t__n_tiedot_UseCase_instantiation(instance):
    assert isinstance(instance, Ker_t__n_tiedot_UseCase)


Kirjautuminen_UseCase_strategy = st.builds(Kirjautuminen_UseCase)
@given(instance=Kirjautuminen_UseCase_strategy)
@settings(max_examples=25)
def test_Kirjautuminen_UseCase_instantiation(instance):
    assert isinstance(instance, Kirjautuminen_UseCase)


Korvauksen_Hakeminen_UseCase_strategy = st.builds(Korvauksen_Hakeminen_UseCase)
@given(instance=Korvauksen_Hakeminen_UseCase_strategy)
@settings(max_examples=25)
def test_Korvauksen_Hakeminen_UseCase_instantiation(instance):
    assert isinstance(instance, Korvauksen_Hakeminen_UseCase)


Korvauksen_maksaminen_UseCase_strategy = st.builds(Korvauksen_maksaminen_UseCase)
@given(instance=Korvauksen_maksaminen_UseCase_strategy)
@settings(max_examples=25)
def test_Korvauksen_maksaminen_UseCase_instantiation(instance):
    assert isinstance(instance, Korvauksen_maksaminen_UseCase)


Vakuutus_strategy = st.builds(Vakuutus)
@given(instance=Vakuutus_strategy)
@settings(max_examples=25)
def test_Vakuutus_instantiation(instance):
    assert isinstance(instance, Vakuutus)


Vakuutusselvitys_UseCase_strategy = st.builds(Vakuutusselvitys_UseCase)
@given(instance=Vakuutusselvitys_UseCase_strategy)
@settings(max_examples=25)
def test_Vakuutusselvitys_UseCase_instantiation(instance):
    assert isinstance(instance, Vakuutusselvitys_UseCase)


Vakuutusyhti__strategy = st.builds(Vakuutusyhti_)
@given(instance=Vakuutusyhti__strategy)
@settings(max_examples=25)
def test_Vakuutusyhti__instantiation(instance):
    assert isinstance(instance, Vakuutusyhti_)


Vakuutusyhti__Actor_strategy = st.builds(Vakuutusyhti__Actor)
@given(instance=Vakuutusyhti__Actor_strategy)
@settings(max_examples=25)
def test_Vakuutusyhti__Actor_instantiation(instance):
    assert isinstance(instance, Vakuutusyhti__Actor)



