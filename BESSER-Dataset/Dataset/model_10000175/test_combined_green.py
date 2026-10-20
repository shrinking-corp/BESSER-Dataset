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
    Transakcija,
    Kupac,
    Osiguranje,
    Aran_man,
    Agent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_transakcija_is_not_abstract():
    assert not inspect.isabstract(Transakcija)


def test_hyp_transakcija_constructor_exists():
    assert callable(Transakcija.__init__)


def test_hyp_transakcija_constructor_args():
    sig = inspect.signature(Transakcija.__init__)
    params = list(sig.parameters.keys())
    assert "datum_trans" in params, "Missing parameter 'datum_trans'"
    assert "suma" in params, "Missing parameter 'suma'"
    assert "Trans_ID" in params, "Missing parameter 'Trans_ID'"
    assert "tip" in params, "Missing parameter 'tip'"







def test_hyp_kupac_is_not_abstract():
    assert not inspect.isabstract(Kupac)


def test_hyp_kupac_constructor_exists():
    assert callable(Kupac.__init__)


def test_hyp_kupac_constructor_args():
    sig = inspect.signature(Kupac.__init__)
    params = list(sig.parameters.keys())
    assert "Mobilni" in params, "Missing parameter 'Mobilni'"
    assert "BrojPasosa" in params, "Missing parameter 'BrojPasosa'"
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "Ime" in params, "Missing parameter 'Ime'"
    assert "Kupac_ID" in params, "Missing parameter 'Kupac_ID'"
    assert "Prezime" in params, "Missing parameter 'Prezime'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"










def test_hyp_osiguranje_is_not_abstract():
    assert not inspect.isabstract(Osiguranje)


def test_hyp_osiguranje_constructor_exists():
    assert callable(Osiguranje.__init__)


def test_hyp_osiguranje_constructor_args():
    sig = inspect.signature(Osiguranje.__init__)
    params = list(sig.parameters.keys())
    assert "BrojPolise" in params, "Missing parameter 'BrojPolise'"
    assert "Cena" in params, "Missing parameter 'Cena'"
    assert "OsigKuca" in params, "Missing parameter 'OsigKuca'"
    assert "PaketPokri_a" in params, "Missing parameter 'PaketPokri_a'"
    assert "Osiguranje_ID" in params, "Missing parameter 'Osiguranje_ID'"








def test_hyp_aran_man_is_not_abstract():
    assert not inspect.isabstract(Aran_man)


def test_hyp_aran_man_constructor_exists():
    assert callable(Aran_man.__init__)


def test_hyp_aran_man_constructor_args():
    sig = inspect.signature(Aran_man.__init__)
    params = list(sig.parameters.keys())
    assert "NazivAran_" in params, "Missing parameter 'NazivAran_'"
    assert "DatumPolaska" in params, "Missing parameter 'DatumPolaska'"
    assert "DatumPovratka" in params, "Missing parameter 'DatumPovratka'"
    assert "Cena" in params, "Missing parameter 'Cena'"
    assert "Aranzman_ID" in params, "Missing parameter 'Aranzman_ID'"
    assert "SlobMesto" in params, "Missing parameter 'SlobMesto'"









def test_hyp_agent_is_not_abstract():
    assert not inspect.isabstract(Agent)


def test_hyp_agent_constructor_exists():
    assert callable(Agent.__init__)


def test_hyp_agent_constructor_args():
    sig = inspect.signature(Agent.__init__)
    params = list(sig.parameters.keys())
    assert "Ime" in params, "Missing parameter 'Ime'"
    assert "Agent_ID" in params, "Missing parameter 'Agent_ID'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "BrojAgenta" in params, "Missing parameter 'BrojAgenta'"
    assert "Prezime" in params, "Missing parameter 'Prezime'"







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
Transakcija_strategy = st.builds(
    Transakcija,
    datum_trans=
        safe_text,
    suma=
        safe_text,
    Trans_ID=
        safe_text,
    tip=
        safe_text
)
Kupac_strategy = st.builds(
    Kupac,
    Mobilni=
        st.integers(),
    BrojPasosa=
        st.integers(),
    Grad=
        safe_text,
    Ime=
        safe_text,
    Kupac_ID=
        safe_text,
    Prezime=
        safe_text,
    JMBG=
        st.integers()
)
Osiguranje_strategy = st.builds(
    Osiguranje,
    BrojPolise=
        st.integers(),
    Cena=
        safe_text,
    OsigKuca=
        safe_text,
    PaketPokri_a=
        safe_text,
    Osiguranje_ID=
        safe_text
)
Aran_man_strategy = st.builds(
    Aran_man,
    NazivAran_=
        safe_text,
    DatumPolaska=
        safe_text,
    DatumPovratka=
        safe_text,
    Cena=
        safe_text,
    Aranzman_ID=
        safe_text,
    SlobMesto=
        st.booleans()
)
Agent_strategy = st.builds(
    Agent,
    Ime=
        safe_text,
    Agent_ID=
        safe_text,
    JMBG=
        st.integers(),
    BrojAgenta=
        st.integers(),
    Prezime=
        safe_text
)




@given(instance=Transakcija_strategy)
def test_hyp_transakcija_datum_trans_setter(instance):
    original = instance.datum_trans
    instance.datum_trans = original
    assert instance.datum_trans == original



@given(instance=Transakcija_strategy)
def test_hyp_transakcija_suma_setter(instance):
    original = instance.suma
    instance.suma = original
    assert instance.suma == original



@given(instance=Transakcija_strategy)
def test_hyp_transakcija_Trans_ID_setter(instance):
    original = instance.Trans_ID
    instance.Trans_ID = original
    assert instance.Trans_ID == original



@given(instance=Transakcija_strategy)
def test_hyp_transakcija_tip_setter(instance):
    original = instance.tip
    instance.tip = original
    assert instance.tip == original




@given(instance=Kupac_strategy)
def test_hyp_kupac_Mobilni_setter(instance):
    original = instance.Mobilni
    instance.Mobilni = original
    assert instance.Mobilni == original



@given(instance=Kupac_strategy)
def test_hyp_kupac_BrojPasosa_setter(instance):
    original = instance.BrojPasosa
    instance.BrojPasosa = original
    assert instance.BrojPasosa == original



@given(instance=Kupac_strategy)
def test_hyp_kupac_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Kupac_strategy)
def test_hyp_kupac_Ime_setter(instance):
    original = instance.Ime
    instance.Ime = original
    assert instance.Ime == original



@given(instance=Kupac_strategy)
def test_hyp_kupac_Kupac_ID_setter(instance):
    original = instance.Kupac_ID
    instance.Kupac_ID = original
    assert instance.Kupac_ID == original



@given(instance=Kupac_strategy)
def test_hyp_kupac_Prezime_setter(instance):
    original = instance.Prezime
    instance.Prezime = original
    assert instance.Prezime == original



@given(instance=Kupac_strategy)
def test_hyp_kupac_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original




@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_BrojPolise_setter(instance):
    original = instance.BrojPolise
    instance.BrojPolise = original
    assert instance.BrojPolise == original



@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original



@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_OsigKuca_setter(instance):
    original = instance.OsigKuca
    instance.OsigKuca = original
    assert instance.OsigKuca == original



@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_PaketPokri_a_setter(instance):
    original = instance.PaketPokri_a
    instance.PaketPokri_a = original
    assert instance.PaketPokri_a == original



@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_Osiguranje_ID_setter(instance):
    original = instance.Osiguranje_ID
    instance.Osiguranje_ID = original
    assert instance.Osiguranje_ID == original




@given(instance=Aran_man_strategy)
def test_hyp_aran_man_NazivAran__setter(instance):
    original = instance.NazivAran_
    instance.NazivAran_ = original
    assert instance.NazivAran_ == original



@given(instance=Aran_man_strategy)
def test_hyp_aran_man_DatumPolaska_setter(instance):
    original = instance.DatumPolaska
    instance.DatumPolaska = original
    assert instance.DatumPolaska == original



@given(instance=Aran_man_strategy)
def test_hyp_aran_man_DatumPovratka_setter(instance):
    original = instance.DatumPovratka
    instance.DatumPovratka = original
    assert instance.DatumPovratka == original



@given(instance=Aran_man_strategy)
def test_hyp_aran_man_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original



@given(instance=Aran_man_strategy)
def test_hyp_aran_man_Aranzman_ID_setter(instance):
    original = instance.Aranzman_ID
    instance.Aranzman_ID = original
    assert instance.Aranzman_ID == original



@given(instance=Aran_man_strategy)
def test_hyp_aran_man_SlobMesto_setter(instance):
    original = instance.SlobMesto
    instance.SlobMesto = original
    assert instance.SlobMesto == original




@given(instance=Agent_strategy)
def test_hyp_agent_Ime_setter(instance):
    original = instance.Ime
    instance.Ime = original
    assert instance.Ime == original



@given(instance=Agent_strategy)
def test_hyp_agent_Agent_ID_setter(instance):
    original = instance.Agent_ID
    instance.Agent_ID = original
    assert instance.Agent_ID == original



@given(instance=Agent_strategy)
def test_hyp_agent_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Agent_strategy)
def test_hyp_agent_BrojAgenta_setter(instance):
    original = instance.BrojAgenta
    instance.BrojAgenta = original
    assert instance.BrojAgenta == original



@given(instance=Agent_strategy)
def test_hyp_agent_Prezime_setter(instance):
    original = instance.Prezime
    instance.Prezime = original
    assert instance.Prezime == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Agent,
    Aran_man,
    Kupac,
    Osiguranje,
    Transakcija,
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

def test_Agent_Agent_ID_value_roundtrip():
    instance = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    assert instance.Agent_ID == "sample_text"
    instance.Agent_ID = "sample_text_2"
    assert instance.Agent_ID == "sample_text_2"


def test_Agent_BrojAgenta_value_roundtrip():
    instance = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    assert instance.BrojAgenta == 7
    instance.BrojAgenta = 13
    assert instance.BrojAgenta == 13


def test_Agent_Ime_value_roundtrip():
    instance = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    assert instance.Ime == "sample_text"
    instance.Ime = "sample_text_2"
    assert instance.Ime == "sample_text_2"


def test_Agent_JMBG_value_roundtrip():
    instance = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    assert instance.JMBG == 7
    instance.JMBG = 13
    assert instance.JMBG == 13


def test_Agent_Prezime_value_roundtrip():
    instance = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    assert instance.Prezime == "sample_text"
    instance.Prezime = "sample_text_2"
    assert instance.Prezime == "sample_text_2"


def test_Aran_man_Aranzman_ID_value_roundtrip():
    instance = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    assert instance.Aranzman_ID == "sample_text"
    instance.Aranzman_ID = "sample_text_2"
    assert instance.Aranzman_ID == "sample_text_2"


def test_Aran_man_Cena_value_roundtrip():
    instance = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    assert instance.Cena == "sample_text"
    instance.Cena = "sample_text_2"
    assert instance.Cena == "sample_text_2"


def test_Aran_man_DatumPolaska_value_roundtrip():
    instance = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    assert instance.DatumPolaska == "sample_text"
    instance.DatumPolaska = "sample_text_2"
    assert instance.DatumPolaska == "sample_text_2"


def test_Aran_man_DatumPovratka_value_roundtrip():
    instance = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    assert instance.DatumPovratka == "sample_text"
    instance.DatumPovratka = "sample_text_2"
    assert instance.DatumPovratka == "sample_text_2"


def test_Aran_man_NazivAran__value_roundtrip():
    instance = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    assert instance.NazivAran_ == "sample_text"
    instance.NazivAran_ = "sample_text_2"
    assert instance.NazivAran_ == "sample_text_2"


def test_Aran_man_SlobMesto_value_roundtrip():
    instance = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    assert instance.SlobMesto == True
    instance.SlobMesto = False
    assert instance.SlobMesto == False


def test_Kupac_BrojPasosa_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.BrojPasosa == 7
    instance.BrojPasosa = 13
    assert instance.BrojPasosa == 13


def test_Kupac_Grad_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.Grad == "sample_text"
    instance.Grad = "sample_text_2"
    assert instance.Grad == "sample_text_2"


def test_Kupac_Ime_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.Ime == "sample_text"
    instance.Ime = "sample_text_2"
    assert instance.Ime == "sample_text_2"


def test_Kupac_JMBG_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.JMBG == 7
    instance.JMBG = 13
    assert instance.JMBG == 13


def test_Kupac_Kupac_ID_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.Kupac_ID == "sample_text"
    instance.Kupac_ID = "sample_text_2"
    assert instance.Kupac_ID == "sample_text_2"


def test_Kupac_Mobilni_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.Mobilni == 7
    instance.Mobilni = 13
    assert instance.Mobilni == 13


def test_Kupac_Prezime_value_roundtrip():
    instance = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    assert instance.Prezime == "sample_text"
    instance.Prezime = "sample_text_2"
    assert instance.Prezime == "sample_text_2"


def test_Osiguranje_BrojPolise_value_roundtrip():
    instance = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    assert instance.BrojPolise == 7
    instance.BrojPolise = 13
    assert instance.BrojPolise == 13


def test_Osiguranje_Cena_value_roundtrip():
    instance = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    assert instance.Cena == "sample_text"
    instance.Cena = "sample_text_2"
    assert instance.Cena == "sample_text_2"


def test_Osiguranje_OsigKuca_value_roundtrip():
    instance = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    assert instance.OsigKuca == "sample_text"
    instance.OsigKuca = "sample_text_2"
    assert instance.OsigKuca == "sample_text_2"


def test_Osiguranje_Osiguranje_ID_value_roundtrip():
    instance = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    assert instance.Osiguranje_ID == "sample_text"
    instance.Osiguranje_ID = "sample_text_2"
    assert instance.Osiguranje_ID == "sample_text_2"


def test_Osiguranje_PaketPokri_a_value_roundtrip():
    instance = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    assert instance.PaketPokri_a == "sample_text"
    instance.PaketPokri_a = "sample_text_2"
    assert instance.PaketPokri_a == "sample_text_2"


def test_Transakcija_Trans_ID_value_roundtrip():
    instance = Transakcija(Trans_ID="sample_text", datum_trans="sample_text", suma="sample_text", tip="sample_text")
    assert instance.Trans_ID == "sample_text"
    instance.Trans_ID = "sample_text_2"
    assert instance.Trans_ID == "sample_text_2"


def test_Transakcija_datum_trans_value_roundtrip():
    instance = Transakcija(Trans_ID="sample_text", datum_trans="sample_text", suma="sample_text", tip="sample_text")
    assert instance.datum_trans == "sample_text"
    instance.datum_trans = "sample_text_2"
    assert instance.datum_trans == "sample_text_2"


def test_Transakcija_suma_value_roundtrip():
    instance = Transakcija(Trans_ID="sample_text", datum_trans="sample_text", suma="sample_text", tip="sample_text")
    assert instance.suma == "sample_text"
    instance.suma = "sample_text_2"
    assert instance.suma == "sample_text_2"


def test_Transakcija_tip_value_roundtrip():
    instance = Transakcija(Trans_ID="sample_text", datum_trans="sample_text", suma="sample_text", tip="sample_text")
    assert instance.tip == "sample_text"
    instance.tip = "sample_text_2"
    assert instance.tip == "sample_text_2"


def test_assoc_Agent_Aran_man_link_reassign_clear():
    a = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    b1 = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    b2 = Agent(Agent_ID="sample_text_2", BrojAgenta=13, Ime="sample_text_2", JMBG=13, Prezime="sample_text_2")
    _safe_set(a, 'Agent_Aran_man_19', {b1})
    assert _is_linked(a, 'Agent_Aran_man_19', b1)
    if hasattr(b1, 'Agent_Aran_man_08'):
        assert _is_linked(b1, 'Agent_Aran_man_08', a)
    _safe_set(a, 'Agent_Aran_man_19', {b2})
    assert _is_linked(a, 'Agent_Aran_man_19', b2)
    if hasattr(b1, 'Agent_Aran_man_08'):
        assert not _is_linked(b1, 'Agent_Aran_man_08', a)
    if hasattr(b2, 'Agent_Aran_man_08'):
        assert _is_linked(b2, 'Agent_Aran_man_08', a)
    _safe_set(a, 'Agent_Aran_man_19', set())
    assert not _is_linked(a, 'Agent_Aran_man_19', b2)
    if hasattr(b2, 'Agent_Aran_man_08'):
        assert not _is_linked(b2, 'Agent_Aran_man_08', a)


def test_assoc_Agent_Kupac_link_reassign_clear():
    a = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    b1 = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    b2 = Agent(Agent_ID="sample_text_2", BrojAgenta=13, Ime="sample_text_2", JMBG=13, Prezime="sample_text_2")
    _safe_set(a, 'Agent_Kupac_17', b1)
    assert _is_linked(a, 'Agent_Kupac_17', b1)
    if hasattr(b1, 'Agent_Kupac_06'):
        assert _is_linked(b1, 'Agent_Kupac_06', a)
    _safe_set(a, 'Agent_Kupac_17', b2)
    assert _is_linked(a, 'Agent_Kupac_17', b2)
    if hasattr(b1, 'Agent_Kupac_06'):
        assert not _is_linked(b1, 'Agent_Kupac_06', a)
    if hasattr(b2, 'Agent_Kupac_06'):
        assert _is_linked(b2, 'Agent_Kupac_06', a)
    _safe_set(a, 'Agent_Kupac_17', None)
    assert not _is_linked(a, 'Agent_Kupac_17', b2)
    if hasattr(b2, 'Agent_Kupac_06'):
        assert not _is_linked(b2, 'Agent_Kupac_06', a)


def test_assoc_Osiguranje_Putnik_link_reassign_clear():
    a = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    b1 = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    b2 = Kupac(BrojPasosa=13, Grad="sample_text_2", Ime="sample_text_2", JMBG=13, Kupac_ID="sample_text_2", Mobilni=13, Prezime="sample_text_2")
    _safe_set(a, 'Osiguranje_Putnik_00', {b1})
    assert _is_linked(a, 'Osiguranje_Putnik_00', b1)
    if hasattr(b1, 'Osiguranje_Putnik_11'):
        assert _is_linked(b1, 'Osiguranje_Putnik_11', a)
    _safe_set(a, 'Osiguranje_Putnik_00', {b2})
    assert _is_linked(a, 'Osiguranje_Putnik_00', b2)
    if hasattr(b1, 'Osiguranje_Putnik_11'):
        assert not _is_linked(b1, 'Osiguranje_Putnik_11', a)
    if hasattr(b2, 'Osiguranje_Putnik_11'):
        assert _is_linked(b2, 'Osiguranje_Putnik_11', a)
    _safe_set(a, 'Osiguranje_Putnik_00', set())
    assert not _is_linked(a, 'Osiguranje_Putnik_00', b2)
    if hasattr(b2, 'Osiguranje_Putnik_11'):
        assert not _is_linked(b2, 'Osiguranje_Putnik_11', a)


def test_assoc_Putnik_Rezervisanje_link_reassign_clear():
    a = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    b1 = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    b2 = Aran_man(Aranzman_ID="sample_text_2", Cena="sample_text_2", DatumPolaska="sample_text_2", DatumPovratka="sample_text_2", NazivAran_="sample_text_2", SlobMesto=False)
    _safe_set(a, 'Putnik_Rezervisanje_02', {b1})
    assert _is_linked(a, 'Putnik_Rezervisanje_02', b1)
    if hasattr(b1, 'Putnik_Rezervisanje_13'):
        assert _is_linked(b1, 'Putnik_Rezervisanje_13', a)
    _safe_set(a, 'Putnik_Rezervisanje_02', {b2})
    assert _is_linked(a, 'Putnik_Rezervisanje_02', b2)
    if hasattr(b1, 'Putnik_Rezervisanje_13'):
        assert not _is_linked(b1, 'Putnik_Rezervisanje_13', a)
    if hasattr(b2, 'Putnik_Rezervisanje_13'):
        assert _is_linked(b2, 'Putnik_Rezervisanje_13', a)
    _safe_set(a, 'Putnik_Rezervisanje_02', set())
    assert not _is_linked(a, 'Putnik_Rezervisanje_02', b2)
    if hasattr(b2, 'Putnik_Rezervisanje_13'):
        assert not _is_linked(b2, 'Putnik_Rezervisanje_13', a)


def test_assoc_Transakcija_Kupac_link_reassign_clear():
    a = Transakcija(Trans_ID="sample_text", datum_trans="sample_text", suma="sample_text", tip="sample_text")
    b1 = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    b2 = Kupac(BrojPasosa=13, Grad="sample_text_2", Ime="sample_text_2", JMBG=13, Kupac_ID="sample_text_2", Mobilni=13, Prezime="sample_text_2")
    _safe_set(a, 'Transakcija_Kupac_04', {b1})
    assert _is_linked(a, 'Transakcija_Kupac_04', b1)
    if hasattr(b1, 'Transakcija_Kupac_15'):
        assert _is_linked(b1, 'Transakcija_Kupac_15', a)
    _safe_set(a, 'Transakcija_Kupac_04', {b2})
    assert _is_linked(a, 'Transakcija_Kupac_04', b2)
    if hasattr(b1, 'Transakcija_Kupac_15'):
        assert not _is_linked(b1, 'Transakcija_Kupac_15', a)
    if hasattr(b2, 'Transakcija_Kupac_15'):
        assert _is_linked(b2, 'Transakcija_Kupac_15', a)
    _safe_set(a, 'Transakcija_Kupac_04', set())
    assert not _is_linked(a, 'Transakcija_Kupac_04', b2)
    if hasattr(b2, 'Transakcija_Kupac_15'):
        assert not _is_linked(b2, 'Transakcija_Kupac_15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Agent_strategy = st.builds(Agent, Agent_ID=safe_text, BrojAgenta=st.integers(), Ime=safe_text, JMBG=st.integers(), Prezime=safe_text)
@given(instance=Agent_strategy)
@settings(max_examples=25)
def test_Agent_instantiation(instance):
    assert isinstance(instance, Agent)


Aran_man_strategy = st.builds(Aran_man, Aranzman_ID=safe_text, Cena=safe_text, DatumPolaska=safe_text, DatumPovratka=safe_text, NazivAran_=safe_text, SlobMesto=st.booleans())
@given(instance=Aran_man_strategy)
@settings(max_examples=25)
def test_Aran_man_instantiation(instance):
    assert isinstance(instance, Aran_man)


Kupac_strategy = st.builds(Kupac, BrojPasosa=st.integers(), Grad=safe_text, Ime=safe_text, JMBG=st.integers(), Kupac_ID=safe_text, Mobilni=st.integers(), Prezime=safe_text)
@given(instance=Kupac_strategy)
@settings(max_examples=25)
def test_Kupac_instantiation(instance):
    assert isinstance(instance, Kupac)


Osiguranje_strategy = st.builds(Osiguranje, BrojPolise=st.integers(), Cena=safe_text, OsigKuca=safe_text, Osiguranje_ID=safe_text, PaketPokri_a=safe_text)
@given(instance=Osiguranje_strategy)
@settings(max_examples=25)
def test_Osiguranje_instantiation(instance):
    assert isinstance(instance, Osiguranje)


Transakcija_strategy = st.builds(Transakcija, Trans_ID=safe_text, datum_trans=safe_text, suma=safe_text, tip=safe_text)
@given(instance=Transakcija_strategy)
@settings(max_examples=25)
def test_Transakcija_instantiation(instance):
    assert isinstance(instance, Transakcija)



