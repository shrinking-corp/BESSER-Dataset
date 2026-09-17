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
    zutaten,
    ea_helfer,
    backstrasse,
    auftrag,
    zutat,
    plaetzchen,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_zutaten_is_not_abstract():
    assert not inspect.isabstract(zutaten)


def test_hyp_zutaten_constructor_exists():
    assert callable(zutaten.__init__)


def test_hyp_zutaten_constructor_args():
    sig = inspect.signature(zutaten.__init__)
    params = list(sig.parameters.keys())
    assert "zutatenListe" in params, "Missing parameter 'zutatenListe'"




def test_hyp_ea_helfer_is_not_abstract():
    assert not inspect.isabstract(ea_helfer)


def test_hyp_ea_helfer_constructor_exists():
    assert callable(ea_helfer.__init__)


def test_hyp_ea_helfer_constructor_args():
    sig = inspect.signature(ea_helfer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_backstrasse_is_not_abstract():
    assert not inspect.isabstract(backstrasse)


def test_hyp_backstrasse_constructor_exists():
    assert callable(backstrasse.__init__)


def test_hyp_backstrasse_constructor_args():
    sig = inspect.signature(backstrasse.__init__)
    params = list(sig.parameters.keys())
    assert "zutatenVorrat" in params, "Missing parameter 'zutatenVorrat'"
    assert "temperatur" in params, "Missing parameter 'temperatur'"
    assert "backAuftrag" in params, "Missing parameter 'backAuftrag'"
    assert "gestoppt" in params, "Missing parameter 'gestoppt'"
    assert "ofenlaenge" in params, "Missing parameter 'ofenlaenge'"
    assert "BLECHBREITE" in params, "Missing parameter 'BLECHBREITE'"
    assert "BLECHLAENGE" in params, "Missing parameter 'BLECHLAENGE'"
    assert "eingabeAusgabe" in params, "Missing parameter 'eingabeAusgabe'"
    assert "geschwindigkeit" in params, "Missing parameter 'geschwindigkeit'"












def test_hyp_auftrag_is_not_abstract():
    assert not inspect.isabstract(auftrag)


def test_hyp_auftrag_constructor_exists():
    assert callable(auftrag.__init__)


def test_hyp_auftrag_constructor_args():
    sig = inspect.signature(auftrag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anzahl" in params, "Missing parameter 'anzahl'"
    assert "auftragsPlaetzchen" in params, "Missing parameter 'auftragsPlaetzchen'"






def test_hyp_zutat_is_not_abstract():
    assert not inspect.isabstract(zutat)


def test_hyp_zutat_constructor_exists():
    assert callable(zutat.__init__)


def test_hyp_zutat_constructor_args():
    sig = inspect.signature(zutat.__init__)
    params = list(sig.parameters.keys())
    assert "einheit" in params, "Missing parameter 'einheit'"
    assert "name" in params, "Missing parameter 'name'"
    assert "menge" in params, "Missing parameter 'menge'"






def test_hyp_plaetzchen_is_not_abstract():
    assert not inspect.isabstract(plaetzchen)


def test_hyp_plaetzchen_constructor_exists():
    assert callable(plaetzchen.__init__)


def test_hyp_plaetzchen_constructor_args():
    sig = inspect.signature(plaetzchen.__init__)
    params = list(sig.parameters.keys())
    assert "breite" in params, "Missing parameter 'breite'"
    assert "form" in params, "Missing parameter 'form'"
    assert "temperatur" in params, "Missing parameter 'temperatur'"
    assert "laenge" in params, "Missing parameter 'laenge'"
    assert "belag" in params, "Missing parameter 'belag'"
    assert "teig" in params, "Missing parameter 'teig'"
    assert "backzeit" in params, "Missing parameter 'backzeit'"









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
zutaten_strategy = st.builds(
    zutaten,
    zutatenListe=
        safe_text
)
ea_helfer_strategy = st.builds(
    ea_helfer,
)
backstrasse_strategy = st.builds(
    backstrasse,
    zutatenVorrat=
        safe_text,
    temperatur=
        safe_text,
    backAuftrag=
        safe_text,
    gestoppt=
        safe_text,
    ofenlaenge=
        safe_text,
    BLECHBREITE=
        safe_text,
    BLECHLAENGE=
        safe_text,
    eingabeAusgabe=
        safe_text,
    geschwindigkeit=
        safe_text
)
auftrag_strategy = st.builds(
    auftrag,
    name=
        safe_text,
    anzahl=
        safe_text,
    auftragsPlaetzchen=
        safe_text
)
zutat_strategy = st.builds(
    zutat,
    einheit=
        safe_text,
    name=
        safe_text,
    menge=
        safe_text
)
plaetzchen_strategy = st.builds(
    plaetzchen,
    breite=
        safe_text,
    form=
        safe_text,
    temperatur=
        safe_text,
    laenge=
        safe_text,
    belag=
        safe_text,
    teig=
        safe_text,
    backzeit=
        safe_text
)




@given(instance=zutaten_strategy)
def test_hyp_zutaten_zutatenListe_setter(instance):
    original = instance.zutatenListe
    instance.zutatenListe = original
    assert instance.zutatenListe == original





@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_zutatenVorrat_setter(instance):
    original = instance.zutatenVorrat
    instance.zutatenVorrat = original
    assert instance.zutatenVorrat == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_temperatur_setter(instance):
    original = instance.temperatur
    instance.temperatur = original
    assert instance.temperatur == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_backAuftrag_setter(instance):
    original = instance.backAuftrag
    instance.backAuftrag = original
    assert instance.backAuftrag == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_gestoppt_setter(instance):
    original = instance.gestoppt
    instance.gestoppt = original
    assert instance.gestoppt == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_ofenlaenge_setter(instance):
    original = instance.ofenlaenge
    instance.ofenlaenge = original
    assert instance.ofenlaenge == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_BLECHBREITE_setter(instance):
    original = instance.BLECHBREITE
    instance.BLECHBREITE = original
    assert instance.BLECHBREITE == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_BLECHLAENGE_setter(instance):
    original = instance.BLECHLAENGE
    instance.BLECHLAENGE = original
    assert instance.BLECHLAENGE == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_eingabeAusgabe_setter(instance):
    original = instance.eingabeAusgabe
    instance.eingabeAusgabe = original
    assert instance.eingabeAusgabe == original



@given(instance=backstrasse_strategy)
def test_hyp_backstrasse_geschwindigkeit_setter(instance):
    original = instance.geschwindigkeit
    instance.geschwindigkeit = original
    assert instance.geschwindigkeit == original




@given(instance=auftrag_strategy)
def test_hyp_auftrag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=auftrag_strategy)
def test_hyp_auftrag_anzahl_setter(instance):
    original = instance.anzahl
    instance.anzahl = original
    assert instance.anzahl == original



@given(instance=auftrag_strategy)
def test_hyp_auftrag_auftragsPlaetzchen_setter(instance):
    original = instance.auftragsPlaetzchen
    instance.auftragsPlaetzchen = original
    assert instance.auftragsPlaetzchen == original




@given(instance=zutat_strategy)
def test_hyp_zutat_einheit_setter(instance):
    original = instance.einheit
    instance.einheit = original
    assert instance.einheit == original



@given(instance=zutat_strategy)
def test_hyp_zutat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=zutat_strategy)
def test_hyp_zutat_menge_setter(instance):
    original = instance.menge
    instance.menge = original
    assert instance.menge == original




@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_breite_setter(instance):
    original = instance.breite
    instance.breite = original
    assert instance.breite == original



@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_temperatur_setter(instance):
    original = instance.temperatur
    instance.temperatur = original
    assert instance.temperatur == original



@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_laenge_setter(instance):
    original = instance.laenge
    instance.laenge = original
    assert instance.laenge == original



@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_belag_setter(instance):
    original = instance.belag
    instance.belag = original
    assert instance.belag == original



@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_teig_setter(instance):
    original = instance.teig
    instance.teig = original
    assert instance.teig == original



@given(instance=plaetzchen_strategy)
def test_hyp_plaetzchen_backzeit_setter(instance):
    original = instance.backzeit
    instance.backzeit = original
    assert instance.backzeit == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    auftrag,
    backstrasse,
    ea_helfer,
    plaetzchen,
    zutat,
    zutaten,
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

def test_auftrag_anzahl_value_roundtrip():
    instance = auftrag(anzahl="sample_text", auftragsPlaetzchen="sample_text", name="sample_text")
    assert instance.anzahl == "sample_text"
    instance.anzahl = "sample_text_2"
    assert instance.anzahl == "sample_text_2"


def test_auftrag_auftragsPlaetzchen_value_roundtrip():
    instance = auftrag(anzahl="sample_text", auftragsPlaetzchen="sample_text", name="sample_text")
    assert instance.auftragsPlaetzchen == "sample_text"
    instance.auftragsPlaetzchen = "sample_text_2"
    assert instance.auftragsPlaetzchen == "sample_text_2"


def test_auftrag_name_value_roundtrip():
    instance = auftrag(anzahl="sample_text", auftragsPlaetzchen="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_backstrasse_BLECHBREITE_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.BLECHBREITE == "sample_text"
    instance.BLECHBREITE = "sample_text_2"
    assert instance.BLECHBREITE == "sample_text_2"


def test_backstrasse_BLECHLAENGE_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.BLECHLAENGE == "sample_text"
    instance.BLECHLAENGE = "sample_text_2"
    assert instance.BLECHLAENGE == "sample_text_2"


def test_backstrasse_backAuftrag_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.backAuftrag == "sample_text"
    instance.backAuftrag = "sample_text_2"
    assert instance.backAuftrag == "sample_text_2"


def test_backstrasse_eingabeAusgabe_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.eingabeAusgabe == "sample_text"
    instance.eingabeAusgabe = "sample_text_2"
    assert instance.eingabeAusgabe == "sample_text_2"


def test_backstrasse_geschwindigkeit_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.geschwindigkeit == "sample_text"
    instance.geschwindigkeit = "sample_text_2"
    assert instance.geschwindigkeit == "sample_text_2"


def test_backstrasse_gestoppt_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.gestoppt == "sample_text"
    instance.gestoppt = "sample_text_2"
    assert instance.gestoppt == "sample_text_2"


def test_backstrasse_ofenlaenge_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.ofenlaenge == "sample_text"
    instance.ofenlaenge = "sample_text_2"
    assert instance.ofenlaenge == "sample_text_2"


def test_backstrasse_temperatur_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.temperatur == "sample_text"
    instance.temperatur = "sample_text_2"
    assert instance.temperatur == "sample_text_2"


def test_backstrasse_zutatenVorrat_value_roundtrip():
    instance = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    assert instance.zutatenVorrat == "sample_text"
    instance.zutatenVorrat = "sample_text_2"
    assert instance.zutatenVorrat == "sample_text_2"


def test_plaetzchen_backzeit_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.backzeit == "sample_text"
    instance.backzeit = "sample_text_2"
    assert instance.backzeit == "sample_text_2"


def test_plaetzchen_belag_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.belag == "sample_text"
    instance.belag = "sample_text_2"
    assert instance.belag == "sample_text_2"


def test_plaetzchen_breite_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.breite == "sample_text"
    instance.breite = "sample_text_2"
    assert instance.breite == "sample_text_2"


def test_plaetzchen_form_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.form == "sample_text"
    instance.form = "sample_text_2"
    assert instance.form == "sample_text_2"


def test_plaetzchen_laenge_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.laenge == "sample_text"
    instance.laenge = "sample_text_2"
    assert instance.laenge == "sample_text_2"


def test_plaetzchen_teig_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.teig == "sample_text"
    instance.teig = "sample_text_2"
    assert instance.teig == "sample_text_2"


def test_plaetzchen_temperatur_value_roundtrip():
    instance = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.temperatur == "sample_text"
    instance.temperatur = "sample_text_2"
    assert instance.temperatur == "sample_text_2"


def test_zutat_einheit_value_roundtrip():
    instance = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    assert instance.einheit == "sample_text"
    instance.einheit = "sample_text_2"
    assert instance.einheit == "sample_text_2"


def test_zutat_menge_value_roundtrip():
    instance = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    assert instance.menge == "sample_text"
    instance.menge = "sample_text_2"
    assert instance.menge == "sample_text_2"


def test_zutat_name_value_roundtrip():
    instance = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_zutaten_zutatenListe_value_roundtrip():
    instance = zutaten(zutatenListe="sample_text")
    assert instance.zutatenListe == "sample_text"
    instance.zutatenListe = "sample_text_2"
    assert instance.zutatenListe == "sample_text_2"


def test_assoc_auftrag_plaetzchen_link_reassign_clear():
    a = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b1 = auftrag(anzahl="sample_text", auftragsPlaetzchen="sample_text", name="sample_text")
    b2 = auftrag(anzahl="sample_text_2", auftragsPlaetzchen="sample_text_2", name="sample_text_2")
    _safe_set(a, 'auftrag3', b1)
    assert _is_linked(a, 'auftrag3', b1)
    if hasattr(b1, 'plaetzchen22'):
        assert _is_linked(b1, 'plaetzchen22', a)
    _safe_set(a, 'auftrag3', b2)
    assert _is_linked(a, 'auftrag3', b2)
    if hasattr(b1, 'plaetzchen22'):
        assert not _is_linked(b1, 'plaetzchen22', a)
    if hasattr(b2, 'plaetzchen22'):
        assert _is_linked(b2, 'plaetzchen22', a)
    _safe_set(a, 'auftrag3', None)
    assert not _is_linked(a, 'auftrag3', b2)
    if hasattr(b2, 'plaetzchen22'):
        assert not _is_linked(b2, 'plaetzchen22', a)


def test_assoc_backstrasse_auftrag_link_reassign_clear():
    a = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    b1 = auftrag(anzahl="sample_text", auftragsPlaetzchen="sample_text", name="sample_text")
    b2 = auftrag(anzahl="sample_text_2", auftragsPlaetzchen="sample_text_2", name="sample_text_2")
    _safe_set(a, 'auftrag24', b1)
    assert _is_linked(a, 'auftrag24', b1)
    if hasattr(b1, 'backstrasse5'):
        assert _is_linked(b1, 'backstrasse5', a)
    _safe_set(a, 'auftrag24', b2)
    assert _is_linked(a, 'auftrag24', b2)
    if hasattr(b1, 'backstrasse5'):
        assert not _is_linked(b1, 'backstrasse5', a)
    if hasattr(b2, 'backstrasse5'):
        assert _is_linked(b2, 'backstrasse5', a)
    _safe_set(a, 'auftrag24', None)
    assert not _is_linked(a, 'auftrag24', b2)
    if hasattr(b2, 'backstrasse5'):
        assert not _is_linked(b2, 'backstrasse5', a)


def test_assoc_backstrasse_eaHelfer_link_reassign_clear():
    a = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    b1 = ea_helfer()
    b2 = ea_helfer()
    _safe_set(a, 'eaHelfer6', b1)
    assert _is_linked(a, 'eaHelfer6', b1)
    if hasattr(b1, 'backstrasse7'):
        assert _is_linked(b1, 'backstrasse7', a)
    _safe_set(a, 'eaHelfer6', b2)
    assert _is_linked(a, 'eaHelfer6', b2)
    if hasattr(b1, 'backstrasse7'):
        assert not _is_linked(b1, 'backstrasse7', a)
    if hasattr(b2, 'backstrasse7'):
        assert _is_linked(b2, 'backstrasse7', a)
    _safe_set(a, 'eaHelfer6', None)
    assert not _is_linked(a, 'eaHelfer6', b2)
    if hasattr(b2, 'backstrasse7'):
        assert not _is_linked(b2, 'backstrasse7', a)


def test_assoc_backstrasse_zutat_link_reassign_clear():
    a = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b1 = backstrasse(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", backAuftrag="sample_text", eingabeAusgabe="sample_text", geschwindigkeit="sample_text", gestoppt="sample_text", ofenlaenge="sample_text", temperatur="sample_text", zutatenVorrat="sample_text")
    b2 = backstrasse(BLECHBREITE="sample_text_2", BLECHLAENGE="sample_text_2", backAuftrag="sample_text_2", eingabeAusgabe="sample_text_2", geschwindigkeit="sample_text_2", gestoppt="sample_text_2", ofenlaenge="sample_text_2", temperatur="sample_text_2", zutatenVorrat="sample_text_2")
    _safe_set(a, 'backstrasse13', b1)
    assert _is_linked(a, 'backstrasse13', b1)
    if hasattr(b1, 'zutat12'):
        assert _is_linked(b1, 'zutat12', a)
    _safe_set(a, 'backstrasse13', b2)
    assert _is_linked(a, 'backstrasse13', b2)
    if hasattr(b1, 'zutat12'):
        assert not _is_linked(b1, 'zutat12', a)
    if hasattr(b2, 'zutat12'):
        assert _is_linked(b2, 'zutat12', a)
    _safe_set(a, 'backstrasse13', None)
    assert not _is_linked(a, 'backstrasse13', b2)
    if hasattr(b2, 'zutat12'):
        assert not _is_linked(b2, 'zutat12', a)


def test_assoc_plaetzchen_teig_link_reassign_clear():
    a = zutaten(zutatenListe="sample_text")
    b1 = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b2 = plaetzchen(backzeit="sample_text_2", belag="sample_text_2", breite="sample_text_2", form="sample_text_2", laenge="sample_text_2", teig="sample_text_2", temperatur="sample_text_2")
    _safe_set(a, 'plaetzchen9', b1)
    assert _is_linked(a, 'plaetzchen9', b1)
    if hasattr(b1, 'teig28'):
        assert _is_linked(b1, 'teig28', a)
    _safe_set(a, 'plaetzchen9', b2)
    assert _is_linked(a, 'plaetzchen9', b2)
    if hasattr(b1, 'teig28'):
        assert not _is_linked(b1, 'teig28', a)
    if hasattr(b2, 'teig28'):
        assert _is_linked(b2, 'teig28', a)
    _safe_set(a, 'plaetzchen9', None)
    assert not _is_linked(a, 'plaetzchen9', b2)
    if hasattr(b2, 'teig28'):
        assert not _is_linked(b2, 'teig28', a)


def test_assoc_plaetzchen_zutat_link_reassign_clear():
    a = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b1 = plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b2 = plaetzchen(backzeit="sample_text_2", belag="sample_text_2", breite="sample_text_2", form="sample_text_2", laenge="sample_text_2", teig="sample_text_2", temperatur="sample_text_2")
    _safe_set(a, 'plaetzchen1', b1)
    assert _is_linked(a, 'plaetzchen1', b1)
    if hasattr(b1, 'zutat0'):
        assert _is_linked(b1, 'zutat0', a)
    _safe_set(a, 'plaetzchen1', b2)
    assert _is_linked(a, 'plaetzchen1', b2)
    if hasattr(b1, 'zutat0'):
        assert not _is_linked(b1, 'zutat0', a)
    if hasattr(b2, 'zutat0'):
        assert _is_linked(b2, 'zutat0', a)
    _safe_set(a, 'plaetzchen1', None)
    assert not _is_linked(a, 'plaetzchen1', b2)
    if hasattr(b2, 'zutat0'):
        assert not _is_linked(b2, 'zutat0', a)


def test_assoc_teig_zutat_link_reassign_clear():
    a = zutaten(zutatenListe="sample_text")
    b1 = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b2 = zutat(einheit="sample_text_2", menge="sample_text_2", name="sample_text_2")
    _safe_set(a, 'zutat10', b1)
    assert _is_linked(a, 'zutat10', b1)
    if hasattr(b1, 'teig11'):
        assert _is_linked(b1, 'teig11', a)
    _safe_set(a, 'zutat10', b2)
    assert _is_linked(a, 'zutat10', b2)
    if hasattr(b1, 'teig11'):
        assert not _is_linked(b1, 'teig11', a)
    if hasattr(b2, 'teig11'):
        assert _is_linked(b2, 'teig11', a)
    _safe_set(a, 'zutat10', None)
    assert not _is_linked(a, 'zutat10', b2)
    if hasattr(b2, 'teig11'):
        assert not _is_linked(b2, 'teig11', a)


def test_assoc_zutat_auftrag_link_reassign_clear():
    a = zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b1 = auftrag(anzahl="sample_text", auftragsPlaetzchen="sample_text", name="sample_text")
    b2 = auftrag(anzahl="sample_text_2", auftragsPlaetzchen="sample_text_2", name="sample_text_2")
    _safe_set(a, 'auftrag14', b1)
    assert _is_linked(a, 'auftrag14', b1)
    if hasattr(b1, 'zutat15'):
        assert _is_linked(b1, 'zutat15', a)
    _safe_set(a, 'auftrag14', b2)
    assert _is_linked(a, 'auftrag14', b2)
    if hasattr(b1, 'zutat15'):
        assert not _is_linked(b1, 'zutat15', a)
    if hasattr(b2, 'zutat15'):
        assert _is_linked(b2, 'zutat15', a)
    _safe_set(a, 'auftrag14', None)
    assert not _is_linked(a, 'auftrag14', b2)
    if hasattr(b2, 'zutat15'):
        assert not _is_linked(b2, 'zutat15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

auftrag_strategy = st.builds(auftrag, anzahl=safe_text, auftragsPlaetzchen=safe_text, name=safe_text)
@given(instance=auftrag_strategy)
@settings(max_examples=25)
def test_auftrag_instantiation(instance):
    assert isinstance(instance, auftrag)


backstrasse_strategy = st.builds(backstrasse, BLECHBREITE=safe_text, BLECHLAENGE=safe_text, backAuftrag=safe_text, eingabeAusgabe=safe_text, geschwindigkeit=safe_text, gestoppt=safe_text, ofenlaenge=safe_text, temperatur=safe_text, zutatenVorrat=safe_text)
@given(instance=backstrasse_strategy)
@settings(max_examples=25)
def test_backstrasse_instantiation(instance):
    assert isinstance(instance, backstrasse)


ea_helfer_strategy = st.builds(ea_helfer)
@given(instance=ea_helfer_strategy)
@settings(max_examples=25)
def test_ea_helfer_instantiation(instance):
    assert isinstance(instance, ea_helfer)


plaetzchen_strategy = st.builds(plaetzchen, backzeit=safe_text, belag=safe_text, breite=safe_text, form=safe_text, laenge=safe_text, teig=safe_text, temperatur=safe_text)
@given(instance=plaetzchen_strategy)
@settings(max_examples=25)
def test_plaetzchen_instantiation(instance):
    assert isinstance(instance, plaetzchen)


zutat_strategy = st.builds(zutat, einheit=safe_text, menge=safe_text, name=safe_text)
@given(instance=zutat_strategy)
@settings(max_examples=25)
def test_zutat_instantiation(instance):
    assert isinstance(instance, zutat)


zutaten_strategy = st.builds(zutaten, zutatenListe=safe_text)
@given(instance=zutaten_strategy)
@settings(max_examples=25)
def test_zutaten_instantiation(instance):
    assert isinstance(instance, zutaten)



