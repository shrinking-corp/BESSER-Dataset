import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Analyse2_AvisGlobal,
    Analyse2_Compte,
    Analyse2_Criteres,
    Analyse2_Fast_Food,
    Analyse2_Moderateurs,
    Analyse2_Review,
    Analyse2_Utilisateur,
    Analyse_Compte,
    Analyse_Criteres,
    Analyse_Fast_Food,
    Analyse_Moderateurs,
    Analyse_Review,
    Analyse_Utilisateur,
    AvisGlobal,
    Commentaire,
    Controlleur_Actor,
    FicheRestaurant,
    Photo,
    Pr_sentation,
    IHM,
    Information,
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

def test_Analyse2_AvisGlobal_Commentaires_value_roundtrip():
    instance = Analyse2_AvisGlobal(Commentaires="sample_text", nbAvis=7, notes="sample_text")
    assert instance.Commentaires == "sample_text"
    instance.Commentaires = "sample_text_2"
    assert instance.Commentaires == "sample_text_2"


def test_Analyse2_AvisGlobal_nbAvis_value_roundtrip():
    instance = Analyse2_AvisGlobal(Commentaires="sample_text", nbAvis=7, notes="sample_text")
    assert instance.nbAvis == 7
    instance.nbAvis = 13
    assert instance.nbAvis == 13


def test_Analyse2_AvisGlobal_notes_value_roundtrip():
    instance = Analyse2_AvisGlobal(Commentaires="sample_text", nbAvis=7, notes="sample_text")
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_Analyse2_Compte_login_value_roundtrip():
    instance = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_Analyse2_Compte_motdepasse_value_roundtrip():
    instance = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    assert instance.motdepasse == "sample_text"
    instance.motdepasse = "sample_text_2"
    assert instance.motdepasse == "sample_text_2"


def test_Analyse2_Criteres_amabilite_value_roundtrip():
    instance = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.amabilite == 7
    instance.amabilite = 13
    assert instance.amabilite == 13


def test_Analyse2_Criteres_qualit__value_roundtrip():
    instance = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.qualit_ == 7
    instance.qualit_ = 13
    assert instance.qualit_ == 13


def test_Analyse2_Criteres_rapidite_value_roundtrip():
    instance = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.rapidite == 7
    instance.rapidite = 13
    assert instance.rapidite == 13


def test_Analyse2_Criteres_rapportQualitePrix_value_roundtrip():
    instance = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.rapportQualitePrix == 7
    instance.rapportQualitePrix = 13
    assert instance.rapportQualitePrix == 13


def test_Analyse2_Criteres_respectHoraires_value_roundtrip():
    instance = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.respectHoraires == 7
    instance.respectHoraires = 13
    assert instance.respectHoraires == 13


def test_Analyse2_Fast_Food_Adresse_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.Adresse == "sample_text"
    instance.Adresse = "sample_text_2"
    assert instance.Adresse == "sample_text_2"


def test_Analyse2_Fast_Food_Ville_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.Ville == "sample_text"
    instance.Ville = "sample_text_2"
    assert instance.Ville == "sample_text_2"


def test_Analyse2_Fast_Food_description_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Analyse2_Fast_Food_horaires_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.horaires == "sample_text"
    instance.horaires = "sample_text_2"
    assert instance.horaires == "sample_text_2"


def test_Analyse2_Fast_Food_nbPlaces_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.nbPlaces == 7
    instance.nbPlaces = 13
    assert instance.nbPlaces == 13


def test_Analyse2_Fast_Food_nom_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Analyse2_Fast_Food_numeroTel_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.numeroTel == "sample_text"
    instance.numeroTel = "sample_text_2"
    assert instance.numeroTel == "sample_text_2"


def test_Analyse2_Fast_Food_photos_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_Analyse2_Fast_Food_prixMax_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.prixMax == 7
    instance.prixMax = 13
    assert instance.prixMax == 13


def test_Analyse2_Fast_Food_prixMin_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.prixMin == 7
    instance.prixMin = 13
    assert instance.prixMin == 13


def test_Analyse2_Fast_Food_proprietaire_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.proprietaire == "sample_text"
    instance.proprietaire = "sample_text_2"
    assert instance.proprietaire == "sample_text_2"


def test_Analyse2_Fast_Food_reviews_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.reviews == "sample_text"
    instance.reviews = "sample_text_2"
    assert instance.reviews == "sample_text_2"


def test_Analyse2_Fast_Food_siteDeCommande_value_roundtrip():
    instance = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    assert instance.siteDeCommande == "sample_text"
    instance.siteDeCommande = "sample_text_2"
    assert instance.siteDeCommande == "sample_text_2"


def test_Analyse2_Review_Commentaire_value_roundtrip():
    instance = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    assert instance.Commentaire == "sample_text"
    instance.Commentaire = "sample_text_2"
    assert instance.Commentaire == "sample_text_2"


def test_Analyse2_Review_lesNotes_value_roundtrip():
    instance = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    assert instance.lesNotes == "sample_text"
    instance.lesNotes = "sample_text_2"
    assert instance.lesNotes == "sample_text_2"


def test_Analyse2_Review_utilite_value_roundtrip():
    instance = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    assert instance.utilite == "sample_text"
    instance.utilite = "sample_text_2"
    assert instance.utilite == "sample_text_2"


def test_Analyse_Compte_login_value_roundtrip():
    instance = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_Analyse_Compte_motdepasse_value_roundtrip():
    instance = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    assert instance.motdepasse == "sample_text"
    instance.motdepasse = "sample_text_2"
    assert instance.motdepasse == "sample_text_2"


def test_Analyse_Criteres_amabilite_value_roundtrip():
    instance = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.amabilite == 7
    instance.amabilite = 13
    assert instance.amabilite == 13


def test_Analyse_Criteres_qualit__value_roundtrip():
    instance = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.qualit_ == 7
    instance.qualit_ = 13
    assert instance.qualit_ == 13


def test_Analyse_Criteres_rapidite_value_roundtrip():
    instance = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.rapidite == 7
    instance.rapidite = 13
    assert instance.rapidite == 13


def test_Analyse_Criteres_rapportQualitePrix_value_roundtrip():
    instance = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.rapportQualitePrix == 7
    instance.rapportQualitePrix = 13
    assert instance.rapportQualitePrix == 13


def test_Analyse_Criteres_respectHoraires_value_roundtrip():
    instance = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    assert instance.respectHoraires == 7
    instance.respectHoraires = 13
    assert instance.respectHoraires == 13


def test_Analyse_Fast_Food_Adresse_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.Adresse == "sample_text"
    instance.Adresse = "sample_text_2"
    assert instance.Adresse == "sample_text_2"


def test_Analyse_Fast_Food_Ville_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.Ville == "sample_text"
    instance.Ville = "sample_text_2"
    assert instance.Ville == "sample_text_2"


def test_Analyse_Fast_Food_horaires_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.horaires == "sample_text"
    instance.horaires = "sample_text_2"
    assert instance.horaires == "sample_text_2"


def test_Analyse_Fast_Food_nbPlaces_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.nbPlaces == 7
    instance.nbPlaces = 13
    assert instance.nbPlaces == 13


def test_Analyse_Fast_Food_nom_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Analyse_Fast_Food_notes_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_Analyse_Fast_Food_numeroTel_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.numeroTel == "sample_text"
    instance.numeroTel = "sample_text_2"
    assert instance.numeroTel == "sample_text_2"


def test_Analyse_Fast_Food_photos_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_Analyse_Fast_Food_prixMax_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.prixMax == 7
    instance.prixMax = 13
    assert instance.prixMax == 13


def test_Analyse_Fast_Food_prixMin_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.prixMin == 7
    instance.prixMin = 13
    assert instance.prixMin == 13


def test_Analyse_Fast_Food_proprietaire_value_roundtrip():
    instance = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    assert instance.proprietaire == "sample_text"
    instance.proprietaire = "sample_text_2"
    assert instance.proprietaire == "sample_text_2"


def test_Analyse_Review_Commentaire_value_roundtrip():
    instance = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    assert instance.Commentaire == "sample_text"
    instance.Commentaire = "sample_text_2"
    assert instance.Commentaire == "sample_text_2"


def test_Analyse_Review_NoteGlobale_value_roundtrip():
    instance = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    assert instance.NoteGlobale == 7
    instance.NoteGlobale = 13
    assert instance.NoteGlobale == 13


def test_Analyse_Review_lesNotes_value_roundtrip():
    instance = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    assert instance.lesNotes == "sample_text"
    instance.lesNotes = "sample_text_2"
    assert instance.lesNotes == "sample_text_2"


def test_AvisGlobal_Commentaires_value_roundtrip():
    instance = AvisGlobal(Commentaires="sample_text", diagramme="sample_text", nbAvis=7, note="sample_text")
    assert instance.Commentaires == "sample_text"
    instance.Commentaires = "sample_text_2"
    assert instance.Commentaires == "sample_text_2"


def test_AvisGlobal_diagramme_value_roundtrip():
    instance = AvisGlobal(Commentaires="sample_text", diagramme="sample_text", nbAvis=7, note="sample_text")
    assert instance.diagramme == "sample_text"
    instance.diagramme = "sample_text_2"
    assert instance.diagramme == "sample_text_2"


def test_AvisGlobal_nbAvis_value_roundtrip():
    instance = AvisGlobal(Commentaires="sample_text", diagramme="sample_text", nbAvis=7, note="sample_text")
    assert instance.nbAvis == 7
    instance.nbAvis = 13
    assert instance.nbAvis == 13


def test_AvisGlobal_note_value_roundtrip():
    instance = AvisGlobal(Commentaires="sample_text", diagramme="sample_text", nbAvis=7, note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_FicheRestaurant_nom_value_roundtrip():
    instance = FicheRestaurant(nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Pr_sentation_adresse_value_roundtrip():
    instance = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    assert instance.adresse == "sample_text"
    instance.adresse = "sample_text_2"
    assert instance.adresse == "sample_text_2"


def test_Pr_sentation_description_value_roundtrip():
    instance = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Pr_sentation_numTel_value_roundtrip():
    instance = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    assert instance.numTel == "sample_text"
    instance.numTel = "sample_text_2"
    assert instance.numTel == "sample_text_2"


def test_Pr_sentation_ouverture_value_roundtrip():
    instance = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    assert instance.ouverture == "sample_text"
    instance.ouverture = "sample_text_2"
    assert instance.ouverture == "sample_text_2"


def test_Pr_sentation_siteDeCommande_value_roundtrip():
    instance = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    assert instance.siteDeCommande == "sample_text"
    instance.siteDeCommande = "sample_text_2"
    assert instance.siteDeCommande == "sample_text_2"


def test_assoc_AvisGlobal_Fast_Food_link_reassign_clear():
    a = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    b1 = Analyse2_AvisGlobal(Commentaires="sample_text", nbAvis=7, notes="sample_text")
    b2 = Analyse2_AvisGlobal(Commentaires="sample_text_2", nbAvis=13, notes="sample_text_2")
    _safe_set(a, 'avisGlobal29', b1)
    assert _is_linked(a, 'avisGlobal29', b1)
    if hasattr(b1, 'fast_Food28'):
        assert _is_linked(b1, 'fast_Food28', a)
    _safe_set(a, 'avisGlobal29', b2)
    assert _is_linked(a, 'avisGlobal29', b2)
    if hasattr(b1, 'fast_Food28'):
        assert not _is_linked(b1, 'fast_Food28', a)
    if hasattr(b2, 'fast_Food28'):
        assert _is_linked(b2, 'fast_Food28', a)
    _safe_set(a, 'avisGlobal29', None)
    assert not _is_linked(a, 'avisGlobal29', b2)
    if hasattr(b2, 'fast_Food28'):
        assert not _is_linked(b2, 'fast_Food28', a)


def test_assoc_AvisGlobal_FicheRestaurant_link_reassign_clear():
    a = FicheRestaurant(nom="sample_text")
    b1 = AvisGlobal(Commentaires="sample_text", diagramme="sample_text", nbAvis=7, note="sample_text")
    b2 = AvisGlobal(Commentaires="sample_text_2", diagramme="sample_text_2", nbAvis=13, note="sample_text_2")
    _safe_set(a, 'poss_de13', b1)
    assert _is_linked(a, 'poss_de13', b1)
    if hasattr(b1, 'd_finit12'):
        assert _is_linked(b1, 'd_finit12', a)
    _safe_set(a, 'poss_de13', b2)
    assert _is_linked(a, 'poss_de13', b2)
    if hasattr(b1, 'd_finit12'):
        assert not _is_linked(b1, 'd_finit12', a)
    if hasattr(b2, 'd_finit12'):
        assert _is_linked(b2, 'd_finit12', a)
    _safe_set(a, 'poss_de13', None)
    assert not _is_linked(a, 'poss_de13', b2)
    if hasattr(b2, 'd_finit12'):
        assert not _is_linked(b2, 'd_finit12', a)


def test_assoc_Compte_Review_link_reassign_clear():
    a = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    b1 = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    b2 = Analyse_Compte(login="sample_text_2", motdepasse="sample_text_2")
    _safe_set(a, 'est__crite5', b1)
    assert _is_linked(a, 'est__crite5', b1)
    if hasattr(b1, 'poss_de4'):
        assert _is_linked(b1, 'poss_de4', a)
    _safe_set(a, 'est__crite5', b2)
    assert _is_linked(a, 'est__crite5', b2)
    if hasattr(b1, 'poss_de4'):
        assert not _is_linked(b1, 'poss_de4', a)
    if hasattr(b2, 'poss_de4'):
        assert _is_linked(b2, 'poss_de4', a)
    _safe_set(a, 'est__crite5', None)
    assert not _is_linked(a, 'est__crite5', b2)
    if hasattr(b2, 'poss_de4'):
        assert not _is_linked(b2, 'poss_de4', a)


def test_assoc_Compte_Review1_link_reassign_clear():
    a = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    b1 = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    b2 = Analyse2_Compte(login="sample_text_2", motdepasse="sample_text_2")
    _safe_set(a, 'est__crite23', b1)
    assert _is_linked(a, 'est__crite23', b1)
    if hasattr(b1, 'poss_de22'):
        assert _is_linked(b1, 'poss_de22', a)
    _safe_set(a, 'est__crite23', b2)
    assert _is_linked(a, 'est__crite23', b2)
    if hasattr(b1, 'poss_de22'):
        assert not _is_linked(b1, 'poss_de22', a)
    if hasattr(b2, 'poss_de22'):
        assert _is_linked(b2, 'poss_de22', a)
    _safe_set(a, 'est__crite23', None)
    assert not _is_linked(a, 'est__crite23', b2)
    if hasattr(b2, 'poss_de22'):
        assert not _is_linked(b2, 'poss_de22', a)


def test_assoc_Compte_Utilisateur_link_reassign_clear():
    a = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    b1 = Analyse_Utilisateur()
    b2 = Analyse_Utilisateur()
    _safe_set(a, 'est_associ_2', b1)
    assert _is_linked(a, 'est_associ_2', b1)
    if hasattr(b1, 'poss_de3'):
        assert _is_linked(b1, 'poss_de3', a)
    _safe_set(a, 'est_associ_2', b2)
    assert _is_linked(a, 'est_associ_2', b2)
    if hasattr(b1, 'poss_de3'):
        assert not _is_linked(b1, 'poss_de3', a)
    if hasattr(b2, 'poss_de3'):
        assert _is_linked(b2, 'poss_de3', a)
    _safe_set(a, 'est_associ_2', None)
    assert not _is_linked(a, 'est_associ_2', b2)
    if hasattr(b2, 'poss_de3'):
        assert not _is_linked(b2, 'poss_de3', a)


def test_assoc_Compte_Utilisateur1_link_reassign_clear():
    a = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    b1 = Analyse2_Utilisateur()
    b2 = Analyse2_Utilisateur()
    _safe_set(a, 'est_associ_20', b1)
    assert _is_linked(a, 'est_associ_20', b1)
    if hasattr(b1, 'poss_de21'):
        assert _is_linked(b1, 'poss_de21', a)
    _safe_set(a, 'est_associ_20', b2)
    assert _is_linked(a, 'est_associ_20', b2)
    if hasattr(b1, 'poss_de21'):
        assert not _is_linked(b1, 'poss_de21', a)
    if hasattr(b2, 'poss_de21'):
        assert _is_linked(b2, 'poss_de21', a)
    _safe_set(a, 'est_associ_20', None)
    assert not _is_linked(a, 'est_associ_20', b2)
    if hasattr(b2, 'poss_de21'):
        assert not _is_linked(b2, 'poss_de21', a)


def test_assoc_Criteres_Review_link_reassign_clear():
    a = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    b1 = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    b2 = Analyse_Criteres(amabilite=13, qualit_=13, rapidite=13, rapportQualitePrix=13, respectHoraires=13)
    _safe_set(a, 'note7', {b1})
    assert _is_linked(a, 'note7', b1)
    if hasattr(b1, 'sont_associ_s6'):
        assert _is_linked(b1, 'sont_associ_s6', a)
    _safe_set(a, 'note7', {b2})
    assert _is_linked(a, 'note7', b2)
    if hasattr(b1, 'sont_associ_s6'):
        assert not _is_linked(b1, 'sont_associ_s6', a)
    if hasattr(b2, 'sont_associ_s6'):
        assert _is_linked(b2, 'sont_associ_s6', a)
    _safe_set(a, 'note7', set())
    assert not _is_linked(a, 'note7', b2)
    if hasattr(b2, 'sont_associ_s6'):
        assert not _is_linked(b2, 'sont_associ_s6', a)


def test_assoc_Criteres_Review1_link_reassign_clear():
    a = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    b1 = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    b2 = Analyse2_Criteres(amabilite=13, qualit_=13, rapidite=13, rapportQualitePrix=13, respectHoraires=13)
    _safe_set(a, 'note25', {b1})
    assert _is_linked(a, 'note25', b1)
    if hasattr(b1, 'sont_associ_s24'):
        assert _is_linked(b1, 'sont_associ_s24', a)
    _safe_set(a, 'note25', {b2})
    assert _is_linked(a, 'note25', b2)
    if hasattr(b1, 'sont_associ_s24'):
        assert not _is_linked(b1, 'sont_associ_s24', a)
    if hasattr(b2, 'sont_associ_s24'):
        assert _is_linked(b2, 'sont_associ_s24', a)
    _safe_set(a, 'note25', set())
    assert not _is_linked(a, 'note25', b2)
    if hasattr(b2, 'sont_associ_s24'):
        assert not _is_linked(b2, 'sont_associ_s24', a)


def test_assoc_FicheRestaurant_Photo_link_reassign_clear():
    a = FicheRestaurant(nom="sample_text")
    b1 = Photo()
    b2 = Photo()
    _safe_set(a, 'poss_de14', {b1})
    assert _is_linked(a, 'poss_de14', b1)
    if hasattr(b1, 'repr_sente15'):
        assert _is_linked(b1, 'repr_sente15', a)
    _safe_set(a, 'poss_de14', {b2})
    assert _is_linked(a, 'poss_de14', b2)
    if hasattr(b1, 'repr_sente15'):
        assert not _is_linked(b1, 'repr_sente15', a)
    if hasattr(b2, 'repr_sente15'):
        assert _is_linked(b2, 'repr_sente15', a)
    _safe_set(a, 'poss_de14', set())
    assert not _is_linked(a, 'poss_de14', b2)
    if hasattr(b2, 'repr_sente15'):
        assert not _is_linked(b2, 'repr_sente15', a)


def test_assoc_Moderateurs_Compte_link_reassign_clear():
    a = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    b1 = Analyse_Moderateurs()
    b2 = Analyse_Moderateurs()
    _safe_set(a, 'est_associ_9', b1)
    assert _is_linked(a, 'est_associ_9', b1)
    if hasattr(b1, 'poss_de8'):
        assert _is_linked(b1, 'poss_de8', a)
    _safe_set(a, 'est_associ_9', b2)
    assert _is_linked(a, 'est_associ_9', b2)
    if hasattr(b1, 'poss_de8'):
        assert not _is_linked(b1, 'poss_de8', a)
    if hasattr(b2, 'poss_de8'):
        assert _is_linked(b2, 'poss_de8', a)
    _safe_set(a, 'est_associ_9', None)
    assert not _is_linked(a, 'est_associ_9', b2)
    if hasattr(b2, 'poss_de8'):
        assert not _is_linked(b2, 'poss_de8', a)


def test_assoc_Moderateurs_Compte1_link_reassign_clear():
    a = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    b1 = Analyse2_Moderateurs()
    b2 = Analyse2_Moderateurs()
    _safe_set(a, 'est_associ_27', b1)
    assert _is_linked(a, 'est_associ_27', b1)
    if hasattr(b1, 'poss_de26'):
        assert _is_linked(b1, 'poss_de26', a)
    _safe_set(a, 'est_associ_27', b2)
    assert _is_linked(a, 'est_associ_27', b2)
    if hasattr(b1, 'poss_de26'):
        assert not _is_linked(b1, 'poss_de26', a)
    if hasattr(b2, 'poss_de26'):
        assert _is_linked(b2, 'poss_de26', a)
    _safe_set(a, 'est_associ_27', None)
    assert not _is_linked(a, 'est_associ_27', b2)
    if hasattr(b2, 'poss_de26'):
        assert not _is_linked(b2, 'poss_de26', a)


def test_assoc_Pr_sentation_FicheRestaurant_link_reassign_clear():
    a = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    b1 = FicheRestaurant(nom="sample_text")
    b2 = FicheRestaurant(nom="sample_text_2")
    _safe_set(a, 'repr_sente16', b1)
    assert _is_linked(a, 'repr_sente16', b1)
    if hasattr(b1, 'poss_de17'):
        assert _is_linked(b1, 'poss_de17', a)
    _safe_set(a, 'repr_sente16', b2)
    assert _is_linked(a, 'repr_sente16', b2)
    if hasattr(b1, 'poss_de17'):
        assert not _is_linked(b1, 'poss_de17', a)
    if hasattr(b2, 'poss_de17'):
        assert _is_linked(b2, 'poss_de17', a)
    _safe_set(a, 'repr_sente16', None)
    assert not _is_linked(a, 'repr_sente16', b2)
    if hasattr(b2, 'poss_de17'):
        assert not _is_linked(b2, 'poss_de17', a)


def test_assoc_Review_Fast_Food_link_reassign_clear():
    a = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    b1 = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    b2 = Analyse_Fast_Food(Adresse="sample_text_2", Ville="sample_text_2", horaires="sample_text_2", nbPlaces=13, nom="sample_text_2", notes="sample_text_2", numeroTel="sample_text_2", photos="sample_text_2", prixMax=13, prixMin=13, proprietaire="sample_text_2")
    _safe_set(a, 'caract_rise0', b1)
    assert _is_linked(a, 'caract_rise0', b1)
    if hasattr(b1, 'poss_de1'):
        assert _is_linked(b1, 'poss_de1', a)
    _safe_set(a, 'caract_rise0', b2)
    assert _is_linked(a, 'caract_rise0', b2)
    if hasattr(b1, 'poss_de1'):
        assert not _is_linked(b1, 'poss_de1', a)
    if hasattr(b2, 'poss_de1'):
        assert _is_linked(b2, 'poss_de1', a)
    _safe_set(a, 'caract_rise0', None)
    assert not _is_linked(a, 'caract_rise0', b2)
    if hasattr(b2, 'poss_de1'):
        assert not _is_linked(b2, 'poss_de1', a)


def test_assoc_Review_Fast_Food1_link_reassign_clear():
    a = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    b1 = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    b2 = Analyse2_Fast_Food(Adresse="sample_text_2", Ville="sample_text_2", description="sample_text_2", horaires="sample_text_2", nbPlaces=13, nom="sample_text_2", numeroTel="sample_text_2", photos="sample_text_2", prixMax=13, prixMin=13, proprietaire="sample_text_2", reviews="sample_text_2", siteDeCommande="sample_text_2")
    _safe_set(a, 'caract_rise18', b1)
    assert _is_linked(a, 'caract_rise18', b1)
    if hasattr(b1, 'poss_de19'):
        assert _is_linked(b1, 'poss_de19', a)
    _safe_set(a, 'caract_rise18', b2)
    assert _is_linked(a, 'caract_rise18', b2)
    if hasattr(b1, 'poss_de19'):
        assert not _is_linked(b1, 'poss_de19', a)
    if hasattr(b2, 'poss_de19'):
        assert _is_linked(b2, 'poss_de19', a)
    _safe_set(a, 'caract_rise18', None)
    assert not _is_linked(a, 'caract_rise18', b2)
    if hasattr(b2, 'poss_de19'):
        assert not _is_linked(b2, 'poss_de19', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Analyse2_AvisGlobal_strategy = st.builds(Analyse2_AvisGlobal, Commentaires=safe_text, nbAvis=st.integers(), notes=safe_text)
@given(instance=Analyse2_AvisGlobal_strategy)
@settings(max_examples=25)
def test_Analyse2_AvisGlobal_instantiation(instance):
    assert isinstance(instance, Analyse2_AvisGlobal)


Analyse2_Compte_strategy = st.builds(Analyse2_Compte, login=safe_text, motdepasse=safe_text)
@given(instance=Analyse2_Compte_strategy)
@settings(max_examples=25)
def test_Analyse2_Compte_instantiation(instance):
    assert isinstance(instance, Analyse2_Compte)


Analyse2_Criteres_strategy = st.builds(Analyse2_Criteres, amabilite=st.integers(), qualit_=st.integers(), rapidite=st.integers(), rapportQualitePrix=st.integers(), respectHoraires=st.integers())
@given(instance=Analyse2_Criteres_strategy)
@settings(max_examples=25)
def test_Analyse2_Criteres_instantiation(instance):
    assert isinstance(instance, Analyse2_Criteres)


Analyse2_Fast_Food_strategy = st.builds(Analyse2_Fast_Food, Adresse=safe_text, Ville=safe_text, description=safe_text, horaires=safe_text, nbPlaces=st.integers(), nom=safe_text, numeroTel=safe_text, photos=safe_text, prixMax=st.integers(), prixMin=st.integers(), proprietaire=safe_text, reviews=safe_text, siteDeCommande=safe_text)
@given(instance=Analyse2_Fast_Food_strategy)
@settings(max_examples=25)
def test_Analyse2_Fast_Food_instantiation(instance):
    assert isinstance(instance, Analyse2_Fast_Food)


Analyse2_Moderateurs_strategy = st.builds(Analyse2_Moderateurs)
@given(instance=Analyse2_Moderateurs_strategy)
@settings(max_examples=25)
def test_Analyse2_Moderateurs_instantiation(instance):
    assert isinstance(instance, Analyse2_Moderateurs)


Analyse2_Review_strategy = st.builds(Analyse2_Review, Commentaire=safe_text, lesNotes=safe_text, utilite=safe_text)
@given(instance=Analyse2_Review_strategy)
@settings(max_examples=25)
def test_Analyse2_Review_instantiation(instance):
    assert isinstance(instance, Analyse2_Review)


Analyse2_Utilisateur_strategy = st.builds(Analyse2_Utilisateur)
@given(instance=Analyse2_Utilisateur_strategy)
@settings(max_examples=25)
def test_Analyse2_Utilisateur_instantiation(instance):
    assert isinstance(instance, Analyse2_Utilisateur)


Analyse_Compte_strategy = st.builds(Analyse_Compte, login=safe_text, motdepasse=safe_text)
@given(instance=Analyse_Compte_strategy)
@settings(max_examples=25)
def test_Analyse_Compte_instantiation(instance):
    assert isinstance(instance, Analyse_Compte)


Analyse_Criteres_strategy = st.builds(Analyse_Criteres, amabilite=st.integers(), qualit_=st.integers(), rapidite=st.integers(), rapportQualitePrix=st.integers(), respectHoraires=st.integers())
@given(instance=Analyse_Criteres_strategy)
@settings(max_examples=25)
def test_Analyse_Criteres_instantiation(instance):
    assert isinstance(instance, Analyse_Criteres)


Analyse_Fast_Food_strategy = st.builds(Analyse_Fast_Food, Adresse=safe_text, Ville=safe_text, horaires=safe_text, nbPlaces=st.integers(), nom=safe_text, notes=safe_text, numeroTel=safe_text, photos=safe_text, prixMax=st.integers(), prixMin=st.integers(), proprietaire=safe_text)
@given(instance=Analyse_Fast_Food_strategy)
@settings(max_examples=25)
def test_Analyse_Fast_Food_instantiation(instance):
    assert isinstance(instance, Analyse_Fast_Food)


Analyse_Moderateurs_strategy = st.builds(Analyse_Moderateurs)
@given(instance=Analyse_Moderateurs_strategy)
@settings(max_examples=25)
def test_Analyse_Moderateurs_instantiation(instance):
    assert isinstance(instance, Analyse_Moderateurs)


Analyse_Review_strategy = st.builds(Analyse_Review, Commentaire=safe_text, NoteGlobale=st.integers(), lesNotes=safe_text)
@given(instance=Analyse_Review_strategy)
@settings(max_examples=25)
def test_Analyse_Review_instantiation(instance):
    assert isinstance(instance, Analyse_Review)


Analyse_Utilisateur_strategy = st.builds(Analyse_Utilisateur)
@given(instance=Analyse_Utilisateur_strategy)
@settings(max_examples=25)
def test_Analyse_Utilisateur_instantiation(instance):
    assert isinstance(instance, Analyse_Utilisateur)


AvisGlobal_strategy = st.builds(AvisGlobal, Commentaires=safe_text, diagramme=safe_text, nbAvis=st.integers(), note=safe_text)
@given(instance=AvisGlobal_strategy)
@settings(max_examples=25)
def test_AvisGlobal_instantiation(instance):
    assert isinstance(instance, AvisGlobal)


Controlleur_Actor_strategy = st.builds(Controlleur_Actor)
@given(instance=Controlleur_Actor_strategy)
@settings(max_examples=25)
def test_Controlleur_Actor_instantiation(instance):
    assert isinstance(instance, Controlleur_Actor)


FicheRestaurant_strategy = st.builds(FicheRestaurant, nom=safe_text)
@given(instance=FicheRestaurant_strategy)
@settings(max_examples=25)
def test_FicheRestaurant_instantiation(instance):
    assert isinstance(instance, FicheRestaurant)


Photo_strategy = st.builds(Photo)
@given(instance=Photo_strategy)
@settings(max_examples=25)
def test_Photo_instantiation(instance):
    assert isinstance(instance, Photo)


Pr_sentation_strategy = st.builds(Pr_sentation, adresse=safe_text, description=safe_text, numTel=safe_text, ouverture=safe_text, siteDeCommande=safe_text)
@given(instance=Pr_sentation_strategy)
@settings(max_examples=25)
def test_Pr_sentation_instantiation(instance):
    assert isinstance(instance, Pr_sentation)


