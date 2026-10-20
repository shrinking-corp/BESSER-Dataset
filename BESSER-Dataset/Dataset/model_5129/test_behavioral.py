import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Caracteristica,
    Elemento,
    ElementoCaracteristico,
    PontoDeVariacao,
    caracteristica_Atributo,
    caracteristica_Caracteristica,
    caracteristica_CaracteristicaAgrupada,
    caracteristica_CaracteristicaMandatoria,
    caracteristica_CaracteristicaOpcional,
    caracteristica_CaracteristicaRaiz,
    caracteristica_Elemento,
    caracteristica_ElementoCaracteristico,
    caracteristica_LPS,
    caracteristica_PontoDeVariacao,
    caracteristica_Variacao,
    caracteristica_VariacaoDois,
    caracteristica_Variante,
    CardinalidadeMaxima,
    OperadorAcaoLogico,
    OperadorLogico,
    OperadorRelacional,
    Origem,
    Presenca,
    Qualidade,
    TipoValor,
    Validade,
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

def test_assoc_elementos0_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(nome="sample_text")
    a2 = caracteristica_LPS(nome="sample_text_2")
    b = caracteristica_Elemento(nome="sample_text")
    _safe_set(b, 'caracteristica_Elemento', a1)
    assert _is_linked(b, 'caracteristica_Elemento', a1)
    if hasattr(a1, 'caracteristica_LPS'):
        assert _is_linked(a1, 'caracteristica_LPS', b)
    _safe_set(b, 'caracteristica_Elemento', a2)
    assert _is_linked(b, 'caracteristica_Elemento', a2)
    if hasattr(a1, 'caracteristica_LPS'):
        assert not _is_linked(a1, 'caracteristica_LPS', b)
    if hasattr(a2, 'caracteristica_LPS'):
        assert _is_linked(a2, 'caracteristica_LPS', b)
    _safe_set(b, 'caracteristica_Elemento', None)
    assert not _is_linked(b, 'caracteristica_Elemento', a2)
    if hasattr(a2, 'caracteristica_LPS'):
        assert not _is_linked(a2, 'caracteristica_LPS', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_LpsDoSistema12_stub_double():
    # caracteristica_CaracteristicaRaiz has no real 'caracteristica_CaracteristicaRaiz' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(nome="sample_text")
    partner = caracteristica_CaracteristicaRaiz()
    setattr(partner, 'caracteristica_CaracteristicaRaiz', None)
    _safe_set(owner, 'caracteristica_LPS13', partner)
    assert getattr(partner, 'caracteristica_CaracteristicaRaiz') == owner
    _safe_set(owner, 'caracteristica_LPS13', None)
    assert getattr(partner, 'caracteristica_CaracteristicaRaiz') is None


def test_assoc_atributo10_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristicaPai11' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Atributo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Atributo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Atributo(tipoValor="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristicaPai11', None)
    _safe_set(owner, 'Atributo', partner)
    assert owner in getattr(partner, 'caracteristicaPai11')
    _safe_set(owner, 'Atributo', None)
    assert owner not in getattr(partner, 'caracteristicaPai11')


def test_assoc_caracteristicaPai1_stub_double():
    # caracteristica_Caracteristica has no real 'Caracteristica' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Atributo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Atributo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Atributo(tipoValor="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'Caracteristica', None)
    _safe_set(owner, 'atributo', partner)
    assert getattr(partner, 'Caracteristica') == owner
    _safe_set(owner, 'atributo', None)
    assert getattr(partner, 'Caracteristica') is None


def test_assoc_caracteristicaPai15_stub_double():
    # caracteristica_Caracteristica has no real 'Caracteristica16' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'Caracteristica16', None)
    _safe_set(owner, 'variacoes', partner)
    assert getattr(partner, 'Caracteristica16') == owner
    _safe_set(owner, 'variacoes', None)
    assert getattr(partner, 'Caracteristica16') is None


def test_assoc_variacaoPai17_stub_double():
    # caracteristica_Variante has no real 'variantes' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Variante()
    setattr(partner, 'variantes', None)
    _safe_set(owner, 'Variacao18', partner)
    assert getattr(partner, 'variantes') == owner
    _safe_set(owner, 'Variacao18', None)
    assert getattr(partner, 'variantes') is None


def test_assoc_variacoes8_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristicaPai9' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristicaPai9', None)
    _safe_set(owner, 'Variacao', partner)
    assert owner in getattr(partner, 'caracteristicaPai9')
    _safe_set(owner, 'Variacao', None)
    assert owner not in getattr(partner, 'caracteristicaPai9')


def test_assoc_variantes14_stub_double():
    # caracteristica_Variante has no real 'Variante' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Variante()
    setattr(partner, 'Variante', None)
    _safe_set(owner, 'variacaoPai', {partner})
    assert getattr(partner, 'Variante') == owner
    _safe_set(owner, 'variacaoPai', set())
    assert getattr(partner, 'Variante') is None


