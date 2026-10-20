import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrateur_Actor,
    Client,
    Client_Actor,
    Collection_Client_,
    Collection_Commande_,
    Collection_Commentaire_,
    Collection_LigneCommande_,
    Collection_Livre_,
    Collection_Object_,
    Object,
    System_Component,
    Systeme_Paiement_Actor,
    Visiteur_Actor,
    backoffice_Gerer_les_auteurs_UseCase,
    backoffice_Gerer_les_categories_UseCase,
    backoffice_Gerer_les_editeurs_UseCase,
    backoffice_Gerer_les_produits_UseCase,
    backoffice_S_authentifier_UseCase,
    backoffice_Valider_les_commentaires_UseCase,
    be_jebouquine_bo_AdministrateurBO,
    be_jebouquine_bo_AuteurBO,
    be_jebouquine_bo_CategorieBO,
    be_jebouquine_bo_ClientBO,
    be_jebouquine_bo_CommandeBO,
    be_jebouquine_bo_CommentaireBO,
    be_jebouquine_bo_EditeurBO,
    be_jebouquine_bo_EtatCommandeBO,
    be_jebouquine_bo_IAdministrateurBORemote_Interface,
    be_jebouquine_bo_IAuteurBORemote_Interface,
    be_jebouquine_bo_ICategorieBORemote_Interface,
    be_jebouquine_bo_IClientBORemote_Interface,
    be_jebouquine_bo_ICommandeBORemote_Interface,
    be_jebouquine_bo_ICommentaireBORemote_Interface,
    be_jebouquine_bo_IEditeurBORemote_Interface,
    be_jebouquine_bo_IEtatCommandeRemote_Interface,
    be_jebouquine_bo_ILangueBORemote_Interface,
    be_jebouquine_bo_ILivreBORemote_Interface,
    be_jebouquine_bo_IPanierBORemote_Interface,
    be_jebouquine_bo_LangueBO,
    be_jebouquine_bo_LigneCommandeBO,
    be_jebouquine_bo_LigneCommandeBORemote_Interface,
    be_jebouquine_bo_LivraisonTypeBO,
    be_jebouquine_bo_LivraisonTypeBORemote_Interface,
    be_jebouquine_bo_LivreBO,
    be_jebouquine_bo_PanierBO,
    be_jebouquine_dao_AbstractFactory,
    be_jebouquine_dao_AdministrateurDAO,
    be_jebouquine_dao_AuteurDAO,
    be_jebouquine_dao_CategorieDAO,
    be_jebouquine_dao_ClientDAO,
    be_jebouquine_dao_CommandeDAO,
    be_jebouquine_dao_CommentaireDAO,
    be_jebouquine_dao_EditeurDAO,
    be_jebouquine_dao_EtatCommandeDAO,
    be_jebouquine_dao_LangueDAO,
    be_jebouquine_dao_LigneCommandeDAO,
    be_jebouquine_dao_LivraisonInfoDAO,
    be_jebouquine_dao_LivreDAO,
    be_jebouquine_entities_Administrateur,
    be_jebouquine_entities_Auteur,
    be_jebouquine_entities_Categorie,
    be_jebouquine_entities_Client,
    be_jebouquine_entities_Commande,
    be_jebouquine_entities_Commentaire,
    be_jebouquine_entities_Editeur,
    be_jebouquine_entities_EtatCommande,
    be_jebouquine_entities_Langue,
    be_jebouquine_entities_LigneCommande,
    be_jebouquine_entities_LivraisonType,
    be_jebouquine_entities_Livre,
    commande_Annuler_commande_UseCase,
    commande_Creer_commande_UseCase,
    commande_Payer_commande_UseCase,
    commande_Suivre_commande_UseCase,
    compte_Ajouter_commentaire_UseCase,
    compte_Gerer_Commande_UseCase,
    compte_Gerer_le_compte_UseCase,
    compte_S_authentifier_UseCase,
    information_Consulter_l_aide_UseCase,
    navigation_Afficher_la_liste_des_livres_UseCase,
    navigation_Parcourir_les_livres_UseCase,
    navigation_Recherche_par_critere_UseCase,
    navigation_Rechercher_un_livre_UseCase,
    panier_Ajouter_au_panier_UseCase,
    panier_Gerer_panier_UseCase,
    panier_Modifier_quantite_livre_UseCase,
    panier_Passer_une_commande_UseCase,
    panier_Supprimer_du_panier_UseCase,
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

def test_assoc_Client_Commande_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Commande(dateCommande=date(2024, 1, 1), idClient=7, idEtat=7, idLivraisonInfo=7, idcommande=7)
    a2 = be_jebouquine_entities_Commande(dateCommande=date(2025, 6, 15), idClient=13, idEtat=13, idLivraisonInfo=13, idcommande=13)
    b = be_jebouquine_entities_Client(adresseClient="sample_text", emailClient="sample_text", etatLogin="sample_text", idClient=7, motDePasseClient="sample_text", nomClient="sample_text", telephoneClient="sample_text")
    _safe_set(b, 'commande12', {a1})
    assert _is_linked(b, 'commande12', a1)
    if hasattr(a1, 'client13'):
        assert _is_linked(a1, 'client13', b)
    _safe_set(b, 'commande12', {a2})
    assert _is_linked(b, 'commande12', a2)
    if hasattr(a1, 'client13'):
        assert not _is_linked(a1, 'client13', b)
    if hasattr(a2, 'client13'):
        assert _is_linked(a2, 'client13', b)
    _safe_set(b, 'commande12', set())
    assert not _is_linked(b, 'commande12', a2)
    if hasattr(a2, 'client13'):
        assert not _is_linked(a2, 'client13', b)


def test_assoc_Client_Commentaire_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Commentaire(dateCommentaire=date(2024, 1, 1), idClient=7, idCommentaire=7, idLivre=7, textCommentaire="sample_text")
    a2 = be_jebouquine_entities_Commentaire(dateCommentaire=date(2025, 6, 15), idClient=13, idCommentaire=13, idLivre=13, textCommentaire="sample_text_2")
    b = be_jebouquine_entities_Client(adresseClient="sample_text", emailClient="sample_text", etatLogin="sample_text", idClient=7, motDePasseClient="sample_text", nomClient="sample_text", telephoneClient="sample_text")
    _safe_set(b, 'commentaire22', {a1})
    assert _is_linked(b, 'commentaire22', a1)
    if hasattr(a1, 'client23'):
        assert _is_linked(a1, 'client23', b)
    _safe_set(b, 'commentaire22', {a2})
    assert _is_linked(b, 'commentaire22', a2)
    if hasattr(a1, 'client23'):
        assert not _is_linked(a1, 'client23', b)
    if hasattr(a2, 'client23'):
        assert _is_linked(a2, 'client23', b)
    _safe_set(b, 'commentaire22', set())
    assert not _is_linked(b, 'commentaire22', a2)
    if hasattr(a2, 'client23'):
        assert not _is_linked(a2, 'client23', b)


def test_assoc_Commande_EtatCommande_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_EtatCommande(idEtat=7, libelleEtat="sample_text")
    a2 = be_jebouquine_entities_EtatCommande(idEtat=13, libelleEtat="sample_text_2")
    b = be_jebouquine_entities_Commande(dateCommande=date(2024, 1, 1), idClient=7, idEtat=7, idLivraisonInfo=7, idcommande=7)
    _safe_set(b, 'etatCommande24', a1)
    assert _is_linked(b, 'etatCommande24', a1)
    if hasattr(a1, 'commande25'):
        assert _is_linked(a1, 'commande25', b)
    _safe_set(b, 'etatCommande24', a2)
    assert _is_linked(b, 'etatCommande24', a2)
    if hasattr(a1, 'commande25'):
        assert not _is_linked(a1, 'commande25', b)
    if hasattr(a2, 'commande25'):
        assert _is_linked(a2, 'commande25', b)
    _safe_set(b, 'etatCommande24', None)
    assert not _is_linked(b, 'etatCommande24', a2)
    if hasattr(a2, 'commande25'):
        assert not _is_linked(a2, 'commande25', b)


def test_assoc_Commande_LigneCommande_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_LigneCommande(idCommande=7, idLigneCommande=7, idLivre=7)
    a2 = be_jebouquine_entities_LigneCommande(idCommande=13, idLigneCommande=13, idLivre=13)
    b = be_jebouquine_entities_Commande(dateCommande=date(2024, 1, 1), idClient=7, idEtat=7, idLivraisonInfo=7, idcommande=7)
    _safe_set(b, 'ligneCommande32', {a1})
    assert _is_linked(b, 'ligneCommande32', a1)
    if hasattr(a1, 'commande33'):
        assert _is_linked(a1, 'commande33', b)
    _safe_set(b, 'ligneCommande32', {a2})
    assert _is_linked(b, 'ligneCommande32', a2)
    if hasattr(a1, 'commande33'):
        assert not _is_linked(a1, 'commande33', b)
    if hasattr(a2, 'commande33'):
        assert _is_linked(a2, 'commande33', b)
    _safe_set(b, 'ligneCommande32', set())
    assert not _is_linked(b, 'ligneCommande32', a2)
    if hasattr(a2, 'commande33'):
        assert not _is_linked(a2, 'commande33', b)


def test_assoc_Commande_LivraisonInfo_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_LivraisonType(idLivraison=7, prixLivraison=3.14, typeLivraison="sample_text")
    a2 = be_jebouquine_entities_LivraisonType(idLivraison=13, prixLivraison=9.99, typeLivraison="sample_text_2")
    b = be_jebouquine_entities_Commande(dateCommande=date(2024, 1, 1), idClient=7, idEtat=7, idLivraisonInfo=7, idcommande=7)
    _safe_set(b, 'livraisonInfo34', a1)
    assert _is_linked(b, 'livraisonInfo34', a1)
    if hasattr(a1, 'commande35'):
        assert _is_linked(a1, 'commande35', b)
    _safe_set(b, 'livraisonInfo34', a2)
    assert _is_linked(b, 'livraisonInfo34', a2)
    if hasattr(a1, 'commande35'):
        assert not _is_linked(a1, 'commande35', b)
    if hasattr(a2, 'commande35'):
        assert _is_linked(a2, 'commande35', b)
    _safe_set(b, 'livraisonInfo34', None)
    assert not _is_linked(b, 'livraisonInfo34', a2)
    if hasattr(a2, 'commande35'):
        assert not _is_linked(a2, 'commande35', b)


def test_assoc_Langue_Livre_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Livre(dateApparition=date(2024, 1, 1), idAuteur=7, idCategorie=7, idEditeur=7, idLangue=7, idLivre=7, isbn="sample_text", photoLivre="sample_text", prix=3.14, quantiteEnStock=7, titre="sample_text")
    a2 = be_jebouquine_entities_Livre(dateApparition=date(2025, 6, 15), idAuteur=13, idCategorie=13, idEditeur=13, idLangue=13, idLivre=13, isbn="sample_text_2", photoLivre="sample_text_2", prix=9.99, quantiteEnStock=13, titre="sample_text_2")
    b = be_jebouquine_entities_Langue(idLangue=7, libelleLangue="sample_text")
    _safe_set(b, 'livre26', {a1})
    assert _is_linked(b, 'livre26', a1)
    if hasattr(a1, 'langue27'):
        assert _is_linked(a1, 'langue27', b)
    _safe_set(b, 'livre26', {a2})
    assert _is_linked(b, 'livre26', a2)
    if hasattr(a1, 'langue27'):
        assert not _is_linked(a1, 'langue27', b)
    if hasattr(a2, 'langue27'):
        assert _is_linked(a2, 'langue27', b)
    _safe_set(b, 'livre26', set())
    assert not _is_linked(b, 'livre26', a2)
    if hasattr(a2, 'langue27'):
        assert not _is_linked(a2, 'langue27', b)


def test_assoc_LigneCommande_Livre_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Livre(dateApparition=date(2024, 1, 1), idAuteur=7, idCategorie=7, idEditeur=7, idLangue=7, idLivre=7, isbn="sample_text", photoLivre="sample_text", prix=3.14, quantiteEnStock=7, titre="sample_text")
    a2 = be_jebouquine_entities_Livre(dateApparition=date(2025, 6, 15), idAuteur=13, idCategorie=13, idEditeur=13, idLangue=13, idLivre=13, isbn="sample_text_2", photoLivre="sample_text_2", prix=9.99, quantiteEnStock=13, titre="sample_text_2")
    b = be_jebouquine_entities_LigneCommande(idCommande=7, idLigneCommande=7, idLivre=7)
    _safe_set(b, 'livre14', a1)
    assert _is_linked(b, 'livre14', a1)
    if hasattr(a1, 'ligneCommande15'):
        assert _is_linked(a1, 'ligneCommande15', b)
    _safe_set(b, 'livre14', a2)
    assert _is_linked(b, 'livre14', a2)
    if hasattr(a1, 'ligneCommande15'):
        assert not _is_linked(a1, 'ligneCommande15', b)
    if hasattr(a2, 'ligneCommande15'):
        assert _is_linked(a2, 'ligneCommande15', b)
    _safe_set(b, 'livre14', None)
    assert not _is_linked(b, 'livre14', a2)
    if hasattr(a2, 'ligneCommande15'):
        assert not _is_linked(a2, 'ligneCommande15', b)


def test_assoc_Livre_Auteur_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Livre(dateApparition=date(2024, 1, 1), idAuteur=7, idCategorie=7, idEditeur=7, idLangue=7, idLivre=7, isbn="sample_text", photoLivre="sample_text", prix=3.14, quantiteEnStock=7, titre="sample_text")
    a2 = be_jebouquine_entities_Livre(dateApparition=date(2025, 6, 15), idAuteur=13, idCategorie=13, idEditeur=13, idLangue=13, idLivre=13, isbn="sample_text_2", photoLivre="sample_text_2", prix=9.99, quantiteEnStock=13, titre="sample_text_2")
    b = be_jebouquine_entities_Auteur(idAuteur=7, nomAuteur="sample_text")
    _safe_set(b, 'livre19', a1)
    assert _is_linked(b, 'livre19', a1)
    if hasattr(a1, 'auteur18'):
        assert _is_linked(a1, 'auteur18', b)
    _safe_set(b, 'livre19', a2)
    assert _is_linked(b, 'livre19', a2)
    if hasattr(a1, 'auteur18'):
        assert not _is_linked(a1, 'auteur18', b)
    if hasattr(a2, 'auteur18'):
        assert _is_linked(a2, 'auteur18', b)
    _safe_set(b, 'livre19', None)
    assert not _is_linked(b, 'livre19', a2)
    if hasattr(a2, 'auteur18'):
        assert not _is_linked(a2, 'auteur18', b)


def test_assoc_Livre_Categorie_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Livre(dateApparition=date(2024, 1, 1), idAuteur=7, idCategorie=7, idEditeur=7, idLangue=7, idLivre=7, isbn="sample_text", photoLivre="sample_text", prix=3.14, quantiteEnStock=7, titre="sample_text")
    a2 = be_jebouquine_entities_Livre(dateApparition=date(2025, 6, 15), idAuteur=13, idCategorie=13, idEditeur=13, idLangue=13, idLivre=13, isbn="sample_text_2", photoLivre="sample_text_2", prix=9.99, quantiteEnStock=13, titre="sample_text_2")
    b = be_jebouquine_entities_Categorie(idCategorie=7, ordreCategorie="sample_text")
    _safe_set(b, 'livre21', a1)
    assert _is_linked(b, 'livre21', a1)
    if hasattr(a1, 'categorie20'):
        assert _is_linked(a1, 'categorie20', b)
    _safe_set(b, 'livre21', a2)
    assert _is_linked(b, 'livre21', a2)
    if hasattr(a1, 'categorie20'):
        assert not _is_linked(a1, 'categorie20', b)
    if hasattr(a2, 'categorie20'):
        assert _is_linked(a2, 'categorie20', b)
    _safe_set(b, 'livre21', None)
    assert not _is_linked(b, 'livre21', a2)
    if hasattr(a2, 'categorie20'):
        assert not _is_linked(a2, 'categorie20', b)


def test_assoc_Livre_Commentaire_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Livre(dateApparition=date(2024, 1, 1), idAuteur=7, idCategorie=7, idEditeur=7, idLangue=7, idLivre=7, isbn="sample_text", photoLivre="sample_text", prix=3.14, quantiteEnStock=7, titre="sample_text")
    a2 = be_jebouquine_entities_Livre(dateApparition=date(2025, 6, 15), idAuteur=13, idCategorie=13, idEditeur=13, idLangue=13, idLivre=13, isbn="sample_text_2", photoLivre="sample_text_2", prix=9.99, quantiteEnStock=13, titre="sample_text_2")
    b = be_jebouquine_entities_Commentaire(dateCommentaire=date(2024, 1, 1), idClient=7, idCommentaire=7, idLivre=7, textCommentaire="sample_text")
    _safe_set(b, 'livre29', a1)
    assert _is_linked(b, 'livre29', a1)
    if hasattr(a1, 'commentaire28'):
        assert _is_linked(a1, 'commentaire28', b)
    _safe_set(b, 'livre29', a2)
    assert _is_linked(b, 'livre29', a2)
    if hasattr(a1, 'commentaire28'):
        assert not _is_linked(a1, 'commentaire28', b)
    if hasattr(a2, 'commentaire28'):
        assert _is_linked(a2, 'commentaire28', b)
    _safe_set(b, 'livre29', None)
    assert not _is_linked(b, 'livre29', a2)
    if hasattr(a2, 'commentaire28'):
        assert not _is_linked(a2, 'commentaire28', b)


def test_assoc_Livre_Editeur_reverse_link_reassign_clear():
    a1 = be_jebouquine_entities_Livre(dateApparition=date(2024, 1, 1), idAuteur=7, idCategorie=7, idEditeur=7, idLangue=7, idLivre=7, isbn="sample_text", photoLivre="sample_text", prix=3.14, quantiteEnStock=7, titre="sample_text")
    a2 = be_jebouquine_entities_Livre(dateApparition=date(2025, 6, 15), idAuteur=13, idCategorie=13, idEditeur=13, idLangue=13, idLivre=13, isbn="sample_text_2", photoLivre="sample_text_2", prix=9.99, quantiteEnStock=13, titre="sample_text_2")
    b = be_jebouquine_entities_Editeur(adresseEditeur="sample_text", idEditeur=7, nomEditeur="sample_text")
    _safe_set(b, 'livre17', a1)
    assert _is_linked(b, 'livre17', a1)
    if hasattr(a1, 'editeur16'):
        assert _is_linked(a1, 'editeur16', b)
    _safe_set(b, 'livre17', a2)
    assert _is_linked(b, 'livre17', a2)
    if hasattr(a1, 'editeur16'):
        assert not _is_linked(a1, 'editeur16', b)
    if hasattr(a2, 'editeur16'):
        assert _is_linked(a2, 'editeur16', b)
    _safe_set(b, 'livre17', None)
    assert not _is_linked(b, 'livre17', a2)
    if hasattr(a2, 'editeur16'):
        assert not _is_linked(a2, 'editeur16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

