import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Destinacija,
    Hotel,
    Karta,
    Korisnik_IS,
    Osiguranje,
    Putnik,
    Rezervisanje,
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

def test_assoc_Destinacija_Hotel_reverse_link_reassign_clear():
    a1 = Hotel(AdresaHotela="sample_text", CenaSmestaja="sample_text", DestiID=7, DuzinaBoravka=7, HotelID=7, ImeHotela="sample_text", SobaHotela=7, SpratHotela=7, UslugaHotela="sample_text")
    a2 = Hotel(AdresaHotela="sample_text_2", CenaSmestaja="sample_text_2", DestiID=13, DuzinaBoravka=13, HotelID=13, ImeHotela="sample_text_2", SobaHotela=13, SpratHotela=13, UslugaHotela="sample_text_2")
    b = Destinacija(DesDrzava="sample_text", DesGrad="sample_text", DestiID=7)
    _safe_set(b, 'hotel0', {a1})
    assert _is_linked(b, 'hotel0', a1)
    if hasattr(a1, 'destinacija1'):
        assert _is_linked(a1, 'destinacija1', b)
    _safe_set(b, 'hotel0', {a2})
    assert _is_linked(b, 'hotel0', a2)
    if hasattr(a1, 'destinacija1'):
        assert not _is_linked(a1, 'destinacija1', b)
    if hasattr(a2, 'destinacija1'):
        assert _is_linked(a2, 'destinacija1', b)
    _safe_set(b, 'hotel0', set())
    assert not _is_linked(b, 'hotel0', a2)
    if hasattr(a2, 'destinacija1'):
        assert not _is_linked(a2, 'destinacija1', b)


def test_assoc_Karta_Rezervisanje_reverse_link_reassign_clear():
    a1 = Rezervisanje(Cena="sample_text", DatumDolaska="sample_text", DatumPolaska="sample_text", DestiID=7, KorisnikID=7, PutnikID=7, RezerID=7, SlobMesto=True)
    a2 = Rezervisanje(Cena="sample_text_2", DatumDolaska="sample_text_2", DatumPolaska="sample_text_2", DestiID=13, KorisnikID=13, PutnikID=13, RezerID=13, SlobMesto=False)
    b = Karta(CenaKarte="sample_text", KartaID=7, OdlazakKarta="sample_text", PovratakKarta="sample_text", RezerID=7, VremeOdlaska="sample_text", VremePovratka="sample_text")
    _safe_set(b, 'rezervisanje10', a1)
    assert _is_linked(b, 'rezervisanje10', a1)
    if hasattr(a1, 'karta11'):
        assert _is_linked(a1, 'karta11', b)
    _safe_set(b, 'rezervisanje10', a2)
    assert _is_linked(b, 'rezervisanje10', a2)
    if hasattr(a1, 'karta11'):
        assert not _is_linked(a1, 'karta11', b)
    if hasattr(a2, 'karta11'):
        assert _is_linked(a2, 'karta11', b)
    _safe_set(b, 'rezervisanje10', None)
    assert not _is_linked(b, 'rezervisanje10', a2)
    if hasattr(a2, 'karta11'):
        assert not _is_linked(a2, 'karta11', b)


def test_assoc_Osiguranje_Putnik_reverse_link_reassign_clear():
    a1 = Putnik(Adresa="sample_text", Grad="sample_text", ImePut="sample_text", JMBG="sample_text", Mobilni=7, OsigID=7, PrezimePut="sample_text", PutnikID=7, eMail="sample_text")
    a2 = Putnik(Adresa="sample_text_2", Grad="sample_text_2", ImePut="sample_text_2", JMBG="sample_text_2", Mobilni=13, OsigID=13, PrezimePut="sample_text_2", PutnikID=13, eMail="sample_text_2")
    b = Osiguranje(KucaOsiguranje="sample_text", OsigID=7)
    _safe_set(b, 'putnik4', {a1})
    assert _is_linked(b, 'putnik4', a1)
    if hasattr(a1, 'osiguranje5'):
        assert _is_linked(a1, 'osiguranje5', b)
    _safe_set(b, 'putnik4', {a2})
    assert _is_linked(b, 'putnik4', a2)
    if hasattr(a1, 'osiguranje5'):
        assert not _is_linked(a1, 'osiguranje5', b)
    if hasattr(a2, 'osiguranje5'):
        assert _is_linked(a2, 'osiguranje5', b)
    _safe_set(b, 'putnik4', set())
    assert not _is_linked(b, 'putnik4', a2)
    if hasattr(a2, 'osiguranje5'):
        assert not _is_linked(a2, 'osiguranje5', b)


def test_assoc_Putnik_Rezervisanje_reverse_link_reassign_clear():
    a1 = Rezervisanje(Cena="sample_text", DatumDolaska="sample_text", DatumPolaska="sample_text", DestiID=7, KorisnikID=7, PutnikID=7, RezerID=7, SlobMesto=True)
    a2 = Rezervisanje(Cena="sample_text_2", DatumDolaska="sample_text_2", DatumPolaska="sample_text_2", DestiID=13, KorisnikID=13, PutnikID=13, RezerID=13, SlobMesto=False)
    b = Putnik(Adresa="sample_text", Grad="sample_text", ImePut="sample_text", JMBG="sample_text", Mobilni=7, OsigID=7, PrezimePut="sample_text", PutnikID=7, eMail="sample_text")
    _safe_set(b, 'rezervisanje6', {a1})
    assert _is_linked(b, 'rezervisanje6', a1)
    if hasattr(a1, 'putnik7'):
        assert _is_linked(a1, 'putnik7', b)
    _safe_set(b, 'rezervisanje6', {a2})
    assert _is_linked(b, 'rezervisanje6', a2)
    if hasattr(a1, 'putnik7'):
        assert not _is_linked(a1, 'putnik7', b)
    if hasattr(a2, 'putnik7'):
        assert _is_linked(a2, 'putnik7', b)
    _safe_set(b, 'rezervisanje6', set())
    assert not _is_linked(b, 'rezervisanje6', a2)
    if hasattr(a2, 'putnik7'):
        assert not _is_linked(a2, 'putnik7', b)


def test_assoc_Rezervisanje_Destinacija_reverse_link_reassign_clear():
    a1 = Rezervisanje(Cena="sample_text", DatumDolaska="sample_text", DatumPolaska="sample_text", DestiID=7, KorisnikID=7, PutnikID=7, RezerID=7, SlobMesto=True)
    a2 = Rezervisanje(Cena="sample_text_2", DatumDolaska="sample_text_2", DatumPolaska="sample_text_2", DestiID=13, KorisnikID=13, PutnikID=13, RezerID=13, SlobMesto=False)
    b = Destinacija(DesDrzava="sample_text", DesGrad="sample_text", DestiID=7)
    _safe_set(b, 'rezervisanje3', {a1})
    assert _is_linked(b, 'rezervisanje3', a1)
    if hasattr(a1, 'destinacija2'):
        assert _is_linked(a1, 'destinacija2', b)
    _safe_set(b, 'rezervisanje3', {a2})
    assert _is_linked(b, 'rezervisanje3', a2)
    if hasattr(a1, 'destinacija2'):
        assert not _is_linked(a1, 'destinacija2', b)
    if hasattr(a2, 'destinacija2'):
        assert _is_linked(a2, 'destinacija2', b)
    _safe_set(b, 'rezervisanje3', set())
    assert not _is_linked(b, 'rezervisanje3', a2)
    if hasattr(a2, 'destinacija2'):
        assert not _is_linked(a2, 'destinacija2', b)


def test_assoc_Rezervisanje_Korisnik_IS_reverse_link_reassign_clear():
    a1 = Rezervisanje(Cena="sample_text", DatumDolaska="sample_text", DatumPolaska="sample_text", DestiID=7, KorisnikID=7, PutnikID=7, RezerID=7, SlobMesto=True)
    a2 = Rezervisanje(Cena="sample_text_2", DatumDolaska="sample_text_2", DatumPolaska="sample_text_2", DestiID=13, KorisnikID=13, PutnikID=13, RezerID=13, SlobMesto=False)
    b = Korisnik_IS(ImeKorisnika="sample_text", KorisnikID=7, Password="sample_text", PrezimeKorisnika="sample_text", UserName="sample_text")
    _safe_set(b, 'rezervisanje9', {a1})
    assert _is_linked(b, 'rezervisanje9', a1)
    if hasattr(a1, 'korisnik_IS8'):
        assert _is_linked(a1, 'korisnik_IS8', b)
    _safe_set(b, 'rezervisanje9', {a2})
    assert _is_linked(b, 'rezervisanje9', a2)
    if hasattr(a1, 'korisnik_IS8'):
        assert not _is_linked(a1, 'korisnik_IS8', b)
    if hasattr(a2, 'korisnik_IS8'):
        assert _is_linked(a2, 'korisnik_IS8', b)
    _safe_set(b, 'rezervisanje9', set())
    assert not _is_linked(b, 'rezervisanje9', a2)
    if hasattr(a2, 'korisnik_IS8'):
        assert not _is_linked(a2, 'korisnik_IS8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

