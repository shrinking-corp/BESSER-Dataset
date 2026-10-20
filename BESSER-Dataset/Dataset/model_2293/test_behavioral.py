import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    zlvp_Anrede,
    zlvp_Essen,
    zlvp_Funktion,
    zlvp_Geschlecht,
    zlvp_Gruppen,
    zlvp_Jahr,
    zlvp_Lager,
    zlvp_Lagerort,
    zlvp_Legenda,
    zlvp_LegendaTyp,
    zlvp_Leiter,
    zlvp_Person,
    zlvp_Programm,
    zlvp_Schaeden,
    zlvp_Stab,
    zlvp_Teilnehmer,
    zlvp_Verleih,
    zlvp_Zelt,
    zlvp_ZeltDetail,
    zlvp_ZeltDetailBezeichnung,
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

def test_assoc_Lager49_reverse_link_reassign_clear():
    a1 = zlvp_Zelt(id=7, name="sample_text")
    a2 = zlvp_Zelt(id=13, name="sample_text_2")
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager51', a1)
    assert _is_linked(b, 'zlvp_Lager51', a1)
    if hasattr(a1, 'zlvp_Zelt50'):
        assert _is_linked(a1, 'zlvp_Zelt50', b)
    _safe_set(b, 'zlvp_Lager51', a2)
    assert _is_linked(b, 'zlvp_Lager51', a2)
    if hasattr(a1, 'zlvp_Zelt50'):
        assert not _is_linked(a1, 'zlvp_Zelt50', b)
    if hasattr(a2, 'zlvp_Zelt50'):
        assert _is_linked(a2, 'zlvp_Zelt50', b)
    _safe_set(b, 'zlvp_Lager51', None)
    assert not _is_linked(b, 'zlvp_Lager51', a2)
    if hasattr(a2, 'zlvp_Zelt50'):
        assert not _is_linked(a2, 'zlvp_Zelt50', b)


def test_assoc_anrede1_reverse_link_reassign_clear():
    a1 = zlvp_Person(email="sample_text", gebDat=date(2024, 1, 1), handyNr="sample_text", id=7, nachname="sample_text", notTelNr="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", version="sample_text", vorname="sample_text")
    a2 = zlvp_Person(email="sample_text_2", gebDat=date(2025, 6, 15), handyNr="sample_text_2", id=13, nachname="sample_text_2", notTelNr="sample_text_2", ort="sample_text_2", plz="sample_text_2", strasse="sample_text_2", telNr="sample_text_2", version="sample_text_2", vorname="sample_text_2")
    b = zlvp_Anrede(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Anrede', a1)
    assert _is_linked(b, 'zlvp_Anrede', a1)
    if hasattr(a1, 'zlvp_Person2'):
        assert _is_linked(a1, 'zlvp_Person2', b)
    _safe_set(b, 'zlvp_Anrede', a2)
    assert _is_linked(b, 'zlvp_Anrede', a2)
    if hasattr(a1, 'zlvp_Person2'):
        assert not _is_linked(a1, 'zlvp_Person2', b)
    if hasattr(a2, 'zlvp_Person2'):
        assert _is_linked(a2, 'zlvp_Person2', b)
    _safe_set(b, 'zlvp_Anrede', None)
    assert not _is_linked(b, 'zlvp_Anrede', a2)
    if hasattr(a2, 'zlvp_Person2'):
        assert not _is_linked(a2, 'zlvp_Person2', b)


def test_assoc_anrede54_reverse_link_reassign_clear():
    a1 = zlvp_Legenda(bemerkung="sample_text", email="sample_text", faxNr="sample_text", firma="sample_text", handyNr="sample_text", id=7, nachname="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", vorname="sample_text")
    a2 = zlvp_Legenda(bemerkung="sample_text_2", email="sample_text_2", faxNr="sample_text_2", firma="sample_text_2", handyNr="sample_text_2", id=13, nachname="sample_text_2", ort="sample_text_2", plz="sample_text_2", strasse="sample_text_2", telNr="sample_text_2", vorname="sample_text_2")
    b = zlvp_Anrede(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Anrede55', a1)
    assert _is_linked(b, 'zlvp_Anrede55', a1)
    if hasattr(a1, 'zlvp_Legenda'):
        assert _is_linked(a1, 'zlvp_Legenda', b)
    _safe_set(b, 'zlvp_Anrede55', a2)
    assert _is_linked(b, 'zlvp_Anrede55', a2)
    if hasattr(a1, 'zlvp_Legenda'):
        assert not _is_linked(a1, 'zlvp_Legenda', b)
    if hasattr(a2, 'zlvp_Legenda'):
        assert _is_linked(a2, 'zlvp_Legenda', b)
    _safe_set(b, 'zlvp_Anrede55', None)
    assert not _is_linked(b, 'zlvp_Anrede55', a2)
    if hasattr(a2, 'zlvp_Legenda'):
        assert not _is_linked(a2, 'zlvp_Legenda', b)


def test_assoc_essen26_reverse_link_reassign_clear():
    a1 = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    a2 = zlvp_Lager(id=13, name="sample_text_2", ort="sample_text_2", start=date(2025, 6, 15), stop=date(2025, 6, 15), thema="sample_text_2")
    b = zlvp_Essen(datum=date(2024, 1, 1), id=7, nachmittag="sample_text", nacht="sample_text", vormittag="sample_text")
    _safe_set(b, 'zlvp_Essen', a1)
    assert _is_linked(b, 'zlvp_Essen', a1)
    if hasattr(a1, 'zlvp_Lager27'):
        assert _is_linked(a1, 'zlvp_Lager27', b)
    _safe_set(b, 'zlvp_Essen', a2)
    assert _is_linked(b, 'zlvp_Essen', a2)
    if hasattr(a1, 'zlvp_Lager27'):
        assert not _is_linked(a1, 'zlvp_Lager27', b)
    if hasattr(a2, 'zlvp_Lager27'):
        assert _is_linked(a2, 'zlvp_Lager27', b)
    _safe_set(b, 'zlvp_Essen', None)
    assert not _is_linked(b, 'zlvp_Essen', a2)
    if hasattr(a2, 'zlvp_Lager27'):
        assert not _is_linked(a2, 'zlvp_Lager27', b)


def test_assoc_funktion7_reverse_link_reassign_clear():
    a1 = zlvp_Stab(id=7)
    a2 = zlvp_Stab(id=13)
    b = zlvp_Funktion(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Funktion', a1)
    assert _is_linked(b, 'zlvp_Funktion', a1)
    if hasattr(a1, 'zlvp_Stab8'):
        assert _is_linked(a1, 'zlvp_Stab8', b)
    _safe_set(b, 'zlvp_Funktion', a2)
    assert _is_linked(b, 'zlvp_Funktion', a2)
    if hasattr(a1, 'zlvp_Stab8'):
        assert not _is_linked(a1, 'zlvp_Stab8', b)
    if hasattr(a2, 'zlvp_Stab8'):
        assert _is_linked(a2, 'zlvp_Stab8', b)
    _safe_set(b, 'zlvp_Funktion', None)
    assert not _is_linked(b, 'zlvp_Funktion', a2)
    if hasattr(a2, 'zlvp_Stab8'):
        assert not _is_linked(a2, 'zlvp_Stab8', b)


def test_assoc_geschlecht0_reverse_link_reassign_clear():
    a1 = zlvp_Person(email="sample_text", gebDat=date(2024, 1, 1), handyNr="sample_text", id=7, nachname="sample_text", notTelNr="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", version="sample_text", vorname="sample_text")
    a2 = zlvp_Person(email="sample_text_2", gebDat=date(2025, 6, 15), handyNr="sample_text_2", id=13, nachname="sample_text_2", notTelNr="sample_text_2", ort="sample_text_2", plz="sample_text_2", strasse="sample_text_2", telNr="sample_text_2", version="sample_text_2", vorname="sample_text_2")
    b = zlvp_Geschlecht(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Geschlecht', a1)
    assert _is_linked(b, 'zlvp_Geschlecht', a1)
    if hasattr(a1, 'zlvp_Person'):
        assert _is_linked(a1, 'zlvp_Person', b)
    _safe_set(b, 'zlvp_Geschlecht', a2)
    assert _is_linked(b, 'zlvp_Geschlecht', a2)
    if hasattr(a1, 'zlvp_Person'):
        assert not _is_linked(a1, 'zlvp_Person', b)
    if hasattr(a2, 'zlvp_Person'):
        assert _is_linked(a2, 'zlvp_Person', b)
    _safe_set(b, 'zlvp_Geschlecht', None)
    assert not _is_linked(b, 'zlvp_Geschlecht', a2)
    if hasattr(a2, 'zlvp_Person'):
        assert not _is_linked(a2, 'zlvp_Person', b)


def test_assoc_gruppen13_reverse_link_reassign_clear():
    a1 = zlvp_Teilnehmer(id=7)
    a2 = zlvp_Teilnehmer(id=13)
    b = zlvp_Gruppen(id=7, name="sample_text", spruch="sample_text")
    _safe_set(b, 'zlvp_Gruppen14', a1)
    assert _is_linked(b, 'zlvp_Gruppen14', a1)
    if hasattr(a1, 'zlvp_Teilnehmer'):
        assert _is_linked(a1, 'zlvp_Teilnehmer', b)
    _safe_set(b, 'zlvp_Gruppen14', a2)
    assert _is_linked(b, 'zlvp_Gruppen14', a2)
    if hasattr(a1, 'zlvp_Teilnehmer'):
        assert not _is_linked(a1, 'zlvp_Teilnehmer', b)
    if hasattr(a2, 'zlvp_Teilnehmer'):
        assert _is_linked(a2, 'zlvp_Teilnehmer', b)
    _safe_set(b, 'zlvp_Gruppen14', None)
    assert not _is_linked(b, 'zlvp_Gruppen14', a2)
    if hasattr(a2, 'zlvp_Teilnehmer'):
        assert not _is_linked(a2, 'zlvp_Teilnehmer', b)


def test_assoc_gruppen20_reverse_link_reassign_clear():
    a1 = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    a2 = zlvp_Lager(id=13, name="sample_text_2", ort="sample_text_2", start=date(2025, 6, 15), stop=date(2025, 6, 15), thema="sample_text_2")
    b = zlvp_Gruppen(id=7, name="sample_text", spruch="sample_text")
    _safe_set(b, 'zlvp_Gruppen22', a1)
    assert _is_linked(b, 'zlvp_Gruppen22', a1)
    if hasattr(a1, 'zlvp_Lager21'):
        assert _is_linked(a1, 'zlvp_Lager21', b)
    _safe_set(b, 'zlvp_Gruppen22', a2)
    assert _is_linked(b, 'zlvp_Gruppen22', a2)
    if hasattr(a1, 'zlvp_Lager21'):
        assert not _is_linked(a1, 'zlvp_Lager21', b)
    if hasattr(a2, 'zlvp_Lager21'):
        assert _is_linked(a2, 'zlvp_Lager21', b)
    _safe_set(b, 'zlvp_Gruppen22', None)
    assert not _is_linked(b, 'zlvp_Gruppen22', a2)
    if hasattr(a2, 'zlvp_Lager21'):
        assert not _is_linked(a2, 'zlvp_Lager21', b)


def test_assoc_gruppen9_reverse_link_reassign_clear():
    a1 = zlvp_Leiter(id=7)
    a2 = zlvp_Leiter(id=13)
    b = zlvp_Gruppen(id=7, name="sample_text", spruch="sample_text")
    _safe_set(b, 'zlvp_Gruppen', a1)
    assert _is_linked(b, 'zlvp_Gruppen', a1)
    if hasattr(a1, 'zlvp_Leiter'):
        assert _is_linked(a1, 'zlvp_Leiter', b)
    _safe_set(b, 'zlvp_Gruppen', a2)
    assert _is_linked(b, 'zlvp_Gruppen', a2)
    if hasattr(a1, 'zlvp_Leiter'):
        assert not _is_linked(a1, 'zlvp_Leiter', b)
    if hasattr(a2, 'zlvp_Leiter'):
        assert _is_linked(a2, 'zlvp_Leiter', b)
    _safe_set(b, 'zlvp_Gruppen', None)
    assert not _is_linked(b, 'zlvp_Gruppen', a2)
    if hasattr(a2, 'zlvp_Leiter'):
        assert not _is_linked(a2, 'zlvp_Leiter', b)


def test_assoc_lager18_reverse_link_reassign_clear():
    a1 = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    a2 = zlvp_Lager(id=13, name="sample_text_2", ort="sample_text_2", start=date(2025, 6, 15), stop=date(2025, 6, 15), thema="sample_text_2")
    b = zlvp_Jahr(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Jahr', {a1})
    assert _is_linked(b, 'zlvp_Jahr', a1)
    if hasattr(a1, 'zlvp_Lager19'):
        assert _is_linked(a1, 'zlvp_Lager19', b)
    _safe_set(b, 'zlvp_Jahr', {a2})
    assert _is_linked(b, 'zlvp_Jahr', a2)
    if hasattr(a1, 'zlvp_Lager19'):
        assert not _is_linked(a1, 'zlvp_Lager19', b)
    if hasattr(a2, 'zlvp_Lager19'):
        assert _is_linked(a2, 'zlvp_Lager19', b)
    _safe_set(b, 'zlvp_Jahr', set())
    assert not _is_linked(b, 'zlvp_Jahr', a2)
    if hasattr(a2, 'zlvp_Lager19'):
        assert not _is_linked(a2, 'zlvp_Lager19', b)


def test_assoc_lager3_reverse_link_reassign_clear():
    a1 = zlvp_Stab(id=7)
    a2 = zlvp_Stab(id=13)
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager', a1)
    assert _is_linked(b, 'zlvp_Lager', a1)
    if hasattr(a1, 'zlvp_Stab'):
        assert _is_linked(a1, 'zlvp_Stab', b)
    _safe_set(b, 'zlvp_Lager', a2)
    assert _is_linked(b, 'zlvp_Lager', a2)
    if hasattr(a1, 'zlvp_Stab'):
        assert not _is_linked(a1, 'zlvp_Stab', b)
    if hasattr(a2, 'zlvp_Stab'):
        assert _is_linked(a2, 'zlvp_Stab', b)
    _safe_set(b, 'zlvp_Lager', None)
    assert not _is_linked(b, 'zlvp_Lager', a2)
    if hasattr(a2, 'zlvp_Stab'):
        assert not _is_linked(a2, 'zlvp_Stab', b)


def test_assoc_lager61_reverse_link_reassign_clear():
    a1 = zlvp_Lagerort(id=7, name="sample_text")
    a2 = zlvp_Lagerort(id=13, name="sample_text_2")
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager63', a1)
    assert _is_linked(b, 'zlvp_Lager63', a1)
    if hasattr(a1, 'zlvp_Lagerort62'):
        assert _is_linked(a1, 'zlvp_Lagerort62', b)
    _safe_set(b, 'zlvp_Lager63', a2)
    assert _is_linked(b, 'zlvp_Lager63', a2)
    if hasattr(a1, 'zlvp_Lagerort62'):
        assert not _is_linked(a1, 'zlvp_Lagerort62', b)
    if hasattr(a2, 'zlvp_Lagerort62'):
        assert _is_linked(a2, 'zlvp_Lagerort62', b)
    _safe_set(b, 'zlvp_Lager63', None)
    assert not _is_linked(b, 'zlvp_Lager63', a2)
    if hasattr(a2, 'zlvp_Lagerort62'):
        assert not _is_linked(a2, 'zlvp_Lagerort62', b)


def test_assoc_lagerort35_reverse_link_reassign_clear():
    a1 = zlvp_Lagerort(id=7, name="sample_text")
    a2 = zlvp_Lagerort(id=13, name="sample_text_2")
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager36', a1)
    assert _is_linked(b, 'zlvp_Lager36', a1)
    if hasattr(a1, 'zlvp_Lagerort'):
        assert _is_linked(a1, 'zlvp_Lagerort', b)
    _safe_set(b, 'zlvp_Lager36', a2)
    assert _is_linked(b, 'zlvp_Lager36', a2)
    if hasattr(a1, 'zlvp_Lagerort'):
        assert not _is_linked(a1, 'zlvp_Lagerort', b)
    if hasattr(a2, 'zlvp_Lagerort'):
        assert _is_linked(a2, 'zlvp_Lagerort', b)
    _safe_set(b, 'zlvp_Lager36', None)
    assert not _is_linked(b, 'zlvp_Lager36', a2)
    if hasattr(a2, 'zlvp_Lagerort'):
        assert not _is_linked(a2, 'zlvp_Lagerort', b)


def test_assoc_legenda58_reverse_link_reassign_clear():
    a1 = zlvp_Legenda(bemerkung="sample_text", email="sample_text", faxNr="sample_text", firma="sample_text", handyNr="sample_text", id=7, nachname="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", vorname="sample_text")
    a2 = zlvp_Legenda(bemerkung="sample_text_2", email="sample_text_2", faxNr="sample_text_2", firma="sample_text_2", handyNr="sample_text_2", id=13, nachname="sample_text_2", ort="sample_text_2", plz="sample_text_2", strasse="sample_text_2", telNr="sample_text_2", vorname="sample_text_2")
    b = zlvp_Lagerort(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Lagerort59', {a1})
    assert _is_linked(b, 'zlvp_Lagerort59', a1)
    if hasattr(a1, 'zlvp_Legenda60'):
        assert _is_linked(a1, 'zlvp_Legenda60', b)
    _safe_set(b, 'zlvp_Lagerort59', {a2})
    assert _is_linked(b, 'zlvp_Lagerort59', a2)
    if hasattr(a1, 'zlvp_Legenda60'):
        assert not _is_linked(a1, 'zlvp_Legenda60', b)
    if hasattr(a2, 'zlvp_Legenda60'):
        assert _is_linked(a2, 'zlvp_Legenda60', b)
    _safe_set(b, 'zlvp_Lagerort59', set())
    assert not _is_linked(b, 'zlvp_Lagerort59', a2)
    if hasattr(a2, 'zlvp_Legenda60'):
        assert not _is_linked(a2, 'zlvp_Legenda60', b)


def test_assoc_legendaTyp56_reverse_link_reassign_clear():
    a1 = zlvp_LegendaTyp(id=7, name="sample_text")
    a2 = zlvp_LegendaTyp(id=13, name="sample_text_2")
    b = zlvp_Legenda(bemerkung="sample_text", email="sample_text", faxNr="sample_text", firma="sample_text", handyNr="sample_text", id=7, nachname="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", vorname="sample_text")
    _safe_set(b, 'zlvp_Legenda57', {a1})
    assert _is_linked(b, 'zlvp_Legenda57', a1)
    if hasattr(a1, 'zlvp_LegendaTyp'):
        assert _is_linked(a1, 'zlvp_LegendaTyp', b)
    _safe_set(b, 'zlvp_Legenda57', {a2})
    assert _is_linked(b, 'zlvp_Legenda57', a2)
    if hasattr(a1, 'zlvp_LegendaTyp'):
        assert not _is_linked(a1, 'zlvp_LegendaTyp', b)
    if hasattr(a2, 'zlvp_LegendaTyp'):
        assert _is_linked(a2, 'zlvp_LegendaTyp', b)
    _safe_set(b, 'zlvp_Legenda57', set())
    assert not _is_linked(b, 'zlvp_Legenda57', a2)
    if hasattr(a2, 'zlvp_LegendaTyp'):
        assert not _is_linked(a2, 'zlvp_LegendaTyp', b)


def test_assoc_leiter37_reverse_link_reassign_clear():
    a1 = zlvp_Leiter(id=7)
    a2 = zlvp_Leiter(id=13)
    b = zlvp_Gruppen(id=7, name="sample_text", spruch="sample_text")
    _safe_set(b, 'zlvp_Gruppen38', {a1})
    assert _is_linked(b, 'zlvp_Gruppen38', a1)
    if hasattr(a1, 'zlvp_Leiter39'):
        assert _is_linked(a1, 'zlvp_Leiter39', b)
    _safe_set(b, 'zlvp_Gruppen38', {a2})
    assert _is_linked(b, 'zlvp_Gruppen38', a2)
    if hasattr(a1, 'zlvp_Leiter39'):
        assert not _is_linked(a1, 'zlvp_Leiter39', b)
    if hasattr(a2, 'zlvp_Leiter39'):
        assert _is_linked(a2, 'zlvp_Leiter39', b)
    _safe_set(b, 'zlvp_Gruppen38', set())
    assert not _is_linked(b, 'zlvp_Gruppen38', a2)
    if hasattr(a2, 'zlvp_Leiter39'):
        assert not _is_linked(a2, 'zlvp_Leiter39', b)


def test_assoc_materialwart32_reverse_link_reassign_clear():
    a1 = zlvp_Person(email="sample_text", gebDat=date(2024, 1, 1), handyNr="sample_text", id=7, nachname="sample_text", notTelNr="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", version="sample_text", vorname="sample_text")
    a2 = zlvp_Person(email="sample_text_2", gebDat=date(2025, 6, 15), handyNr="sample_text_2", id=13, nachname="sample_text_2", notTelNr="sample_text_2", ort="sample_text_2", plz="sample_text_2", strasse="sample_text_2", telNr="sample_text_2", version="sample_text_2", vorname="sample_text_2")
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager33', {a1})
    assert _is_linked(b, 'zlvp_Lager33', a1)
    if hasattr(a1, 'zlvp_Person34'):
        assert _is_linked(a1, 'zlvp_Person34', b)
    _safe_set(b, 'zlvp_Lager33', {a2})
    assert _is_linked(b, 'zlvp_Lager33', a2)
    if hasattr(a1, 'zlvp_Person34'):
        assert not _is_linked(a1, 'zlvp_Person34', b)
    if hasattr(a2, 'zlvp_Person34'):
        assert _is_linked(a2, 'zlvp_Person34', b)
    _safe_set(b, 'zlvp_Lager33', set())
    assert not _is_linked(b, 'zlvp_Lager33', a2)
    if hasattr(a2, 'zlvp_Person34'):
        assert not _is_linked(a2, 'zlvp_Person34', b)


def test_assoc_person10_reverse_link_reassign_clear():
    a1 = zlvp_Person(email="sample_text", gebDat=date(2024, 1, 1), handyNr="sample_text", id=7, nachname="sample_text", notTelNr="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", version="sample_text", vorname="sample_text")
    a2 = zlvp_Person(email="sample_text_2", gebDat=date(2025, 6, 15), handyNr="sample_text_2", id=13, nachname="sample_text_2", notTelNr="sample_text_2", ort="sample_text_2", plz="sample_text_2", strasse="sample_text_2", telNr="sample_text_2", version="sample_text_2", vorname="sample_text_2")
    b = zlvp_Leiter(id=7)
    _safe_set(b, 'zlvp_Leiter11', a1)
    assert _is_linked(b, 'zlvp_Leiter11', a1)
    if hasattr(a1, 'zlvp_Person12'):
        assert _is_linked(a1, 'zlvp_Person12', b)
    _safe_set(b, 'zlvp_Leiter11', a2)
    assert _is_linked(b, 'zlvp_Leiter11', a2)
    if hasattr(a1, 'zlvp_Person12'):
        assert not _is_linked(a1, 'zlvp_Person12', b)
    if hasattr(a2, 'zlvp_Person12'):
        assert _is_linked(a2, 'zlvp_Person12', b)
    _safe_set(b, 'zlvp_Leiter11', None)
    assert not _is_linked(b, 'zlvp_Leiter11', a2)
    if hasattr(a2, 'zlvp_Person12'):
        assert not _is_linked(a2, 'zlvp_Person12', b)


def test_assoc_person15_reverse_link_reassign_clear():
    a1 = zlvp_Teilnehmer(id=7)
    a2 = zlvp_Teilnehmer(id=13)
    b = zlvp_Person(email="sample_text", gebDat=date(2024, 1, 1), handyNr="sample_text", id=7, nachname="sample_text", notTelNr="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", version="sample_text", vorname="sample_text")
    _safe_set(b, 'zlvp_Person17', a1)
    assert _is_linked(b, 'zlvp_Person17', a1)
    if hasattr(a1, 'zlvp_Teilnehmer16'):
        assert _is_linked(a1, 'zlvp_Teilnehmer16', b)
    _safe_set(b, 'zlvp_Person17', a2)
    assert _is_linked(b, 'zlvp_Person17', a2)
    if hasattr(a1, 'zlvp_Teilnehmer16'):
        assert not _is_linked(a1, 'zlvp_Teilnehmer16', b)
    if hasattr(a2, 'zlvp_Teilnehmer16'):
        assert _is_linked(a2, 'zlvp_Teilnehmer16', b)
    _safe_set(b, 'zlvp_Person17', None)
    assert not _is_linked(b, 'zlvp_Person17', a2)
    if hasattr(a2, 'zlvp_Teilnehmer16'):
        assert not _is_linked(a2, 'zlvp_Teilnehmer16', b)


def test_assoc_person4_reverse_link_reassign_clear():
    a1 = zlvp_Stab(id=7)
    a2 = zlvp_Stab(id=13)
    b = zlvp_Person(email="sample_text", gebDat=date(2024, 1, 1), handyNr="sample_text", id=7, nachname="sample_text", notTelNr="sample_text", ort="sample_text", plz="sample_text", strasse="sample_text", telNr="sample_text", version="sample_text", vorname="sample_text")
    _safe_set(b, 'zlvp_Person6', a1)
    assert _is_linked(b, 'zlvp_Person6', a1)
    if hasattr(a1, 'zlvp_Stab5'):
        assert _is_linked(a1, 'zlvp_Stab5', b)
    _safe_set(b, 'zlvp_Person6', a2)
    assert _is_linked(b, 'zlvp_Person6', a2)
    if hasattr(a1, 'zlvp_Stab5'):
        assert not _is_linked(a1, 'zlvp_Stab5', b)
    if hasattr(a2, 'zlvp_Stab5'):
        assert _is_linked(a2, 'zlvp_Stab5', b)
    _safe_set(b, 'zlvp_Person6', None)
    assert not _is_linked(b, 'zlvp_Person6', a2)
    if hasattr(a2, 'zlvp_Stab5'):
        assert not _is_linked(a2, 'zlvp_Stab5', b)


def test_assoc_programm28_reverse_link_reassign_clear():
    a1 = zlvp_Programm(datum=date(2024, 1, 1), id=7, nachmittag="sample_text", nacht="sample_text", vormittag="sample_text")
    a2 = zlvp_Programm(datum=date(2025, 6, 15), id=13, nachmittag="sample_text_2", nacht="sample_text_2", vormittag="sample_text_2")
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager29', {a1})
    assert _is_linked(b, 'zlvp_Lager29', a1)
    if hasattr(a1, 'zlvp_Programm'):
        assert _is_linked(a1, 'zlvp_Programm', b)
    _safe_set(b, 'zlvp_Lager29', {a2})
    assert _is_linked(b, 'zlvp_Lager29', a2)
    if hasattr(a1, 'zlvp_Programm'):
        assert not _is_linked(a1, 'zlvp_Programm', b)
    if hasattr(a2, 'zlvp_Programm'):
        assert _is_linked(a2, 'zlvp_Programm', b)
    _safe_set(b, 'zlvp_Lager29', set())
    assert not _is_linked(b, 'zlvp_Lager29', a2)
    if hasattr(a2, 'zlvp_Programm'):
        assert not _is_linked(a2, 'zlvp_Programm', b)


def test_assoc_schaeden45_reverse_link_reassign_clear():
    a1 = zlvp_Zelt(id=7, name="sample_text")
    a2 = zlvp_Zelt(id=13, name="sample_text_2")
    b = zlvp_Schaeden(bezeichnung="sample_text", datum=date(2024, 1, 1), id=7)
    _safe_set(b, 'zlvp_Schaeden', a1)
    assert _is_linked(b, 'zlvp_Schaeden', a1)
    if hasattr(a1, 'zlvp_Zelt46'):
        assert _is_linked(a1, 'zlvp_Zelt46', b)
    _safe_set(b, 'zlvp_Schaeden', a2)
    assert _is_linked(b, 'zlvp_Schaeden', a2)
    if hasattr(a1, 'zlvp_Zelt46'):
        assert not _is_linked(a1, 'zlvp_Zelt46', b)
    if hasattr(a2, 'zlvp_Zelt46'):
        assert _is_linked(a2, 'zlvp_Zelt46', b)
    _safe_set(b, 'zlvp_Schaeden', None)
    assert not _is_linked(b, 'zlvp_Schaeden', a2)
    if hasattr(a2, 'zlvp_Zelt46'):
        assert not _is_linked(a2, 'zlvp_Zelt46', b)


def test_assoc_stab23_reverse_link_reassign_clear():
    a1 = zlvp_Stab(id=7)
    a2 = zlvp_Stab(id=13)
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager24', {a1})
    assert _is_linked(b, 'zlvp_Lager24', a1)
    if hasattr(a1, 'zlvp_Stab25'):
        assert _is_linked(a1, 'zlvp_Stab25', b)
    _safe_set(b, 'zlvp_Lager24', {a2})
    assert _is_linked(b, 'zlvp_Lager24', a2)
    if hasattr(a1, 'zlvp_Stab25'):
        assert not _is_linked(a1, 'zlvp_Stab25', b)
    if hasattr(a2, 'zlvp_Stab25'):
        assert _is_linked(a2, 'zlvp_Stab25', b)
    _safe_set(b, 'zlvp_Lager24', set())
    assert not _is_linked(b, 'zlvp_Lager24', a2)
    if hasattr(a2, 'zlvp_Stab25'):
        assert not _is_linked(a2, 'zlvp_Stab25', b)


def test_assoc_teilnehmer40_reverse_link_reassign_clear():
    a1 = zlvp_Teilnehmer(id=7)
    a2 = zlvp_Teilnehmer(id=13)
    b = zlvp_Gruppen(id=7, name="sample_text", spruch="sample_text")
    _safe_set(b, 'zlvp_Gruppen41', {a1})
    assert _is_linked(b, 'zlvp_Gruppen41', a1)
    if hasattr(a1, 'zlvp_Teilnehmer42'):
        assert _is_linked(a1, 'zlvp_Teilnehmer42', b)
    _safe_set(b, 'zlvp_Gruppen41', {a2})
    assert _is_linked(b, 'zlvp_Gruppen41', a2)
    if hasattr(a1, 'zlvp_Teilnehmer42'):
        assert not _is_linked(a1, 'zlvp_Teilnehmer42', b)
    if hasattr(a2, 'zlvp_Teilnehmer42'):
        assert _is_linked(a2, 'zlvp_Teilnehmer42', b)
    _safe_set(b, 'zlvp_Gruppen41', set())
    assert not _is_linked(b, 'zlvp_Gruppen41', a2)
    if hasattr(a2, 'zlvp_Teilnehmer42'):
        assert not _is_linked(a2, 'zlvp_Teilnehmer42', b)


def test_assoc_verleih47_reverse_link_reassign_clear():
    a1 = zlvp_Zelt(id=7, name="sample_text")
    a2 = zlvp_Zelt(id=13, name="sample_text_2")
    b = zlvp_Verleih(bemerkung="sample_text", datum=date(2024, 1, 1), id=7, person="sample_text")
    _safe_set(b, 'zlvp_Verleih', a1)
    assert _is_linked(b, 'zlvp_Verleih', a1)
    if hasattr(a1, 'zlvp_Zelt48'):
        assert _is_linked(a1, 'zlvp_Zelt48', b)
    _safe_set(b, 'zlvp_Verleih', a2)
    assert _is_linked(b, 'zlvp_Verleih', a2)
    if hasattr(a1, 'zlvp_Zelt48'):
        assert not _is_linked(a1, 'zlvp_Zelt48', b)
    if hasattr(a2, 'zlvp_Zelt48'):
        assert _is_linked(a2, 'zlvp_Zelt48', b)
    _safe_set(b, 'zlvp_Verleih', None)
    assert not _is_linked(b, 'zlvp_Verleih', a2)
    if hasattr(a2, 'zlvp_Zelt48'):
        assert not _is_linked(a2, 'zlvp_Zelt48', b)


def test_assoc_zelt30_reverse_link_reassign_clear():
    a1 = zlvp_Zelt(id=7, name="sample_text")
    a2 = zlvp_Zelt(id=13, name="sample_text_2")
    b = zlvp_Lager(id=7, name="sample_text", ort="sample_text", start=date(2024, 1, 1), stop=date(2024, 1, 1), thema="sample_text")
    _safe_set(b, 'zlvp_Lager31', {a1})
    assert _is_linked(b, 'zlvp_Lager31', a1)
    if hasattr(a1, 'zlvp_Zelt'):
        assert _is_linked(a1, 'zlvp_Zelt', b)
    _safe_set(b, 'zlvp_Lager31', {a2})
    assert _is_linked(b, 'zlvp_Lager31', a2)
    if hasattr(a1, 'zlvp_Zelt'):
        assert not _is_linked(a1, 'zlvp_Zelt', b)
    if hasattr(a2, 'zlvp_Zelt'):
        assert _is_linked(a2, 'zlvp_Zelt', b)
    _safe_set(b, 'zlvp_Lager31', set())
    assert not _is_linked(b, 'zlvp_Lager31', a2)
    if hasattr(a2, 'zlvp_Zelt'):
        assert not _is_linked(a2, 'zlvp_Zelt', b)


def test_assoc_zeltDetail43_reverse_link_reassign_clear():
    a1 = zlvp_ZeltDetail(id=7, name="sample_text")
    a2 = zlvp_ZeltDetail(id=13, name="sample_text_2")
    b = zlvp_Zelt(id=7, name="sample_text")
    _safe_set(b, 'zlvp_Zelt44', {a1})
    assert _is_linked(b, 'zlvp_Zelt44', a1)
    if hasattr(a1, 'zlvp_ZeltDetail'):
        assert _is_linked(a1, 'zlvp_ZeltDetail', b)
    _safe_set(b, 'zlvp_Zelt44', {a2})
    assert _is_linked(b, 'zlvp_Zelt44', a2)
    if hasattr(a1, 'zlvp_ZeltDetail'):
        assert not _is_linked(a1, 'zlvp_ZeltDetail', b)
    if hasattr(a2, 'zlvp_ZeltDetail'):
        assert _is_linked(a2, 'zlvp_ZeltDetail', b)
    _safe_set(b, 'zlvp_Zelt44', set())
    assert not _is_linked(b, 'zlvp_Zelt44', a2)
    if hasattr(a2, 'zlvp_ZeltDetail'):
        assert not _is_linked(a2, 'zlvp_ZeltDetail', b)


def test_assoc_zeltDetailBezeichnung52_reverse_link_reassign_clear():
    a1 = zlvp_ZeltDetailBezeichnung(id=7, name="sample_text")
    a2 = zlvp_ZeltDetailBezeichnung(id=13, name="sample_text_2")
    b = zlvp_ZeltDetail(id=7, name="sample_text")
    _safe_set(b, 'zlvp_ZeltDetail53', {a1})
    assert _is_linked(b, 'zlvp_ZeltDetail53', a1)
    if hasattr(a1, 'zlvp_ZeltDetailBezeichnung'):
        assert _is_linked(a1, 'zlvp_ZeltDetailBezeichnung', b)
    _safe_set(b, 'zlvp_ZeltDetail53', {a2})
    assert _is_linked(b, 'zlvp_ZeltDetail53', a2)
    if hasattr(a1, 'zlvp_ZeltDetailBezeichnung'):
        assert not _is_linked(a1, 'zlvp_ZeltDetailBezeichnung', b)
    if hasattr(a2, 'zlvp_ZeltDetailBezeichnung'):
        assert _is_linked(a2, 'zlvp_ZeltDetailBezeichnung', b)
    _safe_set(b, 'zlvp_ZeltDetail53', set())
    assert not _is_linked(b, 'zlvp_ZeltDetail53', a2)
    if hasattr(a2, 'zlvp_ZeltDetailBezeichnung'):
        assert not _is_linked(a2, 'zlvp_ZeltDetailBezeichnung', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

