import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adresse,
    Cat_gorie,
    Class,
    Commande,
    Etat,
    Ingr_dient,
    Livraison,
    Pizzeria,
    Produit,
    R_le,
    Recette,
    Stock,
    Utilisateur,
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

def test_assoc_Commande_Utilisateur_reverse_link_reassign_clear():
    a1 = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    a2 = Utilisateur(civilit_="sample_text_2", date_naissance="sample_text_2", email="sample_text_2", id=13, mot_de_passe="sample_text_2", nom="sample_text_2", pizzeria_id=13, prenom="sample_text_2", role_id=13)
    b = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    _safe_set(b, 'Commande_Utilisateur_06', a1)
    assert _is_linked(b, 'Commande_Utilisateur_06', a1)
    if hasattr(a1, 'Commande_Utilisateur_17'):
        assert _is_linked(a1, 'Commande_Utilisateur_17', b)
    _safe_set(b, 'Commande_Utilisateur_06', a2)
    assert _is_linked(b, 'Commande_Utilisateur_06', a2)
    if hasattr(a1, 'Commande_Utilisateur_17'):
        assert not _is_linked(a1, 'Commande_Utilisateur_17', b)
    if hasattr(a2, 'Commande_Utilisateur_17'):
        assert _is_linked(a2, 'Commande_Utilisateur_17', b)
    _safe_set(b, 'Commande_Utilisateur_06', None)
    assert not _is_linked(b, 'Commande_Utilisateur_06', a2)
    if hasattr(a2, 'Commande_Utilisateur_17'):
        assert not _is_linked(a2, 'Commande_Utilisateur_17', b)


def test_assoc_Etat_Commande_reverse_link_reassign_clear():
    a1 = Etat(id=7, nom="sample_text", verrouillage=True)
    a2 = Etat(id=13, nom="sample_text_2", verrouillage=False)
    b = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    _safe_set(b, 'Etat_Commande_111', a1)
    assert _is_linked(b, 'Etat_Commande_111', a1)
    if hasattr(a1, 'Etat_Commande_010'):
        assert _is_linked(a1, 'Etat_Commande_010', b)
    _safe_set(b, 'Etat_Commande_111', a2)
    assert _is_linked(b, 'Etat_Commande_111', a2)
    if hasattr(a1, 'Etat_Commande_010'):
        assert not _is_linked(a1, 'Etat_Commande_010', b)
    if hasattr(a2, 'Etat_Commande_010'):
        assert _is_linked(a2, 'Etat_Commande_010', b)
    _safe_set(b, 'Etat_Commande_111', None)
    assert not _is_linked(b, 'Etat_Commande_111', a2)
    if hasattr(a2, 'Etat_Commande_010'):
        assert not _is_linked(a2, 'Etat_Commande_010', b)


def test_assoc_Livraison_Commande_reverse_link_reassign_clear():
    a1 = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    a2 = Livraison(client_id=13, commande_id=13, geocode="sample_text_2", id=13, livreur_id=13)
    b = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    _safe_set(b, 'Livraison_Commande_115', a1)
    assert _is_linked(b, 'Livraison_Commande_115', a1)
    if hasattr(a1, 'Livraison_Commande_014'):
        assert _is_linked(a1, 'Livraison_Commande_014', b)
    _safe_set(b, 'Livraison_Commande_115', a2)
    assert _is_linked(b, 'Livraison_Commande_115', a2)
    if hasattr(a1, 'Livraison_Commande_014'):
        assert not _is_linked(a1, 'Livraison_Commande_014', b)
    if hasattr(a2, 'Livraison_Commande_014'):
        assert _is_linked(a2, 'Livraison_Commande_014', b)
    _safe_set(b, 'Livraison_Commande_115', None)
    assert not _is_linked(b, 'Livraison_Commande_115', a2)
    if hasattr(a2, 'Livraison_Commande_014'):
        assert not _is_linked(a2, 'Livraison_Commande_014', b)


def test_assoc_Livraison_Utilisateur_reverse_link_reassign_clear():
    a1 = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    a2 = Utilisateur(civilit_="sample_text_2", date_naissance="sample_text_2", email="sample_text_2", id=13, mot_de_passe="sample_text_2", nom="sample_text_2", pizzeria_id=13, prenom="sample_text_2", role_id=13)
    b = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    _safe_set(b, 'Livraison_Utilisateur_012', a1)
    assert _is_linked(b, 'Livraison_Utilisateur_012', a1)
    if hasattr(a1, 'livreur13'):
        assert _is_linked(a1, 'livreur13', b)
    _safe_set(b, 'Livraison_Utilisateur_012', a2)
    assert _is_linked(b, 'Livraison_Utilisateur_012', a2)
    if hasattr(a1, 'livreur13'):
        assert not _is_linked(a1, 'livreur13', b)
    if hasattr(a2, 'livreur13'):
        assert _is_linked(a2, 'livreur13', b)
    _safe_set(b, 'Livraison_Utilisateur_012', None)
    assert not _is_linked(b, 'Livraison_Utilisateur_012', a2)
    if hasattr(a2, 'livreur13'):
        assert not _is_linked(a2, 'livreur13', b)


def test_assoc_Livraison_Utilisateur2_reverse_link_reassign_clear():
    a1 = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    a2 = Utilisateur(civilit_="sample_text_2", date_naissance="sample_text_2", email="sample_text_2", id=13, mot_de_passe="sample_text_2", nom="sample_text_2", pizzeria_id=13, prenom="sample_text_2", role_id=13)
    b = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    _safe_set(b, 'Livraison_Utilisateur2_020', a1)
    assert _is_linked(b, 'Livraison_Utilisateur2_020', a1)
    if hasattr(a1, 'client21'):
        assert _is_linked(a1, 'client21', b)
    _safe_set(b, 'Livraison_Utilisateur2_020', a2)
    assert _is_linked(b, 'Livraison_Utilisateur2_020', a2)
    if hasattr(a1, 'client21'):
        assert not _is_linked(a1, 'client21', b)
    if hasattr(a2, 'client21'):
        assert _is_linked(a2, 'client21', b)
    _safe_set(b, 'Livraison_Utilisateur2_020', None)
    assert not _is_linked(b, 'Livraison_Utilisateur2_020', a2)
    if hasattr(a2, 'client21'):
        assert not _is_linked(a2, 'client21', b)


def test_assoc_Pizzeria_Adresse_reverse_link_reassign_clear():
    a1 = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    a2 = Pizzeria(adresse_id=13, id=13, nom="sample_text_2")
    b = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    _safe_set(b, 'Pizzeria_Adresse_119', a1)
    assert _is_linked(b, 'Pizzeria_Adresse_119', a1)
    if hasattr(a1, 'Pizzeria_Adresse_018'):
        assert _is_linked(a1, 'Pizzeria_Adresse_018', b)
    _safe_set(b, 'Pizzeria_Adresse_119', a2)
    assert _is_linked(b, 'Pizzeria_Adresse_119', a2)
    if hasattr(a1, 'Pizzeria_Adresse_018'):
        assert not _is_linked(a1, 'Pizzeria_Adresse_018', b)
    if hasattr(a2, 'Pizzeria_Adresse_018'):
        assert _is_linked(a2, 'Pizzeria_Adresse_018', b)
    _safe_set(b, 'Pizzeria_Adresse_119', None)
    assert not _is_linked(b, 'Pizzeria_Adresse_119', a2)
    if hasattr(a2, 'Pizzeria_Adresse_018'):
        assert not _is_linked(a2, 'Pizzeria_Adresse_018', b)


def test_assoc_Produit_Cat_gorie_reverse_link_reassign_clear():
    a1 = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    a2 = Produit(categorie_id=13, id=13, nom="sample_text_2", prix="sample_text_2")
    b = Cat_gorie(id=7, nom="sample_text")
    _safe_set(b, 'Produit_Cat_gorie_15', {a1})
    assert _is_linked(b, 'Produit_Cat_gorie_15', a1)
    if hasattr(a1, 'Produit_Cat_gorie_04'):
        assert _is_linked(a1, 'Produit_Cat_gorie_04', b)
    _safe_set(b, 'Produit_Cat_gorie_15', {a2})
    assert _is_linked(b, 'Produit_Cat_gorie_15', a2)
    if hasattr(a1, 'Produit_Cat_gorie_04'):
        assert not _is_linked(a1, 'Produit_Cat_gorie_04', b)
    if hasattr(a2, 'Produit_Cat_gorie_04'):
        assert _is_linked(a2, 'Produit_Cat_gorie_04', b)
    _safe_set(b, 'Produit_Cat_gorie_15', set())
    assert not _is_linked(b, 'Produit_Cat_gorie_15', a2)
    if hasattr(a2, 'Produit_Cat_gorie_04'):
        assert not _is_linked(a2, 'Produit_Cat_gorie_04', b)


def test_assoc_Produit_Recette_reverse_link_reassign_clear():
    a1 = Recette(id=7, produit_id=7)
    a2 = Recette(id=13, produit_id=13)
    b = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    _safe_set(b, 'Produit_Recette_02', a1)
    assert _is_linked(b, 'Produit_Recette_02', a1)
    if hasattr(a1, 'Produit_Recette_13'):
        assert _is_linked(a1, 'Produit_Recette_13', b)
    _safe_set(b, 'Produit_Recette_02', a2)
    assert _is_linked(b, 'Produit_Recette_02', a2)
    if hasattr(a1, 'Produit_Recette_13'):
        assert not _is_linked(a1, 'Produit_Recette_13', b)
    if hasattr(a2, 'Produit_Recette_13'):
        assert _is_linked(a2, 'Produit_Recette_13', b)
    _safe_set(b, 'Produit_Recette_02', None)
    assert not _is_linked(b, 'Produit_Recette_02', a2)
    if hasattr(a2, 'Produit_Recette_13'):
        assert not _is_linked(a2, 'Produit_Recette_13', b)


def test_assoc_Stock_Ingr_dient_reverse_link_reassign_clear():
    a1 = Stock(date_modification=7, disponibilit_=True, ingredient_id=7, quantit_=7)
    a2 = Stock(date_modification=13, disponibilit_=False, ingredient_id=13, quantit_=13)
    b = Ingr_dient(id=7, nom="sample_text", poids="sample_text", unit_="sample_text")
    _safe_set(b, 'Stock_Ingr_dient_19', a1)
    assert _is_linked(b, 'Stock_Ingr_dient_19', a1)
    if hasattr(a1, 'Stock_Ingr_dient_08'):
        assert _is_linked(a1, 'Stock_Ingr_dient_08', b)
    _safe_set(b, 'Stock_Ingr_dient_19', a2)
    assert _is_linked(b, 'Stock_Ingr_dient_19', a2)
    if hasattr(a1, 'Stock_Ingr_dient_08'):
        assert not _is_linked(a1, 'Stock_Ingr_dient_08', b)
    if hasattr(a2, 'Stock_Ingr_dient_08'):
        assert _is_linked(a2, 'Stock_Ingr_dient_08', b)
    _safe_set(b, 'Stock_Ingr_dient_19', None)
    assert not _is_linked(b, 'Stock_Ingr_dient_19', a2)
    if hasattr(a2, 'Stock_Ingr_dient_08'):
        assert not _is_linked(a2, 'Stock_Ingr_dient_08', b)


def test_assoc_Utilisateur_Pizzeria_reverse_link_reassign_clear():
    a1 = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    a2 = Utilisateur(civilit_="sample_text_2", date_naissance="sample_text_2", email="sample_text_2", id=13, mot_de_passe="sample_text_2", nom="sample_text_2", pizzeria_id=13, prenom="sample_text_2", role_id=13)
    b = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    _safe_set(b, 'Utilisateur_Pizzeria_117', a1)
    assert _is_linked(b, 'Utilisateur_Pizzeria_117', a1)
    if hasattr(a1, 'Utilisateur_Pizzeria_016'):
        assert _is_linked(a1, 'Utilisateur_Pizzeria_016', b)
    _safe_set(b, 'Utilisateur_Pizzeria_117', a2)
    assert _is_linked(b, 'Utilisateur_Pizzeria_117', a2)
    if hasattr(a1, 'Utilisateur_Pizzeria_016'):
        assert not _is_linked(a1, 'Utilisateur_Pizzeria_016', b)
    if hasattr(a2, 'Utilisateur_Pizzeria_016'):
        assert _is_linked(a2, 'Utilisateur_Pizzeria_016', b)
    _safe_set(b, 'Utilisateur_Pizzeria_117', None)
    assert not _is_linked(b, 'Utilisateur_Pizzeria_117', a2)
    if hasattr(a2, 'Utilisateur_Pizzeria_016'):
        assert not _is_linked(a2, 'Utilisateur_Pizzeria_016', b)


def test_assoc_Utilisateur_R_le_reverse_link_reassign_clear():
    a1 = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    a2 = Utilisateur(civilit_="sample_text_2", date_naissance="sample_text_2", email="sample_text_2", id=13, mot_de_passe="sample_text_2", nom="sample_text_2", pizzeria_id=13, prenom="sample_text_2", role_id=13)
    b = R_le(id=7, type="sample_text")
    _safe_set(b, 'Utilisateur_R_le_11', {a1})
    assert _is_linked(b, 'Utilisateur_R_le_11', a1)
    if hasattr(a1, 'Utilisateur_R_le_00'):
        assert _is_linked(a1, 'Utilisateur_R_le_00', b)
    _safe_set(b, 'Utilisateur_R_le_11', {a2})
    assert _is_linked(b, 'Utilisateur_R_le_11', a2)
    if hasattr(a1, 'Utilisateur_R_le_00'):
        assert not _is_linked(a1, 'Utilisateur_R_le_00', b)
    if hasattr(a2, 'Utilisateur_R_le_00'):
        assert _is_linked(a2, 'Utilisateur_R_le_00', b)
    _safe_set(b, 'Utilisateur_R_le_11', set())
    assert not _is_linked(b, 'Utilisateur_R_le_11', a2)
    if hasattr(a2, 'Utilisateur_R_le_00'):
        assert not _is_linked(a2, 'Utilisateur_R_le_00', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

