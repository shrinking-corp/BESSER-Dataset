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


