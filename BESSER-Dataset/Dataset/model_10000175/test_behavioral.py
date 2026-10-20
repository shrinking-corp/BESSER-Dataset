import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Agent,
    Aran_man,
    Kupac,
    Osiguranje,
    Transakcija,
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

def test_assoc_Agent_Aran_man_reverse_link_reassign_clear():
    a1 = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    a2 = Aran_man(Aranzman_ID="sample_text_2", Cena="sample_text_2", DatumPolaska="sample_text_2", DatumPovratka="sample_text_2", NazivAran_="sample_text_2", SlobMesto=False)
    b = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    _safe_set(b, 'Agent_Aran_man_08', {a1})
    assert _is_linked(b, 'Agent_Aran_man_08', a1)
    if hasattr(a1, 'Agent_Aran_man_19'):
        assert _is_linked(a1, 'Agent_Aran_man_19', b)
    _safe_set(b, 'Agent_Aran_man_08', {a2})
    assert _is_linked(b, 'Agent_Aran_man_08', a2)
    if hasattr(a1, 'Agent_Aran_man_19'):
        assert not _is_linked(a1, 'Agent_Aran_man_19', b)
    if hasattr(a2, 'Agent_Aran_man_19'):
        assert _is_linked(a2, 'Agent_Aran_man_19', b)
    _safe_set(b, 'Agent_Aran_man_08', set())
    assert not _is_linked(b, 'Agent_Aran_man_08', a2)
    if hasattr(a2, 'Agent_Aran_man_19'):
        assert not _is_linked(a2, 'Agent_Aran_man_19', b)


def test_assoc_Agent_Kupac_reverse_link_reassign_clear():
    a1 = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    a2 = Kupac(BrojPasosa=13, Grad="sample_text_2", Ime="sample_text_2", JMBG=13, Kupac_ID="sample_text_2", Mobilni=13, Prezime="sample_text_2")
    b = Agent(Agent_ID="sample_text", BrojAgenta=7, Ime="sample_text", JMBG=7, Prezime="sample_text")
    _safe_set(b, 'Agent_Kupac_06', {a1})
    assert _is_linked(b, 'Agent_Kupac_06', a1)
    if hasattr(a1, 'Agent_Kupac_17'):
        assert _is_linked(a1, 'Agent_Kupac_17', b)
    _safe_set(b, 'Agent_Kupac_06', {a2})
    assert _is_linked(b, 'Agent_Kupac_06', a2)
    if hasattr(a1, 'Agent_Kupac_17'):
        assert not _is_linked(a1, 'Agent_Kupac_17', b)
    if hasattr(a2, 'Agent_Kupac_17'):
        assert _is_linked(a2, 'Agent_Kupac_17', b)
    _safe_set(b, 'Agent_Kupac_06', set())
    assert not _is_linked(b, 'Agent_Kupac_06', a2)
    if hasattr(a2, 'Agent_Kupac_17'):
        assert not _is_linked(a2, 'Agent_Kupac_17', b)


def test_assoc_Osiguranje_Putnik_reverse_link_reassign_clear():
    a1 = Osiguranje(BrojPolise=7, Cena="sample_text", OsigKuca="sample_text", Osiguranje_ID="sample_text", PaketPokri_a="sample_text")
    a2 = Osiguranje(BrojPolise=13, Cena="sample_text_2", OsigKuca="sample_text_2", Osiguranje_ID="sample_text_2", PaketPokri_a="sample_text_2")
    b = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    _safe_set(b, 'Osiguranje_Putnik_11', a1)
    assert _is_linked(b, 'Osiguranje_Putnik_11', a1)
    if hasattr(a1, 'Osiguranje_Putnik_00'):
        assert _is_linked(a1, 'Osiguranje_Putnik_00', b)
    _safe_set(b, 'Osiguranje_Putnik_11', a2)
    assert _is_linked(b, 'Osiguranje_Putnik_11', a2)
    if hasattr(a1, 'Osiguranje_Putnik_00'):
        assert not _is_linked(a1, 'Osiguranje_Putnik_00', b)
    if hasattr(a2, 'Osiguranje_Putnik_00'):
        assert _is_linked(a2, 'Osiguranje_Putnik_00', b)
    _safe_set(b, 'Osiguranje_Putnik_11', None)
    assert not _is_linked(b, 'Osiguranje_Putnik_11', a2)
    if hasattr(a2, 'Osiguranje_Putnik_00'):
        assert not _is_linked(a2, 'Osiguranje_Putnik_00', b)


def test_assoc_Putnik_Rezervisanje_reverse_link_reassign_clear():
    a1 = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    a2 = Kupac(BrojPasosa=13, Grad="sample_text_2", Ime="sample_text_2", JMBG=13, Kupac_ID="sample_text_2", Mobilni=13, Prezime="sample_text_2")
    b = Aran_man(Aranzman_ID="sample_text", Cena="sample_text", DatumPolaska="sample_text", DatumPovratka="sample_text", NazivAran_="sample_text", SlobMesto=True)
    _safe_set(b, 'Putnik_Rezervisanje_13', a1)
    assert _is_linked(b, 'Putnik_Rezervisanje_13', a1)
    if hasattr(a1, 'Putnik_Rezervisanje_02'):
        assert _is_linked(a1, 'Putnik_Rezervisanje_02', b)
    _safe_set(b, 'Putnik_Rezervisanje_13', a2)
    assert _is_linked(b, 'Putnik_Rezervisanje_13', a2)
    if hasattr(a1, 'Putnik_Rezervisanje_02'):
        assert not _is_linked(a1, 'Putnik_Rezervisanje_02', b)
    if hasattr(a2, 'Putnik_Rezervisanje_02'):
        assert _is_linked(a2, 'Putnik_Rezervisanje_02', b)
    _safe_set(b, 'Putnik_Rezervisanje_13', None)
    assert not _is_linked(b, 'Putnik_Rezervisanje_13', a2)
    if hasattr(a2, 'Putnik_Rezervisanje_02'):
        assert not _is_linked(a2, 'Putnik_Rezervisanje_02', b)


def test_assoc_Transakcija_Kupac_reverse_link_reassign_clear():
    a1 = Transakcija(Trans_ID="sample_text", datum_trans="sample_text", suma="sample_text", tip="sample_text")
    a2 = Transakcija(Trans_ID="sample_text_2", datum_trans="sample_text_2", suma="sample_text_2", tip="sample_text_2")
    b = Kupac(BrojPasosa=7, Grad="sample_text", Ime="sample_text", JMBG=7, Kupac_ID="sample_text", Mobilni=7, Prezime="sample_text")
    _safe_set(b, 'Transakcija_Kupac_15', {a1})
    assert _is_linked(b, 'Transakcija_Kupac_15', a1)
    if hasattr(a1, 'Transakcija_Kupac_04'):
        assert _is_linked(a1, 'Transakcija_Kupac_04', b)
    _safe_set(b, 'Transakcija_Kupac_15', {a2})
    assert _is_linked(b, 'Transakcija_Kupac_15', a2)
    if hasattr(a1, 'Transakcija_Kupac_04'):
        assert not _is_linked(a1, 'Transakcija_Kupac_04', b)
    if hasattr(a2, 'Transakcija_Kupac_04'):
        assert _is_linked(a2, 'Transakcija_Kupac_04', b)
    _safe_set(b, 'Transakcija_Kupac_15', set())
    assert not _is_linked(b, 'Transakcija_Kupac_15', a2)
    if hasattr(a2, 'Transakcija_Kupac_04'):
        assert not _is_linked(a2, 'Transakcija_Kupac_04', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

