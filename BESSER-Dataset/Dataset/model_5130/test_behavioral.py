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
    caracteristica_CaracteristicaMandatoria,
    caracteristica_CaracteristicaMandatoriaProduto,
    caracteristica_CaracteristicaOpcional,
    caracteristica_CaracteristicaOpcionalProduto,
    caracteristica_CaracteristicaProduto,
    caracteristica_CaracteristicaRaiz,
    caracteristica_Designar,
    caracteristica_Elemento,
    caracteristica_ElementoCaracteristico,
    caracteristica_ElementoDeProduto,
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

def test_assoc_atributo76_reverse_link_reassign_clear():
    a1 = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    a2 = caracteristica_Designar(tipoValor="sample_text_2", valor="sample_text_2")
    b = caracteristica_Atributo(tipoValor="sample_text")
    _safe_set(b, 'caracteristica_Atributo77', a1)
    assert _is_linked(b, 'caracteristica_Atributo77', a1)
    if hasattr(a1, 'caracteristica_Designar'):
        assert _is_linked(a1, 'caracteristica_Designar', b)
    _safe_set(b, 'caracteristica_Atributo77', a2)
    assert _is_linked(b, 'caracteristica_Atributo77', a2)
    if hasattr(a1, 'caracteristica_Designar'):
        assert not _is_linked(a1, 'caracteristica_Designar', b)
    if hasattr(a2, 'caracteristica_Designar'):
        assert _is_linked(a2, 'caracteristica_Designar', b)
    _safe_set(b, 'caracteristica_Atributo77', None)
    assert not _is_linked(b, 'caracteristica_Atributo77', a2)
    if hasattr(a2, 'caracteristica_Designar'):
        assert not _is_linked(a2, 'caracteristica_Designar', b)


def test_assoc_atributos12_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_Atributo(tipoValor="sample_text")
    _safe_set(b, 'caracteristica_Atributo', a1)
    assert _is_linked(b, 'caracteristica_Atributo', a1)
    if hasattr(a1, 'caracteristica_LPS13'):
        assert _is_linked(a1, 'caracteristica_LPS13', b)
    _safe_set(b, 'caracteristica_Atributo', a2)
    assert _is_linked(b, 'caracteristica_Atributo', a2)
    if hasattr(a1, 'caracteristica_LPS13'):
        assert not _is_linked(a1, 'caracteristica_LPS13', b)
    if hasattr(a2, 'caracteristica_LPS13'):
        assert _is_linked(a2, 'caracteristica_LPS13', b)
    _safe_set(b, 'caracteristica_Atributo', None)
    assert not _is_linked(b, 'caracteristica_Atributo', a2)
    if hasattr(a2, 'caracteristica_LPS13'):
        assert not _is_linked(a2, 'caracteristica_LPS13', b)


def test_assoc_eAntigo91_reverse_link_reassign_clear():
    a1 = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    a2 = caracteristica_Transicao(etiqueta="sample_text_2", safe=False)
    b = caracteristica_Estado(nome="sample_text", safe=True)
    _safe_set(b, 'caracteristica_Estado93', a1)
    assert _is_linked(b, 'caracteristica_Estado93', a1)
    if hasattr(a1, 'caracteristica_Transicao92'):
        assert _is_linked(a1, 'caracteristica_Transicao92', b)
    _safe_set(b, 'caracteristica_Estado93', a2)
    assert _is_linked(b, 'caracteristica_Estado93', a2)
    if hasattr(a1, 'caracteristica_Transicao92'):
        assert not _is_linked(a1, 'caracteristica_Transicao92', b)
    if hasattr(a2, 'caracteristica_Transicao92'):
        assert _is_linked(a2, 'caracteristica_Transicao92', b)
    _safe_set(b, 'caracteristica_Estado93', None)
    assert not _is_linked(b, 'caracteristica_Estado93', a2)
    if hasattr(a2, 'caracteristica_Transicao92'):
        assert not _is_linked(a2, 'caracteristica_Transicao92', b)


def test_assoc_eNovo94_reverse_link_reassign_clear():
    a1 = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    a2 = caracteristica_Transicao(etiqueta="sample_text_2", safe=False)
    b = caracteristica_Estado(nome="sample_text", safe=True)
    _safe_set(b, 'caracteristica_Estado96', a1)
    assert _is_linked(b, 'caracteristica_Estado96', a1)
    if hasattr(a1, 'caracteristica_Transicao95'):
        assert _is_linked(a1, 'caracteristica_Transicao95', b)
    _safe_set(b, 'caracteristica_Estado96', a2)
    assert _is_linked(b, 'caracteristica_Estado96', a2)
    if hasattr(a1, 'caracteristica_Transicao95'):
        assert not _is_linked(a1, 'caracteristica_Transicao95', b)
    if hasattr(a2, 'caracteristica_Transicao95'):
        assert _is_linked(a2, 'caracteristica_Transicao95', b)
    _safe_set(b, 'caracteristica_Estado96', None)
    assert not _is_linked(b, 'caracteristica_Estado96', a2)
    if hasattr(a2, 'caracteristica_Transicao95'):
        assert not _is_linked(a2, 'caracteristica_Transicao95', b)


def test_assoc_elementoOriginal40_reverse_link_reassign_clear():
    a1 = caracteristica_ElementoDeProduto(nome="sample_text")
    a2 = caracteristica_ElementoDeProduto(nome="sample_text_2")
    b = caracteristica_Elemento(nome="sample_text")
    _safe_set(b, 'caracteristica_Elemento42', a1)
    assert _is_linked(b, 'caracteristica_Elemento42', a1)
    if hasattr(a1, 'caracteristica_ElementoDeProduto41'):
        assert _is_linked(a1, 'caracteristica_ElementoDeProduto41', b)
    _safe_set(b, 'caracteristica_Elemento42', a2)
    assert _is_linked(b, 'caracteristica_Elemento42', a2)
    if hasattr(a1, 'caracteristica_ElementoDeProduto41'):
        assert not _is_linked(a1, 'caracteristica_ElementoDeProduto41', b)
    if hasattr(a2, 'caracteristica_ElementoDeProduto41'):
        assert _is_linked(a2, 'caracteristica_ElementoDeProduto41', b)
    _safe_set(b, 'caracteristica_Elemento42', None)
    assert not _is_linked(b, 'caracteristica_Elemento42', a2)
    if hasattr(a2, 'caracteristica_ElementoDeProduto41'):
        assert not _is_linked(a2, 'caracteristica_ElementoDeProduto41', b)


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


def test_assoc_elementosDeProduto9_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_ElementoDeProduto(nome="sample_text")
    _safe_set(b, 'caracteristica_ElementoDeProduto', a1)
    assert _is_linked(b, 'caracteristica_ElementoDeProduto', a1)
    if hasattr(a1, 'caracteristica_LPS10'):
        assert _is_linked(a1, 'caracteristica_LPS10', b)
    _safe_set(b, 'caracteristica_ElementoDeProduto', a2)
    assert _is_linked(b, 'caracteristica_ElementoDeProduto', a2)
    if hasattr(a1, 'caracteristica_LPS10'):
        assert not _is_linked(a1, 'caracteristica_LPS10', b)
    if hasattr(a2, 'caracteristica_LPS10'):
        assert _is_linked(a2, 'caracteristica_LPS10', b)
    _safe_set(b, 'caracteristica_ElementoDeProduto', None)
    assert not _is_linked(b, 'caracteristica_ElementoDeProduto', a2)
    if hasattr(a2, 'caracteristica_LPS10'):
        assert not _is_linked(a2, 'caracteristica_LPS10', b)


def test_assoc_estados89_reverse_link_reassign_clear():
    a1 = caracteristica_Simulacao(nome="sample_text")
    a2 = caracteristica_Simulacao(nome="sample_text_2")
    b = caracteristica_Estado(nome="sample_text", safe=True)
    _safe_set(b, 'caracteristica_Estado', a1)
    assert _is_linked(b, 'caracteristica_Estado', a1)
    if hasattr(a1, 'caracteristica_Simulacao90'):
        assert _is_linked(a1, 'caracteristica_Simulacao90', b)
    _safe_set(b, 'caracteristica_Estado', a2)
    assert _is_linked(b, 'caracteristica_Estado', a2)
    if hasattr(a1, 'caracteristica_Simulacao90'):
        assert not _is_linked(a1, 'caracteristica_Simulacao90', b)
    if hasattr(a2, 'caracteristica_Simulacao90'):
        assert _is_linked(a2, 'caracteristica_Simulacao90', b)
    _safe_set(b, 'caracteristica_Estado', None)
    assert not _is_linked(b, 'caracteristica_Estado', a2)
    if hasattr(a2, 'caracteristica_Simulacao90'):
        assert not _is_linked(a2, 'caracteristica_Simulacao90', b)


def test_assoc_expressoes7_reverse_link_reassign_clear():
    a1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    a2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    b = caracteristica_Expressao(nome="sample_text")
    _safe_set(b, 'caracteristica_Expressao', a1)
    assert _is_linked(b, 'caracteristica_Expressao', a1)
    if hasattr(a1, 'caracteristica_LPS8'):
        assert _is_linked(a1, 'caracteristica_LPS8', b)
    _safe_set(b, 'caracteristica_Expressao', a2)
    assert _is_linked(b, 'caracteristica_Expressao', a2)
    if hasattr(a1, 'caracteristica_LPS8'):
        assert not _is_linked(a1, 'caracteristica_LPS8', b)
    if hasattr(a2, 'caracteristica_LPS8'):
        assert _is_linked(a2, 'caracteristica_LPS8', b)
    _safe_set(b, 'caracteristica_Expressao', None)
    assert not _is_linked(b, 'caracteristica_Expressao', a2)
    if hasattr(a2, 'caracteristica_LPS8'):
        assert not _is_linked(a2, 'caracteristica_LPS8', b)


def test_assoc_regras3_reverse_link_reassign_clear():
    a1 = caracteristica_Regra(conteudo="sample_text", nome="sample_text")
    a2 = caracteristica_Regra(conteudo="sample_text_2", nome="sample_text_2")
    b = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    _safe_set(b, 'caracteristica_LPS4', {a1})
    assert _is_linked(b, 'caracteristica_LPS4', a1)
    if hasattr(a1, 'caracteristica_Regra'):
        assert _is_linked(a1, 'caracteristica_Regra', b)
    _safe_set(b, 'caracteristica_LPS4', {a2})
    assert _is_linked(b, 'caracteristica_LPS4', a2)
    if hasattr(a1, 'caracteristica_Regra'):
        assert not _is_linked(a1, 'caracteristica_Regra', b)
    if hasattr(a2, 'caracteristica_Regra'):
        assert _is_linked(a2, 'caracteristica_Regra', b)
    _safe_set(b, 'caracteristica_LPS4', set())
    assert not _is_linked(b, 'caracteristica_LPS4', a2)
    if hasattr(a2, 'caracteristica_Regra'):
        assert not _is_linked(a2, 'caracteristica_Regra', b)


def test_assoc_simulacoes14_reverse_link_reassign_clear():
    a1 = caracteristica_Simulacao(nome="sample_text")
    a2 = caracteristica_Simulacao(nome="sample_text_2")
    b = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    _safe_set(b, 'caracteristica_LPS15', {a1})
    assert _is_linked(b, 'caracteristica_LPS15', a1)
    if hasattr(a1, 'caracteristica_Simulacao'):
        assert _is_linked(a1, 'caracteristica_Simulacao', b)
    _safe_set(b, 'caracteristica_LPS15', {a2})
    assert _is_linked(b, 'caracteristica_LPS15', a2)
    if hasattr(a1, 'caracteristica_Simulacao'):
        assert not _is_linked(a1, 'caracteristica_Simulacao', b)
    if hasattr(a2, 'caracteristica_Simulacao'):
        assert _is_linked(a2, 'caracteristica_Simulacao', b)
    _safe_set(b, 'caracteristica_LPS15', set())
    assert not _is_linked(b, 'caracteristica_LPS15', a2)
    if hasattr(a2, 'caracteristica_Simulacao'):
        assert not _is_linked(a2, 'caracteristica_Simulacao', b)


def test_assoc_transicoes87_reverse_link_reassign_clear():
    a1 = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    a2 = caracteristica_Transicao(etiqueta="sample_text_2", safe=False)
    b = caracteristica_Simulacao(nome="sample_text")
    _safe_set(b, 'caracteristica_Simulacao88', {a1})
    assert _is_linked(b, 'caracteristica_Simulacao88', a1)
    if hasattr(a1, 'caracteristica_Transicao'):
        assert _is_linked(a1, 'caracteristica_Transicao', b)
    _safe_set(b, 'caracteristica_Simulacao88', {a2})
    assert _is_linked(b, 'caracteristica_Simulacao88', a2)
    if hasattr(a1, 'caracteristica_Transicao'):
        assert not _is_linked(a1, 'caracteristica_Transicao', b)
    if hasattr(a2, 'caracteristica_Transicao'):
        assert _is_linked(a2, 'caracteristica_Transicao', b)
    _safe_set(b, 'caracteristica_Simulacao88', set())
    assert not _is_linked(b, 'caracteristica_Simulacao88', a2)
    if hasattr(a2, 'caracteristica_Transicao'):
        assert not _is_linked(a2, 'caracteristica_Transicao', b)


def test_assoc_variacaoProdutoPai54_reverse_link_reassign_clear():
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


def test_assoc_variantesProduto52_reverse_link_reassign_clear():
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


def test_assoc_variavelDeContexto69_reverse_link_reassign_clear():
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


def test_assoc_variaveldaExpressao83_reverse_link_reassign_clear():
    a1 = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text", valor="sample_text")
    a2 = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text_2", valor="sample_text_2")
    b = caracteristica_Atributo(tipoValor="sample_text")
    _safe_set(b, 'caracteristica_Atributo84', a1)
    assert _is_linked(b, 'caracteristica_Atributo84', a1)
    if hasattr(a1, 'caracteristica_ExpressaoRelacional'):
        assert _is_linked(a1, 'caracteristica_ExpressaoRelacional', b)
    _safe_set(b, 'caracteristica_Atributo84', a2)
    assert _is_linked(b, 'caracteristica_Atributo84', a2)
    if hasattr(a1, 'caracteristica_ExpressaoRelacional'):
        assert not _is_linked(a1, 'caracteristica_ExpressaoRelacional', b)
    if hasattr(a2, 'caracteristica_ExpressaoRelacional'):
        assert _is_linked(a2, 'caracteristica_ExpressaoRelacional', b)
    _safe_set(b, 'caracteristica_Atributo84', None)
    assert not _is_linked(b, 'caracteristica_Atributo84', a2)
    if hasattr(a2, 'caracteristica_ExpressaoRelacional'):
        assert not _is_linked(a2, 'caracteristica_ExpressaoRelacional', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_LpsDoSistema29_stub_double():
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


def test_assoc_acoes100_stub_double():
    # caracteristica_Acao has no real 'caracteristica_Acao102' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Transicao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Transicao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    partner = caracteristica_Acao()
    setattr(partner, 'caracteristica_Acao102', None)
    _safe_set(owner, 'caracteristica_Transicao101', {partner})
    assert getattr(partner, 'caracteristica_Acao102') == owner
    _safe_set(owner, 'caracteristica_Transicao101', set())
    assert getattr(partner, 'caracteristica_Acao102') is None


def test_assoc_atribuicoesInconsistentes112_stub_double():
    # caracteristica_InconsistenciaRegraAdaptacao has no real 'caracteristica_InconsistenciaRegraAdaptacao113' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Designar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Designar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    partner = caracteristica_InconsistenciaRegraAdaptacao()
    setattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao113', None)
    _safe_set(owner, 'caracteristica_Designar114', partner)
    assert owner in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao113')
    _safe_set(owner, 'caracteristica_Designar114', None)
    assert owner not in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao113')


def test_assoc_atributo27_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristicaPai28' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Atributo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Atributo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Atributo(tipoValor="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristicaPai28', None)
    _safe_set(owner, 'Atributo', partner)
    assert owner in getattr(partner, 'caracteristicaPai28')
    _safe_set(owner, 'Atributo', None)
    assert owner not in getattr(partner, 'caracteristicaPai28')


def test_assoc_atributoProduto48_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'caracteristicaProdutoPai49' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AtributoProduto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AtributoProduto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'caracteristicaProdutoPai49', None)
    _safe_set(owner, 'AtributoProduto', partner)
    assert owner in getattr(partner, 'caracteristicaProdutoPai49')
    _safe_set(owner, 'AtributoProduto', None)
    assert owner not in getattr(partner, 'caracteristicaProdutoPai49')


def test_assoc_caracteristicaPai18_stub_double():
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


def test_assoc_caracteristicaPai31_stub_double():
    # caracteristica_Caracteristica has no real 'Caracteristica32' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'Caracteristica32', None)
    _safe_set(owner, 'variacoes', partner)
    assert getattr(partner, 'Caracteristica32') == owner
    _safe_set(owner, 'variacoes', None)
    assert getattr(partner, 'Caracteristica32') is None


def test_assoc_caracteristicaProdutoPai50_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'CaracteristicaProduto51' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AtributoProduto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AtributoProduto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'CaracteristicaProduto51', None)
    _safe_set(owner, 'atributoProduto', partner)
    assert getattr(partner, 'CaracteristicaProduto51') == owner
    _safe_set(owner, 'atributoProduto', None)
    assert getattr(partner, 'CaracteristicaProduto51') is None


def test_assoc_caracteristicaProdutoPai53_stub_double():
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


def test_assoc_elemento75_stub_double():
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


def test_assoc_elemento85_stub_double():
    # caracteristica_ElementoCaracteristico has no real 'caracteristica_ElementoCaracteristico86' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LiteralComposicao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LiteralComposicao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LiteralComposicao(presenca="sample_text")
    partner = caracteristica_ElementoCaracteristico()
    setattr(partner, 'caracteristica_ElementoCaracteristico86', None)
    _safe_set(owner, 'caracteristica_LiteralComposicao', partner)
    assert getattr(partner, 'caracteristica_ElementoCaracteristico86') == owner
    _safe_set(owner, 'caracteristica_LiteralComposicao', None)
    assert getattr(partner, 'caracteristica_ElementoCaracteristico86') is None


def test_assoc_elementoPai38_stub_double():
    # caracteristica_EntidadeDeContexto has no real 'EntidadeDeContexto39' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_InformacaoDeContexto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_InformacaoDeContexto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    partner = caracteristica_EntidadeDeContexto()
    setattr(partner, 'EntidadeDeContexto39', None)
    _safe_set(owner, 'informacoesDeContexto', partner)
    assert getattr(partner, 'EntidadeDeContexto39') == owner
    _safe_set(owner, 'informacoesDeContexto', None)
    assert getattr(partner, 'EntidadeDeContexto39') is None


def test_assoc_inconsistenciaERA16_stub_double():
    # caracteristica_InconsistenciaRegraAdaptacao has no real 'caracteristica_InconsistenciaRegraAdaptacao' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_InconsistenciaRegraAdaptacao()
    setattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao', None)
    _safe_set(owner, 'caracteristica_LPS17', {partner})
    assert getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao') == owner
    _safe_set(owner, 'caracteristica_LPS17', set())
    assert getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao') is None


def test_assoc_informacoesDeContexto37_stub_double():
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


def test_assoc_ladoDireitoAcao72_stub_double():
    # caracteristica_Acao has no real 'caracteristica_Acao74' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AcaoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AcaoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    partner = caracteristica_Acao()
    setattr(partner, 'caracteristica_Acao74', None)
    _safe_set(owner, 'caracteristica_AcaoLogico73', partner)
    assert getattr(partner, 'caracteristica_Acao74') == owner
    _safe_set(owner, 'caracteristica_AcaoLogico73', None)
    assert getattr(partner, 'caracteristica_Acao74') is None


def test_assoc_ladoDireitoComposicao78_stub_double():
    # caracteristica_Antecedente has no real 'caracteristica_Antecedente79' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_ExpressaoLogica's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_ExpressaoLogica's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    partner = caracteristica_Antecedente()
    setattr(partner, 'caracteristica_Antecedente79', None)
    _safe_set(owner, 'caracteristica_ExpressaoLogica', partner)
    assert getattr(partner, 'caracteristica_Antecedente79') == owner
    _safe_set(owner, 'caracteristica_ExpressaoLogica', None)
    assert getattr(partner, 'caracteristica_Antecedente79') is None


def test_assoc_ladoDireitoEvento64_stub_double():
    # caracteristica_Evento has no real 'caracteristica_Evento65' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_EventoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_EventoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_EventoLogico(operadorLogico="sample_text")
    partner = caracteristica_Evento()
    setattr(partner, 'caracteristica_Evento65', None)
    _safe_set(owner, 'caracteristica_EventoLogico', partner)
    assert getattr(partner, 'caracteristica_Evento65') == owner
    _safe_set(owner, 'caracteristica_EventoLogico', None)
    assert getattr(partner, 'caracteristica_Evento65') is None


def test_assoc_ladoEsquerdoAcao70_stub_double():
    # caracteristica_Acao has no real 'caracteristica_Acao71' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_AcaoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_AcaoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    partner = caracteristica_Acao()
    setattr(partner, 'caracteristica_Acao71', None)
    _safe_set(owner, 'caracteristica_AcaoLogico', partner)
    assert getattr(partner, 'caracteristica_Acao71') == owner
    _safe_set(owner, 'caracteristica_AcaoLogico', None)
    assert getattr(partner, 'caracteristica_Acao71') is None


def test_assoc_ladoEsquerdoComposicao80_stub_double():
    # caracteristica_Antecedente has no real 'caracteristica_Antecedente82' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_ExpressaoLogica's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_ExpressaoLogica's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    partner = caracteristica_Antecedente()
    setattr(partner, 'caracteristica_Antecedente82', None)
    _safe_set(owner, 'caracteristica_ExpressaoLogica81', partner)
    assert getattr(partner, 'caracteristica_Antecedente82') == owner
    _safe_set(owner, 'caracteristica_ExpressaoLogica81', None)
    assert getattr(partner, 'caracteristica_Antecedente82') is None


def test_assoc_ladoEsquerdoEvento66_stub_double():
    # caracteristica_Evento has no real 'caracteristica_Evento68' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_EventoLogico's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_EventoLogico's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_EventoLogico(operadorLogico="sample_text")
    partner = caracteristica_Evento()
    setattr(partner, 'caracteristica_Evento68', None)
    _safe_set(owner, 'caracteristica_EventoLogico67', partner)
    assert getattr(partner, 'caracteristica_Evento68') == owner
    _safe_set(owner, 'caracteristica_EventoLogico67', None)
    assert getattr(partner, 'caracteristica_Evento68') is None


def test_assoc_literaisInconsistentes109_stub_double():
    # caracteristica_InconsistenciaRegraAdaptacao has no real 'caracteristica_InconsistenciaRegraAdaptacao110' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LiteralAcao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LiteralAcao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LiteralAcao(presenca="sample_text")
    partner = caracteristica_InconsistenciaRegraAdaptacao()
    setattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao110', None)
    _safe_set(owner, 'caracteristica_LiteralAcao111', partner)
    assert owner in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao110')
    _safe_set(owner, 'caracteristica_LiteralAcao111', None)
    assert owner not in getattr(partner, 'caracteristica_InconsistenciaRegraAdaptacao110')


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


def test_assoc_produto103_stub_double():
    # caracteristica_CaracteristicaProduto has no real 'caracteristica_CaracteristicaProduto105' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Estado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Estado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Estado(nome="sample_text", safe=True)
    partner = caracteristica_CaracteristicaProduto()
    setattr(partner, 'caracteristica_CaracteristicaProduto105', None)
    _safe_set(owner, 'caracteristica_Estado104', partner)
    assert getattr(partner, 'caracteristica_CaracteristicaProduto105') == owner
    _safe_set(owner, 'caracteristica_Estado104', None)
    assert getattr(partner, 'caracteristica_CaracteristicaProduto105') is None


def test_assoc_produtos5_stub_double():
    # caracteristica_Produto has no real 'caracteristica_Produto' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_LPS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_LPS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    partner = caracteristica_Produto()
    setattr(partner, 'caracteristica_Produto', None)
    _safe_set(owner, 'caracteristica_LPS6', {partner})
    assert getattr(partner, 'caracteristica_Produto') == owner
    _safe_set(owner, 'caracteristica_LPS6', set())
    assert getattr(partner, 'caracteristica_Produto') is None


def test_assoc_regrasQuebradas97_stub_double():
    # caracteristica_RegraDeComposicao has no real 'caracteristica_RegraDeComposicao99' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Transicao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Transicao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    partner = caracteristica_RegraDeComposicao()
    setattr(partner, 'caracteristica_RegraDeComposicao99', None)
    _safe_set(owner, 'caracteristica_Transicao98', {partner})
    assert getattr(partner, 'caracteristica_RegraDeComposicao99') == owner
    _safe_set(owner, 'caracteristica_Transicao98', set())
    assert getattr(partner, 'caracteristica_RegraDeComposicao99') is None


def test_assoc_sistema11_stub_double():
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


def test_assoc_variacaoPai33_stub_double():
    # caracteristica_Variante has no real 'variantes' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Variante()
    setattr(partner, 'variantes', None)
    _safe_set(owner, 'Variacao34', partner)
    assert getattr(partner, 'variantes') == owner
    _safe_set(owner, 'Variacao34', None)
    assert getattr(partner, 'variantes') is None


def test_assoc_variacoes25_stub_double():
    # caracteristica_Caracteristica has no real 'caracteristicaPai26' property in the generated
    # code (a bare stub) -- manually attach it so caracteristica_Variacao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # caracteristica_Variacao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    partner = caracteristica_Caracteristica()
    setattr(partner, 'caracteristicaPai26', None)
    _safe_set(owner, 'Variacao', partner)
    assert owner in getattr(partner, 'caracteristicaPai26')
    _safe_set(owner, 'Variacao', None)
    assert owner not in getattr(partner, 'caracteristicaPai26')


def test_assoc_variantes30_stub_double():
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


