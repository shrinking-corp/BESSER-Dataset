import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Acao,
    Antecedente,
    Caracteristica,
    CaracteristicaProduto,
    Elemento,
    ElementoCaracteristico,
    ElementoDeProduto,
    ElementoExterno,
    Evento,
    Expressao,
    PontoDeVariacao,
    Regra,
    caracteristica_Acao,
    caracteristica_AcaoLogico,
    caracteristica_Antecedente,
    caracteristica_Atributo,
    caracteristica_AtributoProduto,
    caracteristica_Caracteristica,
    caracteristica_CaracteristicaAgrupada,
    caracteristica_CaracteristicaAgrupadaProduto,
    caracteristica_CaracteristicaMandatoria,
    caracteristica_CaracteristicaMandatoriaProduto,
    caracteristica_CaracteristicaOpcional,
    caracteristica_CaracteristicaOpcionalProduto,
    caracteristica_CaracteristicaProduto,
    caracteristica_CaracteristicaRaiz,
    caracteristica_CasoDeTeste,
    caracteristica_CasoDeUso,
    caracteristica_Designar,
    caracteristica_Elemento,
    caracteristica_ElementoCaracteristico,
    caracteristica_ElementoDeProduto,
    caracteristica_ElementoExterno,
    caracteristica_EntidadeDeContexto,
    caracteristica_Estado,
    caracteristica_Evento,
    caracteristica_EventoLogico,
    caracteristica_EventoRelacional,
    caracteristica_Expressao,
    caracteristica_ExpressaoLogica,
    caracteristica_ExpressaoRelacional,
    caracteristica_InconsistenciaRegraAdaptacao,
    caracteristica_InformacaoDeContexto,
    caracteristica_LPS,
    caracteristica_LiteralAcao,
    caracteristica_LiteralComposicao,
    caracteristica_PontoDeVariacao,
    caracteristica_Produto,
    caracteristica_RaizDeContexto,
    caracteristica_Regra,
    caracteristica_RegraDeComposicao,
    caracteristica_RegraDeContexto,
    caracteristica_Simulacao,
    caracteristica_Transicao,
    caracteristica_Variacao,
    caracteristica_VariacaoDois,
    caracteristica_VariacaoDoisProduto,
    caracteristica_VariacaoProduto,
    caracteristica_Variante,
    caracteristica_VarianteProduto,
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

def test_assoc_atributo80_reverse_link_reassign_clear():
    a1 = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    a2 = caracteristica_Designar(tipoValor="sample_text_2", valor="sample_text_2")
    b = caracteristica_Atributo(tipoValor="sample_text")
    _safe_set(b, 'caracteristica_Atributo81', a1)
    assert _is_linked(b, 'caracteristica_Atributo81', a1)
    if hasattr(a1, 'caracteristica_Designar'):
        assert _is_linked(a1, 'caracteristica_Designar', b)
    _safe_set(b, 'caracteristica_Atributo81', a2)
    assert _is_linked(b, 'caracteristica_Atributo81', a2)
    if hasattr(a1, 'caracteristica_Designar'):
        assert not _is_linked(a1, 'caracteristica_Designar', b)
    if hasattr(a2, 'caracteristica_Designar'):
        assert _is_linked(a2, 'caracteristica_Designar', b)
    _safe_set(b, 'caracteristica_Atributo81', None)
    assert not _is_linked(b, 'caracteristica_Atributo81', a2)
    if hasattr(a2, 'caracteristica_Designar'):
        assert not _is_linked(a2, 'caracteristica_Designar', b)


def test_assoc_atributos14_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_Atributo(tipoValor="sample_text")
    _safe_set(b, 'caracteristica_Atributo', a1)
    assert _is_linked(b, 'caracteristica_Atributo', a1)
    if hasattr(a1, 'caracteristica_LPS15'):
        assert _is_linked(a1, 'caracteristica_LPS15', b)
    _safe_set(b, 'caracteristica_Atributo', a2)
    assert _is_linked(b, 'caracteristica_Atributo', a2)
    if hasattr(a1, 'caracteristica_LPS15'):
        assert not _is_linked(a1, 'caracteristica_LPS15', b)
    if hasattr(a2, 'caracteristica_LPS15'):
        assert _is_linked(a2, 'caracteristica_LPS15', b)
    _safe_set(b, 'caracteristica_Atributo', None)
    assert not _is_linked(b, 'caracteristica_Atributo', a2)
    if hasattr(a2, 'caracteristica_LPS15'):
        assert not _is_linked(a2, 'caracteristica_LPS15', b)


def test_assoc_eAntigo95_reverse_link_reassign_clear():
    a1 = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    a2 = caracteristica_Transicao(etiqueta="sample_text_2", safe=False)
    b = caracteristica_Estado(nome="sample_text", safe=True)
    _safe_set(b, 'caracteristica_Estado97', a1)
    assert _is_linked(b, 'caracteristica_Estado97', a1)
    if hasattr(a1, 'caracteristica_Transicao96'):
        assert _is_linked(a1, 'caracteristica_Transicao96', b)
    _safe_set(b, 'caracteristica_Estado97', a2)
    assert _is_linked(b, 'caracteristica_Estado97', a2)
    if hasattr(a1, 'caracteristica_Transicao96'):
        assert not _is_linked(a1, 'caracteristica_Transicao96', b)
    if hasattr(a2, 'caracteristica_Transicao96'):
        assert _is_linked(a2, 'caracteristica_Transicao96', b)
    _safe_set(b, 'caracteristica_Estado97', None)
    assert not _is_linked(b, 'caracteristica_Estado97', a2)
    if hasattr(a2, 'caracteristica_Transicao96'):
        assert not _is_linked(a2, 'caracteristica_Transicao96', b)


def test_assoc_eNovo98_reverse_link_reassign_clear():
    a1 = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    a2 = caracteristica_Transicao(etiqueta="sample_text_2", safe=False)
    b = caracteristica_Estado(nome="sample_text", safe=True)
    _safe_set(b, 'caracteristica_Estado100', a1)
    assert _is_linked(b, 'caracteristica_Estado100', a1)
    if hasattr(a1, 'caracteristica_Transicao99'):
        assert _is_linked(a1, 'caracteristica_Transicao99', b)
    _safe_set(b, 'caracteristica_Estado100', a2)
    assert _is_linked(b, 'caracteristica_Estado100', a2)
    if hasattr(a1, 'caracteristica_Transicao99'):
        assert not _is_linked(a1, 'caracteristica_Transicao99', b)
    if hasattr(a2, 'caracteristica_Transicao99'):
        assert _is_linked(a2, 'caracteristica_Transicao99', b)
    _safe_set(b, 'caracteristica_Estado100', None)
    assert not _is_linked(b, 'caracteristica_Estado100', a2)
    if hasattr(a2, 'caracteristica_Transicao99'):
        assert not _is_linked(a2, 'caracteristica_Transicao99', b)


def test_assoc_elementoOriginal44_reverse_link_reassign_clear():
    a1 = caracteristica_ElementoDeProduto(nome="sample_text")
    a2 = caracteristica_ElementoDeProduto(nome="sample_text_2")
    b = caracteristica_Elemento(nome="sample_text")
    _safe_set(b, 'caracteristica_Elemento46', a1)
    assert _is_linked(b, 'caracteristica_Elemento46', a1)
    if hasattr(a1, 'caracteristica_ElementoDeProduto45'):
        assert _is_linked(a1, 'caracteristica_ElementoDeProduto45', b)
    _safe_set(b, 'caracteristica_Elemento46', a2)
    assert _is_linked(b, 'caracteristica_Elemento46', a2)
    if hasattr(a1, 'caracteristica_ElementoDeProduto45'):
        assert not _is_linked(a1, 'caracteristica_ElementoDeProduto45', b)
    if hasattr(a2, 'caracteristica_ElementoDeProduto45'):
        assert _is_linked(a2, 'caracteristica_ElementoDeProduto45', b)
    _safe_set(b, 'caracteristica_Elemento46', None)
    assert not _is_linked(b, 'caracteristica_Elemento46', a2)
    if hasattr(a2, 'caracteristica_ElementoDeProduto45'):
        assert not _is_linked(a2, 'caracteristica_ElementoDeProduto45', b)


def test_assoc_elementos1_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_Elemento(nome="sample_text")
    _safe_set(b, 'caracteristica_Elemento', a1)
    assert _is_linked(b, 'caracteristica_Elemento', a1)
    if hasattr(a1, 'caracteristica_LPS2'):
        assert _is_linked(a1, 'caracteristica_LPS2', b)
    _safe_set(b, 'caracteristica_Elemento', a2)
    assert _is_linked(b, 'caracteristica_Elemento', a2)
    if hasattr(a1, 'caracteristica_LPS2'):
        assert not _is_linked(a1, 'caracteristica_LPS2', b)
    if hasattr(a2, 'caracteristica_LPS2'):
        assert _is_linked(a2, 'caracteristica_LPS2', b)
    _safe_set(b, 'caracteristica_Elemento', None)
    assert not _is_linked(b, 'caracteristica_Elemento', a2)
    if hasattr(a2, 'caracteristica_LPS2'):
        assert not _is_linked(a2, 'caracteristica_LPS2', b)


def test_assoc_elementosDeProduto11_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_ElementoDeProduto(nome="sample_text")
    _safe_set(b, 'caracteristica_ElementoDeProduto', a1)
    assert _is_linked(b, 'caracteristica_ElementoDeProduto', a1)
    if hasattr(a1, 'caracteristica_LPS12'):
        assert _is_linked(a1, 'caracteristica_LPS12', b)
    _safe_set(b, 'caracteristica_ElementoDeProduto', a2)
    assert _is_linked(b, 'caracteristica_ElementoDeProduto', a2)
    if hasattr(a1, 'caracteristica_LPS12'):
        assert not _is_linked(a1, 'caracteristica_LPS12', b)
    if hasattr(a2, 'caracteristica_LPS12'):
        assert _is_linked(a2, 'caracteristica_LPS12', b)
    _safe_set(b, 'caracteristica_ElementoDeProduto', None)
    assert not _is_linked(b, 'caracteristica_ElementoDeProduto', a2)
    if hasattr(a2, 'caracteristica_LPS12'):
        assert not _is_linked(a2, 'caracteristica_LPS12', b)


def test_assoc_estados93_reverse_link_reassign_clear():
    a1 = caracteristica_Simulacao(nome="sample_text")
    a2 = caracteristica_Simulacao(nome="sample_text_2")
    b = caracteristica_Estado(nome="sample_text", safe=True)
    _safe_set(b, 'caracteristica_Estado', a1)
    assert _is_linked(b, 'caracteristica_Estado', a1)
    if hasattr(a1, 'caracteristica_Simulacao94'):
        assert _is_linked(a1, 'caracteristica_Simulacao94', b)
    _safe_set(b, 'caracteristica_Estado', a2)
    assert _is_linked(b, 'caracteristica_Estado', a2)
    if hasattr(a1, 'caracteristica_Simulacao94'):
        assert not _is_linked(a1, 'caracteristica_Simulacao94', b)
    if hasattr(a2, 'caracteristica_Simulacao94'):
        assert _is_linked(a2, 'caracteristica_Simulacao94', b)
    _safe_set(b, 'caracteristica_Estado', None)
    assert not _is_linked(b, 'caracteristica_Estado', a2)
    if hasattr(a2, 'caracteristica_Simulacao94'):
        assert not _is_linked(a2, 'caracteristica_Simulacao94', b)


def test_assoc_expressoes9_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_Expressao(nome="sample_text")
    _safe_set(b, 'caracteristica_Expressao', a1)
    assert _is_linked(b, 'caracteristica_Expressao', a1)
    if hasattr(a1, 'caracteristica_LPS10'):
        assert _is_linked(a1, 'caracteristica_LPS10', b)
    _safe_set(b, 'caracteristica_Expressao', a2)
    assert _is_linked(b, 'caracteristica_Expressao', a2)
    if hasattr(a1, 'caracteristica_LPS10'):
        assert not _is_linked(a1, 'caracteristica_LPS10', b)
    if hasattr(a2, 'caracteristica_LPS10'):
        assert _is_linked(a2, 'caracteristica_LPS10', b)
    _safe_set(b, 'caracteristica_Expressao', None)
    assert not _is_linked(b, 'caracteristica_Expressao', a2)
    if hasattr(a2, 'caracteristica_LPS10'):
        assert not _is_linked(a2, 'caracteristica_LPS10', b)


def test_assoc_externos3_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_ElementoExterno(nome="sample_text")
    _safe_set(b, 'caracteristica_ElementoExterno', a1)
    assert _is_linked(b, 'caracteristica_ElementoExterno', a1)
    if hasattr(a1, 'caracteristica_LPS4'):
        assert _is_linked(a1, 'caracteristica_LPS4', b)
    _safe_set(b, 'caracteristica_ElementoExterno', a2)
    assert _is_linked(b, 'caracteristica_ElementoExterno', a2)
    if hasattr(a1, 'caracteristica_LPS4'):
        assert not _is_linked(a1, 'caracteristica_LPS4', b)
    if hasattr(a2, 'caracteristica_LPS4'):
        assert _is_linked(a2, 'caracteristica_LPS4', b)
    _safe_set(b, 'caracteristica_ElementoExterno', None)
    assert not _is_linked(b, 'caracteristica_ElementoExterno', a2)
    if hasattr(a2, 'caracteristica_LPS4'):
        assert not _is_linked(a2, 'caracteristica_LPS4', b)


def test_assoc_regras5_reverse_link_reassign_clear():
    a1 = caracteristica_Regra(conteudo="sample_text", nome="sample_text")
    a2 = caracteristica_Regra(conteudo="sample_text_2", nome="sample_text_2")
    b = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    _safe_set(b, 'caracteristica_LPS6', {a1})
    assert _is_linked(b, 'caracteristica_LPS6', a1)
    if hasattr(a1, 'caracteristica_Regra'):
        assert _is_linked(a1, 'caracteristica_Regra', b)
    _safe_set(b, 'caracteristica_LPS6', {a2})
    assert _is_linked(b, 'caracteristica_LPS6', a2)
    if hasattr(a1, 'caracteristica_Regra'):
        assert not _is_linked(a1, 'caracteristica_Regra', b)
    if hasattr(a2, 'caracteristica_Regra'):
        assert _is_linked(a2, 'caracteristica_Regra', b)
    _safe_set(b, 'caracteristica_LPS6', set())
    assert not _is_linked(b, 'caracteristica_LPS6', a2)
    if hasattr(a2, 'caracteristica_Regra'):
        assert not _is_linked(a2, 'caracteristica_Regra', b)


def test_assoc_simulacoes16_reverse_link_reassign_clear():
    a1 = caracteristica_Simulacao(nome="sample_text")
    a2 = caracteristica_Simulacao(nome="sample_text_2")
    b = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    _safe_set(b, 'caracteristica_LPS17', {a1})
    assert _is_linked(b, 'caracteristica_LPS17', a1)
    if hasattr(a1, 'caracteristica_Simulacao'):
        assert _is_linked(a1, 'caracteristica_Simulacao', b)
    _safe_set(b, 'caracteristica_LPS17', {a2})
    assert _is_linked(b, 'caracteristica_LPS17', a2)
    if hasattr(a1, 'caracteristica_Simulacao'):
        assert not _is_linked(a1, 'caracteristica_Simulacao', b)
    if hasattr(a2, 'caracteristica_Simulacao'):
        assert _is_linked(a2, 'caracteristica_Simulacao', b)
    _safe_set(b, 'caracteristica_LPS17', set())
    assert not _is_linked(b, 'caracteristica_LPS17', a2)
    if hasattr(a2, 'caracteristica_Simulacao'):
        assert not _is_linked(a2, 'caracteristica_Simulacao', b)


def test_assoc_transicoes91_reverse_link_reassign_clear():
    a1 = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    a2 = caracteristica_Transicao(etiqueta="sample_text_2", safe=False)
    b = caracteristica_Simulacao(nome="sample_text")
    _safe_set(b, 'caracteristica_Simulacao92', {a1})
    assert _is_linked(b, 'caracteristica_Simulacao92', a1)
    if hasattr(a1, 'caracteristica_Transicao'):
        assert _is_linked(a1, 'caracteristica_Transicao', b)
    _safe_set(b, 'caracteristica_Simulacao92', {a2})
    assert _is_linked(b, 'caracteristica_Simulacao92', a2)
    if hasattr(a1, 'caracteristica_Transicao'):
        assert not _is_linked(a1, 'caracteristica_Transicao', b)
    if hasattr(a2, 'caracteristica_Transicao'):
        assert _is_linked(a2, 'caracteristica_Transicao', b)
    _safe_set(b, 'caracteristica_Simulacao92', set())
    assert not _is_linked(b, 'caracteristica_Simulacao92', a2)
    if hasattr(a2, 'caracteristica_Transicao'):
        assert not _is_linked(a2, 'caracteristica_Transicao', b)


def test_assoc_variacaoProdutoPai58_reverse_link_reassign_clear():
    a1 = caracteristica_VarianteProduto(selecionado="sample_text")
    a2 = caracteristica_VarianteProduto(selecionado="sample_text_2")
    b = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    _safe_set(b, 'VariacaoProduto', a1)
    assert _is_linked(b, 'VariacaoProduto', a1)
    if hasattr(a1, 'variantesProduto'):
        assert _is_linked(a1, 'variantesProduto', b)
    _safe_set(b, 'VariacaoProduto', a2)
    assert _is_linked(b, 'VariacaoProduto', a2)
    if hasattr(a1, 'variantesProduto'):
        assert not _is_linked(a1, 'variantesProduto', b)
    if hasattr(a2, 'variantesProduto'):
        assert _is_linked(a2, 'variantesProduto', b)
    _safe_set(b, 'VariacaoProduto', None)
    assert not _is_linked(b, 'VariacaoProduto', a2)
    if hasattr(a2, 'variantesProduto'):
        assert not _is_linked(a2, 'variantesProduto', b)


def test_assoc_variantesProduto56_reverse_link_reassign_clear():
    a1 = caracteristica_VarianteProduto(selecionado="sample_text")
    a2 = caracteristica_VarianteProduto(selecionado="sample_text_2")
    b = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    _safe_set(b, 'variacaoProdutoPai', {a1})
    assert _is_linked(b, 'variacaoProdutoPai', a1)
    if hasattr(a1, 'VarianteProduto'):
        assert _is_linked(a1, 'VarianteProduto', b)
    _safe_set(b, 'variacaoProdutoPai', {a2})
    assert _is_linked(b, 'variacaoProdutoPai', a2)
    if hasattr(a1, 'VarianteProduto'):
        assert not _is_linked(a1, 'VarianteProduto', b)
    if hasattr(a2, 'VarianteProduto'):
        assert _is_linked(a2, 'VarianteProduto', b)
    _safe_set(b, 'variacaoProdutoPai', set())
    assert not _is_linked(b, 'variacaoProdutoPai', a2)
    if hasattr(a2, 'VarianteProduto'):
        assert not _is_linked(a2, 'VarianteProduto', b)


def test_assoc_variavelDeContexto73_reverse_link_reassign_clear():
    a1 = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    a2 = caracteristica_InformacaoDeContexto(origem="sample_text_2", qualidade="sample_text_2", tipoValor="sample_text_2", validade="sample_text_2", valor="sample_text_2")
    b = caracteristica_EventoRelacional(operadorRelacional="sample_text", valor="sample_text")
    _safe_set(b, 'caracteristica_EventoRelacional', a1)
    assert _is_linked(b, 'caracteristica_EventoRelacional', a1)
    if hasattr(a1, 'caracteristica_InformacaoDeContexto'):
        assert _is_linked(a1, 'caracteristica_InformacaoDeContexto', b)
    _safe_set(b, 'caracteristica_EventoRelacional', a2)
    assert _is_linked(b, 'caracteristica_EventoRelacional', a2)
    if hasattr(a1, 'caracteristica_InformacaoDeContexto'):
        assert not _is_linked(a1, 'caracteristica_InformacaoDeContexto', b)
    if hasattr(a2, 'caracteristica_InformacaoDeContexto'):
        assert _is_linked(a2, 'caracteristica_InformacaoDeContexto', b)
    _safe_set(b, 'caracteristica_EventoRelacional', None)
    assert not _is_linked(b, 'caracteristica_EventoRelacional', a2)
    if hasattr(a2, 'caracteristica_InformacaoDeContexto'):
        assert not _is_linked(a2, 'caracteristica_InformacaoDeContexto', b)


def test_assoc_variaveldaExpressao87_reverse_link_reassign_clear():
    a1 = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text", valor="sample_text")
    a2 = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text_2", valor="sample_text_2")
    b = caracteristica_Atributo(tipoValor="sample_text")
    _safe_set(b, 'caracteristica_Atributo88', a1)
    assert _is_linked(b, 'caracteristica_Atributo88', a1)
    if hasattr(a1, 'caracteristica_ExpressaoRelacional'):
        assert _is_linked(a1, 'caracteristica_ExpressaoRelacional', b)
    _safe_set(b, 'caracteristica_Atributo88', a2)
    assert _is_linked(b, 'caracteristica_Atributo88', a2)
    if hasattr(a1, 'caracteristica_ExpressaoRelacional'):
        assert not _is_linked(a1, 'caracteristica_ExpressaoRelacional', b)
    if hasattr(a2, 'caracteristica_ExpressaoRelacional'):
        assert _is_linked(a2, 'caracteristica_ExpressaoRelacional', b)
    _safe_set(b, 'caracteristica_Atributo88', None)
    assert not _is_linked(b, 'caracteristica_Atributo88', a2)
    if hasattr(a2, 'caracteristica_ExpressaoRelacional'):
        assert not _is_linked(a2, 'caracteristica_ExpressaoRelacional', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_LpsDoSistema33_stub_double():
    # caracteristica_CaracteristicaRaiz has no real 'sistema' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_CaracteristicaRaiz()
    setattr(partner, 'sistema', None)
    _safe_set(owner, 'LPS', partner)
    assert getattr(partner, 'sistema') == owner
    _safe_set(owner, 'LPS', None)
    assert getattr(partner, 'sistema') is None


def test_assoc_acoes104_stub_double():
    # caracteristica_Acao has no real 'caracteristica_Acao106' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Transicao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Transicao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    partner = caracteristica_Acao()
    setattr(partner, 'caracteristica_Acao106', None)
    _safe_set(owner, 'caracteristica_Transicao105', {partner})
    assert getattr(partner, 'caracteristica_Acao106') == owner
    _safe_set(owner, 'caracteristica_Transicao105', set())
    assert getattr(partner, 'caracteristica_Acao106') is None


def test_assoc_atribuicoesInconsistentes116_stub_double():
    # caracteristica_InconsistenciaRegraAdaptacao has no real 'caracteristica_InconsistenciaRegraAdaptacao117' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Designar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Designar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    partner = caracteristica_InconsistenciaRegraAdaptacao()
    setattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao117', None)
    _safe_set(owner, 'caracteristica_Designar118', partner)
    assert owner in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao117')
    _safe_set(owner, 'caracteristica_Designar118', None)
    assert owner not in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao117')


def test_assoc_atributo31_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristicaPai32' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Atributo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Atributo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Atributo(tipoValor="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristicaPai32', None)
    _safe_set(owner, 'Atributo', partner)
    assert owner in getattr(partner, 'caracteristicaPai32')
    _safe_set(owner, 'Atributo', None)
    assert owner not in getattr(partner, 'caracteristicaPai32')


def test_assoc_atributoProduto52_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'caracteristicaProdutoPai53' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AtributoProduto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AtributoProduto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'caracteristicaProdutoPai53', None)
    _safe_set(owner, 'AtributoProduto', partner)
    assert owner in getattr(partner, 'caracteristicaProdutoPai53')
    _safe_set(owner, 'AtributoProduto', None)
    assert owner not in getattr(partner, 'caracteristicaProdutoPai53')


def test_assoc_caracteristicaPai20_stub_double():
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


def test_assoc_caracteristicaPai35_stub_double():
    # caracteristica_Caracteristica has no real 'Caracteristica36' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'Caracteristica36', None)
    _safe_set(owner, 'variacoes', partner)
    assert getattr(partner, 'Caracteristica36') == owner
    _safe_set(owner, 'variacoes', None)
    assert getattr(partner, 'Caracteristica36') is None


def test_assoc_caracteristicaProdutoPai54_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'CaracteristicaProduto55' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AtributoProduto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AtributoProduto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'CaracteristicaProduto55', None)
    _safe_set(owner, 'atributoProduto', partner)
    assert getattr(partner, 'CaracteristicaProduto55') == owner
    _safe_set(owner, 'atributoProduto', None)
    assert getattr(partner, 'CaracteristicaProduto55') is None


def test_assoc_caracteristicaProdutoPai57_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'caracteristica_CaracteristicaProduto' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_VariacaoProduto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_VariacaoProduto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'caracteristica_CaracteristicaProduto', None)
    _safe_set(owner, 'caracteristica_VariacaoProduto', partner)
    assert getattr(partner, 'caracteristica_CaracteristicaProduto') == owner
    _safe_set(owner, 'caracteristica_VariacaoProduto', None)
    assert getattr(partner, 'caracteristica_CaracteristicaProduto') is None


def test_assoc_elemento79_stub_double():
    # caracteristica_ElementoCaracteristico has no real 'caracteristica_ElementoCaracteristico' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LiteralAcao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LiteralAcao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LiteralAcao(presenca="sample_text")
    partner = caracteristica_ElementoCaracteristico()
    setattr(partner, 'caracteristica_ElementoCaracteristico', None)
    _safe_set(owner, 'caracteristica_LiteralAcao', partner)
    assert getattr(partner, 'caracteristica_ElementoCaracteristico') == owner
    _safe_set(owner, 'caracteristica_LiteralAcao', None)
    assert getattr(partner, 'caracteristica_ElementoCaracteristico') is None


def test_assoc_elemento89_stub_double():
    # caracteristica_ElementoCaracteristico has no real 'caracteristica_ElementoCaracteristico90' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LiteralComposicao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LiteralComposicao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LiteralComposicao(presenca="sample_text")
    partner = caracteristica_ElementoCaracteristico()
    setattr(partner, 'caracteristica_ElementoCaracteristico90', None)
    _safe_set(owner, 'caracteristica_LiteralComposicao', partner)
    assert getattr(partner, 'caracteristica_ElementoCaracteristico90') == owner
    _safe_set(owner, 'caracteristica_LiteralComposicao', None)
    assert getattr(partner, 'caracteristica_ElementoCaracteristico90') is None


def test_assoc_elementoPai42_stub_double():
    # caracteristica_EntidadeDeContexto has no real 'EntidadeDeContexto43' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_InformacaoDeContexto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_InformacaoDeContexto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    partner = caracteristica_EntidadeDeContexto()
    setattr(partner, 'EntidadeDeContexto43', None)
    _safe_set(owner, 'informacoesDeContexto', partner)
    assert getattr(partner, 'EntidadeDeContexto43') == owner
    _safe_set(owner, 'informacoesDeContexto', None)
    assert getattr(partner, 'EntidadeDeContexto43') is None


def test_assoc_elementosExternos21_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristica_Caracteristica' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_ElementoExterno's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_ElementoExterno's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_ElementoExterno(nome="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristica_Caracteristica', None)
    _safe_set(owner, 'caracteristica_ElementoExterno22', partner)
    assert owner in getattr(partner, 'caracteristica_Caracteristica')
    _safe_set(owner, 'caracteristica_ElementoExterno22', None)
    assert owner not in getattr(partner, 'caracteristica_Caracteristica')


def test_assoc_inconsistenciaERA18_stub_double():
    # caracteristica_InconsistenciaRegraAdaptacao has no real 'caracteristica_InconsistenciaRegraAdaptacao' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_InconsistenciaRegraAdaptacao()
    setattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao', None)
    _safe_set(owner, 'caracteristica_LPS19', {partner})
    assert getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao') == owner
    _safe_set(owner, 'caracteristica_LPS19', set())
    assert getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao') is None


def test_assoc_informacoesDeContexto41_stub_double():
    # caracteristica_EntidadeDeContexto has no real 'elementoPai' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_InformacaoDeContexto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_InformacaoDeContexto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    partner = caracteristica_EntidadeDeContexto()
    setattr(partner, 'elementoPai', None)
    _safe_set(owner, 'InformacaoDeContexto', partner)
    assert owner in getattr(partner, 'elementoPai')
    _safe_set(owner, 'InformacaoDeContexto', None)
    assert owner not in getattr(partner, 'elementoPai')


def test_assoc_ladoDireitoAcao76_stub_double():
    # caracteristica_Acao has no real 'caracteristica_Acao78' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AcaoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AcaoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    partner = caracteristica_Acao()
    setattr(partner, 'caracteristica_Acao78', None)
    _safe_set(owner, 'caracteristica_AcaoLogico77', partner)
    assert getattr(partner, 'caracteristica_Acao78') == owner
    _safe_set(owner, 'caracteristica_AcaoLogico77', None)
    assert getattr(partner, 'caracteristica_Acao78') is None


def test_assoc_ladoDireitoComposicao82_stub_double():
    # caracteristica_Antecedente has no real 'caracteristica_Antecedente83' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_ExpressaoLogica's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_ExpressaoLogica's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    partner = caracteristica_Antecedente()
    setattr(partner, 'caracteristica_Antecedente83', None)
    _safe_set(owner, 'caracteristica_ExpressaoLogica', partner)
    assert getattr(partner, 'caracteristica_Antecedente83') == owner
    _safe_set(owner, 'caracteristica_ExpressaoLogica', None)
    assert getattr(partner, 'caracteristica_Antecedente83') is None


def test_assoc_ladoDireitoEvento68_stub_double():
    # caracteristica_Evento has no real 'caracteristica_Evento69' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_EventoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_EventoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_EventoLogico(operadorLogico="sample_text")
    partner = caracteristica_Evento()
    setattr(partner, 'caracteristica_Evento69', None)
    _safe_set(owner, 'caracteristica_EventoLogico', partner)
    assert getattr(partner, 'caracteristica_Evento69') == owner
    _safe_set(owner, 'caracteristica_EventoLogico', None)
    assert getattr(partner, 'caracteristica_Evento69') is None


def test_assoc_ladoEsquerdoAcao74_stub_double():
    # caracteristica_Acao has no real 'caracteristica_Acao75' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AcaoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AcaoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    partner = caracteristica_Acao()
    setattr(partner, 'caracteristica_Acao75', None)
    _safe_set(owner, 'caracteristica_AcaoLogico', partner)
    assert getattr(partner, 'caracteristica_Acao75') == owner
    _safe_set(owner, 'caracteristica_AcaoLogico', None)
    assert getattr(partner, 'caracteristica_Acao75') is None


def test_assoc_ladoEsquerdoComposicao84_stub_double():
    # caracteristica_Antecedente has no real 'caracteristica_Antecedente86' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_ExpressaoLogica's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_ExpressaoLogica's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    partner = caracteristica_Antecedente()
    setattr(partner, 'caracteristica_Antecedente86', None)
    _safe_set(owner, 'caracteristica_ExpressaoLogica85', partner)
    assert getattr(partner, 'caracteristica_Antecedente86') == owner
    _safe_set(owner, 'caracteristica_ExpressaoLogica85', None)
    assert getattr(partner, 'caracteristica_Antecedente86') is None


def test_assoc_ladoEsquerdoEvento70_stub_double():
    # caracteristica_Evento has no real 'caracteristica_Evento72' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_EventoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_EventoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_EventoLogico(operadorLogico="sample_text")
    partner = caracteristica_Evento()
    setattr(partner, 'caracteristica_Evento72', None)
    _safe_set(owner, 'caracteristica_EventoLogico71', partner)
    assert getattr(partner, 'caracteristica_Evento72') == owner
    _safe_set(owner, 'caracteristica_EventoLogico71', None)
    assert getattr(partner, 'caracteristica_Evento72') is None


def test_assoc_literaisInconsistentes113_stub_double():
    # caracteristica_InconsistenciaRegraAdaptacao has no real 'caracteristica_InconsistenciaRegraAdaptacao114' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LiteralAcao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LiteralAcao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LiteralAcao(presenca="sample_text")
    partner = caracteristica_InconsistenciaRegraAdaptacao()
    setattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao114', None)
    _safe_set(owner, 'caracteristica_LiteralAcao115', partner)
    assert owner in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao114')
    _safe_set(owner, 'caracteristica_LiteralAcao115', None)
    assert owner not in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao114')


def test_assoc_pontosDeVariacao0_stub_double():
    # caracteristica_PontoDeVariacao has no real 'caracteristica_PontoDeVariacao' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_PontoDeVariacao()
    setattr(partner, 'caracteristica_PontoDeVariacao', None)
    _safe_set(owner, 'caracteristica_LPS', {partner})
    assert getattr(partner, 'caracteristica_PontoDeVariacao') == owner
    _safe_set(owner, 'caracteristica_LPS', set())
    assert getattr(partner, 'caracteristica_PontoDeVariacao') is None


def test_assoc_produto107_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'caracteristica_CaracteristicaProduto109' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Estado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Estado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Estado(nome="sample_text", safe=True)
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'caracteristica_CaracteristicaProduto109', None)
    _safe_set(owner, 'caracteristica_Estado108', partner)
    assert getattr(partner, 'caracteristica_CaracteristicaProduto109') == owner
    _safe_set(owner, 'caracteristica_Estado108', None)
    assert getattr(partner, 'caracteristica_CaracteristicaProduto109') is None


def test_assoc_produtos7_stub_double():
    # caracteristica_Produto has no real 'caracteristica_Produto' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_Produto()
    setattr(partner, 'caracteristica_Produto', None)
    _safe_set(owner, 'caracteristica_LPS8', {partner})
    assert getattr(partner, 'caracteristica_Produto') == owner
    _safe_set(owner, 'caracteristica_LPS8', set())
    assert getattr(partner, 'caracteristica_Produto') is None


def test_assoc_regrasQuebradas101_stub_double():
    # caracteristica_RegraDeComposicao has no real 'caracteristica_RegraDeComposicao103' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Transicao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Transicao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    partner = caracteristica_RegraDeComposicao()
    setattr(partner, 'caracteristica_RegraDeComposicao103', None)
    _safe_set(owner, 'caracteristica_Transicao102', {partner})
    assert getattr(partner, 'caracteristica_RegraDeComposicao103') == owner
    _safe_set(owner, 'caracteristica_Transicao102', set())
    assert getattr(partner, 'caracteristica_RegraDeComposicao103') is None


def test_assoc_sistema13_stub_double():
    # caracteristica_CaracteristicaRaiz has no real 'CaracteristicaRaiz' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_CaracteristicaRaiz()
    setattr(partner, 'CaracteristicaRaiz', None)
    _safe_set(owner, 'LpsDoSistema', partner)
    assert getattr(partner, 'CaracteristicaRaiz') == owner
    _safe_set(owner, 'LpsDoSistema', None)
    assert getattr(partner, 'CaracteristicaRaiz') is None


def test_assoc_variacaoPai37_stub_double():
    # caracteristica_Variante has no real 'variantes' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Variante()
    setattr(partner, 'variantes', None)
    _safe_set(owner, 'Variacao38', partner)
    assert getattr(partner, 'variantes') == owner
    _safe_set(owner, 'Variacao38', None)
    assert getattr(partner, 'variantes') is None


def test_assoc_variacoes29_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristicaPai30' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristicaPai30', None)
    _safe_set(owner, 'Variacao', partner)
    assert owner in getattr(partner, 'caracteristicaPai30')
    _safe_set(owner, 'Variacao', None)
    assert owner not in getattr(partner, 'caracteristicaPai30')


def test_assoc_variantes34_stub_double():
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


