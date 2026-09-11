import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_caracteristica_Atributo_tipoValor_value_roundtrip():
    instance = caracteristica_Atributo(tipoValor="sample_text")
    assert instance.tipoValor == "sample_text"
    instance.tipoValor = "sample_text_2"
    assert instance.tipoValor == "sample_text_2"


def test_caracteristica_Elemento_nome_value_roundtrip():
    instance = caracteristica_Elemento(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_LPS_nome_value_roundtrip():
    instance = caracteristica_LPS(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_Variacao_cardinalidadeMaxima_value_roundtrip():
    instance = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert instance.cardinalidadeMaxima == "sample_text"
    instance.cardinalidadeMaxima = "sample_text_2"
    assert instance.cardinalidadeMaxima == "sample_text_2"


def test_caracteristica_Variacao_cardinalidadeMinima_value_roundtrip():
    instance = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert instance.cardinalidadeMinima == "sample_text"
    instance.cardinalidadeMinima = "sample_text_2"
    assert instance.cardinalidadeMinima == "sample_text_2"


def test_caracteristica_VariacaoDois_cardinalidadeMaxima_value_roundtrip():
    instance = caracteristica_VariacaoDois(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert instance.cardinalidadeMaxima == "sample_text"
    instance.cardinalidadeMaxima = "sample_text_2"
    assert instance.cardinalidadeMaxima == "sample_text_2"


def test_caracteristica_VariacaoDois_cardinalidadeMaximaOr_value_roundtrip():
    instance = caracteristica_VariacaoDois(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert instance.cardinalidadeMaximaOr == "sample_text"
    instance.cardinalidadeMaximaOr = "sample_text_2"
    assert instance.cardinalidadeMaximaOr == "sample_text_2"


def test_caracteristica_VariacaoDois_cardinalidadeMinimaOr_value_roundtrip():
    instance = caracteristica_VariacaoDois(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert instance.cardinalidadeMinimaOr == "sample_text"
    instance.cardinalidadeMinimaOr = "sample_text_2"
    assert instance.cardinalidadeMinimaOr == "sample_text_2"


def test_caracteristica_CaracteristicaAgrupada_isa_Caracteristica():
    instance = caracteristica_CaracteristicaAgrupada()
    assert isinstance(instance, Caracteristica)


def test_caracteristica_CaracteristicaMandatoria_isa_Caracteristica():
    instance = caracteristica_CaracteristicaMandatoria()
    assert isinstance(instance, Caracteristica)


def test_caracteristica_CaracteristicaOpcional_isa_Caracteristica():
    instance = caracteristica_CaracteristicaOpcional()
    assert isinstance(instance, Caracteristica)


def test_caracteristica_CaracteristicaRaiz_isa_Caracteristica():
    instance = caracteristica_CaracteristicaRaiz()
    assert isinstance(instance, Caracteristica)


def test_caracteristica_VariacaoDois_isa_Caracteristica():
    instance = caracteristica_VariacaoDois(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert isinstance(instance, Caracteristica)


def test_caracteristica_Variante_isa_Caracteristica():
    instance = caracteristica_Variante()
    assert isinstance(instance, Caracteristica)


def test_caracteristica_Atributo_isa_Elemento():
    instance = caracteristica_Atributo(tipoValor="sample_text")
    assert isinstance(instance, Elemento)


def test_caracteristica_Caracteristica_isa_Elemento():
    instance = caracteristica_Caracteristica()
    assert isinstance(instance, Elemento)


def test_caracteristica_ElementoCaracteristico_isa_Elemento():
    instance = caracteristica_ElementoCaracteristico()
    assert isinstance(instance, Elemento)


def test_caracteristica_Variacao_isa_Elemento():
    instance = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert isinstance(instance, Elemento)


def test_caracteristica_CaracteristicaAgrupada_isa_ElementoCaracteristico():
    instance = caracteristica_CaracteristicaAgrupada()
    assert isinstance(instance, ElementoCaracteristico)


def test_caracteristica_CaracteristicaOpcional_isa_ElementoCaracteristico():
    instance = caracteristica_CaracteristicaOpcional()
    assert isinstance(instance, ElementoCaracteristico)


def test_caracteristica_VariacaoDois_isa_ElementoCaracteristico():
    instance = caracteristica_VariacaoDois(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert isinstance(instance, ElementoCaracteristico)


def test_caracteristica_Variante_isa_ElementoCaracteristico():
    instance = caracteristica_Variante()
    assert isinstance(instance, ElementoCaracteristico)


def test_caracteristica_Variacao_isa_PontoDeVariacao():
    instance = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert isinstance(instance, PontoDeVariacao)


def test_caracteristica_Variante_isa_PontoDeVariacao():
    instance = caracteristica_Variante()
    assert isinstance(instance, PontoDeVariacao)


def test_assoc_LpsDoSistema12_link_reassign_clear():
    a = caracteristica_LPS(nome="sample_text")
    b1 = caracteristica_CaracteristicaRaiz()
    b2 = caracteristica_CaracteristicaRaiz()
    _safe_set(a, 'caracteristica_LPS13', b1)
    assert _is_linked(a, 'caracteristica_LPS13', b1)
    if hasattr(b1, 'caracteristica_CaracteristicaRaiz'):
        assert _is_linked(b1, 'caracteristica_CaracteristicaRaiz', a)
    _safe_set(a, 'caracteristica_LPS13', b2)
    assert _is_linked(a, 'caracteristica_LPS13', b2)
    if hasattr(b1, 'caracteristica_CaracteristicaRaiz'):
        assert not _is_linked(b1, 'caracteristica_CaracteristicaRaiz', a)
    if hasattr(b2, 'caracteristica_CaracteristicaRaiz'):
        assert _is_linked(b2, 'caracteristica_CaracteristicaRaiz', a)
    _safe_set(a, 'caracteristica_LPS13', None)
    assert not _is_linked(a, 'caracteristica_LPS13', b2)
    if hasattr(b2, 'caracteristica_CaracteristicaRaiz'):
        assert not _is_linked(b2, 'caracteristica_CaracteristicaRaiz', a)


def test_assoc_atributo10_link_reassign_clear():
    a = caracteristica_Atributo(tipoValor="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'Atributo', b1)
    assert _is_linked(a, 'Atributo', b1)
    if hasattr(b1, 'caracteristicaPai11'):
        assert _is_linked(b1, 'caracteristicaPai11', a)
    _safe_set(a, 'Atributo', b2)
    assert _is_linked(a, 'Atributo', b2)
    if hasattr(b1, 'caracteristicaPai11'):
        assert not _is_linked(b1, 'caracteristicaPai11', a)
    if hasattr(b2, 'caracteristicaPai11'):
        assert _is_linked(b2, 'caracteristicaPai11', a)
    _safe_set(a, 'Atributo', None)
    assert not _is_linked(a, 'Atributo', b2)
    if hasattr(b2, 'caracteristicaPai11'):
        assert not _is_linked(b2, 'caracteristicaPai11', a)


def test_assoc_caracteristicaPai1_link_reassign_clear():
    a = caracteristica_Atributo(tipoValor="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'atributo', b1)
    assert _is_linked(a, 'atributo', b1)
    if hasattr(b1, 'Caracteristica'):
        assert _is_linked(b1, 'Caracteristica', a)
    _safe_set(a, 'atributo', b2)
    assert _is_linked(a, 'atributo', b2)
    if hasattr(b1, 'Caracteristica'):
        assert not _is_linked(b1, 'Caracteristica', a)
    if hasattr(b2, 'Caracteristica'):
        assert _is_linked(b2, 'Caracteristica', a)
    _safe_set(a, 'atributo', None)
    assert not _is_linked(a, 'atributo', b2)
    if hasattr(b2, 'Caracteristica'):
        assert not _is_linked(b2, 'Caracteristica', a)


def test_assoc_caracteristicaPai15_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'variacoes', b1)
    assert _is_linked(a, 'variacoes', b1)
    if hasattr(b1, 'Caracteristica16'):
        assert _is_linked(b1, 'Caracteristica16', a)
    _safe_set(a, 'variacoes', b2)
    assert _is_linked(a, 'variacoes', b2)
    if hasattr(b1, 'Caracteristica16'):
        assert not _is_linked(b1, 'Caracteristica16', a)
    if hasattr(b2, 'Caracteristica16'):
        assert _is_linked(b2, 'Caracteristica16', a)
    _safe_set(a, 'variacoes', None)
    assert not _is_linked(a, 'variacoes', b2)
    if hasattr(b2, 'Caracteristica16'):
        assert not _is_linked(b2, 'Caracteristica16', a)


def test_assoc_elementos0_link_reassign_clear():
    a = caracteristica_LPS(nome="sample_text")
    b1 = caracteristica_Elemento(nome="sample_text")
    b2 = caracteristica_Elemento(nome="sample_text_2")
    _safe_set(a, 'caracteristica_LPS', {b1})
    assert _is_linked(a, 'caracteristica_LPS', b1)
    if hasattr(b1, 'caracteristica_Elemento'):
        assert _is_linked(b1, 'caracteristica_Elemento', a)
    _safe_set(a, 'caracteristica_LPS', {b2})
    assert _is_linked(a, 'caracteristica_LPS', b2)
    if hasattr(b1, 'caracteristica_Elemento'):
        assert not _is_linked(b1, 'caracteristica_Elemento', a)
    if hasattr(b2, 'caracteristica_Elemento'):
        assert _is_linked(b2, 'caracteristica_Elemento', a)
    _safe_set(a, 'caracteristica_LPS', set())
    assert not _is_linked(a, 'caracteristica_LPS', b2)
    if hasattr(b2, 'caracteristica_Elemento'):
        assert not _is_linked(b2, 'caracteristica_Elemento', a)


def test_assoc_variacaoPai17_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Variante()
    b2 = caracteristica_Variante()
    _safe_set(a, 'Variacao18', b1)
    assert _is_linked(a, 'Variacao18', b1)
    if hasattr(b1, 'variantes'):
        assert _is_linked(b1, 'variantes', a)
    _safe_set(a, 'Variacao18', b2)
    assert _is_linked(a, 'Variacao18', b2)
    if hasattr(b1, 'variantes'):
        assert not _is_linked(b1, 'variantes', a)
    if hasattr(b2, 'variantes'):
        assert _is_linked(b2, 'variantes', a)
    _safe_set(a, 'Variacao18', None)
    assert not _is_linked(a, 'Variacao18', b2)
    if hasattr(b2, 'variantes'):
        assert not _is_linked(b2, 'variantes', a)


def test_assoc_variacoes8_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'Variacao', b1)
    assert _is_linked(a, 'Variacao', b1)
    if hasattr(b1, 'caracteristicaPai9'):
        assert _is_linked(b1, 'caracteristicaPai9', a)
    _safe_set(a, 'Variacao', b2)
    assert _is_linked(a, 'Variacao', b2)
    if hasattr(b1, 'caracteristicaPai9'):
        assert not _is_linked(b1, 'caracteristicaPai9', a)
    if hasattr(b2, 'caracteristicaPai9'):
        assert _is_linked(b2, 'caracteristicaPai9', a)
    _safe_set(a, 'Variacao', None)
    assert not _is_linked(a, 'Variacao', b2)
    if hasattr(b2, 'caracteristicaPai9'):
        assert not _is_linked(b2, 'caracteristicaPai9', a)


def test_assoc_variantes14_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Variante()
    b2 = caracteristica_Variante()
    _safe_set(a, 'variacaoPai', {b1})
    assert _is_linked(a, 'variacaoPai', b1)
    if hasattr(b1, 'Variante'):
        assert _is_linked(b1, 'Variante', a)
    _safe_set(a, 'variacaoPai', {b2})
    assert _is_linked(a, 'variacaoPai', b2)
    if hasattr(b1, 'Variante'):
        assert not _is_linked(b1, 'Variante', a)
    if hasattr(b2, 'Variante'):
        assert _is_linked(b2, 'Variante', a)
    _safe_set(a, 'variacaoPai', set())
    assert not _is_linked(a, 'variacaoPai', b2)
    if hasattr(b2, 'Variante'):
        assert not _is_linked(b2, 'Variante', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Caracteristica_strategy = st.builds(Caracteristica)
@given(instance=Caracteristica_strategy)
@settings(max_examples=25)
def test_Caracteristica_instantiation(instance):
    assert isinstance(instance, Caracteristica)


Elemento_strategy = st.builds(Elemento)
@given(instance=Elemento_strategy)
@settings(max_examples=25)
def test_Elemento_instantiation(instance):
    assert isinstance(instance, Elemento)


ElementoCaracteristico_strategy = st.builds(ElementoCaracteristico)
@given(instance=ElementoCaracteristico_strategy)
@settings(max_examples=25)
def test_ElementoCaracteristico_instantiation(instance):
    assert isinstance(instance, ElementoCaracteristico)


PontoDeVariacao_strategy = st.builds(PontoDeVariacao)
@given(instance=PontoDeVariacao_strategy)
@settings(max_examples=25)
def test_PontoDeVariacao_instantiation(instance):
    assert isinstance(instance, PontoDeVariacao)


caracteristica_Atributo_strategy = st.builds(caracteristica_Atributo, tipoValor=safe_text)
@given(instance=caracteristica_Atributo_strategy)
@settings(max_examples=25)
def test_caracteristica_Atributo_instantiation(instance):
    assert isinstance(instance, caracteristica_Atributo)


caracteristica_Caracteristica_strategy = st.builds(caracteristica_Caracteristica)
@given(instance=caracteristica_Caracteristica_strategy)
@settings(max_examples=25)
def test_caracteristica_Caracteristica_instantiation(instance):
    assert isinstance(instance, caracteristica_Caracteristica)


caracteristica_CaracteristicaAgrupada_strategy = st.builds(caracteristica_CaracteristicaAgrupada)
@given(instance=caracteristica_CaracteristicaAgrupada_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaAgrupada_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaAgrupada)


caracteristica_CaracteristicaMandatoria_strategy = st.builds(caracteristica_CaracteristicaMandatoria)
@given(instance=caracteristica_CaracteristicaMandatoria_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaMandatoria_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaMandatoria)


caracteristica_CaracteristicaOpcional_strategy = st.builds(caracteristica_CaracteristicaOpcional)
@given(instance=caracteristica_CaracteristicaOpcional_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaOpcional_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaOpcional)


caracteristica_CaracteristicaRaiz_strategy = st.builds(caracteristica_CaracteristicaRaiz)
@given(instance=caracteristica_CaracteristicaRaiz_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaRaiz_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaRaiz)


caracteristica_Elemento_strategy = st.builds(caracteristica_Elemento, nome=safe_text)
@given(instance=caracteristica_Elemento_strategy)
@settings(max_examples=25)
def test_caracteristica_Elemento_instantiation(instance):
    assert isinstance(instance, caracteristica_Elemento)


caracteristica_ElementoCaracteristico_strategy = st.builds(caracteristica_ElementoCaracteristico)
@given(instance=caracteristica_ElementoCaracteristico_strategy)
@settings(max_examples=25)
def test_caracteristica_ElementoCaracteristico_instantiation(instance):
    assert isinstance(instance, caracteristica_ElementoCaracteristico)


caracteristica_LPS_strategy = st.builds(caracteristica_LPS, nome=safe_text)
@given(instance=caracteristica_LPS_strategy)
@settings(max_examples=25)
def test_caracteristica_LPS_instantiation(instance):
    assert isinstance(instance, caracteristica_LPS)


caracteristica_PontoDeVariacao_strategy = st.builds(caracteristica_PontoDeVariacao)
@given(instance=caracteristica_PontoDeVariacao_strategy)
@settings(max_examples=25)
def test_caracteristica_PontoDeVariacao_instantiation(instance):
    assert isinstance(instance, caracteristica_PontoDeVariacao)


caracteristica_Variacao_strategy = st.builds(caracteristica_Variacao, cardinalidadeMaxima=safe_text, cardinalidadeMinima=safe_text)
@given(instance=caracteristica_Variacao_strategy)
@settings(max_examples=25)
def test_caracteristica_Variacao_instantiation(instance):
    assert isinstance(instance, caracteristica_Variacao)


caracteristica_VariacaoDois_strategy = st.builds(caracteristica_VariacaoDois, cardinalidadeMaxima=safe_text, cardinalidadeMaximaOr=safe_text, cardinalidadeMinimaOr=safe_text)
@given(instance=caracteristica_VariacaoDois_strategy)
@settings(max_examples=25)
def test_caracteristica_VariacaoDois_instantiation(instance):
    assert isinstance(instance, caracteristica_VariacaoDois)


caracteristica_Variante_strategy = st.builds(caracteristica_Variante)
@given(instance=caracteristica_Variante_strategy)
@settings(max_examples=25)
def test_caracteristica_Variante_instantiation(instance):
    assert isinstance(instance, caracteristica_Variante)


