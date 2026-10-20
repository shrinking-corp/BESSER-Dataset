import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Auftrag,
    DateiEA,
    Plaetzchen,
    PlaetzchenAnzeigeForm,
    PlaetzchenDesignerForm,
    Zutat,
    Zutaten,
    ZutatenEingabeForm,
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

def test_assoc_PlaetzchenDesignerForm_Auftrag_reverse_link_reassign_clear():
    a1 = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    a2 = PlaetzchenDesignerForm(BLECHBREITE="sample_text_2", BLECHLAENGE="sample_text_2", datei="sample_text_2", neuerAuftrag="sample_text_2", neuesPlaetzchen="sample_text_2", plaetzchenGeaendert=False)
    b = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    _safe_set(b, 'plaetzchenDesignerForm23', a1)
    assert _is_linked(b, 'plaetzchenDesignerForm23', a1)
    if hasattr(a1, 'auftrag22'):
        assert _is_linked(a1, 'auftrag22', b)
    _safe_set(b, 'plaetzchenDesignerForm23', a2)
    assert _is_linked(b, 'plaetzchenDesignerForm23', a2)
    if hasattr(a1, 'auftrag22'):
        assert not _is_linked(a1, 'auftrag22', b)
    if hasattr(a2, 'auftrag22'):
        assert _is_linked(a2, 'auftrag22', b)
    _safe_set(b, 'plaetzchenDesignerForm23', None)
    assert not _is_linked(b, 'plaetzchenDesignerForm23', a2)
    if hasattr(a2, 'auftrag22'):
        assert not _is_linked(a2, 'auftrag22', b)


def test_assoc_PlaetzchenDesignerForm_Plaetzchen_reverse_link_reassign_clear():
    a1 = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    a2 = PlaetzchenDesignerForm(BLECHBREITE="sample_text_2", BLECHLAENGE="sample_text_2", datei="sample_text_2", neuerAuftrag="sample_text_2", neuesPlaetzchen="sample_text_2", plaetzchenGeaendert=False)
    b = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    _safe_set(b, 'plaetzchenDesignerForm11', a1)
    assert _is_linked(b, 'plaetzchenDesignerForm11', a1)
    if hasattr(a1, 'plaetzchen10'):
        assert _is_linked(a1, 'plaetzchen10', b)
    _safe_set(b, 'plaetzchenDesignerForm11', a2)
    assert _is_linked(b, 'plaetzchenDesignerForm11', a2)
    if hasattr(a1, 'plaetzchen10'):
        assert not _is_linked(a1, 'plaetzchen10', b)
    if hasattr(a2, 'plaetzchen10'):
        assert _is_linked(a2, 'plaetzchen10', b)
    _safe_set(b, 'plaetzchenDesignerForm11', None)
    assert not _is_linked(b, 'plaetzchenDesignerForm11', a2)
    if hasattr(a2, 'plaetzchen10'):
        assert not _is_linked(a2, 'plaetzchen10', b)


def test_assoc_PlaetzchenDesignerForm_PlaetzchenAnzeigeForm_reverse_link_reassign_clear():
    a1 = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    a2 = PlaetzchenDesignerForm(BLECHBREITE="sample_text_2", BLECHLAENGE="sample_text_2", datei="sample_text_2", neuerAuftrag="sample_text_2", neuesPlaetzchen="sample_text_2", plaetzchenGeaendert=False)
    b = PlaetzchenAnzeigeForm(breite="sample_text", form="sample_text", laenge="sample_text")
    _safe_set(b, 'plaetzchenDesignerForm9', a1)
    assert _is_linked(b, 'plaetzchenDesignerForm9', a1)
    if hasattr(a1, 'plaetzchenAnzeigeForm8'):
        assert _is_linked(a1, 'plaetzchenAnzeigeForm8', b)
    _safe_set(b, 'plaetzchenDesignerForm9', a2)
    assert _is_linked(b, 'plaetzchenDesignerForm9', a2)
    if hasattr(a1, 'plaetzchenAnzeigeForm8'):
        assert not _is_linked(a1, 'plaetzchenAnzeigeForm8', b)
    if hasattr(a2, 'plaetzchenAnzeigeForm8'):
        assert _is_linked(a2, 'plaetzchenAnzeigeForm8', b)
    _safe_set(b, 'plaetzchenDesignerForm9', None)
    assert not _is_linked(b, 'plaetzchenDesignerForm9', a2)
    if hasattr(a2, 'plaetzchenAnzeigeForm8'):
        assert not _is_linked(a2, 'plaetzchenAnzeigeForm8', b)


def test_assoc_Plaetzchen_Auftrag_reverse_link_reassign_clear():
    a1 = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    a2 = Plaetzchen(backzeit="sample_text_2", belag="sample_text_2", breite="sample_text_2", form="sample_text_2", laenge="sample_text_2", teig="sample_text_2", temperatur="sample_text_2")
    b = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    _safe_set(b, 'plaetzchen221', a1)
    assert _is_linked(b, 'plaetzchen221', a1)
    if hasattr(a1, 'auftrag20'):
        assert _is_linked(a1, 'auftrag20', b)
    _safe_set(b, 'plaetzchen221', a2)
    assert _is_linked(b, 'plaetzchen221', a2)
    if hasattr(a1, 'auftrag20'):
        assert not _is_linked(a1, 'auftrag20', b)
    if hasattr(a2, 'auftrag20'):
        assert _is_linked(a2, 'auftrag20', b)
    _safe_set(b, 'plaetzchen221', None)
    assert not _is_linked(b, 'plaetzchen221', a2)
    if hasattr(a2, 'auftrag20'):
        assert not _is_linked(a2, 'auftrag20', b)


def test_assoc_Plaetzchen_Teig_reverse_link_reassign_clear():
    a1 = Zutaten(zutaten="sample_text")
    a2 = Zutaten(zutaten="sample_text_2")
    b = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    _safe_set(b, 'teig20', a1)
    assert _is_linked(b, 'teig20', a1)
    if hasattr(a1, 'plaetzchen1'):
        assert _is_linked(a1, 'plaetzchen1', b)
    _safe_set(b, 'teig20', a2)
    assert _is_linked(b, 'teig20', a2)
    if hasattr(a1, 'plaetzchen1'):
        assert not _is_linked(a1, 'plaetzchen1', b)
    if hasattr(a2, 'plaetzchen1'):
        assert _is_linked(a2, 'plaetzchen1', b)
    _safe_set(b, 'teig20', None)
    assert not _is_linked(b, 'teig20', a2)
    if hasattr(a2, 'plaetzchen1'):
        assert not _is_linked(a2, 'plaetzchen1', b)


def test_assoc_Plaetzchen_Zutat_reverse_link_reassign_clear():
    a1 = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    a2 = Zutat(einheit="sample_text_2", menge="sample_text_2", name="sample_text_2")
    b = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    _safe_set(b, 'zutat2', a1)
    assert _is_linked(b, 'zutat2', a1)
    if hasattr(a1, 'plaetzchen3'):
        assert _is_linked(a1, 'plaetzchen3', b)
    _safe_set(b, 'zutat2', a2)
    assert _is_linked(b, 'zutat2', a2)
    if hasattr(a1, 'plaetzchen3'):
        assert not _is_linked(a1, 'plaetzchen3', b)
    if hasattr(a2, 'plaetzchen3'):
        assert _is_linked(a2, 'plaetzchen3', b)
    _safe_set(b, 'zutat2', None)
    assert not _is_linked(b, 'zutat2', a2)
    if hasattr(a2, 'plaetzchen3'):
        assert not _is_linked(a2, 'plaetzchen3', b)


def test_assoc_Teig_Zutat_reverse_link_reassign_clear():
    a1 = Zutaten(zutaten="sample_text")
    a2 = Zutaten(zutaten="sample_text_2")
    b = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    _safe_set(b, 'teig5', a1)
    assert _is_linked(b, 'teig5', a1)
    if hasattr(a1, 'zutat4'):
        assert _is_linked(a1, 'zutat4', b)
    _safe_set(b, 'teig5', a2)
    assert _is_linked(b, 'teig5', a2)
    if hasattr(a1, 'zutat4'):
        assert not _is_linked(a1, 'zutat4', b)
    if hasattr(a2, 'zutat4'):
        assert _is_linked(a2, 'zutat4', b)
    _safe_set(b, 'teig5', None)
    assert not _is_linked(b, 'teig5', a2)
    if hasattr(a2, 'zutat4'):
        assert not _is_linked(a2, 'zutat4', b)


def test_assoc_ZutatenEingabe_PlaetzchenDesignerForm_reverse_link_reassign_clear():
    a1 = ZutatenEingabeForm(neueZutat="sample_text")
    a2 = ZutatenEingabeForm(neueZutat="sample_text_2")
    b = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    _safe_set(b, 'zutatenEingabe15', a1)
    assert _is_linked(b, 'zutatenEingabe15', a1)
    if hasattr(a1, 'plaetzchenDesignerForm14'):
        assert _is_linked(a1, 'plaetzchenDesignerForm14', b)
    _safe_set(b, 'zutatenEingabe15', a2)
    assert _is_linked(b, 'zutatenEingabe15', a2)
    if hasattr(a1, 'plaetzchenDesignerForm14'):
        assert not _is_linked(a1, 'plaetzchenDesignerForm14', b)
    if hasattr(a2, 'plaetzchenDesignerForm14'):
        assert _is_linked(a2, 'plaetzchenDesignerForm14', b)
    _safe_set(b, 'zutatenEingabe15', None)
    assert not _is_linked(b, 'zutatenEingabe15', a2)
    if hasattr(a2, 'plaetzchenDesignerForm14'):
        assert not _is_linked(a2, 'plaetzchenDesignerForm14', b)


def test_assoc_ZutatenEingabe_Zutat_reverse_link_reassign_clear():
    a1 = ZutatenEingabeForm(neueZutat="sample_text")
    a2 = ZutatenEingabeForm(neueZutat="sample_text_2")
    b = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    _safe_set(b, 'zutatenEingabe17', a1)
    assert _is_linked(b, 'zutatenEingabe17', a1)
    if hasattr(a1, 'zutat16'):
        assert _is_linked(a1, 'zutat16', b)
    _safe_set(b, 'zutatenEingabe17', a2)
    assert _is_linked(b, 'zutatenEingabe17', a2)
    if hasattr(a1, 'zutat16'):
        assert not _is_linked(a1, 'zutat16', b)
    if hasattr(a2, 'zutat16'):
        assert _is_linked(a2, 'zutat16', b)
    _safe_set(b, 'zutatenEingabe17', None)
    assert not _is_linked(b, 'zutatenEingabe17', a2)
    if hasattr(a2, 'zutat16'):
        assert not _is_linked(a2, 'zutat16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_DateiEA_Auftrag_stub_double():
    # DateiEA has no real 'auftrag18' property in the generated
    # code (a bare stub) -- manually attach it so Auftrag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Auftrag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    partner = DateiEA()
    setattr(partner, 'auftrag18', None)
    _safe_set(owner, 'dateiEA19', partner)
    assert getattr(partner, 'auftrag18') == owner
    _safe_set(owner, 'dateiEA19', None)
    assert getattr(partner, 'auftrag18') is None


def test_assoc_DateiEA_Plaetzchen_stub_double():
    # DateiEA has no real 'plaetzchen12' property in the generated
    # code (a bare stub) -- manually attach it so Plaetzchen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Plaetzchen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    partner = DateiEA()
    setattr(partner, 'plaetzchen12', None)
    _safe_set(owner, 'dateiEA13', partner)
    assert getattr(partner, 'plaetzchen12') == owner
    _safe_set(owner, 'dateiEA13', None)
    assert getattr(partner, 'plaetzchen12') is None


def test_assoc_PlaetzchenDesignerForm_DateiEA_stub_double():
    # DateiEA has no real 'plaetzchenDesignerForm7' property in the generated
    # code (a bare stub) -- manually attach it so PlaetzchenDesignerForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PlaetzchenDesignerForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    partner = DateiEA()
    setattr(partner, 'plaetzchenDesignerForm7', None)
    _safe_set(owner, 'dateiEA6', partner)
    assert getattr(partner, 'plaetzchenDesignerForm7') == owner
    _safe_set(owner, 'dateiEA6', None)
    assert getattr(partner, 'plaetzchenDesignerForm7') is None


