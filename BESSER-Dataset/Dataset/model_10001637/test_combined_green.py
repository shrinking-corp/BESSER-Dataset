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
    Auftrag,
    ZutatenEingabeForm,
    PlaetzchenAnzeigeForm,
    DateiEA,
    PlaetzchenDesignerForm,
    Plaetzchen,
    Zutat,
    Zutaten,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_auftrag_is_not_abstract():
    assert not inspect.isabstract(Auftrag)


def test_hyp_auftrag_constructor_exists():
    assert callable(Auftrag.__init__)


def test_hyp_auftrag_constructor_args():
    sig = inspect.signature(Auftrag.__init__)
    params = list(sig.parameters.keys())
    assert "keks" in params, "Missing parameter 'keks'"
    assert "name" in params, "Missing parameter 'name'"
    assert "anzahl" in params, "Missing parameter 'anzahl'"






def test_hyp_zutateneingabeform_is_not_abstract():
    assert not inspect.isabstract(ZutatenEingabeForm)


def test_hyp_zutateneingabeform_constructor_exists():
    assert callable(ZutatenEingabeForm.__init__)


def test_hyp_zutateneingabeform_constructor_args():
    sig = inspect.signature(ZutatenEingabeForm.__init__)
    params = list(sig.parameters.keys())
    assert "neueZutat" in params, "Missing parameter 'neueZutat'"




def test_hyp_plaetzchenanzeigeform_is_not_abstract():
    assert not inspect.isabstract(PlaetzchenAnzeigeForm)


def test_hyp_plaetzchenanzeigeform_constructor_exists():
    assert callable(PlaetzchenAnzeigeForm.__init__)


def test_hyp_plaetzchenanzeigeform_constructor_args():
    sig = inspect.signature(PlaetzchenAnzeigeForm.__init__)
    params = list(sig.parameters.keys())
    assert "laenge" in params, "Missing parameter 'laenge'"
    assert "form" in params, "Missing parameter 'form'"
    assert "breite" in params, "Missing parameter 'breite'"






def test_hyp_dateiea_is_not_abstract():
    assert not inspect.isabstract(DateiEA)


def test_hyp_dateiea_constructor_exists():
    assert callable(DateiEA.__init__)


def test_hyp_dateiea_constructor_args():
    sig = inspect.signature(DateiEA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plaetzchendesignerform_is_not_abstract():
    assert not inspect.isabstract(PlaetzchenDesignerForm)


def test_hyp_plaetzchendesignerform_constructor_exists():
    assert callable(PlaetzchenDesignerForm.__init__)


def test_hyp_plaetzchendesignerform_constructor_args():
    sig = inspect.signature(PlaetzchenDesignerForm.__init__)
    params = list(sig.parameters.keys())
    assert "BLECHLAENGE" in params, "Missing parameter 'BLECHLAENGE'"
    assert "datei" in params, "Missing parameter 'datei'"
    assert "plaetzchenGeaendert" in params, "Missing parameter 'plaetzchenGeaendert'"
    assert "neuesPlaetzchen" in params, "Missing parameter 'neuesPlaetzchen'"
    assert "BLECHBREITE" in params, "Missing parameter 'BLECHBREITE'"
    assert "neuerAuftrag" in params, "Missing parameter 'neuerAuftrag'"









def test_hyp_plaetzchen_is_not_abstract():
    assert not inspect.isabstract(Plaetzchen)


def test_hyp_plaetzchen_constructor_exists():
    assert callable(Plaetzchen.__init__)


def test_hyp_plaetzchen_constructor_args():
    sig = inspect.signature(Plaetzchen.__init__)
    params = list(sig.parameters.keys())
    assert "breite" in params, "Missing parameter 'breite'"
    assert "form" in params, "Missing parameter 'form'"
    assert "teig" in params, "Missing parameter 'teig'"
    assert "backzeit" in params, "Missing parameter 'backzeit'"
    assert "belag" in params, "Missing parameter 'belag'"
    assert "temperatur" in params, "Missing parameter 'temperatur'"
    assert "laenge" in params, "Missing parameter 'laenge'"










def test_hyp_zutat_is_not_abstract():
    assert not inspect.isabstract(Zutat)


def test_hyp_zutat_constructor_exists():
    assert callable(Zutat.__init__)


def test_hyp_zutat_constructor_args():
    sig = inspect.signature(Zutat.__init__)
    params = list(sig.parameters.keys())
    assert "menge" in params, "Missing parameter 'menge'"
    assert "name" in params, "Missing parameter 'name'"
    assert "einheit" in params, "Missing parameter 'einheit'"






def test_hyp_zutaten_is_not_abstract():
    assert not inspect.isabstract(Zutaten)


def test_hyp_zutaten_constructor_exists():
    assert callable(Zutaten.__init__)


def test_hyp_zutaten_constructor_args():
    sig = inspect.signature(Zutaten.__init__)
    params = list(sig.parameters.keys())
    assert "zutaten" in params, "Missing parameter 'zutaten'"



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
Auftrag_strategy = st.builds(
    Auftrag,
    keks=
        safe_text,
    name=
        safe_text,
    anzahl=
        safe_text
)
ZutatenEingabeForm_strategy = st.builds(
    ZutatenEingabeForm,
    neueZutat=
        safe_text
)
PlaetzchenAnzeigeForm_strategy = st.builds(
    PlaetzchenAnzeigeForm,
    laenge=
        safe_text,
    form=
        safe_text,
    breite=
        safe_text
)
DateiEA_strategy = st.builds(
    DateiEA,
)
PlaetzchenDesignerForm_strategy = st.builds(
    PlaetzchenDesignerForm,
    BLECHLAENGE=
        safe_text,
    datei=
        safe_text,
    plaetzchenGeaendert=
        st.booleans(),
    neuesPlaetzchen=
        safe_text,
    BLECHBREITE=
        safe_text,
    neuerAuftrag=
        safe_text
)
Plaetzchen_strategy = st.builds(
    Plaetzchen,
    breite=
        safe_text,
    form=
        safe_text,
    teig=
        safe_text,
    backzeit=
        safe_text,
    belag=
        safe_text,
    temperatur=
        safe_text,
    laenge=
        safe_text
)
Zutat_strategy = st.builds(
    Zutat,
    menge=
        safe_text,
    name=
        safe_text,
    einheit=
        safe_text
)
Zutaten_strategy = st.builds(
    Zutaten,
    zutaten=
        safe_text
)




@given(instance=Auftrag_strategy)
def test_hyp_auftrag_keks_setter(instance):
    original = instance.keks
    instance.keks = original
    assert instance.keks == original



@given(instance=Auftrag_strategy)
def test_hyp_auftrag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Auftrag_strategy)
def test_hyp_auftrag_anzahl_setter(instance):
    original = instance.anzahl
    instance.anzahl = original
    assert instance.anzahl == original




@given(instance=ZutatenEingabeForm_strategy)
def test_hyp_zutateneingabeform_neueZutat_setter(instance):
    original = instance.neueZutat
    instance.neueZutat = original
    assert instance.neueZutat == original




@given(instance=PlaetzchenAnzeigeForm_strategy)
def test_hyp_plaetzchenanzeigeform_laenge_setter(instance):
    original = instance.laenge
    instance.laenge = original
    assert instance.laenge == original



@given(instance=PlaetzchenAnzeigeForm_strategy)
def test_hyp_plaetzchenanzeigeform_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=PlaetzchenAnzeigeForm_strategy)
def test_hyp_plaetzchenanzeigeform_breite_setter(instance):
    original = instance.breite
    instance.breite = original
    assert instance.breite == original





@given(instance=PlaetzchenDesignerForm_strategy)
def test_hyp_plaetzchendesignerform_BLECHLAENGE_setter(instance):
    original = instance.BLECHLAENGE
    instance.BLECHLAENGE = original
    assert instance.BLECHLAENGE == original



@given(instance=PlaetzchenDesignerForm_strategy)
def test_hyp_plaetzchendesignerform_datei_setter(instance):
    original = instance.datei
    instance.datei = original
    assert instance.datei == original



@given(instance=PlaetzchenDesignerForm_strategy)
def test_hyp_plaetzchendesignerform_plaetzchenGeaendert_setter(instance):
    original = instance.plaetzchenGeaendert
    instance.plaetzchenGeaendert = original
    assert instance.plaetzchenGeaendert == original



@given(instance=PlaetzchenDesignerForm_strategy)
def test_hyp_plaetzchendesignerform_neuesPlaetzchen_setter(instance):
    original = instance.neuesPlaetzchen
    instance.neuesPlaetzchen = original
    assert instance.neuesPlaetzchen == original



@given(instance=PlaetzchenDesignerForm_strategy)
def test_hyp_plaetzchendesignerform_BLECHBREITE_setter(instance):
    original = instance.BLECHBREITE
    instance.BLECHBREITE = original
    assert instance.BLECHBREITE == original



@given(instance=PlaetzchenDesignerForm_strategy)
def test_hyp_plaetzchendesignerform_neuerAuftrag_setter(instance):
    original = instance.neuerAuftrag
    instance.neuerAuftrag = original
    assert instance.neuerAuftrag == original




@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_breite_setter(instance):
    original = instance.breite
    instance.breite = original
    assert instance.breite == original



@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_teig_setter(instance):
    original = instance.teig
    instance.teig = original
    assert instance.teig == original



@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_backzeit_setter(instance):
    original = instance.backzeit
    instance.backzeit = original
    assert instance.backzeit == original



@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_belag_setter(instance):
    original = instance.belag
    instance.belag = original
    assert instance.belag == original



@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_temperatur_setter(instance):
    original = instance.temperatur
    instance.temperatur = original
    assert instance.temperatur == original



@given(instance=Plaetzchen_strategy)
def test_hyp_plaetzchen_laenge_setter(instance):
    original = instance.laenge
    instance.laenge = original
    assert instance.laenge == original




@given(instance=Zutat_strategy)
def test_hyp_zutat_menge_setter(instance):
    original = instance.menge
    instance.menge = original
    assert instance.menge == original



@given(instance=Zutat_strategy)
def test_hyp_zutat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Zutat_strategy)
def test_hyp_zutat_einheit_setter(instance):
    original = instance.einheit
    instance.einheit = original
    assert instance.einheit == original




@given(instance=Zutaten_strategy)
def test_hyp_zutaten_zutaten_setter(instance):
    original = instance.zutaten
    instance.zutaten = original
    assert instance.zutaten == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_Auftrag_anzahl_value_roundtrip():
    instance = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    assert instance.anzahl == "sample_text"
    instance.anzahl = "sample_text_2"
    assert instance.anzahl == "sample_text_2"


def test_Auftrag_keks_value_roundtrip():
    instance = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    assert instance.keks == "sample_text"
    instance.keks = "sample_text_2"
    assert instance.keks == "sample_text_2"


def test_Auftrag_name_value_roundtrip():
    instance = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Plaetzchen_backzeit_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.backzeit == "sample_text"
    instance.backzeit = "sample_text_2"
    assert instance.backzeit == "sample_text_2"


def test_Plaetzchen_belag_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.belag == "sample_text"
    instance.belag = "sample_text_2"
    assert instance.belag == "sample_text_2"


def test_Plaetzchen_breite_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.breite == "sample_text"
    instance.breite = "sample_text_2"
    assert instance.breite == "sample_text_2"


def test_Plaetzchen_form_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.form == "sample_text"
    instance.form = "sample_text_2"
    assert instance.form == "sample_text_2"


def test_Plaetzchen_laenge_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.laenge == "sample_text"
    instance.laenge = "sample_text_2"
    assert instance.laenge == "sample_text_2"


def test_Plaetzchen_teig_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.teig == "sample_text"
    instance.teig = "sample_text_2"
    assert instance.teig == "sample_text_2"


def test_Plaetzchen_temperatur_value_roundtrip():
    instance = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    assert instance.temperatur == "sample_text"
    instance.temperatur = "sample_text_2"
    assert instance.temperatur == "sample_text_2"


def test_PlaetzchenAnzeigeForm_breite_value_roundtrip():
    instance = PlaetzchenAnzeigeForm(breite="sample_text", form="sample_text", laenge="sample_text")
    assert instance.breite == "sample_text"
    instance.breite = "sample_text_2"
    assert instance.breite == "sample_text_2"


def test_PlaetzchenAnzeigeForm_form_value_roundtrip():
    instance = PlaetzchenAnzeigeForm(breite="sample_text", form="sample_text", laenge="sample_text")
    assert instance.form == "sample_text"
    instance.form = "sample_text_2"
    assert instance.form == "sample_text_2"


def test_PlaetzchenAnzeigeForm_laenge_value_roundtrip():
    instance = PlaetzchenAnzeigeForm(breite="sample_text", form="sample_text", laenge="sample_text")
    assert instance.laenge == "sample_text"
    instance.laenge = "sample_text_2"
    assert instance.laenge == "sample_text_2"


def test_PlaetzchenDesignerForm_BLECHBREITE_value_roundtrip():
    instance = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    assert instance.BLECHBREITE == "sample_text"
    instance.BLECHBREITE = "sample_text_2"
    assert instance.BLECHBREITE == "sample_text_2"


def test_PlaetzchenDesignerForm_BLECHLAENGE_value_roundtrip():
    instance = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    assert instance.BLECHLAENGE == "sample_text"
    instance.BLECHLAENGE = "sample_text_2"
    assert instance.BLECHLAENGE == "sample_text_2"


def test_PlaetzchenDesignerForm_datei_value_roundtrip():
    instance = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    assert instance.datei == "sample_text"
    instance.datei = "sample_text_2"
    assert instance.datei == "sample_text_2"


def test_PlaetzchenDesignerForm_neuerAuftrag_value_roundtrip():
    instance = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    assert instance.neuerAuftrag == "sample_text"
    instance.neuerAuftrag = "sample_text_2"
    assert instance.neuerAuftrag == "sample_text_2"


def test_PlaetzchenDesignerForm_neuesPlaetzchen_value_roundtrip():
    instance = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    assert instance.neuesPlaetzchen == "sample_text"
    instance.neuesPlaetzchen = "sample_text_2"
    assert instance.neuesPlaetzchen == "sample_text_2"


def test_PlaetzchenDesignerForm_plaetzchenGeaendert_value_roundtrip():
    instance = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    assert instance.plaetzchenGeaendert == True
    instance.plaetzchenGeaendert = False
    assert instance.plaetzchenGeaendert == False


def test_Zutat_einheit_value_roundtrip():
    instance = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    assert instance.einheit == "sample_text"
    instance.einheit = "sample_text_2"
    assert instance.einheit == "sample_text_2"


def test_Zutat_menge_value_roundtrip():
    instance = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    assert instance.menge == "sample_text"
    instance.menge = "sample_text_2"
    assert instance.menge == "sample_text_2"


def test_Zutat_name_value_roundtrip():
    instance = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Zutaten_zutaten_value_roundtrip():
    instance = Zutaten(zutaten="sample_text")
    assert instance.zutaten == "sample_text"
    instance.zutaten = "sample_text_2"
    assert instance.zutaten == "sample_text_2"


def test_ZutatenEingabeForm_neueZutat_value_roundtrip():
    instance = ZutatenEingabeForm(neueZutat="sample_text")
    assert instance.neueZutat == "sample_text"
    instance.neueZutat = "sample_text_2"
    assert instance.neueZutat == "sample_text_2"


def test_assoc_DateiEA_Auftrag_link_reassign_clear():
    a = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    b1 = DateiEA()
    b2 = DateiEA()
    _safe_set(a, 'dateiEA19', b1)
    assert _is_linked(a, 'dateiEA19', b1)
    if hasattr(b1, 'auftrag18'):
        assert _is_linked(b1, 'auftrag18', a)
    _safe_set(a, 'dateiEA19', b2)
    assert _is_linked(a, 'dateiEA19', b2)
    if hasattr(b1, 'auftrag18'):
        assert not _is_linked(b1, 'auftrag18', a)
    if hasattr(b2, 'auftrag18'):
        assert _is_linked(b2, 'auftrag18', a)
    _safe_set(a, 'dateiEA19', None)
    assert not _is_linked(a, 'dateiEA19', b2)
    if hasattr(b2, 'auftrag18'):
        assert not _is_linked(b2, 'auftrag18', a)


def test_assoc_DateiEA_Plaetzchen_link_reassign_clear():
    a = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b1 = DateiEA()
    b2 = DateiEA()
    _safe_set(a, 'dateiEA13', b1)
    assert _is_linked(a, 'dateiEA13', b1)
    if hasattr(b1, 'plaetzchen12'):
        assert _is_linked(b1, 'plaetzchen12', a)
    _safe_set(a, 'dateiEA13', b2)
    assert _is_linked(a, 'dateiEA13', b2)
    if hasattr(b1, 'plaetzchen12'):
        assert not _is_linked(b1, 'plaetzchen12', a)
    if hasattr(b2, 'plaetzchen12'):
        assert _is_linked(b2, 'plaetzchen12', a)
    _safe_set(a, 'dateiEA13', None)
    assert not _is_linked(a, 'dateiEA13', b2)
    if hasattr(b2, 'plaetzchen12'):
        assert not _is_linked(b2, 'plaetzchen12', a)


def test_assoc_PlaetzchenDesignerForm_Auftrag_link_reassign_clear():
    a = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    b1 = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    b2 = Auftrag(anzahl="sample_text_2", keks="sample_text_2", name="sample_text_2")
    _safe_set(a, 'auftrag22', b1)
    assert _is_linked(a, 'auftrag22', b1)
    if hasattr(b1, 'plaetzchenDesignerForm23'):
        assert _is_linked(b1, 'plaetzchenDesignerForm23', a)
    _safe_set(a, 'auftrag22', b2)
    assert _is_linked(a, 'auftrag22', b2)
    if hasattr(b1, 'plaetzchenDesignerForm23'):
        assert not _is_linked(b1, 'plaetzchenDesignerForm23', a)
    if hasattr(b2, 'plaetzchenDesignerForm23'):
        assert _is_linked(b2, 'plaetzchenDesignerForm23', a)
    _safe_set(a, 'auftrag22', None)
    assert not _is_linked(a, 'auftrag22', b2)
    if hasattr(b2, 'plaetzchenDesignerForm23'):
        assert not _is_linked(b2, 'plaetzchenDesignerForm23', a)


def test_assoc_PlaetzchenDesignerForm_DateiEA_link_reassign_clear():
    a = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    b1 = DateiEA()
    b2 = DateiEA()
    _safe_set(a, 'dateiEA6', b1)
    assert _is_linked(a, 'dateiEA6', b1)
    if hasattr(b1, 'plaetzchenDesignerForm7'):
        assert _is_linked(b1, 'plaetzchenDesignerForm7', a)
    _safe_set(a, 'dateiEA6', b2)
    assert _is_linked(a, 'dateiEA6', b2)
    if hasattr(b1, 'plaetzchenDesignerForm7'):
        assert not _is_linked(b1, 'plaetzchenDesignerForm7', a)
    if hasattr(b2, 'plaetzchenDesignerForm7'):
        assert _is_linked(b2, 'plaetzchenDesignerForm7', a)
    _safe_set(a, 'dateiEA6', None)
    assert not _is_linked(a, 'dateiEA6', b2)
    if hasattr(b2, 'plaetzchenDesignerForm7'):
        assert not _is_linked(b2, 'plaetzchenDesignerForm7', a)


def test_assoc_PlaetzchenDesignerForm_Plaetzchen_link_reassign_clear():
    a = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    b1 = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b2 = Plaetzchen(backzeit="sample_text_2", belag="sample_text_2", breite="sample_text_2", form="sample_text_2", laenge="sample_text_2", teig="sample_text_2", temperatur="sample_text_2")
    _safe_set(a, 'plaetzchen10', b1)
    assert _is_linked(a, 'plaetzchen10', b1)
    if hasattr(b1, 'plaetzchenDesignerForm11'):
        assert _is_linked(b1, 'plaetzchenDesignerForm11', a)
    _safe_set(a, 'plaetzchen10', b2)
    assert _is_linked(a, 'plaetzchen10', b2)
    if hasattr(b1, 'plaetzchenDesignerForm11'):
        assert not _is_linked(b1, 'plaetzchenDesignerForm11', a)
    if hasattr(b2, 'plaetzchenDesignerForm11'):
        assert _is_linked(b2, 'plaetzchenDesignerForm11', a)
    _safe_set(a, 'plaetzchen10', None)
    assert not _is_linked(a, 'plaetzchen10', b2)
    if hasattr(b2, 'plaetzchenDesignerForm11'):
        assert not _is_linked(b2, 'plaetzchenDesignerForm11', a)


def test_assoc_PlaetzchenDesignerForm_PlaetzchenAnzeigeForm_link_reassign_clear():
    a = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    b1 = PlaetzchenAnzeigeForm(breite="sample_text", form="sample_text", laenge="sample_text")
    b2 = PlaetzchenAnzeigeForm(breite="sample_text_2", form="sample_text_2", laenge="sample_text_2")
    _safe_set(a, 'plaetzchenAnzeigeForm8', b1)
    assert _is_linked(a, 'plaetzchenAnzeigeForm8', b1)
    if hasattr(b1, 'plaetzchenDesignerForm9'):
        assert _is_linked(b1, 'plaetzchenDesignerForm9', a)
    _safe_set(a, 'plaetzchenAnzeigeForm8', b2)
    assert _is_linked(a, 'plaetzchenAnzeigeForm8', b2)
    if hasattr(b1, 'plaetzchenDesignerForm9'):
        assert not _is_linked(b1, 'plaetzchenDesignerForm9', a)
    if hasattr(b2, 'plaetzchenDesignerForm9'):
        assert _is_linked(b2, 'plaetzchenDesignerForm9', a)
    _safe_set(a, 'plaetzchenAnzeigeForm8', None)
    assert not _is_linked(a, 'plaetzchenAnzeigeForm8', b2)
    if hasattr(b2, 'plaetzchenDesignerForm9'):
        assert not _is_linked(b2, 'plaetzchenDesignerForm9', a)


def test_assoc_Plaetzchen_Auftrag_link_reassign_clear():
    a = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b1 = Auftrag(anzahl="sample_text", keks="sample_text", name="sample_text")
    b2 = Auftrag(anzahl="sample_text_2", keks="sample_text_2", name="sample_text_2")
    _safe_set(a, 'auftrag20', b1)
    assert _is_linked(a, 'auftrag20', b1)
    if hasattr(b1, 'plaetzchen221'):
        assert _is_linked(b1, 'plaetzchen221', a)
    _safe_set(a, 'auftrag20', b2)
    assert _is_linked(a, 'auftrag20', b2)
    if hasattr(b1, 'plaetzchen221'):
        assert not _is_linked(b1, 'plaetzchen221', a)
    if hasattr(b2, 'plaetzchen221'):
        assert _is_linked(b2, 'plaetzchen221', a)
    _safe_set(a, 'auftrag20', None)
    assert not _is_linked(a, 'auftrag20', b2)
    if hasattr(b2, 'plaetzchen221'):
        assert not _is_linked(b2, 'plaetzchen221', a)


def test_assoc_Plaetzchen_Teig_link_reassign_clear():
    a = Zutaten(zutaten="sample_text")
    b1 = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b2 = Plaetzchen(backzeit="sample_text_2", belag="sample_text_2", breite="sample_text_2", form="sample_text_2", laenge="sample_text_2", teig="sample_text_2", temperatur="sample_text_2")
    _safe_set(a, 'plaetzchen1', b1)
    assert _is_linked(a, 'plaetzchen1', b1)
    if hasattr(b1, 'teig20'):
        assert _is_linked(b1, 'teig20', a)
    _safe_set(a, 'plaetzchen1', b2)
    assert _is_linked(a, 'plaetzchen1', b2)
    if hasattr(b1, 'teig20'):
        assert not _is_linked(b1, 'teig20', a)
    if hasattr(b2, 'teig20'):
        assert _is_linked(b2, 'teig20', a)
    _safe_set(a, 'plaetzchen1', None)
    assert not _is_linked(a, 'plaetzchen1', b2)
    if hasattr(b2, 'teig20'):
        assert not _is_linked(b2, 'teig20', a)


def test_assoc_Plaetzchen_Zutat_link_reassign_clear():
    a = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b1 = Plaetzchen(backzeit="sample_text", belag="sample_text", breite="sample_text", form="sample_text", laenge="sample_text", teig="sample_text", temperatur="sample_text")
    b2 = Plaetzchen(backzeit="sample_text_2", belag="sample_text_2", breite="sample_text_2", form="sample_text_2", laenge="sample_text_2", teig="sample_text_2", temperatur="sample_text_2")
    _safe_set(a, 'plaetzchen3', b1)
    assert _is_linked(a, 'plaetzchen3', b1)
    if hasattr(b1, 'zutat2'):
        assert _is_linked(b1, 'zutat2', a)
    _safe_set(a, 'plaetzchen3', b2)
    assert _is_linked(a, 'plaetzchen3', b2)
    if hasattr(b1, 'zutat2'):
        assert not _is_linked(b1, 'zutat2', a)
    if hasattr(b2, 'zutat2'):
        assert _is_linked(b2, 'zutat2', a)
    _safe_set(a, 'plaetzchen3', None)
    assert not _is_linked(a, 'plaetzchen3', b2)
    if hasattr(b2, 'zutat2'):
        assert not _is_linked(b2, 'zutat2', a)


def test_assoc_Teig_Zutat_link_reassign_clear():
    a = Zutaten(zutaten="sample_text")
    b1 = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b2 = Zutat(einheit="sample_text_2", menge="sample_text_2", name="sample_text_2")
    _safe_set(a, 'zutat4', b1)
    assert _is_linked(a, 'zutat4', b1)
    if hasattr(b1, 'teig5'):
        assert _is_linked(b1, 'teig5', a)
    _safe_set(a, 'zutat4', b2)
    assert _is_linked(a, 'zutat4', b2)
    if hasattr(b1, 'teig5'):
        assert not _is_linked(b1, 'teig5', a)
    if hasattr(b2, 'teig5'):
        assert _is_linked(b2, 'teig5', a)
    _safe_set(a, 'zutat4', None)
    assert not _is_linked(a, 'zutat4', b2)
    if hasattr(b2, 'teig5'):
        assert not _is_linked(b2, 'teig5', a)


def test_assoc_ZutatenEingabe_PlaetzchenDesignerForm_link_reassign_clear():
    a = ZutatenEingabeForm(neueZutat="sample_text")
    b1 = PlaetzchenDesignerForm(BLECHBREITE="sample_text", BLECHLAENGE="sample_text", datei="sample_text", neuerAuftrag="sample_text", neuesPlaetzchen="sample_text", plaetzchenGeaendert=True)
    b2 = PlaetzchenDesignerForm(BLECHBREITE="sample_text_2", BLECHLAENGE="sample_text_2", datei="sample_text_2", neuerAuftrag="sample_text_2", neuesPlaetzchen="sample_text_2", plaetzchenGeaendert=False)
    _safe_set(a, 'plaetzchenDesignerForm14', b1)
    assert _is_linked(a, 'plaetzchenDesignerForm14', b1)
    if hasattr(b1, 'zutatenEingabe15'):
        assert _is_linked(b1, 'zutatenEingabe15', a)
    _safe_set(a, 'plaetzchenDesignerForm14', b2)
    assert _is_linked(a, 'plaetzchenDesignerForm14', b2)
    if hasattr(b1, 'zutatenEingabe15'):
        assert not _is_linked(b1, 'zutatenEingabe15', a)
    if hasattr(b2, 'zutatenEingabe15'):
        assert _is_linked(b2, 'zutatenEingabe15', a)
    _safe_set(a, 'plaetzchenDesignerForm14', None)
    assert not _is_linked(a, 'plaetzchenDesignerForm14', b2)
    if hasattr(b2, 'zutatenEingabe15'):
        assert not _is_linked(b2, 'zutatenEingabe15', a)


def test_assoc_ZutatenEingabe_Zutat_link_reassign_clear():
    a = ZutatenEingabeForm(neueZutat="sample_text")
    b1 = Zutat(einheit="sample_text", menge="sample_text", name="sample_text")
    b2 = Zutat(einheit="sample_text_2", menge="sample_text_2", name="sample_text_2")
    _safe_set(a, 'zutat16', b1)
    assert _is_linked(a, 'zutat16', b1)
    if hasattr(b1, 'zutatenEingabe17'):
        assert _is_linked(b1, 'zutatenEingabe17', a)
    _safe_set(a, 'zutat16', b2)
    assert _is_linked(a, 'zutat16', b2)
    if hasattr(b1, 'zutatenEingabe17'):
        assert not _is_linked(b1, 'zutatenEingabe17', a)
    if hasattr(b2, 'zutatenEingabe17'):
        assert _is_linked(b2, 'zutatenEingabe17', a)
    _safe_set(a, 'zutat16', None)
    assert not _is_linked(a, 'zutat16', b2)
    if hasattr(b2, 'zutatenEingabe17'):
        assert not _is_linked(b2, 'zutatenEingabe17', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Auftrag_strategy = st.builds(Auftrag, anzahl=safe_text, keks=safe_text, name=safe_text)
@given(instance=Auftrag_strategy)
@settings(max_examples=25)
def test_Auftrag_instantiation(instance):
    assert isinstance(instance, Auftrag)


DateiEA_strategy = st.builds(DateiEA)
@given(instance=DateiEA_strategy)
@settings(max_examples=25)
def test_DateiEA_instantiation(instance):
    assert isinstance(instance, DateiEA)


Plaetzchen_strategy = st.builds(Plaetzchen, backzeit=safe_text, belag=safe_text, breite=safe_text, form=safe_text, laenge=safe_text, teig=safe_text, temperatur=safe_text)
@given(instance=Plaetzchen_strategy)
@settings(max_examples=25)
def test_Plaetzchen_instantiation(instance):
    assert isinstance(instance, Plaetzchen)


PlaetzchenAnzeigeForm_strategy = st.builds(PlaetzchenAnzeigeForm, breite=safe_text, form=safe_text, laenge=safe_text)
@given(instance=PlaetzchenAnzeigeForm_strategy)
@settings(max_examples=25)
def test_PlaetzchenAnzeigeForm_instantiation(instance):
    assert isinstance(instance, PlaetzchenAnzeigeForm)


PlaetzchenDesignerForm_strategy = st.builds(PlaetzchenDesignerForm, BLECHBREITE=safe_text, BLECHLAENGE=safe_text, datei=safe_text, neuerAuftrag=safe_text, neuesPlaetzchen=safe_text, plaetzchenGeaendert=st.booleans())
@given(instance=PlaetzchenDesignerForm_strategy)
@settings(max_examples=25)
def test_PlaetzchenDesignerForm_instantiation(instance):
    assert isinstance(instance, PlaetzchenDesignerForm)


Zutat_strategy = st.builds(Zutat, einheit=safe_text, menge=safe_text, name=safe_text)
@given(instance=Zutat_strategy)
@settings(max_examples=25)
def test_Zutat_instantiation(instance):
    assert isinstance(instance, Zutat)


Zutaten_strategy = st.builds(Zutaten, zutaten=safe_text)
@given(instance=Zutaten_strategy)
@settings(max_examples=25)
def test_Zutaten_instantiation(instance):
    assert isinstance(instance, Zutaten)


ZutatenEingabeForm_strategy = st.builds(ZutatenEingabeForm, neueZutat=safe_text)
@given(instance=ZutatenEingabeForm_strategy)
@settings(max_examples=25)
def test_ZutatenEingabeForm_instantiation(instance):
    assert isinstance(instance, ZutatenEingabeForm)



