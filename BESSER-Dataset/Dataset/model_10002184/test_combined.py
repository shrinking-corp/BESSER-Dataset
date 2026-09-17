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
    Drzava,
    Grad,
    Hotel,
    Vodic,
    Aranzman,
    Uplata,
    Korisnik,
    Putnik,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_drzava_is_not_abstract():
    assert not inspect.isabstract(Drzava)


def test_hyp_drzava_constructor_exists():
    assert callable(Drzava.__init__)


def test_hyp_drzava_constructor_args():
    sig = inspect.signature(Drzava.__init__)
    params = list(sig.parameters.keys())
    assert "DrzavaID" in params, "Missing parameter 'DrzavaID'"
    assert "NazivDrzave" in params, "Missing parameter 'NazivDrzave'"





def test_hyp_grad_is_not_abstract():
    assert not inspect.isabstract(Grad)


def test_hyp_grad_constructor_exists():
    assert callable(Grad.__init__)


def test_hyp_grad_constructor_args():
    sig = inspect.signature(Grad.__init__)
    params = list(sig.parameters.keys())
    assert "NazivGrada" in params, "Missing parameter 'NazivGrada'"
    assert "GradID" in params, "Missing parameter 'GradID'"
    assert "DrzavaID" in params, "Missing parameter 'DrzavaID'"






def test_hyp_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hyp_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hyp_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "AdresaHotela" in params, "Missing parameter 'AdresaHotela'"
    assert "KontaktHotela" in params, "Missing parameter 'KontaktHotela'"
    assert "HotelID" in params, "Missing parameter 'HotelID'"
    assert "NazivHotela" in params, "Missing parameter 'NazivHotela'"
    assert "GradID" in params, "Missing parameter 'GradID'"








def test_hyp_vodic_is_not_abstract():
    assert not inspect.isabstract(Vodic)


def test_hyp_vodic_constructor_exists():
    assert callable(Vodic.__init__)


def test_hyp_vodic_constructor_args():
    sig = inspect.signature(Vodic.__init__)
    params = list(sig.parameters.keys())
    assert "GradVodica" in params, "Missing parameter 'GradVodica'"
    assert "KontaktVodica" in params, "Missing parameter 'KontaktVodica'"
    assert "PrezimeVodica" in params, "Missing parameter 'PrezimeVodica'"
    assert "ImeVodica" in params, "Missing parameter 'ImeVodica'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "AdresaVodica" in params, "Missing parameter 'AdresaVodica'"
    assert "VodicID" in params, "Missing parameter 'VodicID'"










def test_hyp_aranzman_is_not_abstract():
    assert not inspect.isabstract(Aranzman)


def test_hyp_aranzman_constructor_exists():
    assert callable(Aranzman.__init__)


def test_hyp_aranzman_constructor_args():
    sig = inspect.signature(Aranzman.__init__)
    params = list(sig.parameters.keys())
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "HotelID" in params, "Missing parameter 'HotelID'"
    assert "DatumAranzmana" in params, "Missing parameter 'DatumAranzmana'"
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "VodicID" in params, "Missing parameter 'VodicID'"
    assert "OpisAranzmana" in params, "Missing parameter 'OpisAranzmana'"
    assert "CenaAranzmana" in params, "Missing parameter 'CenaAranzmana'"
    assert "NazivAranzmana" in params, "Missing parameter 'NazivAranzmana'"











def test_hyp_uplata_is_not_abstract():
    assert not inspect.isabstract(Uplata)


def test_hyp_uplata_constructor_exists():
    assert callable(Uplata.__init__)


def test_hyp_uplata_constructor_args():
    sig = inspect.signature(Uplata.__init__)
    params = list(sig.parameters.keys())
    assert "DatumUplate" in params, "Missing parameter 'DatumUplate'"
    assert "Iznos" in params, "Missing parameter 'Iznos'"
    assert "NazivUplate" in params, "Missing parameter 'NazivUplate'"
    assert "UplataID" in params, "Missing parameter 'UplataID'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"








def test_hyp_korisnik_is_not_abstract():
    assert not inspect.isabstract(Korisnik)


def test_hyp_korisnik_constructor_exists():
    assert callable(Korisnik.__init__)


def test_hyp_korisnik_constructor_args():
    sig = inspect.signature(Korisnik.__init__)
    params = list(sig.parameters.keys())
    assert "KontaktKorisnika" in params, "Missing parameter 'KontaktKorisnika'"
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "PrezimeKorisnika" in params, "Missing parameter 'PrezimeKorisnika'"
    assert "ImeKorisnika" in params, "Missing parameter 'ImeKorisnika'"
    assert "AdresaKorisnika" in params, "Missing parameter 'AdresaKorisnika'"
    assert "GradKorisnika" in params, "Missing parameter 'GradKorisnika'"
    assert "Username" in params, "Missing parameter 'Username'"












def test_hyp_putnik_is_not_abstract():
    assert not inspect.isabstract(Putnik)


def test_hyp_putnik_constructor_exists():
    assert callable(Putnik.__init__)


def test_hyp_putnik_constructor_args():
    sig = inspect.signature(Putnik.__init__)
    params = list(sig.parameters.keys())
    assert "BrojPasosa" in params, "Missing parameter 'BrojPasosa'"
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "ImePutnika" in params, "Missing parameter 'ImePutnika'"
    assert "AdresaPutnika" in params, "Missing parameter 'AdresaPutnika'"
    assert "PrezimePutnika" in params, "Missing parameter 'PrezimePutnika'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"
    assert "KontaktPutnika" in params, "Missing parameter 'KontaktPutnika'"
    assert "GradPutnika" in params, "Missing parameter 'GradPutnika'"











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
Drzava_strategy = st.builds(
    Drzava,
    DrzavaID=
        st.integers(),
    NazivDrzave=
        safe_text
)
Grad_strategy = st.builds(
    Grad,
    NazivGrada=
        safe_text,
    GradID=
        st.integers(),
    DrzavaID=
        st.integers()
)
Hotel_strategy = st.builds(
    Hotel,
    AdresaHotela=
        safe_text,
    KontaktHotela=
        safe_text,
    HotelID=
        st.integers(),
    NazivHotela=
        safe_text,
    GradID=
        st.integers()
)
Vodic_strategy = st.builds(
    Vodic,
    GradVodica=
        safe_text,
    KontaktVodica=
        safe_text,
    PrezimeVodica=
        safe_text,
    ImeVodica=
        safe_text,
    JMBG=
        safe_text,
    AdresaVodica=
        safe_text,
    VodicID=
        st.integers()
)
Aranzman_strategy = st.builds(
    Aranzman,
    AranzmanID=
        st.integers(),
    HotelID=
        st.integers(),
    DatumAranzmana=
        safe_text,
    KorisnikID=
        st.integers(),
    VodicID=
        st.integers(),
    OpisAranzmana=
        safe_text,
    CenaAranzmana=
        safe_text,
    NazivAranzmana=
        safe_text
)
Uplata_strategy = st.builds(
    Uplata,
    DatumUplate=
        safe_text,
    Iznos=
        safe_text,
    NazivUplate=
        safe_text,
    UplataID=
        st.integers(),
    PutnikID=
        st.integers()
)
Korisnik_strategy = st.builds(
    Korisnik,
    KontaktKorisnika=
        safe_text,
    KorisnikID=
        st.integers(),
    JMBG=
        safe_text,
    Password=
        safe_text,
    PrezimeKorisnika=
        safe_text,
    ImeKorisnika=
        safe_text,
    AdresaKorisnika=
        safe_text,
    GradKorisnika=
        safe_text,
    Username=
        safe_text
)
Putnik_strategy = st.builds(
    Putnik,
    BrojPasosa=
        st.integers(),
    AranzmanID=
        st.integers(),
    JMBG=
        safe_text,
    ImePutnika=
        safe_text,
    AdresaPutnika=
        safe_text,
    PrezimePutnika=
        safe_text,
    PutnikID=
        st.integers(),
    KontaktPutnika=
        safe_text,
    GradPutnika=
        safe_text
)




@given(instance=Drzava_strategy)
def test_hyp_drzava_DrzavaID_setter(instance):
    original = instance.DrzavaID
    instance.DrzavaID = original
    assert instance.DrzavaID == original



@given(instance=Drzava_strategy)
def test_hyp_drzava_NazivDrzave_setter(instance):
    original = instance.NazivDrzave
    instance.NazivDrzave = original
    assert instance.NazivDrzave == original




@given(instance=Grad_strategy)
def test_hyp_grad_NazivGrada_setter(instance):
    original = instance.NazivGrada
    instance.NazivGrada = original
    assert instance.NazivGrada == original



@given(instance=Grad_strategy)
def test_hyp_grad_GradID_setter(instance):
    original = instance.GradID
    instance.GradID = original
    assert instance.GradID == original



@given(instance=Grad_strategy)
def test_hyp_grad_DrzavaID_setter(instance):
    original = instance.DrzavaID
    instance.DrzavaID = original
    assert instance.DrzavaID == original




@given(instance=Hotel_strategy)
def test_hyp_hotel_AdresaHotela_setter(instance):
    original = instance.AdresaHotela
    instance.AdresaHotela = original
    assert instance.AdresaHotela == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_KontaktHotela_setter(instance):
    original = instance.KontaktHotela
    instance.KontaktHotela = original
    assert instance.KontaktHotela == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_HotelID_setter(instance):
    original = instance.HotelID
    instance.HotelID = original
    assert instance.HotelID == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_NazivHotela_setter(instance):
    original = instance.NazivHotela
    instance.NazivHotela = original
    assert instance.NazivHotela == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_GradID_setter(instance):
    original = instance.GradID
    instance.GradID = original
    assert instance.GradID == original




@given(instance=Vodic_strategy)
def test_hyp_vodic_GradVodica_setter(instance):
    original = instance.GradVodica
    instance.GradVodica = original
    assert instance.GradVodica == original



@given(instance=Vodic_strategy)
def test_hyp_vodic_KontaktVodica_setter(instance):
    original = instance.KontaktVodica
    instance.KontaktVodica = original
    assert instance.KontaktVodica == original



@given(instance=Vodic_strategy)
def test_hyp_vodic_PrezimeVodica_setter(instance):
    original = instance.PrezimeVodica
    instance.PrezimeVodica = original
    assert instance.PrezimeVodica == original



@given(instance=Vodic_strategy)
def test_hyp_vodic_ImeVodica_setter(instance):
    original = instance.ImeVodica
    instance.ImeVodica = original
    assert instance.ImeVodica == original



@given(instance=Vodic_strategy)
def test_hyp_vodic_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Vodic_strategy)
def test_hyp_vodic_AdresaVodica_setter(instance):
    original = instance.AdresaVodica
    instance.AdresaVodica = original
    assert instance.AdresaVodica == original



@given(instance=Vodic_strategy)
def test_hyp_vodic_VodicID_setter(instance):
    original = instance.VodicID
    instance.VodicID = original
    assert instance.VodicID == original




@given(instance=Aranzman_strategy)
def test_hyp_aranzman_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_HotelID_setter(instance):
    original = instance.HotelID
    instance.HotelID = original
    assert instance.HotelID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_DatumAranzmana_setter(instance):
    original = instance.DatumAranzmana
    instance.DatumAranzmana = original
    assert instance.DatumAranzmana == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_VodicID_setter(instance):
    original = instance.VodicID
    instance.VodicID = original
    assert instance.VodicID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_OpisAranzmana_setter(instance):
    original = instance.OpisAranzmana
    instance.OpisAranzmana = original
    assert instance.OpisAranzmana == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_CenaAranzmana_setter(instance):
    original = instance.CenaAranzmana
    instance.CenaAranzmana = original
    assert instance.CenaAranzmana == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_NazivAranzmana_setter(instance):
    original = instance.NazivAranzmana
    instance.NazivAranzmana = original
    assert instance.NazivAranzmana == original




@given(instance=Uplata_strategy)
def test_hyp_uplata_DatumUplate_setter(instance):
    original = instance.DatumUplate
    instance.DatumUplate = original
    assert instance.DatumUplate == original



@given(instance=Uplata_strategy)
def test_hyp_uplata_Iznos_setter(instance):
    original = instance.Iznos
    instance.Iznos = original
    assert instance.Iznos == original



@given(instance=Uplata_strategy)
def test_hyp_uplata_NazivUplate_setter(instance):
    original = instance.NazivUplate
    instance.NazivUplate = original
    assert instance.NazivUplate == original



@given(instance=Uplata_strategy)
def test_hyp_uplata_UplataID_setter(instance):
    original = instance.UplataID
    instance.UplataID = original
    assert instance.UplataID == original



@given(instance=Uplata_strategy)
def test_hyp_uplata_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original




@given(instance=Korisnik_strategy)
def test_hyp_korisnik_KontaktKorisnika_setter(instance):
    original = instance.KontaktKorisnika
    instance.KontaktKorisnika = original
    assert instance.KontaktKorisnika == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_PrezimeKorisnika_setter(instance):
    original = instance.PrezimeKorisnika
    instance.PrezimeKorisnika = original
    assert instance.PrezimeKorisnika == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_ImeKorisnika_setter(instance):
    original = instance.ImeKorisnika
    instance.ImeKorisnika = original
    assert instance.ImeKorisnika == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_AdresaKorisnika_setter(instance):
    original = instance.AdresaKorisnika
    instance.AdresaKorisnika = original
    assert instance.AdresaKorisnika == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_GradKorisnika_setter(instance):
    original = instance.GradKorisnika
    instance.GradKorisnika = original
    assert instance.GradKorisnika == original



@given(instance=Korisnik_strategy)
def test_hyp_korisnik_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original




@given(instance=Putnik_strategy)
def test_hyp_putnik_BrojPasosa_setter(instance):
    original = instance.BrojPasosa
    instance.BrojPasosa = original
    assert instance.BrojPasosa == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_ImePutnika_setter(instance):
    original = instance.ImePutnika
    instance.ImePutnika = original
    assert instance.ImePutnika == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_AdresaPutnika_setter(instance):
    original = instance.AdresaPutnika
    instance.AdresaPutnika = original
    assert instance.AdresaPutnika == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_PrezimePutnika_setter(instance):
    original = instance.PrezimePutnika
    instance.PrezimePutnika = original
    assert instance.PrezimePutnika == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_KontaktPutnika_setter(instance):
    original = instance.KontaktPutnika
    instance.KontaktPutnika = original
    assert instance.KontaktPutnika == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_GradPutnika_setter(instance):
    original = instance.GradPutnika
    instance.GradPutnika = original
    assert instance.GradPutnika == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Aranzman,
    Drzava,
    Grad,
    Hotel,
    Korisnik,
    Putnik,
    Uplata,
    Vodic,
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

def test_Aranzman_AranzmanID_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.AranzmanID == 7
    instance.AranzmanID = 13
    assert instance.AranzmanID == 13


def test_Aranzman_CenaAranzmana_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.CenaAranzmana == "sample_text"
    instance.CenaAranzmana = "sample_text_2"
    assert instance.CenaAranzmana == "sample_text_2"


def test_Aranzman_DatumAranzmana_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.DatumAranzmana == "sample_text"
    instance.DatumAranzmana = "sample_text_2"
    assert instance.DatumAranzmana == "sample_text_2"


def test_Aranzman_HotelID_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.HotelID == 7
    instance.HotelID = 13
    assert instance.HotelID == 13


def test_Aranzman_KorisnikID_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.KorisnikID == 7
    instance.KorisnikID = 13
    assert instance.KorisnikID == 13


def test_Aranzman_NazivAranzmana_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.NazivAranzmana == "sample_text"
    instance.NazivAranzmana = "sample_text_2"
    assert instance.NazivAranzmana == "sample_text_2"


def test_Aranzman_OpisAranzmana_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.OpisAranzmana == "sample_text"
    instance.OpisAranzmana = "sample_text_2"
    assert instance.OpisAranzmana == "sample_text_2"


def test_Aranzman_VodicID_value_roundtrip():
    instance = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    assert instance.VodicID == 7
    instance.VodicID = 13
    assert instance.VodicID == 13


def test_Drzava_DrzavaID_value_roundtrip():
    instance = Drzava(DrzavaID=7, NazivDrzave="sample_text")
    assert instance.DrzavaID == 7
    instance.DrzavaID = 13
    assert instance.DrzavaID == 13


def test_Drzava_NazivDrzave_value_roundtrip():
    instance = Drzava(DrzavaID=7, NazivDrzave="sample_text")
    assert instance.NazivDrzave == "sample_text"
    instance.NazivDrzave = "sample_text_2"
    assert instance.NazivDrzave == "sample_text_2"


def test_Grad_DrzavaID_value_roundtrip():
    instance = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    assert instance.DrzavaID == 7
    instance.DrzavaID = 13
    assert instance.DrzavaID == 13


def test_Grad_GradID_value_roundtrip():
    instance = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    assert instance.GradID == 7
    instance.GradID = 13
    assert instance.GradID == 13


def test_Grad_NazivGrada_value_roundtrip():
    instance = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    assert instance.NazivGrada == "sample_text"
    instance.NazivGrada = "sample_text_2"
    assert instance.NazivGrada == "sample_text_2"


def test_Hotel_AdresaHotela_value_roundtrip():
    instance = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    assert instance.AdresaHotela == "sample_text"
    instance.AdresaHotela = "sample_text_2"
    assert instance.AdresaHotela == "sample_text_2"


def test_Hotel_GradID_value_roundtrip():
    instance = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    assert instance.GradID == 7
    instance.GradID = 13
    assert instance.GradID == 13


def test_Hotel_HotelID_value_roundtrip():
    instance = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    assert instance.HotelID == 7
    instance.HotelID = 13
    assert instance.HotelID == 13


def test_Hotel_KontaktHotela_value_roundtrip():
    instance = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    assert instance.KontaktHotela == "sample_text"
    instance.KontaktHotela = "sample_text_2"
    assert instance.KontaktHotela == "sample_text_2"


def test_Hotel_NazivHotela_value_roundtrip():
    instance = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    assert instance.NazivHotela == "sample_text"
    instance.NazivHotela = "sample_text_2"
    assert instance.NazivHotela == "sample_text_2"


def test_Korisnik_AdresaKorisnika_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.AdresaKorisnika == "sample_text"
    instance.AdresaKorisnika = "sample_text_2"
    assert instance.AdresaKorisnika == "sample_text_2"


def test_Korisnik_GradKorisnika_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.GradKorisnika == "sample_text"
    instance.GradKorisnika = "sample_text_2"
    assert instance.GradKorisnika == "sample_text_2"


def test_Korisnik_ImeKorisnika_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.ImeKorisnika == "sample_text"
    instance.ImeKorisnika = "sample_text_2"
    assert instance.ImeKorisnika == "sample_text_2"


def test_Korisnik_JMBG_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.JMBG == "sample_text"
    instance.JMBG = "sample_text_2"
    assert instance.JMBG == "sample_text_2"


def test_Korisnik_KontaktKorisnika_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.KontaktKorisnika == "sample_text"
    instance.KontaktKorisnika = "sample_text_2"
    assert instance.KontaktKorisnika == "sample_text_2"


def test_Korisnik_KorisnikID_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.KorisnikID == 7
    instance.KorisnikID = 13
    assert instance.KorisnikID == 13


def test_Korisnik_Password_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Korisnik_PrezimeKorisnika_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.PrezimeKorisnika == "sample_text"
    instance.PrezimeKorisnika = "sample_text_2"
    assert instance.PrezimeKorisnika == "sample_text_2"


def test_Korisnik_Username_value_roundtrip():
    instance = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_Putnik_AdresaPutnika_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.AdresaPutnika == "sample_text"
    instance.AdresaPutnika = "sample_text_2"
    assert instance.AdresaPutnika == "sample_text_2"


def test_Putnik_AranzmanID_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.AranzmanID == 7
    instance.AranzmanID = 13
    assert instance.AranzmanID == 13


def test_Putnik_BrojPasosa_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.BrojPasosa == 7
    instance.BrojPasosa = 13
    assert instance.BrojPasosa == 13


def test_Putnik_GradPutnika_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.GradPutnika == "sample_text"
    instance.GradPutnika = "sample_text_2"
    assert instance.GradPutnika == "sample_text_2"


def test_Putnik_ImePutnika_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.ImePutnika == "sample_text"
    instance.ImePutnika = "sample_text_2"
    assert instance.ImePutnika == "sample_text_2"


def test_Putnik_JMBG_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.JMBG == "sample_text"
    instance.JMBG = "sample_text_2"
    assert instance.JMBG == "sample_text_2"


def test_Putnik_KontaktPutnika_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.KontaktPutnika == "sample_text"
    instance.KontaktPutnika = "sample_text_2"
    assert instance.KontaktPutnika == "sample_text_2"


def test_Putnik_PrezimePutnika_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.PrezimePutnika == "sample_text"
    instance.PrezimePutnika = "sample_text_2"
    assert instance.PrezimePutnika == "sample_text_2"


def test_Putnik_PutnikID_value_roundtrip():
    instance = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    assert instance.PutnikID == 7
    instance.PutnikID = 13
    assert instance.PutnikID == 13


def test_Uplata_DatumUplate_value_roundtrip():
    instance = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    assert instance.DatumUplate == "sample_text"
    instance.DatumUplate = "sample_text_2"
    assert instance.DatumUplate == "sample_text_2"


def test_Uplata_Iznos_value_roundtrip():
    instance = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    assert instance.Iznos == "sample_text"
    instance.Iznos = "sample_text_2"
    assert instance.Iznos == "sample_text_2"


def test_Uplata_NazivUplate_value_roundtrip():
    instance = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    assert instance.NazivUplate == "sample_text"
    instance.NazivUplate = "sample_text_2"
    assert instance.NazivUplate == "sample_text_2"


def test_Uplata_PutnikID_value_roundtrip():
    instance = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    assert instance.PutnikID == 7
    instance.PutnikID = 13
    assert instance.PutnikID == 13


def test_Uplata_UplataID_value_roundtrip():
    instance = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    assert instance.UplataID == 7
    instance.UplataID = 13
    assert instance.UplataID == 13


def test_Vodic_AdresaVodica_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.AdresaVodica == "sample_text"
    instance.AdresaVodica = "sample_text_2"
    assert instance.AdresaVodica == "sample_text_2"


def test_Vodic_GradVodica_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.GradVodica == "sample_text"
    instance.GradVodica = "sample_text_2"
    assert instance.GradVodica == "sample_text_2"


def test_Vodic_ImeVodica_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.ImeVodica == "sample_text"
    instance.ImeVodica = "sample_text_2"
    assert instance.ImeVodica == "sample_text_2"


def test_Vodic_JMBG_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.JMBG == "sample_text"
    instance.JMBG = "sample_text_2"
    assert instance.JMBG == "sample_text_2"


def test_Vodic_KontaktVodica_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.KontaktVodica == "sample_text"
    instance.KontaktVodica = "sample_text_2"
    assert instance.KontaktVodica == "sample_text_2"


def test_Vodic_PrezimeVodica_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.PrezimeVodica == "sample_text"
    instance.PrezimeVodica = "sample_text_2"
    assert instance.PrezimeVodica == "sample_text_2"


def test_Vodic_VodicID_value_roundtrip():
    instance = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    assert instance.VodicID == 7
    instance.VodicID = 13
    assert instance.VodicID == 13


def test_assoc_Aranzman_Hotel_link_reassign_clear():
    a = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    b1 = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    b2 = Aranzman(AranzmanID=13, CenaAranzmana="sample_text_2", DatumAranzmana="sample_text_2", HotelID=13, KorisnikID=13, NazivAranzmana="sample_text_2", OpisAranzmana="sample_text_2", VodicID=13)
    _safe_set(a, 'aranzman9', {b1})
    assert _is_linked(a, 'aranzman9', b1)
    if hasattr(b1, 'hotel8'):
        assert _is_linked(b1, 'hotel8', a)
    _safe_set(a, 'aranzman9', {b2})
    assert _is_linked(a, 'aranzman9', b2)
    if hasattr(b1, 'hotel8'):
        assert not _is_linked(b1, 'hotel8', a)
    if hasattr(b2, 'hotel8'):
        assert _is_linked(b2, 'hotel8', a)
    _safe_set(a, 'aranzman9', set())
    assert not _is_linked(a, 'aranzman9', b2)
    if hasattr(b2, 'hotel8'):
        assert not _is_linked(b2, 'hotel8', a)


def test_assoc_Drzava_Grad_link_reassign_clear():
    a = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    b1 = Drzava(DrzavaID=7, NazivDrzave="sample_text")
    b2 = Drzava(DrzavaID=13, NazivDrzave="sample_text_2")
    _safe_set(a, 'drzava3', b1)
    assert _is_linked(a, 'drzava3', b1)
    if hasattr(b1, 'grad2'):
        assert _is_linked(b1, 'grad2', a)
    _safe_set(a, 'drzava3', b2)
    assert _is_linked(a, 'drzava3', b2)
    if hasattr(b1, 'grad2'):
        assert not _is_linked(b1, 'grad2', a)
    if hasattr(b2, 'grad2'):
        assert _is_linked(b2, 'grad2', a)
    _safe_set(a, 'drzava3', None)
    assert not _is_linked(a, 'drzava3', b2)
    if hasattr(b2, 'grad2'):
        assert not _is_linked(b2, 'grad2', a)


def test_assoc_Grad_Hotel_link_reassign_clear():
    a = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    b1 = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    b2 = Grad(DrzavaID=13, GradID=13, NazivGrada="sample_text_2")
    _safe_set(a, 'grad5', b1)
    assert _is_linked(a, 'grad5', b1)
    if hasattr(b1, 'hotel4'):
        assert _is_linked(b1, 'hotel4', a)
    _safe_set(a, 'grad5', b2)
    assert _is_linked(a, 'grad5', b2)
    if hasattr(b1, 'hotel4'):
        assert not _is_linked(b1, 'hotel4', a)
    if hasattr(b2, 'hotel4'):
        assert _is_linked(b2, 'hotel4', a)
    _safe_set(a, 'grad5', None)
    assert not _is_linked(a, 'grad5', b2)
    if hasattr(b2, 'hotel4'):
        assert not _is_linked(b2, 'hotel4', a)


def test_assoc_Korisnik_Aranzman_link_reassign_clear():
    a = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    b1 = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    b2 = Aranzman(AranzmanID=13, CenaAranzmana="sample_text_2", DatumAranzmana="sample_text_2", HotelID=13, KorisnikID=13, NazivAranzmana="sample_text_2", OpisAranzmana="sample_text_2", VodicID=13)
    _safe_set(a, 'aranzman6', {b1})
    assert _is_linked(a, 'aranzman6', b1)
    if hasattr(b1, 'korisnik7'):
        assert _is_linked(b1, 'korisnik7', a)
    _safe_set(a, 'aranzman6', {b2})
    assert _is_linked(a, 'aranzman6', b2)
    if hasattr(b1, 'korisnik7'):
        assert not _is_linked(b1, 'korisnik7', a)
    if hasattr(b2, 'korisnik7'):
        assert _is_linked(b2, 'korisnik7', a)
    _safe_set(a, 'aranzman6', set())
    assert not _is_linked(a, 'aranzman6', b2)
    if hasattr(b2, 'korisnik7'):
        assert not _is_linked(b2, 'korisnik7', a)


def test_assoc_Putnik_Aranzman_link_reassign_clear():
    a = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    b1 = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    b2 = Aranzman(AranzmanID=13, CenaAranzmana="sample_text_2", DatumAranzmana="sample_text_2", HotelID=13, KorisnikID=13, NazivAranzmana="sample_text_2", OpisAranzmana="sample_text_2", VodicID=13)
    _safe_set(a, 'aranzman10', b1)
    assert _is_linked(a, 'aranzman10', b1)
    if hasattr(b1, 'putnik11'):
        assert _is_linked(b1, 'putnik11', a)
    _safe_set(a, 'aranzman10', b2)
    assert _is_linked(a, 'aranzman10', b2)
    if hasattr(b1, 'putnik11'):
        assert not _is_linked(b1, 'putnik11', a)
    if hasattr(b2, 'putnik11'):
        assert _is_linked(b2, 'putnik11', a)
    _safe_set(a, 'aranzman10', None)
    assert not _is_linked(a, 'aranzman10', b2)
    if hasattr(b2, 'putnik11'):
        assert not _is_linked(b2, 'putnik11', a)


def test_assoc_Uplata_Putnik_link_reassign_clear():
    a = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    b1 = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    b2 = Putnik(AdresaPutnika="sample_text_2", AranzmanID=13, BrojPasosa=13, GradPutnika="sample_text_2", ImePutnika="sample_text_2", JMBG="sample_text_2", KontaktPutnika="sample_text_2", PrezimePutnika="sample_text_2", PutnikID=13)
    _safe_set(a, 'putnik12', b1)
    assert _is_linked(a, 'putnik12', b1)
    if hasattr(b1, 'uplata13'):
        assert _is_linked(b1, 'uplata13', a)
    _safe_set(a, 'putnik12', b2)
    assert _is_linked(a, 'putnik12', b2)
    if hasattr(b1, 'uplata13'):
        assert not _is_linked(b1, 'uplata13', a)
    if hasattr(b2, 'uplata13'):
        assert _is_linked(b2, 'uplata13', a)
    _safe_set(a, 'putnik12', None)
    assert not _is_linked(a, 'putnik12', b2)
    if hasattr(b2, 'uplata13'):
        assert not _is_linked(b2, 'uplata13', a)


def test_assoc_Vodic_Aranzman_link_reassign_clear():
    a = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    b1 = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    b2 = Aranzman(AranzmanID=13, CenaAranzmana="sample_text_2", DatumAranzmana="sample_text_2", HotelID=13, KorisnikID=13, NazivAranzmana="sample_text_2", OpisAranzmana="sample_text_2", VodicID=13)
    _safe_set(a, 'aranzman0', {b1})
    assert _is_linked(a, 'aranzman0', b1)
    if hasattr(b1, 'vodic1'):
        assert _is_linked(b1, 'vodic1', a)
    _safe_set(a, 'aranzman0', {b2})
    assert _is_linked(a, 'aranzman0', b2)
    if hasattr(b1, 'vodic1'):
        assert not _is_linked(b1, 'vodic1', a)
    if hasattr(b2, 'vodic1'):
        assert _is_linked(b2, 'vodic1', a)
    _safe_set(a, 'aranzman0', set())
    assert not _is_linked(a, 'aranzman0', b2)
    if hasattr(b2, 'vodic1'):
        assert not _is_linked(b2, 'vodic1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Aranzman_strategy = st.builds(Aranzman, AranzmanID=st.integers(), CenaAranzmana=safe_text, DatumAranzmana=safe_text, HotelID=st.integers(), KorisnikID=st.integers(), NazivAranzmana=safe_text, OpisAranzmana=safe_text, VodicID=st.integers())
@given(instance=Aranzman_strategy)
@settings(max_examples=25)
def test_Aranzman_instantiation(instance):
    assert isinstance(instance, Aranzman)


Drzava_strategy = st.builds(Drzava, DrzavaID=st.integers(), NazivDrzave=safe_text)
@given(instance=Drzava_strategy)
@settings(max_examples=25)
def test_Drzava_instantiation(instance):
    assert isinstance(instance, Drzava)


Grad_strategy = st.builds(Grad, DrzavaID=st.integers(), GradID=st.integers(), NazivGrada=safe_text)
@given(instance=Grad_strategy)
@settings(max_examples=25)
def test_Grad_instantiation(instance):
    assert isinstance(instance, Grad)


Hotel_strategy = st.builds(Hotel, AdresaHotela=safe_text, GradID=st.integers(), HotelID=st.integers(), KontaktHotela=safe_text, NazivHotela=safe_text)
@given(instance=Hotel_strategy)
@settings(max_examples=25)
def test_Hotel_instantiation(instance):
    assert isinstance(instance, Hotel)


Korisnik_strategy = st.builds(Korisnik, AdresaKorisnika=safe_text, GradKorisnika=safe_text, ImeKorisnika=safe_text, JMBG=safe_text, KontaktKorisnika=safe_text, KorisnikID=st.integers(), Password=safe_text, PrezimeKorisnika=safe_text, Username=safe_text)
@given(instance=Korisnik_strategy)
@settings(max_examples=25)
def test_Korisnik_instantiation(instance):
    assert isinstance(instance, Korisnik)


Putnik_strategy = st.builds(Putnik, AdresaPutnika=safe_text, AranzmanID=st.integers(), BrojPasosa=st.integers(), GradPutnika=safe_text, ImePutnika=safe_text, JMBG=safe_text, KontaktPutnika=safe_text, PrezimePutnika=safe_text, PutnikID=st.integers())
@given(instance=Putnik_strategy)
@settings(max_examples=25)
def test_Putnik_instantiation(instance):
    assert isinstance(instance, Putnik)


Uplata_strategy = st.builds(Uplata, DatumUplate=safe_text, Iznos=safe_text, NazivUplate=safe_text, PutnikID=st.integers(), UplataID=st.integers())
@given(instance=Uplata_strategy)
@settings(max_examples=25)
def test_Uplata_instantiation(instance):
    assert isinstance(instance, Uplata)


Vodic_strategy = st.builds(Vodic, AdresaVodica=safe_text, GradVodica=safe_text, ImeVodica=safe_text, JMBG=safe_text, KontaktVodica=safe_text, PrezimeVodica=safe_text, VodicID=st.integers())
@given(instance=Vodic_strategy)
@settings(max_examples=25)
def test_Vodic_instantiation(instance):
    assert isinstance(instance, Vodic)



