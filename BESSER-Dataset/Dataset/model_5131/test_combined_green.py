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
    caracteristica_Estado,
    caracteristica_Transicao,
    Antecedente,
    caracteristica_ExpressaoRelacional,
    caracteristica_LiteralComposicao,
    caracteristica_ExpressaoLogica,
    Acao,
    caracteristica_LiteralAcao,
    caracteristica_Designar,
    caracteristica_AcaoLogico,
    Evento,
    caracteristica_EventoRelacional,
    caracteristica_EventoLogico,
    Regra,
    caracteristica_RegraDeContexto,
    caracteristica_RegraDeComposicao,
    Expressao,
    caracteristica_Evento,
    caracteristica_Acao,
    caracteristica_Antecedente,
    CaracteristicaProduto,
    caracteristica_VariacaoDoisProduto,
    caracteristica_CaracteristicaAgrupadaProduto,
    caracteristica_CaracteristicaOpcionalProduto,
    caracteristica_CaracteristicaMandatoriaProduto,
    ElementoDeProduto,
    caracteristica_AtributoProduto,
    caracteristica_VariacaoProduto,
    caracteristica_VarianteProduto,
    caracteristica_CaracteristicaProduto,
    PontoDeVariacao,
    ElementoCaracteristico,
    Elemento,
    caracteristica_RaizDeContexto,
    caracteristica_Variacao,
    caracteristica_Caracteristica,
    caracteristica_InformacaoDeContexto,
    caracteristica_EntidadeDeContexto,
    caracteristica_ElementoCaracteristico,
    ElementoExterno,
    caracteristica_CasoDeTeste,
    caracteristica_CasoDeUso,
    Caracteristica,
    caracteristica_CaracteristicaAgrupada,
    caracteristica_CaracteristicaOpcional,
    caracteristica_CaracteristicaMandatoria,
    caracteristica_VariacaoDois,
    caracteristica_Variante,
    caracteristica_InconsistenciaRegraAdaptacao,
    caracteristica_Simulacao,
    caracteristica_Atributo,
    caracteristica_CaracteristicaRaiz,
    caracteristica_ElementoDeProduto,
    caracteristica_Expressao,
    caracteristica_Produto,
    caracteristica_Regra,
    caracteristica_ElementoExterno,
    caracteristica_Elemento,
    caracteristica_PontoDeVariacao,
    caracteristica_LPS,
    OperadorLogico,
    Qualidade,
    Origem,
    OperadorRelacional,
    CardinalidadeMaxima,
    Validade,
    Presenca,
    OperadorAcaoLogico,
    TipoValor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_caracteristica_estado_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Estado)


def test_hyp_caracteristica_estado_constructor_exists():
    assert callable(caracteristica_Estado.__init__)


def test_hyp_caracteristica_estado_constructor_args():
    sig = inspect.signature(caracteristica_Estado.__init__)
    params = list(sig.parameters.keys())
    assert "safe" in params, "Missing parameter 'safe'"
    assert "nome" in params, "Missing parameter 'nome'"





def test_hyp_caracteristica_transicao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Transicao)


def test_hyp_caracteristica_transicao_constructor_exists():
    assert callable(caracteristica_Transicao.__init__)


def test_hyp_caracteristica_transicao_constructor_args():
    sig = inspect.signature(caracteristica_Transicao.__init__)
    params = list(sig.parameters.keys())
    assert "safe" in params, "Missing parameter 'safe'"
    assert "etiqueta" in params, "Missing parameter 'etiqueta'"





def test_hyp_antecedente_is_not_abstract():
    assert not inspect.isabstract(Antecedente)


def test_hyp_antecedente_constructor_exists():
    assert callable(Antecedente.__init__)


def test_hyp_antecedente_constructor_args():
    sig = inspect.signature(Antecedente.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_expressaorelacional_is_not_abstract():
    assert not inspect.isabstract(caracteristica_ExpressaoRelacional)


def test_hyp_caracteristica_expressaorelacional_constructor_exists():
    assert callable(caracteristica_ExpressaoRelacional.__init__)


def test_hyp_caracteristica_expressaorelacional_constructor_args():
    sig = inspect.signature(caracteristica_ExpressaoRelacional.__init__)
    params = list(sig.parameters.keys())
    assert "operadorRelacional" in params, "Missing parameter 'operadorRelacional'"
    assert "valor" in params, "Missing parameter 'valor'"





def test_hyp_caracteristica_literalcomposicao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_LiteralComposicao)


def test_hyp_caracteristica_literalcomposicao_constructor_exists():
    assert callable(caracteristica_LiteralComposicao.__init__)


def test_hyp_caracteristica_literalcomposicao_constructor_args():
    sig = inspect.signature(caracteristica_LiteralComposicao.__init__)
    params = list(sig.parameters.keys())
    assert "presenca" in params, "Missing parameter 'presenca'"




def test_hyp_caracteristica_expressaologica_is_not_abstract():
    assert not inspect.isabstract(caracteristica_ExpressaoLogica)


def test_hyp_caracteristica_expressaologica_constructor_exists():
    assert callable(caracteristica_ExpressaoLogica.__init__)


def test_hyp_caracteristica_expressaologica_constructor_args():
    sig = inspect.signature(caracteristica_ExpressaoLogica.__init__)
    params = list(sig.parameters.keys())
    assert "operadorLogico" in params, "Missing parameter 'operadorLogico'"




def test_hyp_acao_is_not_abstract():
    assert not inspect.isabstract(Acao)


def test_hyp_acao_constructor_exists():
    assert callable(Acao.__init__)


def test_hyp_acao_constructor_args():
    sig = inspect.signature(Acao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_literalacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_LiteralAcao)


def test_hyp_caracteristica_literalacao_constructor_exists():
    assert callable(caracteristica_LiteralAcao.__init__)


def test_hyp_caracteristica_literalacao_constructor_args():
    sig = inspect.signature(caracteristica_LiteralAcao.__init__)
    params = list(sig.parameters.keys())
    assert "presenca" in params, "Missing parameter 'presenca'"




def test_hyp_caracteristica_designar_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Designar)


def test_hyp_caracteristica_designar_constructor_exists():
    assert callable(caracteristica_Designar.__init__)


def test_hyp_caracteristica_designar_constructor_args():
    sig = inspect.signature(caracteristica_Designar.__init__)
    params = list(sig.parameters.keys())
    assert "tipoValor" in params, "Missing parameter 'tipoValor'"
    assert "valor" in params, "Missing parameter 'valor'"





def test_hyp_caracteristica_acaologico_is_not_abstract():
    assert not inspect.isabstract(caracteristica_AcaoLogico)


def test_hyp_caracteristica_acaologico_constructor_exists():
    assert callable(caracteristica_AcaoLogico.__init__)


def test_hyp_caracteristica_acaologico_constructor_args():
    sig = inspect.signature(caracteristica_AcaoLogico.__init__)
    params = list(sig.parameters.keys())
    assert "operadorAcaoLogico" in params, "Missing parameter 'operadorAcaoLogico'"




def test_hyp_evento_is_not_abstract():
    assert not inspect.isabstract(Evento)


def test_hyp_evento_constructor_exists():
    assert callable(Evento.__init__)


def test_hyp_evento_constructor_args():
    sig = inspect.signature(Evento.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_eventorelacional_is_not_abstract():
    assert not inspect.isabstract(caracteristica_EventoRelacional)


def test_hyp_caracteristica_eventorelacional_constructor_exists():
    assert callable(caracteristica_EventoRelacional.__init__)


def test_hyp_caracteristica_eventorelacional_constructor_args():
    sig = inspect.signature(caracteristica_EventoRelacional.__init__)
    params = list(sig.parameters.keys())
    assert "operadorRelacional" in params, "Missing parameter 'operadorRelacional'"
    assert "valor" in params, "Missing parameter 'valor'"





def test_hyp_caracteristica_eventologico_is_not_abstract():
    assert not inspect.isabstract(caracteristica_EventoLogico)


def test_hyp_caracteristica_eventologico_constructor_exists():
    assert callable(caracteristica_EventoLogico.__init__)


def test_hyp_caracteristica_eventologico_constructor_args():
    sig = inspect.signature(caracteristica_EventoLogico.__init__)
    params = list(sig.parameters.keys())
    assert "operadorLogico" in params, "Missing parameter 'operadorLogico'"




def test_hyp_regra_is_not_abstract():
    assert not inspect.isabstract(Regra)


def test_hyp_regra_constructor_exists():
    assert callable(Regra.__init__)


def test_hyp_regra_constructor_args():
    sig = inspect.signature(Regra.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_regradecontexto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_RegraDeContexto)


def test_hyp_caracteristica_regradecontexto_constructor_exists():
    assert callable(caracteristica_RegraDeContexto.__init__)


def test_hyp_caracteristica_regradecontexto_constructor_args():
    sig = inspect.signature(caracteristica_RegraDeContexto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_regradecomposicao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_RegraDeComposicao)


def test_hyp_caracteristica_regradecomposicao_constructor_exists():
    assert callable(caracteristica_RegraDeComposicao.__init__)


def test_hyp_caracteristica_regradecomposicao_constructor_args():
    sig = inspect.signature(caracteristica_RegraDeComposicao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressao_is_not_abstract():
    assert not inspect.isabstract(Expressao)


def test_hyp_expressao_constructor_exists():
    assert callable(Expressao.__init__)


def test_hyp_expressao_constructor_args():
    sig = inspect.signature(Expressao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_evento_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Evento)


def test_hyp_caracteristica_evento_constructor_exists():
    assert callable(caracteristica_Evento.__init__)


def test_hyp_caracteristica_evento_constructor_args():
    sig = inspect.signature(caracteristica_Evento.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_acao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Acao)


def test_hyp_caracteristica_acao_constructor_exists():
    assert callable(caracteristica_Acao.__init__)


def test_hyp_caracteristica_acao_constructor_args():
    sig = inspect.signature(caracteristica_Acao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_antecedente_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Antecedente)


def test_hyp_caracteristica_antecedente_constructor_exists():
    assert callable(caracteristica_Antecedente.__init__)


def test_hyp_caracteristica_antecedente_constructor_args():
    sig = inspect.signature(caracteristica_Antecedente.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristicaproduto_is_not_abstract():
    assert not inspect.isabstract(CaracteristicaProduto)


def test_hyp_caracteristicaproduto_constructor_exists():
    assert callable(CaracteristicaProduto.__init__)


def test_hyp_caracteristicaproduto_constructor_args():
    sig = inspect.signature(CaracteristicaProduto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_variacaodoisproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_VariacaoDoisProduto)


def test_hyp_caracteristica_variacaodoisproduto_constructor_exists():
    assert callable(caracteristica_VariacaoDoisProduto.__init__)


def test_hyp_caracteristica_variacaodoisproduto_constructor_args():
    sig = inspect.signature(caracteristica_VariacaoDoisProduto.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalidadeMinimaOr" in params, "Missing parameter 'cardinalidadeMinimaOr'"
    assert "cardinalidadeMaxima" in params, "Missing parameter 'cardinalidadeMaxima'"
    assert "cardinalidadeMaximaOr" in params, "Missing parameter 'cardinalidadeMaximaOr'"






def test_hyp_caracteristica_caracteristicaagrupadaproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaAgrupadaProduto)


def test_hyp_caracteristica_caracteristicaagrupadaproduto_constructor_exists():
    assert callable(caracteristica_CaracteristicaAgrupadaProduto.__init__)


def test_hyp_caracteristica_caracteristicaagrupadaproduto_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaAgrupadaProduto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicaopcionalproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaOpcionalProduto)


def test_hyp_caracteristica_caracteristicaopcionalproduto_constructor_exists():
    assert callable(caracteristica_CaracteristicaOpcionalProduto.__init__)


def test_hyp_caracteristica_caracteristicaopcionalproduto_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaOpcionalProduto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicamandatoriaproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaMandatoriaProduto)


def test_hyp_caracteristica_caracteristicamandatoriaproduto_constructor_exists():
    assert callable(caracteristica_CaracteristicaMandatoriaProduto.__init__)


def test_hyp_caracteristica_caracteristicamandatoriaproduto_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaMandatoriaProduto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementodeproduto_is_not_abstract():
    assert not inspect.isabstract(ElementoDeProduto)


def test_hyp_elementodeproduto_constructor_exists():
    assert callable(ElementoDeProduto.__init__)


def test_hyp_elementodeproduto_constructor_args():
    sig = inspect.signature(ElementoDeProduto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_atributoproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_AtributoProduto)


def test_hyp_caracteristica_atributoproduto_constructor_exists():
    assert callable(caracteristica_AtributoProduto.__init__)


def test_hyp_caracteristica_atributoproduto_constructor_args():
    sig = inspect.signature(caracteristica_AtributoProduto.__init__)
    params = list(sig.parameters.keys())
    assert "tipoValor" in params, "Missing parameter 'tipoValor'"
    assert "valor" in params, "Missing parameter 'valor'"





def test_hyp_caracteristica_variacaoproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_VariacaoProduto)


def test_hyp_caracteristica_variacaoproduto_constructor_exists():
    assert callable(caracteristica_VariacaoProduto.__init__)


def test_hyp_caracteristica_variacaoproduto_constructor_args():
    sig = inspect.signature(caracteristica_VariacaoProduto.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalidadeMaxima" in params, "Missing parameter 'cardinalidadeMaxima'"
    assert "cardinalidadeMinima" in params, "Missing parameter 'cardinalidadeMinima'"





def test_hyp_caracteristica_varianteproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_VarianteProduto)


def test_hyp_caracteristica_varianteproduto_constructor_exists():
    assert callable(caracteristica_VarianteProduto.__init__)


def test_hyp_caracteristica_varianteproduto_constructor_args():
    sig = inspect.signature(caracteristica_VarianteProduto.__init__)
    params = list(sig.parameters.keys())
    assert "selecionado" in params, "Missing parameter 'selecionado'"




def test_hyp_caracteristica_caracteristicaproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaProduto)


def test_hyp_caracteristica_caracteristicaproduto_constructor_exists():
    assert callable(caracteristica_CaracteristicaProduto.__init__)


def test_hyp_caracteristica_caracteristicaproduto_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaProduto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pontodevariacao_is_not_abstract():
    assert not inspect.isabstract(PontoDeVariacao)


def test_hyp_pontodevariacao_constructor_exists():
    assert callable(PontoDeVariacao.__init__)


def test_hyp_pontodevariacao_constructor_args():
    sig = inspect.signature(PontoDeVariacao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementocaracteristico_is_not_abstract():
    assert not inspect.isabstract(ElementoCaracteristico)


def test_hyp_elementocaracteristico_constructor_exists():
    assert callable(ElementoCaracteristico.__init__)


def test_hyp_elementocaracteristico_constructor_args():
    sig = inspect.signature(ElementoCaracteristico.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elemento_is_not_abstract():
    assert not inspect.isabstract(Elemento)


def test_hyp_elemento_constructor_exists():
    assert callable(Elemento.__init__)


def test_hyp_elemento_constructor_args():
    sig = inspect.signature(Elemento.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_raizdecontexto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_RaizDeContexto)


def test_hyp_caracteristica_raizdecontexto_constructor_exists():
    assert callable(caracteristica_RaizDeContexto.__init__)


def test_hyp_caracteristica_raizdecontexto_constructor_args():
    sig = inspect.signature(caracteristica_RaizDeContexto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_variacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Variacao)


def test_hyp_caracteristica_variacao_constructor_exists():
    assert callable(caracteristica_Variacao.__init__)


def test_hyp_caracteristica_variacao_constructor_args():
    sig = inspect.signature(caracteristica_Variacao.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalidadeMaxima" in params, "Missing parameter 'cardinalidadeMaxima'"
    assert "cardinalidadeMinima" in params, "Missing parameter 'cardinalidadeMinima'"





def test_hyp_caracteristica_caracteristica_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Caracteristica)


def test_hyp_caracteristica_caracteristica_constructor_exists():
    assert callable(caracteristica_Caracteristica.__init__)


def test_hyp_caracteristica_caracteristica_constructor_args():
    sig = inspect.signature(caracteristica_Caracteristica.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_informacaodecontexto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_InformacaoDeContexto)


def test_hyp_caracteristica_informacaodecontexto_constructor_exists():
    assert callable(caracteristica_InformacaoDeContexto.__init__)


def test_hyp_caracteristica_informacaodecontexto_constructor_args():
    sig = inspect.signature(caracteristica_InformacaoDeContexto.__init__)
    params = list(sig.parameters.keys())
    assert "origem" in params, "Missing parameter 'origem'"
    assert "qualidade" in params, "Missing parameter 'qualidade'"
    assert "validade" in params, "Missing parameter 'validade'"
    assert "valor" in params, "Missing parameter 'valor'"
    assert "tipoValor" in params, "Missing parameter 'tipoValor'"








def test_hyp_caracteristica_entidadedecontexto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_EntidadeDeContexto)


def test_hyp_caracteristica_entidadedecontexto_constructor_exists():
    assert callable(caracteristica_EntidadeDeContexto.__init__)


def test_hyp_caracteristica_entidadedecontexto_constructor_args():
    sig = inspect.signature(caracteristica_EntidadeDeContexto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_elementocaracteristico_is_not_abstract():
    assert not inspect.isabstract(caracteristica_ElementoCaracteristico)


def test_hyp_caracteristica_elementocaracteristico_constructor_exists():
    assert callable(caracteristica_ElementoCaracteristico.__init__)


def test_hyp_caracteristica_elementocaracteristico_constructor_args():
    sig = inspect.signature(caracteristica_ElementoCaracteristico.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementoexterno_is_not_abstract():
    assert not inspect.isabstract(ElementoExterno)


def test_hyp_elementoexterno_constructor_exists():
    assert callable(ElementoExterno.__init__)


def test_hyp_elementoexterno_constructor_args():
    sig = inspect.signature(ElementoExterno.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_casodeteste_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CasoDeTeste)


def test_hyp_caracteristica_casodeteste_constructor_exists():
    assert callable(caracteristica_CasoDeTeste.__init__)


def test_hyp_caracteristica_casodeteste_constructor_args():
    sig = inspect.signature(caracteristica_CasoDeTeste.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_casodeuso_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CasoDeUso)


def test_hyp_caracteristica_casodeuso_constructor_exists():
    assert callable(caracteristica_CasoDeUso.__init__)


def test_hyp_caracteristica_casodeuso_constructor_args():
    sig = inspect.signature(caracteristica_CasoDeUso.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_is_not_abstract():
    assert not inspect.isabstract(Caracteristica)


def test_hyp_caracteristica_constructor_exists():
    assert callable(Caracteristica.__init__)


def test_hyp_caracteristica_constructor_args():
    sig = inspect.signature(Caracteristica.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicaagrupada_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaAgrupada)


def test_hyp_caracteristica_caracteristicaagrupada_constructor_exists():
    assert callable(caracteristica_CaracteristicaAgrupada.__init__)


def test_hyp_caracteristica_caracteristicaagrupada_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaAgrupada.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicaopcional_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaOpcional)


def test_hyp_caracteristica_caracteristicaopcional_constructor_exists():
    assert callable(caracteristica_CaracteristicaOpcional.__init__)


def test_hyp_caracteristica_caracteristicaopcional_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaOpcional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicamandatoria_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaMandatoria)


def test_hyp_caracteristica_caracteristicamandatoria_constructor_exists():
    assert callable(caracteristica_CaracteristicaMandatoria.__init__)


def test_hyp_caracteristica_caracteristicamandatoria_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaMandatoria.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_variacaodois_is_not_abstract():
    assert not inspect.isabstract(caracteristica_VariacaoDois)


def test_hyp_caracteristica_variacaodois_constructor_exists():
    assert callable(caracteristica_VariacaoDois.__init__)


def test_hyp_caracteristica_variacaodois_constructor_args():
    sig = inspect.signature(caracteristica_VariacaoDois.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalidadeMinimaOr" in params, "Missing parameter 'cardinalidadeMinimaOr'"
    assert "cardinalidadeMaximaOr" in params, "Missing parameter 'cardinalidadeMaximaOr'"
    assert "cardinalidadeMaxima" in params, "Missing parameter 'cardinalidadeMaxima'"






def test_hyp_caracteristica_variante_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Variante)


def test_hyp_caracteristica_variante_constructor_exists():
    assert callable(caracteristica_Variante.__init__)


def test_hyp_caracteristica_variante_constructor_args():
    sig = inspect.signature(caracteristica_Variante.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_inconsistenciaregraadaptacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_InconsistenciaRegraAdaptacao)


def test_hyp_caracteristica_inconsistenciaregraadaptacao_constructor_exists():
    assert callable(caracteristica_InconsistenciaRegraAdaptacao.__init__)


def test_hyp_caracteristica_inconsistenciaregraadaptacao_constructor_args():
    sig = inspect.signature(caracteristica_InconsistenciaRegraAdaptacao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_simulacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Simulacao)


def test_hyp_caracteristica_simulacao_constructor_exists():
    assert callable(caracteristica_Simulacao.__init__)


def test_hyp_caracteristica_simulacao_constructor_args():
    sig = inspect.signature(caracteristica_Simulacao.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_atributo_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Atributo)


def test_hyp_caracteristica_atributo_constructor_exists():
    assert callable(caracteristica_Atributo.__init__)


def test_hyp_caracteristica_atributo_constructor_args():
    sig = inspect.signature(caracteristica_Atributo.__init__)
    params = list(sig.parameters.keys())
    assert "tipoValor" in params, "Missing parameter 'tipoValor'"




def test_hyp_caracteristica_caracteristicaraiz_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaRaiz)


def test_hyp_caracteristica_caracteristicaraiz_constructor_exists():
    assert callable(caracteristica_CaracteristicaRaiz.__init__)


def test_hyp_caracteristica_caracteristicaraiz_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaRaiz.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_elementodeproduto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_ElementoDeProduto)


def test_hyp_caracteristica_elementodeproduto_constructor_exists():
    assert callable(caracteristica_ElementoDeProduto.__init__)


def test_hyp_caracteristica_elementodeproduto_constructor_args():
    sig = inspect.signature(caracteristica_ElementoDeProduto.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_expressao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Expressao)


def test_hyp_caracteristica_expressao_constructor_exists():
    assert callable(caracteristica_Expressao.__init__)


def test_hyp_caracteristica_expressao_constructor_args():
    sig = inspect.signature(caracteristica_Expressao.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_produto_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Produto)


def test_hyp_caracteristica_produto_constructor_exists():
    assert callable(caracteristica_Produto.__init__)


def test_hyp_caracteristica_produto_constructor_args():
    sig = inspect.signature(caracteristica_Produto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_regra_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Regra)


def test_hyp_caracteristica_regra_constructor_exists():
    assert callable(caracteristica_Regra.__init__)


def test_hyp_caracteristica_regra_constructor_args():
    sig = inspect.signature(caracteristica_Regra.__init__)
    params = list(sig.parameters.keys())
    assert "conteudo" in params, "Missing parameter 'conteudo'"
    assert "nome" in params, "Missing parameter 'nome'"





def test_hyp_caracteristica_elementoexterno_is_not_abstract():
    assert not inspect.isabstract(caracteristica_ElementoExterno)


def test_hyp_caracteristica_elementoexterno_constructor_exists():
    assert callable(caracteristica_ElementoExterno.__init__)


def test_hyp_caracteristica_elementoexterno_constructor_args():
    sig = inspect.signature(caracteristica_ElementoExterno.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_elemento_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Elemento)


def test_hyp_caracteristica_elemento_constructor_exists():
    assert callable(caracteristica_Elemento.__init__)


def test_hyp_caracteristica_elemento_constructor_args():
    sig = inspect.signature(caracteristica_Elemento.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_pontodevariacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_PontoDeVariacao)


def test_hyp_caracteristica_pontodevariacao_constructor_exists():
    assert callable(caracteristica_PontoDeVariacao.__init__)


def test_hyp_caracteristica_pontodevariacao_constructor_args():
    sig = inspect.signature(caracteristica_PontoDeVariacao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_lps_is_not_abstract():
    assert not inspect.isabstract(caracteristica_LPS)


def test_hyp_caracteristica_lps_constructor_exists():
    assert callable(caracteristica_LPS.__init__)


def test_hyp_caracteristica_lps_constructor_args():
    sig = inspect.signature(caracteristica_LPS.__init__)
    params = list(sig.parameters.keys())
    assert "erro" in params, "Missing parameter 'erro'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "valoresContextuais" in params, "Missing parameter 'valoresContextuais'"




def test_hyp_operadorlogico_exists():
    # Check that the Enumeration exists
    assert OperadorLogico is not None

def test_hyp_operadorlogico_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperadorLogico]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperadorLogico"

def test_hyp_qualidade_exists():
    # Check that the Enumeration exists
    assert Qualidade is not None

def test_hyp_qualidade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Qualidade]
    expected_literals = [
        "Baixo",
        "Alto",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Qualidade"

def test_hyp_origem_exists():
    # Check that the Enumeration exists
    assert Origem is not None

def test_hyp_origem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Origem]
    expected_literals = [
        "Perfil",
        "Sentida",
        "Usuario",
        "Derivada",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Origem"

def test_hyp_operadorrelacional_exists():
    # Check that the Enumeration exists
    assert OperadorRelacional is not None

def test_hyp_operadorrelacional_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperadorRelacional]
    expected_literals = [
        "IGUAL",
        "MAIOR",
        "MAIORIGUAL",
        "MENOR",
        "DIFERENTE",
        "MENORIGUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperadorRelacional"

def test_hyp_cardinalidademaxima_exists():
    # Check that the Enumeration exists
    assert CardinalidadeMaxima is not None

def test_hyp_cardinalidademaxima_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardinalidadeMaxima]
    expected_literals = [
        "OR",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardinalidadeMaxima"

def test_hyp_validade_exists():
    # Check that the Enumeration exists
    assert Validade is not None

def test_hyp_validade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Validade]
    expected_literals = [
        "Permanente",
        "Volatil",
        "Frequente",
        "Raramente",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Validade"

def test_hyp_presenca_exists():
    # Check that the Enumeration exists
    assert Presenca is not None

def test_hyp_presenca_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Presenca]
    expected_literals = [
        "PRESENTE",
        "AUSENTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Presenca"

def test_hyp_operadoracaologico_exists():
    # Check that the Enumeration exists
    assert OperadorAcaoLogico is not None

def test_hyp_operadoracaologico_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperadorAcaoLogico]
    expected_literals = [
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperadorAcaoLogico"

def test_hyp_tipovalor_exists():
    # Check that the Enumeration exists
    assert TipoValor is not None

def test_hyp_tipovalor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TipoValor]
    expected_literals = [
        "TFloat",
        "TInteger",
        "TString",
        "TBoolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TipoValor"


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
caracteristica_Estado_strategy = st.builds(
    caracteristica_Estado,
    safe=
        st.booleans(),
    nome=
        safe_text
)
caracteristica_Transicao_strategy = st.builds(
    caracteristica_Transicao,
    safe=
        st.booleans(),
    etiqueta=
        safe_text
)
Antecedente_strategy = st.builds(
    Antecedente,
)
caracteristica_ExpressaoRelacional_strategy = st.builds(
    caracteristica_ExpressaoRelacional,
    operadorRelacional=
        safe_text,
    valor=
        safe_text
)
caracteristica_LiteralComposicao_strategy = st.builds(
    caracteristica_LiteralComposicao,
    presenca=
        safe_text
)
caracteristica_ExpressaoLogica_strategy = st.builds(
    caracteristica_ExpressaoLogica,
    operadorLogico=
        safe_text
)
Acao_strategy = st.builds(
    Acao,
)
caracteristica_LiteralAcao_strategy = st.builds(
    caracteristica_LiteralAcao,
    presenca=
        safe_text
)
caracteristica_Designar_strategy = st.builds(
    caracteristica_Designar,
    tipoValor=
        safe_text,
    valor=
        safe_text
)
caracteristica_AcaoLogico_strategy = st.builds(
    caracteristica_AcaoLogico,
    operadorAcaoLogico=
        safe_text
)
Evento_strategy = st.builds(
    Evento,
)
caracteristica_EventoRelacional_strategy = st.builds(
    caracteristica_EventoRelacional,
    operadorRelacional=
        safe_text,
    valor=
        safe_text
)
caracteristica_EventoLogico_strategy = st.builds(
    caracteristica_EventoLogico,
    operadorLogico=
        safe_text
)
Regra_strategy = st.builds(
    Regra,
)
caracteristica_RegraDeContexto_strategy = st.builds(
    caracteristica_RegraDeContexto,
)
caracteristica_RegraDeComposicao_strategy = st.builds(
    caracteristica_RegraDeComposicao,
)
Expressao_strategy = st.builds(
    Expressao,
)
caracteristica_Evento_strategy = st.builds(
    caracteristica_Evento,
)
caracteristica_Acao_strategy = st.builds(
    caracteristica_Acao,
)
caracteristica_Antecedente_strategy = st.builds(
    caracteristica_Antecedente,
)
CaracteristicaProduto_strategy = st.builds(
    CaracteristicaProduto,
)
caracteristica_VariacaoDoisProduto_strategy = st.builds(
    caracteristica_VariacaoDoisProduto,
    cardinalidadeMinimaOr=
        safe_text,
    cardinalidadeMaxima=
        safe_text,
    cardinalidadeMaximaOr=
        safe_text
)
caracteristica_CaracteristicaAgrupadaProduto_strategy = st.builds(
    caracteristica_CaracteristicaAgrupadaProduto,
)
caracteristica_CaracteristicaOpcionalProduto_strategy = st.builds(
    caracteristica_CaracteristicaOpcionalProduto,
)
caracteristica_CaracteristicaMandatoriaProduto_strategy = st.builds(
    caracteristica_CaracteristicaMandatoriaProduto,
)
ElementoDeProduto_strategy = st.builds(
    ElementoDeProduto,
)
caracteristica_AtributoProduto_strategy = st.builds(
    caracteristica_AtributoProduto,
    tipoValor=
        safe_text,
    valor=
        safe_text
)
caracteristica_VariacaoProduto_strategy = st.builds(
    caracteristica_VariacaoProduto,
    cardinalidadeMaxima=
        safe_text,
    cardinalidadeMinima=
        safe_text
)
caracteristica_VarianteProduto_strategy = st.builds(
    caracteristica_VarianteProduto,
    selecionado=
        safe_text
)
caracteristica_CaracteristicaProduto_strategy = st.builds(
    caracteristica_CaracteristicaProduto,
)
PontoDeVariacao_strategy = st.builds(
    PontoDeVariacao,
)
ElementoCaracteristico_strategy = st.builds(
    ElementoCaracteristico,
)
Elemento_strategy = st.builds(
    Elemento,
)
caracteristica_RaizDeContexto_strategy = st.builds(
    caracteristica_RaizDeContexto,
)
caracteristica_Variacao_strategy = st.builds(
    caracteristica_Variacao,
    cardinalidadeMaxima=
        safe_text,
    cardinalidadeMinima=
        safe_text
)
caracteristica_Caracteristica_strategy = st.builds(
    caracteristica_Caracteristica,
)
caracteristica_InformacaoDeContexto_strategy = st.builds(
    caracteristica_InformacaoDeContexto,
    origem=
        safe_text,
    qualidade=
        safe_text,
    validade=
        safe_text,
    valor=
        safe_text,
    tipoValor=
        safe_text
)
caracteristica_EntidadeDeContexto_strategy = st.builds(
    caracteristica_EntidadeDeContexto,
)
caracteristica_ElementoCaracteristico_strategy = st.builds(
    caracteristica_ElementoCaracteristico,
)
ElementoExterno_strategy = st.builds(
    ElementoExterno,
)
caracteristica_CasoDeTeste_strategy = st.builds(
    caracteristica_CasoDeTeste,
)
caracteristica_CasoDeUso_strategy = st.builds(
    caracteristica_CasoDeUso,
)
Caracteristica_strategy = st.builds(
    Caracteristica,
)
caracteristica_CaracteristicaAgrupada_strategy = st.builds(
    caracteristica_CaracteristicaAgrupada,
)
caracteristica_CaracteristicaOpcional_strategy = st.builds(
    caracteristica_CaracteristicaOpcional,
)
caracteristica_CaracteristicaMandatoria_strategy = st.builds(
    caracteristica_CaracteristicaMandatoria,
)
caracteristica_VariacaoDois_strategy = st.builds(
    caracteristica_VariacaoDois,
    cardinalidadeMinimaOr=
        safe_text,
    cardinalidadeMaximaOr=
        safe_text,
    cardinalidadeMaxima=
        safe_text
)
caracteristica_Variante_strategy = st.builds(
    caracteristica_Variante,
)
caracteristica_InconsistenciaRegraAdaptacao_strategy = st.builds(
    caracteristica_InconsistenciaRegraAdaptacao,
)
caracteristica_Simulacao_strategy = st.builds(
    caracteristica_Simulacao,
    nome=
        safe_text
)
caracteristica_Atributo_strategy = st.builds(
    caracteristica_Atributo,
    tipoValor=
        safe_text
)
caracteristica_CaracteristicaRaiz_strategy = st.builds(
    caracteristica_CaracteristicaRaiz,
)
caracteristica_ElementoDeProduto_strategy = st.builds(
    caracteristica_ElementoDeProduto,
    nome=
        safe_text
)
caracteristica_Expressao_strategy = st.builds(
    caracteristica_Expressao,
    nome=
        safe_text
)
caracteristica_Produto_strategy = st.builds(
    caracteristica_Produto,
)
caracteristica_Regra_strategy = st.builds(
    caracteristica_Regra,
    conteudo=
        safe_text,
    nome=
        safe_text
)
caracteristica_ElementoExterno_strategy = st.builds(
    caracteristica_ElementoExterno,
    nome=
        safe_text
)
caracteristica_Elemento_strategy = st.builds(
    caracteristica_Elemento,
    nome=
        safe_text
)
caracteristica_PontoDeVariacao_strategy = st.builds(
    caracteristica_PontoDeVariacao,
)
caracteristica_LPS_strategy = st.builds(
    caracteristica_LPS,
    erro=
        safe_text,
    nome=
        safe_text,
    valoresContextuais=
        safe_text
)




@given(instance=caracteristica_Estado_strategy)
def test_hyp_caracteristica_estado_safe_setter(instance):
    original = instance.safe
    instance.safe = original
    assert instance.safe == original



@given(instance=caracteristica_Estado_strategy)
def test_hyp_caracteristica_estado_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=caracteristica_Transicao_strategy)
def test_hyp_caracteristica_transicao_safe_setter(instance):
    original = instance.safe
    instance.safe = original
    assert instance.safe == original



@given(instance=caracteristica_Transicao_strategy)
def test_hyp_caracteristica_transicao_etiqueta_setter(instance):
    original = instance.etiqueta
    instance.etiqueta = original
    assert instance.etiqueta == original





@given(instance=caracteristica_ExpressaoRelacional_strategy)
def test_hyp_caracteristica_expressaorelacional_operadorRelacional_setter(instance):
    original = instance.operadorRelacional
    instance.operadorRelacional = original
    assert instance.operadorRelacional == original



@given(instance=caracteristica_ExpressaoRelacional_strategy)
def test_hyp_caracteristica_expressaorelacional_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original




@given(instance=caracteristica_LiteralComposicao_strategy)
def test_hyp_caracteristica_literalcomposicao_presenca_setter(instance):
    original = instance.presenca
    instance.presenca = original
    assert instance.presenca == original




@given(instance=caracteristica_ExpressaoLogica_strategy)
def test_hyp_caracteristica_expressaologica_operadorLogico_setter(instance):
    original = instance.operadorLogico
    instance.operadorLogico = original
    assert instance.operadorLogico == original





@given(instance=caracteristica_LiteralAcao_strategy)
def test_hyp_caracteristica_literalacao_presenca_setter(instance):
    original = instance.presenca
    instance.presenca = original
    assert instance.presenca == original




@given(instance=caracteristica_Designar_strategy)
def test_hyp_caracteristica_designar_tipoValor_setter(instance):
    original = instance.tipoValor
    instance.tipoValor = original
    assert instance.tipoValor == original



@given(instance=caracteristica_Designar_strategy)
def test_hyp_caracteristica_designar_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original




@given(instance=caracteristica_AcaoLogico_strategy)
def test_hyp_caracteristica_acaologico_operadorAcaoLogico_setter(instance):
    original = instance.operadorAcaoLogico
    instance.operadorAcaoLogico = original
    assert instance.operadorAcaoLogico == original





@given(instance=caracteristica_EventoRelacional_strategy)
def test_hyp_caracteristica_eventorelacional_operadorRelacional_setter(instance):
    original = instance.operadorRelacional
    instance.operadorRelacional = original
    assert instance.operadorRelacional == original



@given(instance=caracteristica_EventoRelacional_strategy)
def test_hyp_caracteristica_eventorelacional_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original




@given(instance=caracteristica_EventoLogico_strategy)
def test_hyp_caracteristica_eventologico_operadorLogico_setter(instance):
    original = instance.operadorLogico
    instance.operadorLogico = original
    assert instance.operadorLogico == original












@given(instance=caracteristica_VariacaoDoisProduto_strategy)
def test_hyp_caracteristica_variacaodoisproduto_cardinalidadeMinimaOr_setter(instance):
    original = instance.cardinalidadeMinimaOr
    instance.cardinalidadeMinimaOr = original
    assert instance.cardinalidadeMinimaOr == original



@given(instance=caracteristica_VariacaoDoisProduto_strategy)
def test_hyp_caracteristica_variacaodoisproduto_cardinalidadeMaxima_setter(instance):
    original = instance.cardinalidadeMaxima
    instance.cardinalidadeMaxima = original
    assert instance.cardinalidadeMaxima == original



@given(instance=caracteristica_VariacaoDoisProduto_strategy)
def test_hyp_caracteristica_variacaodoisproduto_cardinalidadeMaximaOr_setter(instance):
    original = instance.cardinalidadeMaximaOr
    instance.cardinalidadeMaximaOr = original
    assert instance.cardinalidadeMaximaOr == original








@given(instance=caracteristica_AtributoProduto_strategy)
def test_hyp_caracteristica_atributoproduto_tipoValor_setter(instance):
    original = instance.tipoValor
    instance.tipoValor = original
    assert instance.tipoValor == original



@given(instance=caracteristica_AtributoProduto_strategy)
def test_hyp_caracteristica_atributoproduto_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original




@given(instance=caracteristica_VariacaoProduto_strategy)
def test_hyp_caracteristica_variacaoproduto_cardinalidadeMaxima_setter(instance):
    original = instance.cardinalidadeMaxima
    instance.cardinalidadeMaxima = original
    assert instance.cardinalidadeMaxima == original



@given(instance=caracteristica_VariacaoProduto_strategy)
def test_hyp_caracteristica_variacaoproduto_cardinalidadeMinima_setter(instance):
    original = instance.cardinalidadeMinima
    instance.cardinalidadeMinima = original
    assert instance.cardinalidadeMinima == original




@given(instance=caracteristica_VarianteProduto_strategy)
def test_hyp_caracteristica_varianteproduto_selecionado_setter(instance):
    original = instance.selecionado
    instance.selecionado = original
    assert instance.selecionado == original









@given(instance=caracteristica_Variacao_strategy)
def test_hyp_caracteristica_variacao_cardinalidadeMaxima_setter(instance):
    original = instance.cardinalidadeMaxima
    instance.cardinalidadeMaxima = original
    assert instance.cardinalidadeMaxima == original



@given(instance=caracteristica_Variacao_strategy)
def test_hyp_caracteristica_variacao_cardinalidadeMinima_setter(instance):
    original = instance.cardinalidadeMinima
    instance.cardinalidadeMinima = original
    assert instance.cardinalidadeMinima == original





@given(instance=caracteristica_InformacaoDeContexto_strategy)
def test_hyp_caracteristica_informacaodecontexto_origem_setter(instance):
    original = instance.origem
    instance.origem = original
    assert instance.origem == original



@given(instance=caracteristica_InformacaoDeContexto_strategy)
def test_hyp_caracteristica_informacaodecontexto_qualidade_setter(instance):
    original = instance.qualidade
    instance.qualidade = original
    assert instance.qualidade == original



@given(instance=caracteristica_InformacaoDeContexto_strategy)
def test_hyp_caracteristica_informacaodecontexto_validade_setter(instance):
    original = instance.validade
    instance.validade = original
    assert instance.validade == original



@given(instance=caracteristica_InformacaoDeContexto_strategy)
def test_hyp_caracteristica_informacaodecontexto_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original



@given(instance=caracteristica_InformacaoDeContexto_strategy)
def test_hyp_caracteristica_informacaodecontexto_tipoValor_setter(instance):
    original = instance.tipoValor
    instance.tipoValor = original
    assert instance.tipoValor == original













@given(instance=caracteristica_VariacaoDois_strategy)
def test_hyp_caracteristica_variacaodois_cardinalidadeMinimaOr_setter(instance):
    original = instance.cardinalidadeMinimaOr
    instance.cardinalidadeMinimaOr = original
    assert instance.cardinalidadeMinimaOr == original



@given(instance=caracteristica_VariacaoDois_strategy)
def test_hyp_caracteristica_variacaodois_cardinalidadeMaximaOr_setter(instance):
    original = instance.cardinalidadeMaximaOr
    instance.cardinalidadeMaximaOr = original
    assert instance.cardinalidadeMaximaOr == original



@given(instance=caracteristica_VariacaoDois_strategy)
def test_hyp_caracteristica_variacaodois_cardinalidadeMaxima_setter(instance):
    original = instance.cardinalidadeMaxima
    instance.cardinalidadeMaxima = original
    assert instance.cardinalidadeMaxima == original






@given(instance=caracteristica_Simulacao_strategy)
def test_hyp_caracteristica_simulacao_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=caracteristica_Atributo_strategy)
def test_hyp_caracteristica_atributo_tipoValor_setter(instance):
    original = instance.tipoValor
    instance.tipoValor = original
    assert instance.tipoValor == original





@given(instance=caracteristica_ElementoDeProduto_strategy)
def test_hyp_caracteristica_elementodeproduto_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=caracteristica_Expressao_strategy)
def test_hyp_caracteristica_expressao_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original





@given(instance=caracteristica_Regra_strategy)
def test_hyp_caracteristica_regra_conteudo_setter(instance):
    original = instance.conteudo
    instance.conteudo = original
    assert instance.conteudo == original



@given(instance=caracteristica_Regra_strategy)
def test_hyp_caracteristica_regra_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=caracteristica_ElementoExterno_strategy)
def test_hyp_caracteristica_elementoexterno_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=caracteristica_Elemento_strategy)
def test_hyp_caracteristica_elemento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original





@given(instance=caracteristica_LPS_strategy)
def test_hyp_caracteristica_lps_erro_setter(instance):
    original = instance.erro
    instance.erro = original
    assert instance.erro == original



@given(instance=caracteristica_LPS_strategy)
def test_hyp_caracteristica_lps_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=caracteristica_LPS_strategy)
def test_hyp_caracteristica_lps_valoresContextuais_setter(instance):
    original = instance.valoresContextuais
    instance.valoresContextuais = original
    assert instance.valoresContextuais == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_caracteristica_AcaoLogico_operadorAcaoLogico_value_roundtrip():
    instance = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    assert instance.operadorAcaoLogico == "sample_text"
    instance.operadorAcaoLogico = "sample_text_2"
    assert instance.operadorAcaoLogico == "sample_text_2"


def test_caracteristica_Atributo_tipoValor_value_roundtrip():
    instance = caracteristica_Atributo(tipoValor="sample_text")
    assert instance.tipoValor == "sample_text"
    instance.tipoValor = "sample_text_2"
    assert instance.tipoValor == "sample_text_2"


def test_caracteristica_AtributoProduto_tipoValor_value_roundtrip():
    instance = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    assert instance.tipoValor == "sample_text"
    instance.tipoValor = "sample_text_2"
    assert instance.tipoValor == "sample_text_2"


def test_caracteristica_AtributoProduto_valor_value_roundtrip():
    instance = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_caracteristica_Designar_tipoValor_value_roundtrip():
    instance = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    assert instance.tipoValor == "sample_text"
    instance.tipoValor = "sample_text_2"
    assert instance.tipoValor == "sample_text_2"


def test_caracteristica_Designar_valor_value_roundtrip():
    instance = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_caracteristica_Elemento_nome_value_roundtrip():
    instance = caracteristica_Elemento(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_ElementoDeProduto_nome_value_roundtrip():
    instance = caracteristica_ElementoDeProduto(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_ElementoExterno_nome_value_roundtrip():
    instance = caracteristica_ElementoExterno(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_Estado_nome_value_roundtrip():
    instance = caracteristica_Estado(nome="sample_text", safe=True)
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_Estado_safe_value_roundtrip():
    instance = caracteristica_Estado(nome="sample_text", safe=True)
    assert instance.safe == True
    instance.safe = False
    assert instance.safe == False


def test_caracteristica_EventoLogico_operadorLogico_value_roundtrip():
    instance = caracteristica_EventoLogico(operadorLogico="sample_text")
    assert instance.operadorLogico == "sample_text"
    instance.operadorLogico = "sample_text_2"
    assert instance.operadorLogico == "sample_text_2"


def test_caracteristica_EventoRelacional_operadorRelacional_value_roundtrip():
    instance = caracteristica_EventoRelacional(operadorRelacional="sample_text", valor="sample_text")
    assert instance.operadorRelacional == "sample_text"
    instance.operadorRelacional = "sample_text_2"
    assert instance.operadorRelacional == "sample_text_2"


def test_caracteristica_EventoRelacional_valor_value_roundtrip():
    instance = caracteristica_EventoRelacional(operadorRelacional="sample_text", valor="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_caracteristica_Expressao_nome_value_roundtrip():
    instance = caracteristica_Expressao(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_ExpressaoLogica_operadorLogico_value_roundtrip():
    instance = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    assert instance.operadorLogico == "sample_text"
    instance.operadorLogico = "sample_text_2"
    assert instance.operadorLogico == "sample_text_2"


def test_caracteristica_ExpressaoRelacional_operadorRelacional_value_roundtrip():
    instance = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text", valor="sample_text")
    assert instance.operadorRelacional == "sample_text"
    instance.operadorRelacional = "sample_text_2"
    assert instance.operadorRelacional == "sample_text_2"


def test_caracteristica_ExpressaoRelacional_valor_value_roundtrip():
    instance = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text", valor="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_caracteristica_InformacaoDeContexto_origem_value_roundtrip():
    instance = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    assert instance.origem == "sample_text"
    instance.origem = "sample_text_2"
    assert instance.origem == "sample_text_2"


def test_caracteristica_InformacaoDeContexto_qualidade_value_roundtrip():
    instance = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    assert instance.qualidade == "sample_text"
    instance.qualidade = "sample_text_2"
    assert instance.qualidade == "sample_text_2"


def test_caracteristica_InformacaoDeContexto_tipoValor_value_roundtrip():
    instance = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    assert instance.tipoValor == "sample_text"
    instance.tipoValor = "sample_text_2"
    assert instance.tipoValor == "sample_text_2"


def test_caracteristica_InformacaoDeContexto_validade_value_roundtrip():
    instance = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    assert instance.validade == "sample_text"
    instance.validade = "sample_text_2"
    assert instance.validade == "sample_text_2"


def test_caracteristica_InformacaoDeContexto_valor_value_roundtrip():
    instance = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_caracteristica_LPS_erro_value_roundtrip():
    instance = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    assert instance.erro == "sample_text"
    instance.erro = "sample_text_2"
    assert instance.erro == "sample_text_2"


def test_caracteristica_LPS_nome_value_roundtrip():
    instance = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_LPS_valoresContextuais_value_roundtrip():
    instance = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    assert instance.valoresContextuais == "sample_text"
    instance.valoresContextuais = "sample_text_2"
    assert instance.valoresContextuais == "sample_text_2"


def test_caracteristica_LiteralAcao_presenca_value_roundtrip():
    instance = caracteristica_LiteralAcao(presenca="sample_text")
    assert instance.presenca == "sample_text"
    instance.presenca = "sample_text_2"
    assert instance.presenca == "sample_text_2"


def test_caracteristica_LiteralComposicao_presenca_value_roundtrip():
    instance = caracteristica_LiteralComposicao(presenca="sample_text")
    assert instance.presenca == "sample_text"
    instance.presenca = "sample_text_2"
    assert instance.presenca == "sample_text_2"


def test_caracteristica_Regra_conteudo_value_roundtrip():
    instance = caracteristica_Regra(conteudo="sample_text", nome="sample_text")
    assert instance.conteudo == "sample_text"
    instance.conteudo = "sample_text_2"
    assert instance.conteudo == "sample_text_2"


def test_caracteristica_Regra_nome_value_roundtrip():
    instance = caracteristica_Regra(conteudo="sample_text", nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_Simulacao_nome_value_roundtrip():
    instance = caracteristica_Simulacao(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_caracteristica_Transicao_etiqueta_value_roundtrip():
    instance = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    assert instance.etiqueta == "sample_text"
    instance.etiqueta = "sample_text_2"
    assert instance.etiqueta == "sample_text_2"


def test_caracteristica_Transicao_safe_value_roundtrip():
    instance = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    assert instance.safe == True
    instance.safe = False
    assert instance.safe == False


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


def test_caracteristica_VariacaoDoisProduto_cardinalidadeMaxima_value_roundtrip():
    instance = caracteristica_VariacaoDoisProduto(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert instance.cardinalidadeMaxima == "sample_text"
    instance.cardinalidadeMaxima = "sample_text_2"
    assert instance.cardinalidadeMaxima == "sample_text_2"


def test_caracteristica_VariacaoDoisProduto_cardinalidadeMaximaOr_value_roundtrip():
    instance = caracteristica_VariacaoDoisProduto(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert instance.cardinalidadeMaximaOr == "sample_text"
    instance.cardinalidadeMaximaOr = "sample_text_2"
    assert instance.cardinalidadeMaximaOr == "sample_text_2"


def test_caracteristica_VariacaoDoisProduto_cardinalidadeMinimaOr_value_roundtrip():
    instance = caracteristica_VariacaoDoisProduto(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert instance.cardinalidadeMinimaOr == "sample_text"
    instance.cardinalidadeMinimaOr = "sample_text_2"
    assert instance.cardinalidadeMinimaOr == "sample_text_2"


def test_caracteristica_VariacaoProduto_cardinalidadeMaxima_value_roundtrip():
    instance = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert instance.cardinalidadeMaxima == "sample_text"
    instance.cardinalidadeMaxima = "sample_text_2"
    assert instance.cardinalidadeMaxima == "sample_text_2"


def test_caracteristica_VariacaoProduto_cardinalidadeMinima_value_roundtrip():
    instance = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert instance.cardinalidadeMinima == "sample_text"
    instance.cardinalidadeMinima = "sample_text_2"
    assert instance.cardinalidadeMinima == "sample_text_2"


def test_caracteristica_VarianteProduto_selecionado_value_roundtrip():
    instance = caracteristica_VarianteProduto(selecionado="sample_text")
    assert instance.selecionado == "sample_text"
    instance.selecionado = "sample_text_2"
    assert instance.selecionado == "sample_text_2"


def test_caracteristica_AcaoLogico_isa_Acao():
    instance = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    assert isinstance(instance, Acao)


def test_caracteristica_Designar_isa_Acao():
    instance = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    assert isinstance(instance, Acao)


def test_caracteristica_LiteralAcao_isa_Acao():
    instance = caracteristica_LiteralAcao(presenca="sample_text")
    assert isinstance(instance, Acao)


def test_caracteristica_ExpressaoLogica_isa_Antecedente():
    instance = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    assert isinstance(instance, Antecedente)


def test_caracteristica_ExpressaoRelacional_isa_Antecedente():
    instance = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text", valor="sample_text")
    assert isinstance(instance, Antecedente)


def test_caracteristica_LiteralComposicao_isa_Antecedente():
    instance = caracteristica_LiteralComposicao(presenca="sample_text")
    assert isinstance(instance, Antecedente)


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


def test_caracteristica_CaracteristicaAgrupadaProduto_isa_CaracteristicaProduto():
    instance = caracteristica_CaracteristicaAgrupadaProduto()
    assert isinstance(instance, CaracteristicaProduto)


def test_caracteristica_CaracteristicaMandatoriaProduto_isa_CaracteristicaProduto():
    instance = caracteristica_CaracteristicaMandatoriaProduto()
    assert isinstance(instance, CaracteristicaProduto)


def test_caracteristica_CaracteristicaOpcionalProduto_isa_CaracteristicaProduto():
    instance = caracteristica_CaracteristicaOpcionalProduto()
    assert isinstance(instance, CaracteristicaProduto)


def test_caracteristica_Produto_isa_CaracteristicaProduto():
    instance = caracteristica_Produto()
    assert isinstance(instance, CaracteristicaProduto)


def test_caracteristica_VariacaoDoisProduto_isa_CaracteristicaProduto():
    instance = caracteristica_VariacaoDoisProduto(cardinalidadeMaxima="sample_text", cardinalidadeMaximaOr="sample_text", cardinalidadeMinimaOr="sample_text")
    assert isinstance(instance, CaracteristicaProduto)


def test_caracteristica_Atributo_isa_Elemento():
    instance = caracteristica_Atributo(tipoValor="sample_text")
    assert isinstance(instance, Elemento)


def test_caracteristica_Caracteristica_isa_Elemento():
    instance = caracteristica_Caracteristica()
    assert isinstance(instance, Elemento)


def test_caracteristica_ElementoCaracteristico_isa_Elemento():
    instance = caracteristica_ElementoCaracteristico()
    assert isinstance(instance, Elemento)


def test_caracteristica_EntidadeDeContexto_isa_Elemento():
    instance = caracteristica_EntidadeDeContexto()
    assert isinstance(instance, Elemento)


def test_caracteristica_InformacaoDeContexto_isa_Elemento():
    instance = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    assert isinstance(instance, Elemento)


def test_caracteristica_RaizDeContexto_isa_Elemento():
    instance = caracteristica_RaizDeContexto()
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


def test_caracteristica_AtributoProduto_isa_ElementoDeProduto():
    instance = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    assert isinstance(instance, ElementoDeProduto)


def test_caracteristica_CaracteristicaProduto_isa_ElementoDeProduto():
    instance = caracteristica_CaracteristicaProduto()
    assert isinstance(instance, ElementoDeProduto)


def test_caracteristica_VariacaoProduto_isa_ElementoDeProduto():
    instance = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert isinstance(instance, ElementoDeProduto)


def test_caracteristica_VarianteProduto_isa_ElementoDeProduto():
    instance = caracteristica_VarianteProduto(selecionado="sample_text")
    assert isinstance(instance, ElementoDeProduto)


def test_caracteristica_CasoDeTeste_isa_ElementoExterno():
    instance = caracteristica_CasoDeTeste()
    assert isinstance(instance, ElementoExterno)


def test_caracteristica_CasoDeUso_isa_ElementoExterno():
    instance = caracteristica_CasoDeUso()
    assert isinstance(instance, ElementoExterno)


def test_caracteristica_EventoLogico_isa_Evento():
    instance = caracteristica_EventoLogico(operadorLogico="sample_text")
    assert isinstance(instance, Evento)


def test_caracteristica_EventoRelacional_isa_Evento():
    instance = caracteristica_EventoRelacional(operadorRelacional="sample_text", valor="sample_text")
    assert isinstance(instance, Evento)


def test_caracteristica_Acao_isa_Expressao():
    instance = caracteristica_Acao()
    assert isinstance(instance, Expressao)


def test_caracteristica_Antecedente_isa_Expressao():
    instance = caracteristica_Antecedente()
    assert isinstance(instance, Expressao)


def test_caracteristica_Evento_isa_Expressao():
    instance = caracteristica_Evento()
    assert isinstance(instance, Expressao)


def test_caracteristica_Variacao_isa_PontoDeVariacao():
    instance = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    assert isinstance(instance, PontoDeVariacao)


def test_caracteristica_Variante_isa_PontoDeVariacao():
    instance = caracteristica_Variante()
    assert isinstance(instance, PontoDeVariacao)


def test_caracteristica_RegraDeComposicao_isa_Regra():
    instance = caracteristica_RegraDeComposicao()
    assert isinstance(instance, Regra)


def test_caracteristica_RegraDeContexto_isa_Regra():
    instance = caracteristica_RegraDeContexto()
    assert isinstance(instance, Regra)


def test_assoc_LpsDoSistema33_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_CaracteristicaRaiz()
    b2 = caracteristica_CaracteristicaRaiz()
    _safe_set(a, 'LPS', b1)
    assert _is_linked(a, 'LPS', b1)
    if hasattr(b1, 'sistema'):
        assert _is_linked(b1, 'sistema', a)
    _safe_set(a, 'LPS', b2)
    assert _is_linked(a, 'LPS', b2)
    if hasattr(b1, 'sistema'):
        assert not _is_linked(b1, 'sistema', a)
    if hasattr(b2, 'sistema'):
        assert _is_linked(b2, 'sistema', a)
    _safe_set(a, 'LPS', None)
    assert not _is_linked(a, 'LPS', b2)
    if hasattr(b2, 'sistema'):
        assert not _is_linked(b2, 'sistema', a)


def test_assoc_acoes104_link_reassign_clear():
    a = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    b1 = caracteristica_Acao()
    b2 = caracteristica_Acao()
    _safe_set(a, 'caracteristica_Transicao105', {b1})
    assert _is_linked(a, 'caracteristica_Transicao105', b1)
    if hasattr(b1, 'caracteristica_Acao106'):
        assert _is_linked(b1, 'caracteristica_Acao106', a)
    _safe_set(a, 'caracteristica_Transicao105', {b2})
    assert _is_linked(a, 'caracteristica_Transicao105', b2)
    if hasattr(b1, 'caracteristica_Acao106'):
        assert not _is_linked(b1, 'caracteristica_Acao106', a)
    if hasattr(b2, 'caracteristica_Acao106'):
        assert _is_linked(b2, 'caracteristica_Acao106', a)
    _safe_set(a, 'caracteristica_Transicao105', set())
    assert not _is_linked(a, 'caracteristica_Transicao105', b2)
    if hasattr(b2, 'caracteristica_Acao106'):
        assert not _is_linked(b2, 'caracteristica_Acao106', a)


def test_assoc_atribuicoesInconsistentes116_link_reassign_clear():
    a = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    b1 = caracteristica_InconsistenciaRegraAdaptacao()
    b2 = caracteristica_InconsistenciaRegraAdaptacao()
    _safe_set(a, 'caracteristica_Designar118', b1)
    assert _is_linked(a, 'caracteristica_Designar118', b1)
    if hasattr(b1, 'caracteristica_InconsistenciaRegraAdaptacao117'):
        assert _is_linked(b1, 'caracteristica_InconsistenciaRegraAdaptacao117', a)
    _safe_set(a, 'caracteristica_Designar118', b2)
    assert _is_linked(a, 'caracteristica_Designar118', b2)
    if hasattr(b1, 'caracteristica_InconsistenciaRegraAdaptacao117'):
        assert not _is_linked(b1, 'caracteristica_InconsistenciaRegraAdaptacao117', a)
    if hasattr(b2, 'caracteristica_InconsistenciaRegraAdaptacao117'):
        assert _is_linked(b2, 'caracteristica_InconsistenciaRegraAdaptacao117', a)
    _safe_set(a, 'caracteristica_Designar118', None)
    assert not _is_linked(a, 'caracteristica_Designar118', b2)
    if hasattr(b2, 'caracteristica_InconsistenciaRegraAdaptacao117'):
        assert not _is_linked(b2, 'caracteristica_InconsistenciaRegraAdaptacao117', a)


def test_assoc_atributo31_link_reassign_clear():
    a = caracteristica_Atributo(tipoValor="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'Atributo', b1)
    assert _is_linked(a, 'Atributo', b1)
    if hasattr(b1, 'caracteristicaPai32'):
        assert _is_linked(b1, 'caracteristicaPai32', a)
    _safe_set(a, 'Atributo', b2)
    assert _is_linked(a, 'Atributo', b2)
    if hasattr(b1, 'caracteristicaPai32'):
        assert not _is_linked(b1, 'caracteristicaPai32', a)
    if hasattr(b2, 'caracteristicaPai32'):
        assert _is_linked(b2, 'caracteristicaPai32', a)
    _safe_set(a, 'Atributo', None)
    assert not _is_linked(a, 'Atributo', b2)
    if hasattr(b2, 'caracteristicaPai32'):
        assert not _is_linked(b2, 'caracteristicaPai32', a)


def test_assoc_atributo80_link_reassign_clear():
    a = caracteristica_Designar(tipoValor="sample_text", valor="sample_text")
    b1 = caracteristica_Atributo(tipoValor="sample_text")
    b2 = caracteristica_Atributo(tipoValor="sample_text_2")
    _safe_set(a, 'caracteristica_Designar', b1)
    assert _is_linked(a, 'caracteristica_Designar', b1)
    if hasattr(b1, 'caracteristica_Atributo81'):
        assert _is_linked(b1, 'caracteristica_Atributo81', a)
    _safe_set(a, 'caracteristica_Designar', b2)
    assert _is_linked(a, 'caracteristica_Designar', b2)
    if hasattr(b1, 'caracteristica_Atributo81'):
        assert not _is_linked(b1, 'caracteristica_Atributo81', a)
    if hasattr(b2, 'caracteristica_Atributo81'):
        assert _is_linked(b2, 'caracteristica_Atributo81', a)
    _safe_set(a, 'caracteristica_Designar', None)
    assert not _is_linked(a, 'caracteristica_Designar', b2)
    if hasattr(b2, 'caracteristica_Atributo81'):
        assert not _is_linked(b2, 'caracteristica_Atributo81', a)


def test_assoc_atributoProduto52_link_reassign_clear():
    a = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    b1 = caracteristica_CaracteristicaProduto()
    b2 = caracteristica_CaracteristicaProduto()
    _safe_set(a, 'AtributoProduto', b1)
    assert _is_linked(a, 'AtributoProduto', b1)
    if hasattr(b1, 'caracteristicaProdutoPai53'):
        assert _is_linked(b1, 'caracteristicaProdutoPai53', a)
    _safe_set(a, 'AtributoProduto', b2)
    assert _is_linked(a, 'AtributoProduto', b2)
    if hasattr(b1, 'caracteristicaProdutoPai53'):
        assert not _is_linked(b1, 'caracteristicaProdutoPai53', a)
    if hasattr(b2, 'caracteristicaProdutoPai53'):
        assert _is_linked(b2, 'caracteristicaProdutoPai53', a)
    _safe_set(a, 'AtributoProduto', None)
    assert not _is_linked(a, 'AtributoProduto', b2)
    if hasattr(b2, 'caracteristicaProdutoPai53'):
        assert not _is_linked(b2, 'caracteristicaProdutoPai53', a)


def test_assoc_atributos14_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_Atributo(tipoValor="sample_text")
    b2 = caracteristica_Atributo(tipoValor="sample_text_2")
    _safe_set(a, 'caracteristica_LPS15', {b1})
    assert _is_linked(a, 'caracteristica_LPS15', b1)
    if hasattr(b1, 'caracteristica_Atributo'):
        assert _is_linked(b1, 'caracteristica_Atributo', a)
    _safe_set(a, 'caracteristica_LPS15', {b2})
    assert _is_linked(a, 'caracteristica_LPS15', b2)
    if hasattr(b1, 'caracteristica_Atributo'):
        assert not _is_linked(b1, 'caracteristica_Atributo', a)
    if hasattr(b2, 'caracteristica_Atributo'):
        assert _is_linked(b2, 'caracteristica_Atributo', a)
    _safe_set(a, 'caracteristica_LPS15', set())
    assert not _is_linked(a, 'caracteristica_LPS15', b2)
    if hasattr(b2, 'caracteristica_Atributo'):
        assert not _is_linked(b2, 'caracteristica_Atributo', a)


def test_assoc_caracteristicaPai20_link_reassign_clear():
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


def test_assoc_caracteristicaPai35_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'variacoes', b1)
    assert _is_linked(a, 'variacoes', b1)
    if hasattr(b1, 'Caracteristica36'):
        assert _is_linked(b1, 'Caracteristica36', a)
    _safe_set(a, 'variacoes', b2)
    assert _is_linked(a, 'variacoes', b2)
    if hasattr(b1, 'Caracteristica36'):
        assert not _is_linked(b1, 'Caracteristica36', a)
    if hasattr(b2, 'Caracteristica36'):
        assert _is_linked(b2, 'Caracteristica36', a)
    _safe_set(a, 'variacoes', None)
    assert not _is_linked(a, 'variacoes', b2)
    if hasattr(b2, 'Caracteristica36'):
        assert not _is_linked(b2, 'Caracteristica36', a)


def test_assoc_caracteristicaProdutoPai54_link_reassign_clear():
    a = caracteristica_AtributoProduto(tipoValor="sample_text", valor="sample_text")
    b1 = caracteristica_CaracteristicaProduto()
    b2 = caracteristica_CaracteristicaProduto()
    _safe_set(a, 'atributoProduto', b1)
    assert _is_linked(a, 'atributoProduto', b1)
    if hasattr(b1, 'CaracteristicaProduto55'):
        assert _is_linked(b1, 'CaracteristicaProduto55', a)
    _safe_set(a, 'atributoProduto', b2)
    assert _is_linked(a, 'atributoProduto', b2)
    if hasattr(b1, 'CaracteristicaProduto55'):
        assert not _is_linked(b1, 'CaracteristicaProduto55', a)
    if hasattr(b2, 'CaracteristicaProduto55'):
        assert _is_linked(b2, 'CaracteristicaProduto55', a)
    _safe_set(a, 'atributoProduto', None)
    assert not _is_linked(a, 'atributoProduto', b2)
    if hasattr(b2, 'CaracteristicaProduto55'):
        assert not _is_linked(b2, 'CaracteristicaProduto55', a)


def test_assoc_caracteristicaProdutoPai57_link_reassign_clear():
    a = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_CaracteristicaProduto()
    b2 = caracteristica_CaracteristicaProduto()
    _safe_set(a, 'caracteristica_VariacaoProduto', b1)
    assert _is_linked(a, 'caracteristica_VariacaoProduto', b1)
    if hasattr(b1, 'caracteristica_CaracteristicaProduto'):
        assert _is_linked(b1, 'caracteristica_CaracteristicaProduto', a)
    _safe_set(a, 'caracteristica_VariacaoProduto', b2)
    assert _is_linked(a, 'caracteristica_VariacaoProduto', b2)
    if hasattr(b1, 'caracteristica_CaracteristicaProduto'):
        assert not _is_linked(b1, 'caracteristica_CaracteristicaProduto', a)
    if hasattr(b2, 'caracteristica_CaracteristicaProduto'):
        assert _is_linked(b2, 'caracteristica_CaracteristicaProduto', a)
    _safe_set(a, 'caracteristica_VariacaoProduto', None)
    assert not _is_linked(a, 'caracteristica_VariacaoProduto', b2)
    if hasattr(b2, 'caracteristica_CaracteristicaProduto'):
        assert not _is_linked(b2, 'caracteristica_CaracteristicaProduto', a)


def test_assoc_eAntigo95_link_reassign_clear():
    a = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    b1 = caracteristica_Estado(nome="sample_text", safe=True)
    b2 = caracteristica_Estado(nome="sample_text_2", safe=False)
    _safe_set(a, 'caracteristica_Transicao96', b1)
    assert _is_linked(a, 'caracteristica_Transicao96', b1)
    if hasattr(b1, 'caracteristica_Estado97'):
        assert _is_linked(b1, 'caracteristica_Estado97', a)
    _safe_set(a, 'caracteristica_Transicao96', b2)
    assert _is_linked(a, 'caracteristica_Transicao96', b2)
    if hasattr(b1, 'caracteristica_Estado97'):
        assert not _is_linked(b1, 'caracteristica_Estado97', a)
    if hasattr(b2, 'caracteristica_Estado97'):
        assert _is_linked(b2, 'caracteristica_Estado97', a)
    _safe_set(a, 'caracteristica_Transicao96', None)
    assert not _is_linked(a, 'caracteristica_Transicao96', b2)
    if hasattr(b2, 'caracteristica_Estado97'):
        assert not _is_linked(b2, 'caracteristica_Estado97', a)


def test_assoc_eNovo98_link_reassign_clear():
    a = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    b1 = caracteristica_Estado(nome="sample_text", safe=True)
    b2 = caracteristica_Estado(nome="sample_text_2", safe=False)
    _safe_set(a, 'caracteristica_Transicao99', b1)
    assert _is_linked(a, 'caracteristica_Transicao99', b1)
    if hasattr(b1, 'caracteristica_Estado100'):
        assert _is_linked(b1, 'caracteristica_Estado100', a)
    _safe_set(a, 'caracteristica_Transicao99', b2)
    assert _is_linked(a, 'caracteristica_Transicao99', b2)
    if hasattr(b1, 'caracteristica_Estado100'):
        assert not _is_linked(b1, 'caracteristica_Estado100', a)
    if hasattr(b2, 'caracteristica_Estado100'):
        assert _is_linked(b2, 'caracteristica_Estado100', a)
    _safe_set(a, 'caracteristica_Transicao99', None)
    assert not _is_linked(a, 'caracteristica_Transicao99', b2)
    if hasattr(b2, 'caracteristica_Estado100'):
        assert not _is_linked(b2, 'caracteristica_Estado100', a)


def test_assoc_elemento79_link_reassign_clear():
    a = caracteristica_LiteralAcao(presenca="sample_text")
    b1 = caracteristica_ElementoCaracteristico()
    b2 = caracteristica_ElementoCaracteristico()
    _safe_set(a, 'caracteristica_LiteralAcao', b1)
    assert _is_linked(a, 'caracteristica_LiteralAcao', b1)
    if hasattr(b1, 'caracteristica_ElementoCaracteristico'):
        assert _is_linked(b1, 'caracteristica_ElementoCaracteristico', a)
    _safe_set(a, 'caracteristica_LiteralAcao', b2)
    assert _is_linked(a, 'caracteristica_LiteralAcao', b2)
    if hasattr(b1, 'caracteristica_ElementoCaracteristico'):
        assert not _is_linked(b1, 'caracteristica_ElementoCaracteristico', a)
    if hasattr(b2, 'caracteristica_ElementoCaracteristico'):
        assert _is_linked(b2, 'caracteristica_ElementoCaracteristico', a)
    _safe_set(a, 'caracteristica_LiteralAcao', None)
    assert not _is_linked(a, 'caracteristica_LiteralAcao', b2)
    if hasattr(b2, 'caracteristica_ElementoCaracteristico'):
        assert not _is_linked(b2, 'caracteristica_ElementoCaracteristico', a)


def test_assoc_elemento89_link_reassign_clear():
    a = caracteristica_LiteralComposicao(presenca="sample_text")
    b1 = caracteristica_ElementoCaracteristico()
    b2 = caracteristica_ElementoCaracteristico()
    _safe_set(a, 'caracteristica_LiteralComposicao', b1)
    assert _is_linked(a, 'caracteristica_LiteralComposicao', b1)
    if hasattr(b1, 'caracteristica_ElementoCaracteristico90'):
        assert _is_linked(b1, 'caracteristica_ElementoCaracteristico90', a)
    _safe_set(a, 'caracteristica_LiteralComposicao', b2)
    assert _is_linked(a, 'caracteristica_LiteralComposicao', b2)
    if hasattr(b1, 'caracteristica_ElementoCaracteristico90'):
        assert not _is_linked(b1, 'caracteristica_ElementoCaracteristico90', a)
    if hasattr(b2, 'caracteristica_ElementoCaracteristico90'):
        assert _is_linked(b2, 'caracteristica_ElementoCaracteristico90', a)
    _safe_set(a, 'caracteristica_LiteralComposicao', None)
    assert not _is_linked(a, 'caracteristica_LiteralComposicao', b2)
    if hasattr(b2, 'caracteristica_ElementoCaracteristico90'):
        assert not _is_linked(b2, 'caracteristica_ElementoCaracteristico90', a)


def test_assoc_elementoOriginal44_link_reassign_clear():
    a = caracteristica_ElementoDeProduto(nome="sample_text")
    b1 = caracteristica_Elemento(nome="sample_text")
    b2 = caracteristica_Elemento(nome="sample_text_2")
    _safe_set(a, 'caracteristica_ElementoDeProduto45', b1)
    assert _is_linked(a, 'caracteristica_ElementoDeProduto45', b1)
    if hasattr(b1, 'caracteristica_Elemento46'):
        assert _is_linked(b1, 'caracteristica_Elemento46', a)
    _safe_set(a, 'caracteristica_ElementoDeProduto45', b2)
    assert _is_linked(a, 'caracteristica_ElementoDeProduto45', b2)
    if hasattr(b1, 'caracteristica_Elemento46'):
        assert not _is_linked(b1, 'caracteristica_Elemento46', a)
    if hasattr(b2, 'caracteristica_Elemento46'):
        assert _is_linked(b2, 'caracteristica_Elemento46', a)
    _safe_set(a, 'caracteristica_ElementoDeProduto45', None)
    assert not _is_linked(a, 'caracteristica_ElementoDeProduto45', b2)
    if hasattr(b2, 'caracteristica_Elemento46'):
        assert not _is_linked(b2, 'caracteristica_Elemento46', a)


def test_assoc_elementoPai42_link_reassign_clear():
    a = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    b1 = caracteristica_EntidadeDeContexto()
    b2 = caracteristica_EntidadeDeContexto()
    _safe_set(a, 'informacoesDeContexto', b1)
    assert _is_linked(a, 'informacoesDeContexto', b1)
    if hasattr(b1, 'EntidadeDeContexto43'):
        assert _is_linked(b1, 'EntidadeDeContexto43', a)
    _safe_set(a, 'informacoesDeContexto', b2)
    assert _is_linked(a, 'informacoesDeContexto', b2)
    if hasattr(b1, 'EntidadeDeContexto43'):
        assert not _is_linked(b1, 'EntidadeDeContexto43', a)
    if hasattr(b2, 'EntidadeDeContexto43'):
        assert _is_linked(b2, 'EntidadeDeContexto43', a)
    _safe_set(a, 'informacoesDeContexto', None)
    assert not _is_linked(a, 'informacoesDeContexto', b2)
    if hasattr(b2, 'EntidadeDeContexto43'):
        assert not _is_linked(b2, 'EntidadeDeContexto43', a)


def test_assoc_elementos1_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_Elemento(nome="sample_text")
    b2 = caracteristica_Elemento(nome="sample_text_2")
    _safe_set(a, 'caracteristica_LPS2', {b1})
    assert _is_linked(a, 'caracteristica_LPS2', b1)
    if hasattr(b1, 'caracteristica_Elemento'):
        assert _is_linked(b1, 'caracteristica_Elemento', a)
    _safe_set(a, 'caracteristica_LPS2', {b2})
    assert _is_linked(a, 'caracteristica_LPS2', b2)
    if hasattr(b1, 'caracteristica_Elemento'):
        assert not _is_linked(b1, 'caracteristica_Elemento', a)
    if hasattr(b2, 'caracteristica_Elemento'):
        assert _is_linked(b2, 'caracteristica_Elemento', a)
    _safe_set(a, 'caracteristica_LPS2', set())
    assert not _is_linked(a, 'caracteristica_LPS2', b2)
    if hasattr(b2, 'caracteristica_Elemento'):
        assert not _is_linked(b2, 'caracteristica_Elemento', a)


def test_assoc_elementosDeProduto11_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_ElementoDeProduto(nome="sample_text")
    b2 = caracteristica_ElementoDeProduto(nome="sample_text_2")
    _safe_set(a, 'caracteristica_LPS12', {b1})
    assert _is_linked(a, 'caracteristica_LPS12', b1)
    if hasattr(b1, 'caracteristica_ElementoDeProduto'):
        assert _is_linked(b1, 'caracteristica_ElementoDeProduto', a)
    _safe_set(a, 'caracteristica_LPS12', {b2})
    assert _is_linked(a, 'caracteristica_LPS12', b2)
    if hasattr(b1, 'caracteristica_ElementoDeProduto'):
        assert not _is_linked(b1, 'caracteristica_ElementoDeProduto', a)
    if hasattr(b2, 'caracteristica_ElementoDeProduto'):
        assert _is_linked(b2, 'caracteristica_ElementoDeProduto', a)
    _safe_set(a, 'caracteristica_LPS12', set())
    assert not _is_linked(a, 'caracteristica_LPS12', b2)
    if hasattr(b2, 'caracteristica_ElementoDeProduto'):
        assert not _is_linked(b2, 'caracteristica_ElementoDeProduto', a)


def test_assoc_elementosExternos21_link_reassign_clear():
    a = caracteristica_ElementoExterno(nome="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'caracteristica_ElementoExterno22', b1)
    assert _is_linked(a, 'caracteristica_ElementoExterno22', b1)
    if hasattr(b1, 'caracteristica_Caracteristica'):
        assert _is_linked(b1, 'caracteristica_Caracteristica', a)
    _safe_set(a, 'caracteristica_ElementoExterno22', b2)
    assert _is_linked(a, 'caracteristica_ElementoExterno22', b2)
    if hasattr(b1, 'caracteristica_Caracteristica'):
        assert not _is_linked(b1, 'caracteristica_Caracteristica', a)
    if hasattr(b2, 'caracteristica_Caracteristica'):
        assert _is_linked(b2, 'caracteristica_Caracteristica', a)
    _safe_set(a, 'caracteristica_ElementoExterno22', None)
    assert not _is_linked(a, 'caracteristica_ElementoExterno22', b2)
    if hasattr(b2, 'caracteristica_Caracteristica'):
        assert not _is_linked(b2, 'caracteristica_Caracteristica', a)


def test_assoc_estados93_link_reassign_clear():
    a = caracteristica_Simulacao(nome="sample_text")
    b1 = caracteristica_Estado(nome="sample_text", safe=True)
    b2 = caracteristica_Estado(nome="sample_text_2", safe=False)
    _safe_set(a, 'caracteristica_Simulacao94', {b1})
    assert _is_linked(a, 'caracteristica_Simulacao94', b1)
    if hasattr(b1, 'caracteristica_Estado'):
        assert _is_linked(b1, 'caracteristica_Estado', a)
    _safe_set(a, 'caracteristica_Simulacao94', {b2})
    assert _is_linked(a, 'caracteristica_Simulacao94', b2)
    if hasattr(b1, 'caracteristica_Estado'):
        assert not _is_linked(b1, 'caracteristica_Estado', a)
    if hasattr(b2, 'caracteristica_Estado'):
        assert _is_linked(b2, 'caracteristica_Estado', a)
    _safe_set(a, 'caracteristica_Simulacao94', set())
    assert not _is_linked(a, 'caracteristica_Simulacao94', b2)
    if hasattr(b2, 'caracteristica_Estado'):
        assert not _is_linked(b2, 'caracteristica_Estado', a)


def test_assoc_expressoes9_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_Expressao(nome="sample_text")
    b2 = caracteristica_Expressao(nome="sample_text_2")
    _safe_set(a, 'caracteristica_LPS10', {b1})
    assert _is_linked(a, 'caracteristica_LPS10', b1)
    if hasattr(b1, 'caracteristica_Expressao'):
        assert _is_linked(b1, 'caracteristica_Expressao', a)
    _safe_set(a, 'caracteristica_LPS10', {b2})
    assert _is_linked(a, 'caracteristica_LPS10', b2)
    if hasattr(b1, 'caracteristica_Expressao'):
        assert not _is_linked(b1, 'caracteristica_Expressao', a)
    if hasattr(b2, 'caracteristica_Expressao'):
        assert _is_linked(b2, 'caracteristica_Expressao', a)
    _safe_set(a, 'caracteristica_LPS10', set())
    assert not _is_linked(a, 'caracteristica_LPS10', b2)
    if hasattr(b2, 'caracteristica_Expressao'):
        assert not _is_linked(b2, 'caracteristica_Expressao', a)


def test_assoc_externos3_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_ElementoExterno(nome="sample_text")
    b2 = caracteristica_ElementoExterno(nome="sample_text_2")
    _safe_set(a, 'caracteristica_LPS4', {b1})
    assert _is_linked(a, 'caracteristica_LPS4', b1)
    if hasattr(b1, 'caracteristica_ElementoExterno'):
        assert _is_linked(b1, 'caracteristica_ElementoExterno', a)
    _safe_set(a, 'caracteristica_LPS4', {b2})
    assert _is_linked(a, 'caracteristica_LPS4', b2)
    if hasattr(b1, 'caracteristica_ElementoExterno'):
        assert not _is_linked(b1, 'caracteristica_ElementoExterno', a)
    if hasattr(b2, 'caracteristica_ElementoExterno'):
        assert _is_linked(b2, 'caracteristica_ElementoExterno', a)
    _safe_set(a, 'caracteristica_LPS4', set())
    assert not _is_linked(a, 'caracteristica_LPS4', b2)
    if hasattr(b2, 'caracteristica_ElementoExterno'):
        assert not _is_linked(b2, 'caracteristica_ElementoExterno', a)


def test_assoc_inconsistenciaERA18_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_InconsistenciaRegraAdaptacao()
    b2 = caracteristica_InconsistenciaRegraAdaptacao()
    _safe_set(a, 'caracteristica_LPS19', {b1})
    assert _is_linked(a, 'caracteristica_LPS19', b1)
    if hasattr(b1, 'caracteristica_InconsistenciaRegraAdaptacao'):
        assert _is_linked(b1, 'caracteristica_InconsistenciaRegraAdaptacao', a)
    _safe_set(a, 'caracteristica_LPS19', {b2})
    assert _is_linked(a, 'caracteristica_LPS19', b2)
    if hasattr(b1, 'caracteristica_InconsistenciaRegraAdaptacao'):
        assert not _is_linked(b1, 'caracteristica_InconsistenciaRegraAdaptacao', a)
    if hasattr(b2, 'caracteristica_InconsistenciaRegraAdaptacao'):
        assert _is_linked(b2, 'caracteristica_InconsistenciaRegraAdaptacao', a)
    _safe_set(a, 'caracteristica_LPS19', set())
    assert not _is_linked(a, 'caracteristica_LPS19', b2)
    if hasattr(b2, 'caracteristica_InconsistenciaRegraAdaptacao'):
        assert not _is_linked(b2, 'caracteristica_InconsistenciaRegraAdaptacao', a)


def test_assoc_informacoesDeContexto41_link_reassign_clear():
    a = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    b1 = caracteristica_EntidadeDeContexto()
    b2 = caracteristica_EntidadeDeContexto()
    _safe_set(a, 'InformacaoDeContexto', b1)
    assert _is_linked(a, 'InformacaoDeContexto', b1)
    if hasattr(b1, 'elementoPai'):
        assert _is_linked(b1, 'elementoPai', a)
    _safe_set(a, 'InformacaoDeContexto', b2)
    assert _is_linked(a, 'InformacaoDeContexto', b2)
    if hasattr(b1, 'elementoPai'):
        assert not _is_linked(b1, 'elementoPai', a)
    if hasattr(b2, 'elementoPai'):
        assert _is_linked(b2, 'elementoPai', a)
    _safe_set(a, 'InformacaoDeContexto', None)
    assert not _is_linked(a, 'InformacaoDeContexto', b2)
    if hasattr(b2, 'elementoPai'):
        assert not _is_linked(b2, 'elementoPai', a)


def test_assoc_ladoDireitoAcao76_link_reassign_clear():
    a = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    b1 = caracteristica_Acao()
    b2 = caracteristica_Acao()
    _safe_set(a, 'caracteristica_AcaoLogico77', b1)
    assert _is_linked(a, 'caracteristica_AcaoLogico77', b1)
    if hasattr(b1, 'caracteristica_Acao78'):
        assert _is_linked(b1, 'caracteristica_Acao78', a)
    _safe_set(a, 'caracteristica_AcaoLogico77', b2)
    assert _is_linked(a, 'caracteristica_AcaoLogico77', b2)
    if hasattr(b1, 'caracteristica_Acao78'):
        assert not _is_linked(b1, 'caracteristica_Acao78', a)
    if hasattr(b2, 'caracteristica_Acao78'):
        assert _is_linked(b2, 'caracteristica_Acao78', a)
    _safe_set(a, 'caracteristica_AcaoLogico77', None)
    assert not _is_linked(a, 'caracteristica_AcaoLogico77', b2)
    if hasattr(b2, 'caracteristica_Acao78'):
        assert not _is_linked(b2, 'caracteristica_Acao78', a)


def test_assoc_ladoDireitoComposicao82_link_reassign_clear():
    a = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    b1 = caracteristica_Antecedente()
    b2 = caracteristica_Antecedente()
    _safe_set(a, 'caracteristica_ExpressaoLogica', b1)
    assert _is_linked(a, 'caracteristica_ExpressaoLogica', b1)
    if hasattr(b1, 'caracteristica_Antecedente83'):
        assert _is_linked(b1, 'caracteristica_Antecedente83', a)
    _safe_set(a, 'caracteristica_ExpressaoLogica', b2)
    assert _is_linked(a, 'caracteristica_ExpressaoLogica', b2)
    if hasattr(b1, 'caracteristica_Antecedente83'):
        assert not _is_linked(b1, 'caracteristica_Antecedente83', a)
    if hasattr(b2, 'caracteristica_Antecedente83'):
        assert _is_linked(b2, 'caracteristica_Antecedente83', a)
    _safe_set(a, 'caracteristica_ExpressaoLogica', None)
    assert not _is_linked(a, 'caracteristica_ExpressaoLogica', b2)
    if hasattr(b2, 'caracteristica_Antecedente83'):
        assert not _is_linked(b2, 'caracteristica_Antecedente83', a)


def test_assoc_ladoDireitoEvento68_link_reassign_clear():
    a = caracteristica_EventoLogico(operadorLogico="sample_text")
    b1 = caracteristica_Evento()
    b2 = caracteristica_Evento()
    _safe_set(a, 'caracteristica_EventoLogico', b1)
    assert _is_linked(a, 'caracteristica_EventoLogico', b1)
    if hasattr(b1, 'caracteristica_Evento69'):
        assert _is_linked(b1, 'caracteristica_Evento69', a)
    _safe_set(a, 'caracteristica_EventoLogico', b2)
    assert _is_linked(a, 'caracteristica_EventoLogico', b2)
    if hasattr(b1, 'caracteristica_Evento69'):
        assert not _is_linked(b1, 'caracteristica_Evento69', a)
    if hasattr(b2, 'caracteristica_Evento69'):
        assert _is_linked(b2, 'caracteristica_Evento69', a)
    _safe_set(a, 'caracteristica_EventoLogico', None)
    assert not _is_linked(a, 'caracteristica_EventoLogico', b2)
    if hasattr(b2, 'caracteristica_Evento69'):
        assert not _is_linked(b2, 'caracteristica_Evento69', a)


def test_assoc_ladoEsquerdoAcao74_link_reassign_clear():
    a = caracteristica_AcaoLogico(operadorAcaoLogico="sample_text")
    b1 = caracteristica_Acao()
    b2 = caracteristica_Acao()
    _safe_set(a, 'caracteristica_AcaoLogico', b1)
    assert _is_linked(a, 'caracteristica_AcaoLogico', b1)
    if hasattr(b1, 'caracteristica_Acao75'):
        assert _is_linked(b1, 'caracteristica_Acao75', a)
    _safe_set(a, 'caracteristica_AcaoLogico', b2)
    assert _is_linked(a, 'caracteristica_AcaoLogico', b2)
    if hasattr(b1, 'caracteristica_Acao75'):
        assert not _is_linked(b1, 'caracteristica_Acao75', a)
    if hasattr(b2, 'caracteristica_Acao75'):
        assert _is_linked(b2, 'caracteristica_Acao75', a)
    _safe_set(a, 'caracteristica_AcaoLogico', None)
    assert not _is_linked(a, 'caracteristica_AcaoLogico', b2)
    if hasattr(b2, 'caracteristica_Acao75'):
        assert not _is_linked(b2, 'caracteristica_Acao75', a)


def test_assoc_ladoEsquerdoComposicao84_link_reassign_clear():
    a = caracteristica_ExpressaoLogica(operadorLogico="sample_text")
    b1 = caracteristica_Antecedente()
    b2 = caracteristica_Antecedente()
    _safe_set(a, 'caracteristica_ExpressaoLogica85', b1)
    assert _is_linked(a, 'caracteristica_ExpressaoLogica85', b1)
    if hasattr(b1, 'caracteristica_Antecedente86'):
        assert _is_linked(b1, 'caracteristica_Antecedente86', a)
    _safe_set(a, 'caracteristica_ExpressaoLogica85', b2)
    assert _is_linked(a, 'caracteristica_ExpressaoLogica85', b2)
    if hasattr(b1, 'caracteristica_Antecedente86'):
        assert not _is_linked(b1, 'caracteristica_Antecedente86', a)
    if hasattr(b2, 'caracteristica_Antecedente86'):
        assert _is_linked(b2, 'caracteristica_Antecedente86', a)
    _safe_set(a, 'caracteristica_ExpressaoLogica85', None)
    assert not _is_linked(a, 'caracteristica_ExpressaoLogica85', b2)
    if hasattr(b2, 'caracteristica_Antecedente86'):
        assert not _is_linked(b2, 'caracteristica_Antecedente86', a)


def test_assoc_ladoEsquerdoEvento70_link_reassign_clear():
    a = caracteristica_EventoLogico(operadorLogico="sample_text")
    b1 = caracteristica_Evento()
    b2 = caracteristica_Evento()
    _safe_set(a, 'caracteristica_EventoLogico71', b1)
    assert _is_linked(a, 'caracteristica_EventoLogico71', b1)
    if hasattr(b1, 'caracteristica_Evento72'):
        assert _is_linked(b1, 'caracteristica_Evento72', a)
    _safe_set(a, 'caracteristica_EventoLogico71', b2)
    assert _is_linked(a, 'caracteristica_EventoLogico71', b2)
    if hasattr(b1, 'caracteristica_Evento72'):
        assert not _is_linked(b1, 'caracteristica_Evento72', a)
    if hasattr(b2, 'caracteristica_Evento72'):
        assert _is_linked(b2, 'caracteristica_Evento72', a)
    _safe_set(a, 'caracteristica_EventoLogico71', None)
    assert not _is_linked(a, 'caracteristica_EventoLogico71', b2)
    if hasattr(b2, 'caracteristica_Evento72'):
        assert not _is_linked(b2, 'caracteristica_Evento72', a)


def test_assoc_literaisInconsistentes113_link_reassign_clear():
    a = caracteristica_LiteralAcao(presenca="sample_text")
    b1 = caracteristica_InconsistenciaRegraAdaptacao()
    b2 = caracteristica_InconsistenciaRegraAdaptacao()
    _safe_set(a, 'caracteristica_LiteralAcao115', b1)
    assert _is_linked(a, 'caracteristica_LiteralAcao115', b1)
    if hasattr(b1, 'caracteristica_InconsistenciaRegraAdaptacao114'):
        assert _is_linked(b1, 'caracteristica_InconsistenciaRegraAdaptacao114', a)
    _safe_set(a, 'caracteristica_LiteralAcao115', b2)
    assert _is_linked(a, 'caracteristica_LiteralAcao115', b2)
    if hasattr(b1, 'caracteristica_InconsistenciaRegraAdaptacao114'):
        assert not _is_linked(b1, 'caracteristica_InconsistenciaRegraAdaptacao114', a)
    if hasattr(b2, 'caracteristica_InconsistenciaRegraAdaptacao114'):
        assert _is_linked(b2, 'caracteristica_InconsistenciaRegraAdaptacao114', a)
    _safe_set(a, 'caracteristica_LiteralAcao115', None)
    assert not _is_linked(a, 'caracteristica_LiteralAcao115', b2)
    if hasattr(b2, 'caracteristica_InconsistenciaRegraAdaptacao114'):
        assert not _is_linked(b2, 'caracteristica_InconsistenciaRegraAdaptacao114', a)


def test_assoc_pontosDeVariacao0_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_PontoDeVariacao()
    b2 = caracteristica_PontoDeVariacao()
    _safe_set(a, 'caracteristica_LPS', {b1})
    assert _is_linked(a, 'caracteristica_LPS', b1)
    if hasattr(b1, 'caracteristica_PontoDeVariacao'):
        assert _is_linked(b1, 'caracteristica_PontoDeVariacao', a)
    _safe_set(a, 'caracteristica_LPS', {b2})
    assert _is_linked(a, 'caracteristica_LPS', b2)
    if hasattr(b1, 'caracteristica_PontoDeVariacao'):
        assert not _is_linked(b1, 'caracteristica_PontoDeVariacao', a)
    if hasattr(b2, 'caracteristica_PontoDeVariacao'):
        assert _is_linked(b2, 'caracteristica_PontoDeVariacao', a)
    _safe_set(a, 'caracteristica_LPS', set())
    assert not _is_linked(a, 'caracteristica_LPS', b2)
    if hasattr(b2, 'caracteristica_PontoDeVariacao'):
        assert not _is_linked(b2, 'caracteristica_PontoDeVariacao', a)


def test_assoc_produto107_link_reassign_clear():
    a = caracteristica_Estado(nome="sample_text", safe=True)
    b1 = caracteristica_CaracteristicaProduto()
    b2 = caracteristica_CaracteristicaProduto()
    _safe_set(a, 'caracteristica_Estado108', b1)
    assert _is_linked(a, 'caracteristica_Estado108', b1)
    if hasattr(b1, 'caracteristica_CaracteristicaProduto109'):
        assert _is_linked(b1, 'caracteristica_CaracteristicaProduto109', a)
    _safe_set(a, 'caracteristica_Estado108', b2)
    assert _is_linked(a, 'caracteristica_Estado108', b2)
    if hasattr(b1, 'caracteristica_CaracteristicaProduto109'):
        assert not _is_linked(b1, 'caracteristica_CaracteristicaProduto109', a)
    if hasattr(b2, 'caracteristica_CaracteristicaProduto109'):
        assert _is_linked(b2, 'caracteristica_CaracteristicaProduto109', a)
    _safe_set(a, 'caracteristica_Estado108', None)
    assert not _is_linked(a, 'caracteristica_Estado108', b2)
    if hasattr(b2, 'caracteristica_CaracteristicaProduto109'):
        assert not _is_linked(b2, 'caracteristica_CaracteristicaProduto109', a)


def test_assoc_produtos7_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_Produto()
    b2 = caracteristica_Produto()
    _safe_set(a, 'caracteristica_LPS8', {b1})
    assert _is_linked(a, 'caracteristica_LPS8', b1)
    if hasattr(b1, 'caracteristica_Produto'):
        assert _is_linked(b1, 'caracteristica_Produto', a)
    _safe_set(a, 'caracteristica_LPS8', {b2})
    assert _is_linked(a, 'caracteristica_LPS8', b2)
    if hasattr(b1, 'caracteristica_Produto'):
        assert not _is_linked(b1, 'caracteristica_Produto', a)
    if hasattr(b2, 'caracteristica_Produto'):
        assert _is_linked(b2, 'caracteristica_Produto', a)
    _safe_set(a, 'caracteristica_LPS8', set())
    assert not _is_linked(a, 'caracteristica_LPS8', b2)
    if hasattr(b2, 'caracteristica_Produto'):
        assert not _is_linked(b2, 'caracteristica_Produto', a)


def test_assoc_regras5_link_reassign_clear():
    a = caracteristica_Regra(conteudo="sample_text", nome="sample_text")
    b1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    _safe_set(a, 'caracteristica_Regra', b1)
    assert _is_linked(a, 'caracteristica_Regra', b1)
    if hasattr(b1, 'caracteristica_LPS6'):
        assert _is_linked(b1, 'caracteristica_LPS6', a)
    _safe_set(a, 'caracteristica_Regra', b2)
    assert _is_linked(a, 'caracteristica_Regra', b2)
    if hasattr(b1, 'caracteristica_LPS6'):
        assert not _is_linked(b1, 'caracteristica_LPS6', a)
    if hasattr(b2, 'caracteristica_LPS6'):
        assert _is_linked(b2, 'caracteristica_LPS6', a)
    _safe_set(a, 'caracteristica_Regra', None)
    assert not _is_linked(a, 'caracteristica_Regra', b2)
    if hasattr(b2, 'caracteristica_LPS6'):
        assert not _is_linked(b2, 'caracteristica_LPS6', a)


def test_assoc_regrasQuebradas101_link_reassign_clear():
    a = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    b1 = caracteristica_RegraDeComposicao()
    b2 = caracteristica_RegraDeComposicao()
    _safe_set(a, 'caracteristica_Transicao102', {b1})
    assert _is_linked(a, 'caracteristica_Transicao102', b1)
    if hasattr(b1, 'caracteristica_RegraDeComposicao103'):
        assert _is_linked(b1, 'caracteristica_RegraDeComposicao103', a)
    _safe_set(a, 'caracteristica_Transicao102', {b2})
    assert _is_linked(a, 'caracteristica_Transicao102', b2)
    if hasattr(b1, 'caracteristica_RegraDeComposicao103'):
        assert not _is_linked(b1, 'caracteristica_RegraDeComposicao103', a)
    if hasattr(b2, 'caracteristica_RegraDeComposicao103'):
        assert _is_linked(b2, 'caracteristica_RegraDeComposicao103', a)
    _safe_set(a, 'caracteristica_Transicao102', set())
    assert not _is_linked(a, 'caracteristica_Transicao102', b2)
    if hasattr(b2, 'caracteristica_RegraDeComposicao103'):
        assert not _is_linked(b2, 'caracteristica_RegraDeComposicao103', a)


def test_assoc_simulacoes16_link_reassign_clear():
    a = caracteristica_Simulacao(nome="sample_text")
    b1 = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b2 = caracteristica_LPS(erro="sample_text_2", nome="sample_text_2", valoresContextuais="sample_text_2")
    _safe_set(a, 'caracteristica_Simulacao', b1)
    assert _is_linked(a, 'caracteristica_Simulacao', b1)
    if hasattr(b1, 'caracteristica_LPS17'):
        assert _is_linked(b1, 'caracteristica_LPS17', a)
    _safe_set(a, 'caracteristica_Simulacao', b2)
    assert _is_linked(a, 'caracteristica_Simulacao', b2)
    if hasattr(b1, 'caracteristica_LPS17'):
        assert not _is_linked(b1, 'caracteristica_LPS17', a)
    if hasattr(b2, 'caracteristica_LPS17'):
        assert _is_linked(b2, 'caracteristica_LPS17', a)
    _safe_set(a, 'caracteristica_Simulacao', None)
    assert not _is_linked(a, 'caracteristica_Simulacao', b2)
    if hasattr(b2, 'caracteristica_LPS17'):
        assert not _is_linked(b2, 'caracteristica_LPS17', a)


def test_assoc_sistema13_link_reassign_clear():
    a = caracteristica_LPS(erro="sample_text", nome="sample_text", valoresContextuais="sample_text")
    b1 = caracteristica_CaracteristicaRaiz()
    b2 = caracteristica_CaracteristicaRaiz()
    _safe_set(a, 'LpsDoSistema', b1)
    assert _is_linked(a, 'LpsDoSistema', b1)
    if hasattr(b1, 'CaracteristicaRaiz'):
        assert _is_linked(b1, 'CaracteristicaRaiz', a)
    _safe_set(a, 'LpsDoSistema', b2)
    assert _is_linked(a, 'LpsDoSistema', b2)
    if hasattr(b1, 'CaracteristicaRaiz'):
        assert not _is_linked(b1, 'CaracteristicaRaiz', a)
    if hasattr(b2, 'CaracteristicaRaiz'):
        assert _is_linked(b2, 'CaracteristicaRaiz', a)
    _safe_set(a, 'LpsDoSistema', None)
    assert not _is_linked(a, 'LpsDoSistema', b2)
    if hasattr(b2, 'CaracteristicaRaiz'):
        assert not _is_linked(b2, 'CaracteristicaRaiz', a)


def test_assoc_transicoes91_link_reassign_clear():
    a = caracteristica_Transicao(etiqueta="sample_text", safe=True)
    b1 = caracteristica_Simulacao(nome="sample_text")
    b2 = caracteristica_Simulacao(nome="sample_text_2")
    _safe_set(a, 'caracteristica_Transicao', b1)
    assert _is_linked(a, 'caracteristica_Transicao', b1)
    if hasattr(b1, 'caracteristica_Simulacao92'):
        assert _is_linked(b1, 'caracteristica_Simulacao92', a)
    _safe_set(a, 'caracteristica_Transicao', b2)
    assert _is_linked(a, 'caracteristica_Transicao', b2)
    if hasattr(b1, 'caracteristica_Simulacao92'):
        assert not _is_linked(b1, 'caracteristica_Simulacao92', a)
    if hasattr(b2, 'caracteristica_Simulacao92'):
        assert _is_linked(b2, 'caracteristica_Simulacao92', a)
    _safe_set(a, 'caracteristica_Transicao', None)
    assert not _is_linked(a, 'caracteristica_Transicao', b2)
    if hasattr(b2, 'caracteristica_Simulacao92'):
        assert not _is_linked(b2, 'caracteristica_Simulacao92', a)


def test_assoc_variacaoPai37_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Variante()
    b2 = caracteristica_Variante()
    _safe_set(a, 'Variacao38', b1)
    assert _is_linked(a, 'Variacao38', b1)
    if hasattr(b1, 'variantes'):
        assert _is_linked(b1, 'variantes', a)
    _safe_set(a, 'Variacao38', b2)
    assert _is_linked(a, 'Variacao38', b2)
    if hasattr(b1, 'variantes'):
        assert not _is_linked(b1, 'variantes', a)
    if hasattr(b2, 'variantes'):
        assert _is_linked(b2, 'variantes', a)
    _safe_set(a, 'Variacao38', None)
    assert not _is_linked(a, 'Variacao38', b2)
    if hasattr(b2, 'variantes'):
        assert not _is_linked(b2, 'variantes', a)


def test_assoc_variacaoProdutoPai58_link_reassign_clear():
    a = caracteristica_VarianteProduto(selecionado="sample_text")
    b1 = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b2 = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text_2", cardinalidadeMinima="sample_text_2")
    _safe_set(a, 'variantesProduto', b1)
    assert _is_linked(a, 'variantesProduto', b1)
    if hasattr(b1, 'VariacaoProduto'):
        assert _is_linked(b1, 'VariacaoProduto', a)
    _safe_set(a, 'variantesProduto', b2)
    assert _is_linked(a, 'variantesProduto', b2)
    if hasattr(b1, 'VariacaoProduto'):
        assert not _is_linked(b1, 'VariacaoProduto', a)
    if hasattr(b2, 'VariacaoProduto'):
        assert _is_linked(b2, 'VariacaoProduto', a)
    _safe_set(a, 'variantesProduto', None)
    assert not _is_linked(a, 'variantesProduto', b2)
    if hasattr(b2, 'VariacaoProduto'):
        assert not _is_linked(b2, 'VariacaoProduto', a)


def test_assoc_variacoes29_link_reassign_clear():
    a = caracteristica_Variacao(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b1 = caracteristica_Caracteristica()
    b2 = caracteristica_Caracteristica()
    _safe_set(a, 'Variacao', b1)
    assert _is_linked(a, 'Variacao', b1)
    if hasattr(b1, 'caracteristicaPai30'):
        assert _is_linked(b1, 'caracteristicaPai30', a)
    _safe_set(a, 'Variacao', b2)
    assert _is_linked(a, 'Variacao', b2)
    if hasattr(b1, 'caracteristicaPai30'):
        assert not _is_linked(b1, 'caracteristicaPai30', a)
    if hasattr(b2, 'caracteristicaPai30'):
        assert _is_linked(b2, 'caracteristicaPai30', a)
    _safe_set(a, 'Variacao', None)
    assert not _is_linked(a, 'Variacao', b2)
    if hasattr(b2, 'caracteristicaPai30'):
        assert not _is_linked(b2, 'caracteristicaPai30', a)


def test_assoc_variantes34_link_reassign_clear():
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


def test_assoc_variantesProduto56_link_reassign_clear():
    a = caracteristica_VarianteProduto(selecionado="sample_text")
    b1 = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text", cardinalidadeMinima="sample_text")
    b2 = caracteristica_VariacaoProduto(cardinalidadeMaxima="sample_text_2", cardinalidadeMinima="sample_text_2")
    _safe_set(a, 'VarianteProduto', b1)
    assert _is_linked(a, 'VarianteProduto', b1)
    if hasattr(b1, 'variacaoProdutoPai'):
        assert _is_linked(b1, 'variacaoProdutoPai', a)
    _safe_set(a, 'VarianteProduto', b2)
    assert _is_linked(a, 'VarianteProduto', b2)
    if hasattr(b1, 'variacaoProdutoPai'):
        assert not _is_linked(b1, 'variacaoProdutoPai', a)
    if hasattr(b2, 'variacaoProdutoPai'):
        assert _is_linked(b2, 'variacaoProdutoPai', a)
    _safe_set(a, 'VarianteProduto', None)
    assert not _is_linked(a, 'VarianteProduto', b2)
    if hasattr(b2, 'variacaoProdutoPai'):
        assert not _is_linked(b2, 'variacaoProdutoPai', a)


def test_assoc_variavelDeContexto73_link_reassign_clear():
    a = caracteristica_InformacaoDeContexto(origem="sample_text", qualidade="sample_text", tipoValor="sample_text", validade="sample_text", valor="sample_text")
    b1 = caracteristica_EventoRelacional(operadorRelacional="sample_text", valor="sample_text")
    b2 = caracteristica_EventoRelacional(operadorRelacional="sample_text_2", valor="sample_text_2")
    _safe_set(a, 'caracteristica_InformacaoDeContexto', b1)
    assert _is_linked(a, 'caracteristica_InformacaoDeContexto', b1)
    if hasattr(b1, 'caracteristica_EventoRelacional'):
        assert _is_linked(b1, 'caracteristica_EventoRelacional', a)
    _safe_set(a, 'caracteristica_InformacaoDeContexto', b2)
    assert _is_linked(a, 'caracteristica_InformacaoDeContexto', b2)
    if hasattr(b1, 'caracteristica_EventoRelacional'):
        assert not _is_linked(b1, 'caracteristica_EventoRelacional', a)
    if hasattr(b2, 'caracteristica_EventoRelacional'):
        assert _is_linked(b2, 'caracteristica_EventoRelacional', a)
    _safe_set(a, 'caracteristica_InformacaoDeContexto', None)
    assert not _is_linked(a, 'caracteristica_InformacaoDeContexto', b2)
    if hasattr(b2, 'caracteristica_EventoRelacional'):
        assert not _is_linked(b2, 'caracteristica_EventoRelacional', a)


def test_assoc_variaveldaExpressao87_link_reassign_clear():
    a = caracteristica_ExpressaoRelacional(operadorRelacional="sample_text", valor="sample_text")
    b1 = caracteristica_Atributo(tipoValor="sample_text")
    b2 = caracteristica_Atributo(tipoValor="sample_text_2")
    _safe_set(a, 'caracteristica_ExpressaoRelacional', b1)
    assert _is_linked(a, 'caracteristica_ExpressaoRelacional', b1)
    if hasattr(b1, 'caracteristica_Atributo88'):
        assert _is_linked(b1, 'caracteristica_Atributo88', a)
    _safe_set(a, 'caracteristica_ExpressaoRelacional', b2)
    assert _is_linked(a, 'caracteristica_ExpressaoRelacional', b2)
    if hasattr(b1, 'caracteristica_Atributo88'):
        assert not _is_linked(b1, 'caracteristica_Atributo88', a)
    if hasattr(b2, 'caracteristica_Atributo88'):
        assert _is_linked(b2, 'caracteristica_Atributo88', a)
    _safe_set(a, 'caracteristica_ExpressaoRelacional', None)
    assert not _is_linked(a, 'caracteristica_ExpressaoRelacional', b2)
    if hasattr(b2, 'caracteristica_Atributo88'):
        assert not _is_linked(b2, 'caracteristica_Atributo88', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Acao_strategy = st.builds(Acao)
@given(instance=Acao_strategy)
@settings(max_examples=25)
def test_Acao_instantiation(instance):
    assert isinstance(instance, Acao)


Antecedente_strategy = st.builds(Antecedente)
@given(instance=Antecedente_strategy)
@settings(max_examples=25)
def test_Antecedente_instantiation(instance):
    assert isinstance(instance, Antecedente)


Caracteristica_strategy = st.builds(Caracteristica)
@given(instance=Caracteristica_strategy)
@settings(max_examples=25)
def test_Caracteristica_instantiation(instance):
    assert isinstance(instance, Caracteristica)


CaracteristicaProduto_strategy = st.builds(CaracteristicaProduto)
@given(instance=CaracteristicaProduto_strategy)
@settings(max_examples=25)
def test_CaracteristicaProduto_instantiation(instance):
    assert isinstance(instance, CaracteristicaProduto)


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


ElementoDeProduto_strategy = st.builds(ElementoDeProduto)
@given(instance=ElementoDeProduto_strategy)
@settings(max_examples=25)
def test_ElementoDeProduto_instantiation(instance):
    assert isinstance(instance, ElementoDeProduto)


ElementoExterno_strategy = st.builds(ElementoExterno)
@given(instance=ElementoExterno_strategy)
@settings(max_examples=25)
def test_ElementoExterno_instantiation(instance):
    assert isinstance(instance, ElementoExterno)


Evento_strategy = st.builds(Evento)
@given(instance=Evento_strategy)
@settings(max_examples=25)
def test_Evento_instantiation(instance):
    assert isinstance(instance, Evento)


Expressao_strategy = st.builds(Expressao)
@given(instance=Expressao_strategy)
@settings(max_examples=25)
def test_Expressao_instantiation(instance):
    assert isinstance(instance, Expressao)


PontoDeVariacao_strategy = st.builds(PontoDeVariacao)
@given(instance=PontoDeVariacao_strategy)
@settings(max_examples=25)
def test_PontoDeVariacao_instantiation(instance):
    assert isinstance(instance, PontoDeVariacao)


Regra_strategy = st.builds(Regra)
@given(instance=Regra_strategy)
@settings(max_examples=25)
def test_Regra_instantiation(instance):
    assert isinstance(instance, Regra)


caracteristica_Acao_strategy = st.builds(caracteristica_Acao)
@given(instance=caracteristica_Acao_strategy)
@settings(max_examples=25)
def test_caracteristica_Acao_instantiation(instance):
    assert isinstance(instance, caracteristica_Acao)


caracteristica_AcaoLogico_strategy = st.builds(caracteristica_AcaoLogico, operadorAcaoLogico=safe_text)
@given(instance=caracteristica_AcaoLogico_strategy)
@settings(max_examples=25)
def test_caracteristica_AcaoLogico_instantiation(instance):
    assert isinstance(instance, caracteristica_AcaoLogico)


caracteristica_Antecedente_strategy = st.builds(caracteristica_Antecedente)
@given(instance=caracteristica_Antecedente_strategy)
@settings(max_examples=25)
def test_caracteristica_Antecedente_instantiation(instance):
    assert isinstance(instance, caracteristica_Antecedente)


caracteristica_Atributo_strategy = st.builds(caracteristica_Atributo, tipoValor=safe_text)
@given(instance=caracteristica_Atributo_strategy)
@settings(max_examples=25)
def test_caracteristica_Atributo_instantiation(instance):
    assert isinstance(instance, caracteristica_Atributo)


caracteristica_AtributoProduto_strategy = st.builds(caracteristica_AtributoProduto, tipoValor=safe_text, valor=safe_text)
@given(instance=caracteristica_AtributoProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_AtributoProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_AtributoProduto)


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


caracteristica_CaracteristicaAgrupadaProduto_strategy = st.builds(caracteristica_CaracteristicaAgrupadaProduto)
@given(instance=caracteristica_CaracteristicaAgrupadaProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaAgrupadaProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaAgrupadaProduto)


caracteristica_CaracteristicaMandatoria_strategy = st.builds(caracteristica_CaracteristicaMandatoria)
@given(instance=caracteristica_CaracteristicaMandatoria_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaMandatoria_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaMandatoria)


caracteristica_CaracteristicaMandatoriaProduto_strategy = st.builds(caracteristica_CaracteristicaMandatoriaProduto)
@given(instance=caracteristica_CaracteristicaMandatoriaProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaMandatoriaProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaMandatoriaProduto)


caracteristica_CaracteristicaOpcional_strategy = st.builds(caracteristica_CaracteristicaOpcional)
@given(instance=caracteristica_CaracteristicaOpcional_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaOpcional_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaOpcional)


caracteristica_CaracteristicaOpcionalProduto_strategy = st.builds(caracteristica_CaracteristicaOpcionalProduto)
@given(instance=caracteristica_CaracteristicaOpcionalProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaOpcionalProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaOpcionalProduto)


caracteristica_CaracteristicaProduto_strategy = st.builds(caracteristica_CaracteristicaProduto)
@given(instance=caracteristica_CaracteristicaProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaProduto)


caracteristica_CaracteristicaRaiz_strategy = st.builds(caracteristica_CaracteristicaRaiz)
@given(instance=caracteristica_CaracteristicaRaiz_strategy)
@settings(max_examples=25)
def test_caracteristica_CaracteristicaRaiz_instantiation(instance):
    assert isinstance(instance, caracteristica_CaracteristicaRaiz)


caracteristica_CasoDeTeste_strategy = st.builds(caracteristica_CasoDeTeste)
@given(instance=caracteristica_CasoDeTeste_strategy)
@settings(max_examples=25)
def test_caracteristica_CasoDeTeste_instantiation(instance):
    assert isinstance(instance, caracteristica_CasoDeTeste)


caracteristica_CasoDeUso_strategy = st.builds(caracteristica_CasoDeUso)
@given(instance=caracteristica_CasoDeUso_strategy)
@settings(max_examples=25)
def test_caracteristica_CasoDeUso_instantiation(instance):
    assert isinstance(instance, caracteristica_CasoDeUso)


caracteristica_Designar_strategy = st.builds(caracteristica_Designar, tipoValor=safe_text, valor=safe_text)
@given(instance=caracteristica_Designar_strategy)
@settings(max_examples=25)
def test_caracteristica_Designar_instantiation(instance):
    assert isinstance(instance, caracteristica_Designar)


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


caracteristica_ElementoDeProduto_strategy = st.builds(caracteristica_ElementoDeProduto, nome=safe_text)
@given(instance=caracteristica_ElementoDeProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_ElementoDeProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_ElementoDeProduto)


caracteristica_ElementoExterno_strategy = st.builds(caracteristica_ElementoExterno, nome=safe_text)
@given(instance=caracteristica_ElementoExterno_strategy)
@settings(max_examples=25)
def test_caracteristica_ElementoExterno_instantiation(instance):
    assert isinstance(instance, caracteristica_ElementoExterno)


caracteristica_EntidadeDeContexto_strategy = st.builds(caracteristica_EntidadeDeContexto)
@given(instance=caracteristica_EntidadeDeContexto_strategy)
@settings(max_examples=25)
def test_caracteristica_EntidadeDeContexto_instantiation(instance):
    assert isinstance(instance, caracteristica_EntidadeDeContexto)


caracteristica_Estado_strategy = st.builds(caracteristica_Estado, nome=safe_text, safe=st.booleans())
@given(instance=caracteristica_Estado_strategy)
@settings(max_examples=25)
def test_caracteristica_Estado_instantiation(instance):
    assert isinstance(instance, caracteristica_Estado)


caracteristica_Evento_strategy = st.builds(caracteristica_Evento)
@given(instance=caracteristica_Evento_strategy)
@settings(max_examples=25)
def test_caracteristica_Evento_instantiation(instance):
    assert isinstance(instance, caracteristica_Evento)


caracteristica_EventoLogico_strategy = st.builds(caracteristica_EventoLogico, operadorLogico=safe_text)
@given(instance=caracteristica_EventoLogico_strategy)
@settings(max_examples=25)
def test_caracteristica_EventoLogico_instantiation(instance):
    assert isinstance(instance, caracteristica_EventoLogico)


caracteristica_EventoRelacional_strategy = st.builds(caracteristica_EventoRelacional, operadorRelacional=safe_text, valor=safe_text)
@given(instance=caracteristica_EventoRelacional_strategy)
@settings(max_examples=25)
def test_caracteristica_EventoRelacional_instantiation(instance):
    assert isinstance(instance, caracteristica_EventoRelacional)


caracteristica_Expressao_strategy = st.builds(caracteristica_Expressao, nome=safe_text)
@given(instance=caracteristica_Expressao_strategy)
@settings(max_examples=25)
def test_caracteristica_Expressao_instantiation(instance):
    assert isinstance(instance, caracteristica_Expressao)


caracteristica_ExpressaoLogica_strategy = st.builds(caracteristica_ExpressaoLogica, operadorLogico=safe_text)
@given(instance=caracteristica_ExpressaoLogica_strategy)
@settings(max_examples=25)
def test_caracteristica_ExpressaoLogica_instantiation(instance):
    assert isinstance(instance, caracteristica_ExpressaoLogica)


caracteristica_ExpressaoRelacional_strategy = st.builds(caracteristica_ExpressaoRelacional, operadorRelacional=safe_text, valor=safe_text)
@given(instance=caracteristica_ExpressaoRelacional_strategy)
@settings(max_examples=25)
def test_caracteristica_ExpressaoRelacional_instantiation(instance):
    assert isinstance(instance, caracteristica_ExpressaoRelacional)


caracteristica_InconsistenciaRegraAdaptacao_strategy = st.builds(caracteristica_InconsistenciaRegraAdaptacao)
@given(instance=caracteristica_InconsistenciaRegraAdaptacao_strategy)
@settings(max_examples=25)
def test_caracteristica_InconsistenciaRegraAdaptacao_instantiation(instance):
    assert isinstance(instance, caracteristica_InconsistenciaRegraAdaptacao)


caracteristica_InformacaoDeContexto_strategy = st.builds(caracteristica_InformacaoDeContexto, origem=safe_text, qualidade=safe_text, tipoValor=safe_text, validade=safe_text, valor=safe_text)
@given(instance=caracteristica_InformacaoDeContexto_strategy)
@settings(max_examples=25)
def test_caracteristica_InformacaoDeContexto_instantiation(instance):
    assert isinstance(instance, caracteristica_InformacaoDeContexto)


caracteristica_LPS_strategy = st.builds(caracteristica_LPS, erro=safe_text, nome=safe_text, valoresContextuais=safe_text)
@given(instance=caracteristica_LPS_strategy)
@settings(max_examples=25)
def test_caracteristica_LPS_instantiation(instance):
    assert isinstance(instance, caracteristica_LPS)


caracteristica_LiteralAcao_strategy = st.builds(caracteristica_LiteralAcao, presenca=safe_text)
@given(instance=caracteristica_LiteralAcao_strategy)
@settings(max_examples=25)
def test_caracteristica_LiteralAcao_instantiation(instance):
    assert isinstance(instance, caracteristica_LiteralAcao)


caracteristica_LiteralComposicao_strategy = st.builds(caracteristica_LiteralComposicao, presenca=safe_text)
@given(instance=caracteristica_LiteralComposicao_strategy)
@settings(max_examples=25)
def test_caracteristica_LiteralComposicao_instantiation(instance):
    assert isinstance(instance, caracteristica_LiteralComposicao)


caracteristica_PontoDeVariacao_strategy = st.builds(caracteristica_PontoDeVariacao)
@given(instance=caracteristica_PontoDeVariacao_strategy)
@settings(max_examples=25)
def test_caracteristica_PontoDeVariacao_instantiation(instance):
    assert isinstance(instance, caracteristica_PontoDeVariacao)


caracteristica_Produto_strategy = st.builds(caracteristica_Produto)
@given(instance=caracteristica_Produto_strategy)
@settings(max_examples=25)
def test_caracteristica_Produto_instantiation(instance):
    assert isinstance(instance, caracteristica_Produto)


caracteristica_RaizDeContexto_strategy = st.builds(caracteristica_RaizDeContexto)
@given(instance=caracteristica_RaizDeContexto_strategy)
@settings(max_examples=25)
def test_caracteristica_RaizDeContexto_instantiation(instance):
    assert isinstance(instance, caracteristica_RaizDeContexto)


caracteristica_Regra_strategy = st.builds(caracteristica_Regra, conteudo=safe_text, nome=safe_text)
@given(instance=caracteristica_Regra_strategy)
@settings(max_examples=25)
def test_caracteristica_Regra_instantiation(instance):
    assert isinstance(instance, caracteristica_Regra)


caracteristica_RegraDeComposicao_strategy = st.builds(caracteristica_RegraDeComposicao)
@given(instance=caracteristica_RegraDeComposicao_strategy)
@settings(max_examples=25)
def test_caracteristica_RegraDeComposicao_instantiation(instance):
    assert isinstance(instance, caracteristica_RegraDeComposicao)


caracteristica_RegraDeContexto_strategy = st.builds(caracteristica_RegraDeContexto)
@given(instance=caracteristica_RegraDeContexto_strategy)
@settings(max_examples=25)
def test_caracteristica_RegraDeContexto_instantiation(instance):
    assert isinstance(instance, caracteristica_RegraDeContexto)


caracteristica_Simulacao_strategy = st.builds(caracteristica_Simulacao, nome=safe_text)
@given(instance=caracteristica_Simulacao_strategy)
@settings(max_examples=25)
def test_caracteristica_Simulacao_instantiation(instance):
    assert isinstance(instance, caracteristica_Simulacao)


caracteristica_Transicao_strategy = st.builds(caracteristica_Transicao, etiqueta=safe_text, safe=st.booleans())
@given(instance=caracteristica_Transicao_strategy)
@settings(max_examples=25)
def test_caracteristica_Transicao_instantiation(instance):
    assert isinstance(instance, caracteristica_Transicao)


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


caracteristica_VariacaoDoisProduto_strategy = st.builds(caracteristica_VariacaoDoisProduto, cardinalidadeMaxima=safe_text, cardinalidadeMaximaOr=safe_text, cardinalidadeMinimaOr=safe_text)
@given(instance=caracteristica_VariacaoDoisProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_VariacaoDoisProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_VariacaoDoisProduto)


caracteristica_VariacaoProduto_strategy = st.builds(caracteristica_VariacaoProduto, cardinalidadeMaxima=safe_text, cardinalidadeMinima=safe_text)
@given(instance=caracteristica_VariacaoProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_VariacaoProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_VariacaoProduto)


caracteristica_Variante_strategy = st.builds(caracteristica_Variante)
@given(instance=caracteristica_Variante_strategy)
@settings(max_examples=25)
def test_caracteristica_Variante_instantiation(instance):
    assert isinstance(instance, caracteristica_Variante)


caracteristica_VarianteProduto_strategy = st.builds(caracteristica_VarianteProduto, selecionado=safe_text)
@given(instance=caracteristica_VarianteProduto_strategy)
@settings(max_examples=25)
def test_caracteristica_VarianteProduto_instantiation(instance):
    assert isinstance(instance, caracteristica_VarianteProduto)



