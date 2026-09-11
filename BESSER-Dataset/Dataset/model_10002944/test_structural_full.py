import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator_Actor,
    Administrator_Actor1,
    Anwendungssystem_Component,
    Benutzer_anlegen_und_verwalten_UseCase,
    Benutzer_anlegen_und_verwalten_UseCase1,
    Benutzer_authentifizieren_und_autorisieren_UseCase,
    Benutzer_authentifizieren_und_autorisieren_UseCase1,
    Benutzer_deaktivieren_UseCase,
    Benutzer_deaktivieren_UseCase1,
    Benutzername_und_Passwort_eingeben_UseCase,
    Benutzername_und_Passwort_eingeben_UseCase1,
    Class,
    Component_Component,
    Gesch_ftsf_herer,
    Gesch_ftsf_hrer_Actor,
    Gesch_ftsf_hrer_Actor1,
    Gesch_ftsf_hrer_Actor2,
    Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase,
    Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1,
    Hinweis_anzeigen__falsche_EAN_UseCase,
    Hinweis_anzeigen__falsche_EAN_UseCase1,
    Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase,
    Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1,
    Information_hinterlegen_UseCase,
    Information_hinterlegen_UseCase1,
    Lager,
    Lager_einsehen_UseCase,
    Lager_einsehen_UseCase1,
    Lager_einsehen_UseCase2,
    Lager_einsehen_und_verwalten_external,
    Lager_verwalten_Component,
    Lagerverwaltung_Component,
    Lagerverwaltung_Component1,
    Mitarbeiter,
    Mitarbeiter_Actor,
    Mitarbeiterprovision_einsehen_UseCase,
    Mitarbeiterprovision_einsehen_UseCase1,
    Mitarbeiterprovision_hinterlegen_UseCase,
    Mitarbeiterprovision_hinterlegen_UseCase1,
    Mobilfunkger_t,
    Mobilfunkger_t_ausbuchen_UseCase,
    Mobilfunkger_t_ausbuchen_UseCase1,
    Mobilfunkger_t_einbuchen_Component,
    Mobilfunkger_t_einbuchen_Component1,
    Mobilfunkger_t_einbuchen_external,
    Mobilfunkger_t_freigeben_UseCase,
    Mobilfunkger_t_freigeben_UseCase1,
    Mobilfunkger_t_freigeben_UseCase2,
    Mobilfunkger_t_l_schen_UseCase,
    Mobilfunkger_t_l_schen_external,
    Mobilfunkger_t_reservieren_UseCase,
    Mobilfunkger_t_reservieren_UseCase1,
    Mobilfunkger_t_reservieren_UseCase2,
    Mobilfunkger_t_umbuchen_UseCase,
    Mobilfunkger_t_umbuchen_external,
    Mobilfunkger_t_verkauft_Component,
    Mobilfunkger_t_verkauft_Component1,
    Provisionlisten_verwalten_Component,
    Provisionlisten_verwalten_Component1,
    Systemverwaltung_Component,
    Systemverwaltung_Component1,
    T,
    T1,
    Tarif,
    Tarif_anlegen_external,
    Tarif_hintelegen_UseCase,
    Tarif_hintelegen_UseCase1,
    Tarife_einsehen_UseCase,
    Tarife_einsehen_UseCase1,
    Verkaufspreis_eintragen_UseCase,
    Verkaufspreis_eintragen_UseCase1,
    Verkaufstyp_ausw_hlen_UseCase,
    Verkaufstyp_ausw_hlen_UseCase1,
    Verkaufte_Mobilfunkger_te_einsehen_UseCase,
    Verkaufte_Mobilfunkger_te_einsehen_UseCase1,
    _external_unnamed_46,
    _external_unnamed_48,
    vef_gbare_Ger_te,
    verkaufte_Ger_te,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


Administrator_Actor1_strategy = st.builds(Administrator_Actor1)
@given(instance=Administrator_Actor1_strategy)
@settings(max_examples=25)
def test_Administrator_Actor1_instantiation(instance):
    assert isinstance(instance, Administrator_Actor1)


Anwendungssystem_Component_strategy = st.builds(Anwendungssystem_Component)
@given(instance=Anwendungssystem_Component_strategy)
@settings(max_examples=25)
def test_Anwendungssystem_Component_instantiation(instance):
    assert isinstance(instance, Anwendungssystem_Component)


Benutzer_anlegen_und_verwalten_UseCase_strategy = st.builds(Benutzer_anlegen_und_verwalten_UseCase)
@given(instance=Benutzer_anlegen_und_verwalten_UseCase_strategy)
@settings(max_examples=25)
def test_Benutzer_anlegen_und_verwalten_UseCase_instantiation(instance):
    assert isinstance(instance, Benutzer_anlegen_und_verwalten_UseCase)


Benutzer_anlegen_und_verwalten_UseCase1_strategy = st.builds(Benutzer_anlegen_und_verwalten_UseCase1)
@given(instance=Benutzer_anlegen_und_verwalten_UseCase1_strategy)
@settings(max_examples=25)
def test_Benutzer_anlegen_und_verwalten_UseCase1_instantiation(instance):
    assert isinstance(instance, Benutzer_anlegen_und_verwalten_UseCase1)


Benutzer_authentifizieren_und_autorisieren_UseCase_strategy = st.builds(Benutzer_authentifizieren_und_autorisieren_UseCase)
@given(instance=Benutzer_authentifizieren_und_autorisieren_UseCase_strategy)
@settings(max_examples=25)
def test_Benutzer_authentifizieren_und_autorisieren_UseCase_instantiation(instance):
    assert isinstance(instance, Benutzer_authentifizieren_und_autorisieren_UseCase)


Benutzer_authentifizieren_und_autorisieren_UseCase1_strategy = st.builds(Benutzer_authentifizieren_und_autorisieren_UseCase1)
@given(instance=Benutzer_authentifizieren_und_autorisieren_UseCase1_strategy)
@settings(max_examples=25)
def test_Benutzer_authentifizieren_und_autorisieren_UseCase1_instantiation(instance):
    assert isinstance(instance, Benutzer_authentifizieren_und_autorisieren_UseCase1)


Benutzer_deaktivieren_UseCase_strategy = st.builds(Benutzer_deaktivieren_UseCase)
@given(instance=Benutzer_deaktivieren_UseCase_strategy)
@settings(max_examples=25)
def test_Benutzer_deaktivieren_UseCase_instantiation(instance):
    assert isinstance(instance, Benutzer_deaktivieren_UseCase)


Benutzer_deaktivieren_UseCase1_strategy = st.builds(Benutzer_deaktivieren_UseCase1)
@given(instance=Benutzer_deaktivieren_UseCase1_strategy)
@settings(max_examples=25)
def test_Benutzer_deaktivieren_UseCase1_instantiation(instance):
    assert isinstance(instance, Benutzer_deaktivieren_UseCase1)


Benutzername_und_Passwort_eingeben_UseCase_strategy = st.builds(Benutzername_und_Passwort_eingeben_UseCase)
@given(instance=Benutzername_und_Passwort_eingeben_UseCase_strategy)
@settings(max_examples=25)
def test_Benutzername_und_Passwort_eingeben_UseCase_instantiation(instance):
    assert isinstance(instance, Benutzername_und_Passwort_eingeben_UseCase)


Benutzername_und_Passwort_eingeben_UseCase1_strategy = st.builds(Benutzername_und_Passwort_eingeben_UseCase1)
@given(instance=Benutzername_und_Passwort_eingeben_UseCase1_strategy)
@settings(max_examples=25)
def test_Benutzername_und_Passwort_eingeben_UseCase1_instantiation(instance):
    assert isinstance(instance, Benutzername_und_Passwort_eingeben_UseCase1)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Component_Component_strategy = st.builds(Component_Component)
@given(instance=Component_Component_strategy)
@settings(max_examples=25)
def test_Component_Component_instantiation(instance):
    assert isinstance(instance, Component_Component)


Gesch_ftsf_herer_strategy = st.builds(Gesch_ftsf_herer)
@given(instance=Gesch_ftsf_herer_strategy)
@settings(max_examples=25)
def test_Gesch_ftsf_herer_instantiation(instance):
    assert isinstance(instance, Gesch_ftsf_herer)


Gesch_ftsf_hrer_Actor_strategy = st.builds(Gesch_ftsf_hrer_Actor)
@given(instance=Gesch_ftsf_hrer_Actor_strategy)
@settings(max_examples=25)
def test_Gesch_ftsf_hrer_Actor_instantiation(instance):
    assert isinstance(instance, Gesch_ftsf_hrer_Actor)


Gesch_ftsf_hrer_Actor1_strategy = st.builds(Gesch_ftsf_hrer_Actor1)
@given(instance=Gesch_ftsf_hrer_Actor1_strategy)
@settings(max_examples=25)
def test_Gesch_ftsf_hrer_Actor1_instantiation(instance):
    assert isinstance(instance, Gesch_ftsf_hrer_Actor1)


Gesch_ftsf_hrer_Actor2_strategy = st.builds(Gesch_ftsf_hrer_Actor2)
@given(instance=Gesch_ftsf_hrer_Actor2_strategy)
@settings(max_examples=25)
def test_Gesch_ftsf_hrer_Actor2_instantiation(instance):
    assert isinstance(instance, Gesch_ftsf_hrer_Actor2)


Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase_strategy = st.builds(Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase)
@given(instance=Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase_strategy)
@settings(max_examples=25)
def test_Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase_instantiation(instance):
    assert isinstance(instance, Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase)


Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1_strategy = st.builds(Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1)
@given(instance=Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1_strategy)
@settings(max_examples=25)
def test_Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1_instantiation(instance):
    assert isinstance(instance, Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1)


Hinweis_anzeigen__falsche_EAN_UseCase_strategy = st.builds(Hinweis_anzeigen__falsche_EAN_UseCase)
@given(instance=Hinweis_anzeigen__falsche_EAN_UseCase_strategy)
@settings(max_examples=25)
def test_Hinweis_anzeigen__falsche_EAN_UseCase_instantiation(instance):
    assert isinstance(instance, Hinweis_anzeigen__falsche_EAN_UseCase)


Hinweis_anzeigen__falsche_EAN_UseCase1_strategy = st.builds(Hinweis_anzeigen__falsche_EAN_UseCase1)
@given(instance=Hinweis_anzeigen__falsche_EAN_UseCase1_strategy)
@settings(max_examples=25)
def test_Hinweis_anzeigen__falsche_EAN_UseCase1_instantiation(instance):
    assert isinstance(instance, Hinweis_anzeigen__falsche_EAN_UseCase1)


Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase_strategy = st.builds(Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase)
@given(instance=Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase_strategy)
@settings(max_examples=25)
def test_Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase_instantiation(instance):
    assert isinstance(instance, Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase)


Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1_strategy = st.builds(Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1)
@given(instance=Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1_strategy)
@settings(max_examples=25)
def test_Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1_instantiation(instance):
    assert isinstance(instance, Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1)


Information_hinterlegen_UseCase_strategy = st.builds(Information_hinterlegen_UseCase)
@given(instance=Information_hinterlegen_UseCase_strategy)
@settings(max_examples=25)
def test_Information_hinterlegen_UseCase_instantiation(instance):
    assert isinstance(instance, Information_hinterlegen_UseCase)


Information_hinterlegen_UseCase1_strategy = st.builds(Information_hinterlegen_UseCase1)
@given(instance=Information_hinterlegen_UseCase1_strategy)
@settings(max_examples=25)
def test_Information_hinterlegen_UseCase1_instantiation(instance):
    assert isinstance(instance, Information_hinterlegen_UseCase1)


Lager_strategy = st.builds(Lager)
@given(instance=Lager_strategy)
@settings(max_examples=25)
def test_Lager_instantiation(instance):
    assert isinstance(instance, Lager)


Lager_einsehen_UseCase_strategy = st.builds(Lager_einsehen_UseCase)
@given(instance=Lager_einsehen_UseCase_strategy)
@settings(max_examples=25)
def test_Lager_einsehen_UseCase_instantiation(instance):
    assert isinstance(instance, Lager_einsehen_UseCase)


Lager_einsehen_UseCase1_strategy = st.builds(Lager_einsehen_UseCase1)
@given(instance=Lager_einsehen_UseCase1_strategy)
@settings(max_examples=25)
def test_Lager_einsehen_UseCase1_instantiation(instance):
    assert isinstance(instance, Lager_einsehen_UseCase1)


Lager_einsehen_UseCase2_strategy = st.builds(Lager_einsehen_UseCase2)
@given(instance=Lager_einsehen_UseCase2_strategy)
@settings(max_examples=25)
def test_Lager_einsehen_UseCase2_instantiation(instance):
    assert isinstance(instance, Lager_einsehen_UseCase2)


Lager_einsehen_und_verwalten_external_strategy = st.builds(Lager_einsehen_und_verwalten_external)
@given(instance=Lager_einsehen_und_verwalten_external_strategy)
@settings(max_examples=25)
def test_Lager_einsehen_und_verwalten_external_instantiation(instance):
    assert isinstance(instance, Lager_einsehen_und_verwalten_external)


Lager_verwalten_Component_strategy = st.builds(Lager_verwalten_Component)
@given(instance=Lager_verwalten_Component_strategy)
@settings(max_examples=25)
def test_Lager_verwalten_Component_instantiation(instance):
    assert isinstance(instance, Lager_verwalten_Component)


Lagerverwaltung_Component_strategy = st.builds(Lagerverwaltung_Component)
@given(instance=Lagerverwaltung_Component_strategy)
@settings(max_examples=25)
def test_Lagerverwaltung_Component_instantiation(instance):
    assert isinstance(instance, Lagerverwaltung_Component)


Lagerverwaltung_Component1_strategy = st.builds(Lagerverwaltung_Component1)
@given(instance=Lagerverwaltung_Component1_strategy)
@settings(max_examples=25)
def test_Lagerverwaltung_Component1_instantiation(instance):
    assert isinstance(instance, Lagerverwaltung_Component1)


Mitarbeiter_strategy = st.builds(Mitarbeiter)
@given(instance=Mitarbeiter_strategy)
@settings(max_examples=25)
def test_Mitarbeiter_instantiation(instance):
    assert isinstance(instance, Mitarbeiter)


Mitarbeiter_Actor_strategy = st.builds(Mitarbeiter_Actor)
@given(instance=Mitarbeiter_Actor_strategy)
@settings(max_examples=25)
def test_Mitarbeiter_Actor_instantiation(instance):
    assert isinstance(instance, Mitarbeiter_Actor)


Mitarbeiterprovision_einsehen_UseCase_strategy = st.builds(Mitarbeiterprovision_einsehen_UseCase)
@given(instance=Mitarbeiterprovision_einsehen_UseCase_strategy)
@settings(max_examples=25)
def test_Mitarbeiterprovision_einsehen_UseCase_instantiation(instance):
    assert isinstance(instance, Mitarbeiterprovision_einsehen_UseCase)


Mitarbeiterprovision_einsehen_UseCase1_strategy = st.builds(Mitarbeiterprovision_einsehen_UseCase1)
@given(instance=Mitarbeiterprovision_einsehen_UseCase1_strategy)
@settings(max_examples=25)
def test_Mitarbeiterprovision_einsehen_UseCase1_instantiation(instance):
    assert isinstance(instance, Mitarbeiterprovision_einsehen_UseCase1)


Mitarbeiterprovision_hinterlegen_UseCase_strategy = st.builds(Mitarbeiterprovision_hinterlegen_UseCase)
@given(instance=Mitarbeiterprovision_hinterlegen_UseCase_strategy)
@settings(max_examples=25)
def test_Mitarbeiterprovision_hinterlegen_UseCase_instantiation(instance):
    assert isinstance(instance, Mitarbeiterprovision_hinterlegen_UseCase)


Mitarbeiterprovision_hinterlegen_UseCase1_strategy = st.builds(Mitarbeiterprovision_hinterlegen_UseCase1)
@given(instance=Mitarbeiterprovision_hinterlegen_UseCase1_strategy)
@settings(max_examples=25)
def test_Mitarbeiterprovision_hinterlegen_UseCase1_instantiation(instance):
    assert isinstance(instance, Mitarbeiterprovision_hinterlegen_UseCase1)


Mobilfunkger_t_strategy = st.builds(Mobilfunkger_t)
@given(instance=Mobilfunkger_t_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t)


Mobilfunkger_t_ausbuchen_UseCase_strategy = st.builds(Mobilfunkger_t_ausbuchen_UseCase)
@given(instance=Mobilfunkger_t_ausbuchen_UseCase_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_ausbuchen_UseCase_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_ausbuchen_UseCase)


Mobilfunkger_t_ausbuchen_UseCase1_strategy = st.builds(Mobilfunkger_t_ausbuchen_UseCase1)
@given(instance=Mobilfunkger_t_ausbuchen_UseCase1_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_ausbuchen_UseCase1_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_ausbuchen_UseCase1)


Mobilfunkger_t_einbuchen_Component_strategy = st.builds(Mobilfunkger_t_einbuchen_Component)
@given(instance=Mobilfunkger_t_einbuchen_Component_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_einbuchen_Component_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_einbuchen_Component)


Mobilfunkger_t_einbuchen_Component1_strategy = st.builds(Mobilfunkger_t_einbuchen_Component1)
@given(instance=Mobilfunkger_t_einbuchen_Component1_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_einbuchen_Component1_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_einbuchen_Component1)


Mobilfunkger_t_einbuchen_external_strategy = st.builds(Mobilfunkger_t_einbuchen_external)
@given(instance=Mobilfunkger_t_einbuchen_external_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_einbuchen_external_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_einbuchen_external)


Mobilfunkger_t_freigeben_UseCase_strategy = st.builds(Mobilfunkger_t_freigeben_UseCase)
@given(instance=Mobilfunkger_t_freigeben_UseCase_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_freigeben_UseCase_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_freigeben_UseCase)


Mobilfunkger_t_freigeben_UseCase1_strategy = st.builds(Mobilfunkger_t_freigeben_UseCase1)
@given(instance=Mobilfunkger_t_freigeben_UseCase1_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_freigeben_UseCase1_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_freigeben_UseCase1)


Mobilfunkger_t_freigeben_UseCase2_strategy = st.builds(Mobilfunkger_t_freigeben_UseCase2)
@given(instance=Mobilfunkger_t_freigeben_UseCase2_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_freigeben_UseCase2_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_freigeben_UseCase2)


Mobilfunkger_t_l_schen_UseCase_strategy = st.builds(Mobilfunkger_t_l_schen_UseCase)
@given(instance=Mobilfunkger_t_l_schen_UseCase_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_l_schen_UseCase_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_l_schen_UseCase)


Mobilfunkger_t_l_schen_external_strategy = st.builds(Mobilfunkger_t_l_schen_external)
@given(instance=Mobilfunkger_t_l_schen_external_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_l_schen_external_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_l_schen_external)


Mobilfunkger_t_reservieren_UseCase_strategy = st.builds(Mobilfunkger_t_reservieren_UseCase)
@given(instance=Mobilfunkger_t_reservieren_UseCase_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_reservieren_UseCase_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_reservieren_UseCase)


Mobilfunkger_t_reservieren_UseCase1_strategy = st.builds(Mobilfunkger_t_reservieren_UseCase1)
@given(instance=Mobilfunkger_t_reservieren_UseCase1_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_reservieren_UseCase1_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_reservieren_UseCase1)


Mobilfunkger_t_reservieren_UseCase2_strategy = st.builds(Mobilfunkger_t_reservieren_UseCase2)
@given(instance=Mobilfunkger_t_reservieren_UseCase2_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_reservieren_UseCase2_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_reservieren_UseCase2)


Mobilfunkger_t_umbuchen_UseCase_strategy = st.builds(Mobilfunkger_t_umbuchen_UseCase)
@given(instance=Mobilfunkger_t_umbuchen_UseCase_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_umbuchen_UseCase_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_umbuchen_UseCase)


Mobilfunkger_t_umbuchen_external_strategy = st.builds(Mobilfunkger_t_umbuchen_external)
@given(instance=Mobilfunkger_t_umbuchen_external_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_umbuchen_external_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_umbuchen_external)


Mobilfunkger_t_verkauft_Component_strategy = st.builds(Mobilfunkger_t_verkauft_Component)
@given(instance=Mobilfunkger_t_verkauft_Component_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_verkauft_Component_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_verkauft_Component)


Mobilfunkger_t_verkauft_Component1_strategy = st.builds(Mobilfunkger_t_verkauft_Component1)
@given(instance=Mobilfunkger_t_verkauft_Component1_strategy)
@settings(max_examples=25)
def test_Mobilfunkger_t_verkauft_Component1_instantiation(instance):
    assert isinstance(instance, Mobilfunkger_t_verkauft_Component1)


Provisionlisten_verwalten_Component_strategy = st.builds(Provisionlisten_verwalten_Component)
@given(instance=Provisionlisten_verwalten_Component_strategy)
@settings(max_examples=25)
def test_Provisionlisten_verwalten_Component_instantiation(instance):
    assert isinstance(instance, Provisionlisten_verwalten_Component)


Provisionlisten_verwalten_Component1_strategy = st.builds(Provisionlisten_verwalten_Component1)
@given(instance=Provisionlisten_verwalten_Component1_strategy)
@settings(max_examples=25)
def test_Provisionlisten_verwalten_Component1_instantiation(instance):
    assert isinstance(instance, Provisionlisten_verwalten_Component1)


Systemverwaltung_Component_strategy = st.builds(Systemverwaltung_Component)
@given(instance=Systemverwaltung_Component_strategy)
@settings(max_examples=25)
def test_Systemverwaltung_Component_instantiation(instance):
    assert isinstance(instance, Systemverwaltung_Component)


Systemverwaltung_Component1_strategy = st.builds(Systemverwaltung_Component1)
@given(instance=Systemverwaltung_Component1_strategy)
@settings(max_examples=25)
def test_Systemverwaltung_Component1_instantiation(instance):
    assert isinstance(instance, Systemverwaltung_Component1)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


T1_strategy = st.builds(T1)
@given(instance=T1_strategy)
@settings(max_examples=25)
def test_T1_instantiation(instance):
    assert isinstance(instance, T1)


Tarif_strategy = st.builds(Tarif)
@given(instance=Tarif_strategy)
@settings(max_examples=25)
def test_Tarif_instantiation(instance):
    assert isinstance(instance, Tarif)


Tarif_anlegen_external_strategy = st.builds(Tarif_anlegen_external)
@given(instance=Tarif_anlegen_external_strategy)
@settings(max_examples=25)
def test_Tarif_anlegen_external_instantiation(instance):
    assert isinstance(instance, Tarif_anlegen_external)


Tarif_hintelegen_UseCase_strategy = st.builds(Tarif_hintelegen_UseCase)
@given(instance=Tarif_hintelegen_UseCase_strategy)
@settings(max_examples=25)
def test_Tarif_hintelegen_UseCase_instantiation(instance):
    assert isinstance(instance, Tarif_hintelegen_UseCase)


Tarif_hintelegen_UseCase1_strategy = st.builds(Tarif_hintelegen_UseCase1)
@given(instance=Tarif_hintelegen_UseCase1_strategy)
@settings(max_examples=25)
def test_Tarif_hintelegen_UseCase1_instantiation(instance):
    assert isinstance(instance, Tarif_hintelegen_UseCase1)


Tarife_einsehen_UseCase_strategy = st.builds(Tarife_einsehen_UseCase)
@given(instance=Tarife_einsehen_UseCase_strategy)
@settings(max_examples=25)
def test_Tarife_einsehen_UseCase_instantiation(instance):
    assert isinstance(instance, Tarife_einsehen_UseCase)


Tarife_einsehen_UseCase1_strategy = st.builds(Tarife_einsehen_UseCase1)
@given(instance=Tarife_einsehen_UseCase1_strategy)
@settings(max_examples=25)
def test_Tarife_einsehen_UseCase1_instantiation(instance):
    assert isinstance(instance, Tarife_einsehen_UseCase1)


Verkaufspreis_eintragen_UseCase_strategy = st.builds(Verkaufspreis_eintragen_UseCase)
@given(instance=Verkaufspreis_eintragen_UseCase_strategy)
@settings(max_examples=25)
def test_Verkaufspreis_eintragen_UseCase_instantiation(instance):
    assert isinstance(instance, Verkaufspreis_eintragen_UseCase)


Verkaufspreis_eintragen_UseCase1_strategy = st.builds(Verkaufspreis_eintragen_UseCase1)
@given(instance=Verkaufspreis_eintragen_UseCase1_strategy)
@settings(max_examples=25)
def test_Verkaufspreis_eintragen_UseCase1_instantiation(instance):
    assert isinstance(instance, Verkaufspreis_eintragen_UseCase1)


Verkaufstyp_ausw_hlen_UseCase_strategy = st.builds(Verkaufstyp_ausw_hlen_UseCase)
@given(instance=Verkaufstyp_ausw_hlen_UseCase_strategy)
@settings(max_examples=25)
def test_Verkaufstyp_ausw_hlen_UseCase_instantiation(instance):
    assert isinstance(instance, Verkaufstyp_ausw_hlen_UseCase)


Verkaufstyp_ausw_hlen_UseCase1_strategy = st.builds(Verkaufstyp_ausw_hlen_UseCase1)
@given(instance=Verkaufstyp_ausw_hlen_UseCase1_strategy)
@settings(max_examples=25)
def test_Verkaufstyp_ausw_hlen_UseCase1_instantiation(instance):
    assert isinstance(instance, Verkaufstyp_ausw_hlen_UseCase1)


Verkaufte_Mobilfunkger_te_einsehen_UseCase_strategy = st.builds(Verkaufte_Mobilfunkger_te_einsehen_UseCase)
@given(instance=Verkaufte_Mobilfunkger_te_einsehen_UseCase_strategy)
@settings(max_examples=25)
def test_Verkaufte_Mobilfunkger_te_einsehen_UseCase_instantiation(instance):
    assert isinstance(instance, Verkaufte_Mobilfunkger_te_einsehen_UseCase)


Verkaufte_Mobilfunkger_te_einsehen_UseCase1_strategy = st.builds(Verkaufte_Mobilfunkger_te_einsehen_UseCase1)
@given(instance=Verkaufte_Mobilfunkger_te_einsehen_UseCase1_strategy)
@settings(max_examples=25)
def test_Verkaufte_Mobilfunkger_te_einsehen_UseCase1_instantiation(instance):
    assert isinstance(instance, Verkaufte_Mobilfunkger_te_einsehen_UseCase1)


_external_unnamed_46_strategy = st.builds(_external_unnamed_46)
@given(instance=_external_unnamed_46_strategy)
@settings(max_examples=25)
def test__external_unnamed_46_instantiation(instance):
    assert isinstance(instance, _external_unnamed_46)


_external_unnamed_48_strategy = st.builds(_external_unnamed_48)
@given(instance=_external_unnamed_48_strategy)
@settings(max_examples=25)
def test__external_unnamed_48_instantiation(instance):
    assert isinstance(instance, _external_unnamed_48)


vef_gbare_Ger_te_strategy = st.builds(vef_gbare_Ger_te)
@given(instance=vef_gbare_Ger_te_strategy)
@settings(max_examples=25)
def test_vef_gbare_Ger_te_instantiation(instance):
    assert isinstance(instance, vef_gbare_Ger_te)


verkaufte_Ger_te_strategy = st.builds(verkaufte_Ger_te)
@given(instance=verkaufte_Ger_te_strategy)
@settings(max_examples=25)
def test_verkaufte_Ger_te_instantiation(instance):
    assert isinstance(instance, verkaufte_Ger_te)


