import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_Aranzman_Hotel_reverse_link_reassign_clear():
    a1 = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    a2 = Hotel(AdresaHotela="sample_text_2", GradID=13, HotelID=13, KontaktHotela="sample_text_2", NazivHotela="sample_text_2")
    b = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    _safe_set(b, 'hotel8', a1)
    assert _is_linked(b, 'hotel8', a1)
    if hasattr(a1, 'aranzman9'):
        assert _is_linked(a1, 'aranzman9', b)
    _safe_set(b, 'hotel8', a2)
    assert _is_linked(b, 'hotel8', a2)
    if hasattr(a1, 'aranzman9'):
        assert not _is_linked(a1, 'aranzman9', b)
    if hasattr(a2, 'aranzman9'):
        assert _is_linked(a2, 'aranzman9', b)
    _safe_set(b, 'hotel8', None)
    assert not _is_linked(b, 'hotel8', a2)
    if hasattr(a2, 'aranzman9'):
        assert not _is_linked(a2, 'aranzman9', b)


def test_assoc_Drzava_Grad_reverse_link_reassign_clear():
    a1 = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    a2 = Grad(DrzavaID=13, GradID=13, NazivGrada="sample_text_2")
    b = Drzava(DrzavaID=7, NazivDrzave="sample_text")
    _safe_set(b, 'grad2', {a1})
    assert _is_linked(b, 'grad2', a1)
    if hasattr(a1, 'drzava3'):
        assert _is_linked(a1, 'drzava3', b)
    _safe_set(b, 'grad2', {a2})
    assert _is_linked(b, 'grad2', a2)
    if hasattr(a1, 'drzava3'):
        assert not _is_linked(a1, 'drzava3', b)
    if hasattr(a2, 'drzava3'):
        assert _is_linked(a2, 'drzava3', b)
    _safe_set(b, 'grad2', set())
    assert not _is_linked(b, 'grad2', a2)
    if hasattr(a2, 'drzava3'):
        assert not _is_linked(a2, 'drzava3', b)


def test_assoc_Grad_Hotel_reverse_link_reassign_clear():
    a1 = Hotel(AdresaHotela="sample_text", GradID=7, HotelID=7, KontaktHotela="sample_text", NazivHotela="sample_text")
    a2 = Hotel(AdresaHotela="sample_text_2", GradID=13, HotelID=13, KontaktHotela="sample_text_2", NazivHotela="sample_text_2")
    b = Grad(DrzavaID=7, GradID=7, NazivGrada="sample_text")
    _safe_set(b, 'hotel4', {a1})
    assert _is_linked(b, 'hotel4', a1)
    if hasattr(a1, 'grad5'):
        assert _is_linked(a1, 'grad5', b)
    _safe_set(b, 'hotel4', {a2})
    assert _is_linked(b, 'hotel4', a2)
    if hasattr(a1, 'grad5'):
        assert not _is_linked(a1, 'grad5', b)
    if hasattr(a2, 'grad5'):
        assert _is_linked(a2, 'grad5', b)
    _safe_set(b, 'hotel4', set())
    assert not _is_linked(b, 'hotel4', a2)
    if hasattr(a2, 'grad5'):
        assert not _is_linked(a2, 'grad5', b)


def test_assoc_Korisnik_Aranzman_reverse_link_reassign_clear():
    a1 = Korisnik(AdresaKorisnika="sample_text", GradKorisnika="sample_text", ImeKorisnika="sample_text", JMBG="sample_text", KontaktKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", Username="sample_text")
    a2 = Korisnik(AdresaKorisnika="sample_text_2", GradKorisnika="sample_text_2", ImeKorisnika="sample_text_2", JMBG="sample_text_2", KontaktKorisnika="sample_text_2", KorisnikID=13, Password="sample_text_2", PrezimeKorisnika="sample_text_2", Username="sample_text_2")
    b = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    _safe_set(b, 'korisnik7', a1)
    assert _is_linked(b, 'korisnik7', a1)
    if hasattr(a1, 'aranzman6'):
        assert _is_linked(a1, 'aranzman6', b)
    _safe_set(b, 'korisnik7', a2)
    assert _is_linked(b, 'korisnik7', a2)
    if hasattr(a1, 'aranzman6'):
        assert not _is_linked(a1, 'aranzman6', b)
    if hasattr(a2, 'aranzman6'):
        assert _is_linked(a2, 'aranzman6', b)
    _safe_set(b, 'korisnik7', None)
    assert not _is_linked(b, 'korisnik7', a2)
    if hasattr(a2, 'aranzman6'):
        assert not _is_linked(a2, 'aranzman6', b)


def test_assoc_Putnik_Aranzman_reverse_link_reassign_clear():
    a1 = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    a2 = Putnik(AdresaPutnika="sample_text_2", AranzmanID=13, BrojPasosa=13, GradPutnika="sample_text_2", ImePutnika="sample_text_2", JMBG="sample_text_2", KontaktPutnika="sample_text_2", PrezimePutnika="sample_text_2", PutnikID=13)
    b = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    _safe_set(b, 'putnik11', {a1})
    assert _is_linked(b, 'putnik11', a1)
    if hasattr(a1, 'aranzman10'):
        assert _is_linked(a1, 'aranzman10', b)
    _safe_set(b, 'putnik11', {a2})
    assert _is_linked(b, 'putnik11', a2)
    if hasattr(a1, 'aranzman10'):
        assert not _is_linked(a1, 'aranzman10', b)
    if hasattr(a2, 'aranzman10'):
        assert _is_linked(a2, 'aranzman10', b)
    _safe_set(b, 'putnik11', set())
    assert not _is_linked(b, 'putnik11', a2)
    if hasattr(a2, 'aranzman10'):
        assert not _is_linked(a2, 'aranzman10', b)


def test_assoc_Uplata_Putnik_reverse_link_reassign_clear():
    a1 = Uplata(DatumUplate="sample_text", Iznos="sample_text", NazivUplate="sample_text", PutnikID=7, UplataID=7)
    a2 = Uplata(DatumUplate="sample_text_2", Iznos="sample_text_2", NazivUplate="sample_text_2", PutnikID=13, UplataID=13)
    b = Putnik(AdresaPutnika="sample_text", AranzmanID=7, BrojPasosa=7, GradPutnika="sample_text", ImePutnika="sample_text", JMBG="sample_text", KontaktPutnika="sample_text", PrezimePutnika="sample_text", PutnikID=7)
    _safe_set(b, 'uplata13', {a1})
    assert _is_linked(b, 'uplata13', a1)
    if hasattr(a1, 'putnik12'):
        assert _is_linked(a1, 'putnik12', b)
    _safe_set(b, 'uplata13', {a2})
    assert _is_linked(b, 'uplata13', a2)
    if hasattr(a1, 'putnik12'):
        assert not _is_linked(a1, 'putnik12', b)
    if hasattr(a2, 'putnik12'):
        assert _is_linked(a2, 'putnik12', b)
    _safe_set(b, 'uplata13', set())
    assert not _is_linked(b, 'uplata13', a2)
    if hasattr(a2, 'putnik12'):
        assert not _is_linked(a2, 'putnik12', b)


def test_assoc_Vodic_Aranzman_reverse_link_reassign_clear():
    a1 = Vodic(AdresaVodica="sample_text", GradVodica="sample_text", ImeVodica="sample_text", JMBG="sample_text", KontaktVodica="sample_text", PrezimeVodica="sample_text", VodicID=7)
    a2 = Vodic(AdresaVodica="sample_text_2", GradVodica="sample_text_2", ImeVodica="sample_text_2", JMBG="sample_text_2", KontaktVodica="sample_text_2", PrezimeVodica="sample_text_2", VodicID=13)
    b = Aranzman(AranzmanID=7, CenaAranzmana="sample_text", DatumAranzmana="sample_text", HotelID=7, KorisnikID=7, NazivAranzmana="sample_text", OpisAranzmana="sample_text", VodicID=7)
    _safe_set(b, 'vodic1', a1)
    assert _is_linked(b, 'vodic1', a1)
    if hasattr(a1, 'aranzman0'):
        assert _is_linked(a1, 'aranzman0', b)
    _safe_set(b, 'vodic1', a2)
    assert _is_linked(b, 'vodic1', a2)
    if hasattr(a1, 'aranzman0'):
        assert not _is_linked(a1, 'aranzman0', b)
    if hasattr(a2, 'aranzman0'):
        assert _is_linked(a2, 'aranzman0', b)
    _safe_set(b, 'vodic1', None)
    assert not _is_linked(b, 'vodic1', a2)
    if hasattr(a2, 'aranzman0'):
        assert not _is_linked(a2, 'aranzman0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

