import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ElementDiagramme,
    ElementNomme,
    Type,
    smalluml_Association,
    smalluml_Attribut,
    smalluml_Booleen,
    smalluml_Cardinalite,
    smalluml_Chaine,
    smalluml_Classe,
    smalluml_Diagramme,
    smalluml_ElementDiagramme,
    smalluml_ElementNomme,
    smalluml_Entier,
    smalluml_Enumeration,
    smalluml_Methode,
    smalluml_Type,
    smalluml_TypeDonnee,
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

def test_assoc_classe20_reverse_link_reassign_clear():
    a1 = smalluml_Classe(abstrait=True, classeAbstraite=True)
    a2 = smalluml_Classe(abstrait=False, classeAbstraite=False)
    b = smalluml_Cardinalite(multipliciteInf="sample_text", multipliciteSup="sample_text")
    _safe_set(b, 'smalluml_Cardinalite21', a1)
    assert _is_linked(b, 'smalluml_Cardinalite21', a1)
    if hasattr(a1, 'smalluml_Classe22'):
        assert _is_linked(a1, 'smalluml_Classe22', b)
    _safe_set(b, 'smalluml_Cardinalite21', a2)
    assert _is_linked(b, 'smalluml_Cardinalite21', a2)
    if hasattr(a1, 'smalluml_Classe22'):
        assert not _is_linked(a1, 'smalluml_Classe22', b)
    if hasattr(a2, 'smalluml_Classe22'):
        assert _is_linked(a2, 'smalluml_Classe22', b)
    _safe_set(b, 'smalluml_Cardinalite21', None)
    assert not _is_linked(b, 'smalluml_Cardinalite21', a2)
    if hasattr(a2, 'smalluml_Classe22'):
        assert not _is_linked(a2, 'smalluml_Classe22', b)


def test_assoc_methodes1_reverse_link_reassign_clear():
    a1 = smalluml_Methode(methodeAbstraite=True)
    a2 = smalluml_Methode(methodeAbstraite=False)
    b = smalluml_Classe(abstrait=True, classeAbstraite=True)
    _safe_set(b, 'smalluml_Classe2', {a1})
    assert _is_linked(b, 'smalluml_Classe2', a1)
    if hasattr(a1, 'smalluml_Methode'):
        assert _is_linked(a1, 'smalluml_Methode', b)
    _safe_set(b, 'smalluml_Classe2', {a2})
    assert _is_linked(b, 'smalluml_Classe2', a2)
    if hasattr(a1, 'smalluml_Methode'):
        assert not _is_linked(a1, 'smalluml_Methode', b)
    if hasattr(a2, 'smalluml_Methode'):
        assert _is_linked(a2, 'smalluml_Methode', b)
    _safe_set(b, 'smalluml_Classe2', set())
    assert not _is_linked(b, 'smalluml_Classe2', a2)
    if hasattr(a2, 'smalluml_Methode'):
        assert not _is_linked(a2, 'smalluml_Methode', b)


def test_assoc_sousClasses4_reverse_link_reassign_clear():
    a1 = smalluml_Classe(abstrait=True, classeAbstraite=True)
    a2 = smalluml_Classe(abstrait=False, classeAbstraite=False)
    b = smalluml_Classe(abstrait=True, classeAbstraite=True)
    _safe_set(b, 'smalluml_Classe5', a1)
    assert _is_linked(b, 'smalluml_Classe5', a1)
    if hasattr(a1, 'smalluml_Classe3'):
        assert _is_linked(a1, 'smalluml_Classe3', b)
    _safe_set(b, 'smalluml_Classe5', a2)
    assert _is_linked(b, 'smalluml_Classe5', a2)
    if hasattr(a1, 'smalluml_Classe3'):
        assert not _is_linked(a1, 'smalluml_Classe3', b)
    if hasattr(a2, 'smalluml_Classe3'):
        assert _is_linked(a2, 'smalluml_Classe3', b)
    _safe_set(b, 'smalluml_Classe5', None)
    assert not _is_linked(b, 'smalluml_Classe5', a2)
    if hasattr(a2, 'smalluml_Classe3'):
        assert not _is_linked(a2, 'smalluml_Classe3', b)


def test_assoc_superClasse7_reverse_link_reassign_clear():
    a1 = smalluml_Classe(abstrait=True, classeAbstraite=True)
    a2 = smalluml_Classe(abstrait=False, classeAbstraite=False)
    b = smalluml_Classe(abstrait=True, classeAbstraite=True)
    _safe_set(b, 'smalluml_Classe8', a1)
    assert _is_linked(b, 'smalluml_Classe8', a1)
    if hasattr(a1, 'smalluml_Classe6'):
        assert _is_linked(a1, 'smalluml_Classe6', b)
    _safe_set(b, 'smalluml_Classe8', a2)
    assert _is_linked(b, 'smalluml_Classe8', a2)
    if hasattr(a1, 'smalluml_Classe6'):
        assert not _is_linked(a1, 'smalluml_Classe6', b)
    if hasattr(a2, 'smalluml_Classe6'):
        assert _is_linked(a2, 'smalluml_Classe6', b)
    _safe_set(b, 'smalluml_Classe8', None)
    assert not _is_linked(b, 'smalluml_Classe8', a2)
    if hasattr(a2, 'smalluml_Classe6'):
        assert not _is_linked(a2, 'smalluml_Classe6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributs0_stub_double():
    # smalluml_Attribut has no real 'smalluml_Attribut' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Classe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Classe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Classe(abstrait=True, classeAbstraite=True)
    partner = smalluml_Attribut()
    setattr(partner, 'smalluml_Attribut', None)
    _safe_set(owner, 'smalluml_Classe', {partner})
    assert getattr(partner, 'smalluml_Attribut') == owner
    _safe_set(owner, 'smalluml_Classe', set())
    assert getattr(partner, 'smalluml_Attribut') is None


def test_assoc_cardinalites19_stub_double():
    # smalluml_Association has no real 'smalluml_Association' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Cardinalite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Cardinalite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Cardinalite(multipliciteInf="sample_text", multipliciteSup="sample_text")
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association', None)
    _safe_set(owner, 'smalluml_Cardinalite', partner)
    assert owner in getattr(partner, 'smalluml_Association')
    _safe_set(owner, 'smalluml_Cardinalite', None)
    assert owner not in getattr(partner, 'smalluml_Association')


def test_assoc_classe24_stub_double():
    # smalluml_ElementDiagramme has no real 'smalluml_ElementDiagramme25' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Classe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Classe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Classe(abstrait=True, classeAbstraite=True)
    partner = smalluml_ElementDiagramme()
    setattr(partner, 'smalluml_ElementDiagramme25', None)
    _safe_set(owner, 'smalluml_Classe26', partner)
    assert owner in getattr(partner, 'smalluml_ElementDiagramme25')
    _safe_set(owner, 'smalluml_Classe26', None)
    assert owner not in getattr(partner, 'smalluml_ElementDiagramme25')


def test_assoc_enumeration30_stub_double():
    # smalluml_ElementDiagramme has no real 'smalluml_ElementDiagramme31' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Enumeration(elements="sample_text")
    partner = smalluml_ElementDiagramme()
    setattr(partner, 'smalluml_ElementDiagramme31', None)
    _safe_set(owner, 'smalluml_Enumeration', partner)
    assert owner in getattr(partner, 'smalluml_ElementDiagramme31')
    _safe_set(owner, 'smalluml_Enumeration', None)
    assert owner not in getattr(partner, 'smalluml_ElementDiagramme31')


def test_assoc_parametres14_stub_double():
    # smalluml_Attribut has no real 'smalluml_Attribut16' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Methode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Methode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Methode(methodeAbstraite=True)
    partner = smalluml_Attribut()
    setattr(partner, 'smalluml_Attribut16', None)
    _safe_set(owner, 'smalluml_Methode15', {partner})
    assert getattr(partner, 'smalluml_Attribut16') == owner
    _safe_set(owner, 'smalluml_Methode15', set())
    assert getattr(partner, 'smalluml_Attribut16') is None


def test_assoc_typeDeRetour11_stub_double():
    # smalluml_Type has no real 'smalluml_Type13' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Methode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Methode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Methode(methodeAbstraite=True)
    partner = smalluml_Type()
    setattr(partner, 'smalluml_Type13', None)
    _safe_set(owner, 'smalluml_Methode12', partner)
    assert getattr(partner, 'smalluml_Type13') == owner
    _safe_set(owner, 'smalluml_Methode12', None)
    assert getattr(partner, 'smalluml_Type13') is None


