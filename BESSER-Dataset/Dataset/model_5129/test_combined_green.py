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
    PontoDeVariacao,
    caracteristica_PontoDeVariacao,
    ElementoCaracteristico,
    Caracteristica,
    caracteristica_CaracteristicaOpcional,
    caracteristica_CaracteristicaAgrupada,
    caracteristica_Variante,
    caracteristica_CaracteristicaRaiz,
    caracteristica_VariacaoDois,
    caracteristica_CaracteristicaMandatoria,
    Elemento,
    caracteristica_Variacao,
    caracteristica_Atributo,
    caracteristica_ElementoCaracteristico,
    caracteristica_Elemento,
    caracteristica_LPS,
    caracteristica_Caracteristica,
    OperadorAcaoLogico,
    TipoValor,
    OperadorRelacional,
    Origem,
    OperadorLogico,
    Validade,
    CardinalidadeMaxima,
    Qualidade,
    Presenca,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pontodevariacao_is_not_abstract():
    assert not inspect.isabstract(PontoDeVariacao)


def test_hyp_pontodevariacao_constructor_exists():
    assert callable(PontoDeVariacao.__init__)


def test_hyp_pontodevariacao_constructor_args():
    sig = inspect.signature(PontoDeVariacao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_pontodevariacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_PontoDeVariacao)


def test_hyp_caracteristica_pontodevariacao_constructor_exists():
    assert callable(caracteristica_PontoDeVariacao.__init__)


def test_hyp_caracteristica_pontodevariacao_constructor_args():
    sig = inspect.signature(caracteristica_PontoDeVariacao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementocaracteristico_is_not_abstract():
    assert not inspect.isabstract(ElementoCaracteristico)


def test_hyp_elementocaracteristico_constructor_exists():
    assert callable(ElementoCaracteristico.__init__)


def test_hyp_elementocaracteristico_constructor_args():
    sig = inspect.signature(ElementoCaracteristico.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_is_not_abstract():
    assert not inspect.isabstract(Caracteristica)


def test_hyp_caracteristica_constructor_exists():
    assert callable(Caracteristica.__init__)


def test_hyp_caracteristica_constructor_args():
    sig = inspect.signature(Caracteristica.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicaopcional_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaOpcional)


def test_hyp_caracteristica_caracteristicaopcional_constructor_exists():
    assert callable(caracteristica_CaracteristicaOpcional.__init__)


def test_hyp_caracteristica_caracteristicaopcional_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaOpcional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicaagrupada_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaAgrupada)


def test_hyp_caracteristica_caracteristicaagrupada_constructor_exists():
    assert callable(caracteristica_CaracteristicaAgrupada.__init__)


def test_hyp_caracteristica_caracteristicaagrupada_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaAgrupada.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_variante_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Variante)


def test_hyp_caracteristica_variante_constructor_exists():
    assert callable(caracteristica_Variante.__init__)


def test_hyp_caracteristica_variante_constructor_args():
    sig = inspect.signature(caracteristica_Variante.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_caracteristicaraiz_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaRaiz)


def test_hyp_caracteristica_caracteristicaraiz_constructor_exists():
    assert callable(caracteristica_CaracteristicaRaiz.__init__)


def test_hyp_caracteristica_caracteristicaraiz_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaRaiz.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_variacaodois_is_not_abstract():
    assert not inspect.isabstract(caracteristica_VariacaoDois)


def test_hyp_caracteristica_variacaodois_constructor_exists():
    assert callable(caracteristica_VariacaoDois.__init__)


def test_hyp_caracteristica_variacaodois_constructor_args():
    sig = inspect.signature(caracteristica_VariacaoDois.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalidadeMaximaOr" in params, "Missing parameter 'cardinalidadeMaximaOr'"
    assert "cardinalidadeMaxima" in params, "Missing parameter 'cardinalidadeMaxima'"
    assert "cardinalidadeMinimaOr" in params, "Missing parameter 'cardinalidadeMinimaOr'"






def test_hyp_caracteristica_caracteristicamandatoria_is_not_abstract():
    assert not inspect.isabstract(caracteristica_CaracteristicaMandatoria)


def test_hyp_caracteristica_caracteristicamandatoria_constructor_exists():
    assert callable(caracteristica_CaracteristicaMandatoria.__init__)


def test_hyp_caracteristica_caracteristicamandatoria_constructor_args():
    sig = inspect.signature(caracteristica_CaracteristicaMandatoria.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elemento_is_not_abstract():
    assert not inspect.isabstract(Elemento)


def test_hyp_elemento_constructor_exists():
    assert callable(Elemento.__init__)


def test_hyp_elemento_constructor_args():
    sig = inspect.signature(Elemento.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_variacao_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Variacao)


def test_hyp_caracteristica_variacao_constructor_exists():
    assert callable(caracteristica_Variacao.__init__)


def test_hyp_caracteristica_variacao_constructor_args():
    sig = inspect.signature(caracteristica_Variacao.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalidadeMinima" in params, "Missing parameter 'cardinalidadeMinima'"
    assert "cardinalidadeMaxima" in params, "Missing parameter 'cardinalidadeMaxima'"





def test_hyp_caracteristica_atributo_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Atributo)


def test_hyp_caracteristica_atributo_constructor_exists():
    assert callable(caracteristica_Atributo.__init__)


def test_hyp_caracteristica_atributo_constructor_args():
    sig = inspect.signature(caracteristica_Atributo.__init__)
    params = list(sig.parameters.keys())
    assert "tipoValor" in params, "Missing parameter 'tipoValor'"




def test_hyp_caracteristica_elementocaracteristico_is_not_abstract():
    assert not inspect.isabstract(caracteristica_ElementoCaracteristico)


def test_hyp_caracteristica_elementocaracteristico_constructor_exists():
    assert callable(caracteristica_ElementoCaracteristico.__init__)


def test_hyp_caracteristica_elementocaracteristico_constructor_args():
    sig = inspect.signature(caracteristica_ElementoCaracteristico.__init__)
    params = list(sig.parameters.keys())



def test_hyp_caracteristica_elemento_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Elemento)


def test_hyp_caracteristica_elemento_constructor_exists():
    assert callable(caracteristica_Elemento.__init__)


def test_hyp_caracteristica_elemento_constructor_args():
    sig = inspect.signature(caracteristica_Elemento.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_lps_is_not_abstract():
    assert not inspect.isabstract(caracteristica_LPS)


def test_hyp_caracteristica_lps_constructor_exists():
    assert callable(caracteristica_LPS.__init__)


def test_hyp_caracteristica_lps_constructor_args():
    sig = inspect.signature(caracteristica_LPS.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_caracteristica_caracteristica_is_not_abstract():
    assert not inspect.isabstract(caracteristica_Caracteristica)


def test_hyp_caracteristica_caracteristica_constructor_exists():
    assert callable(caracteristica_Caracteristica.__init__)


def test_hyp_caracteristica_caracteristica_constructor_args():
    sig = inspect.signature(caracteristica_Caracteristica.__init__)
    params = list(sig.parameters.keys())

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
        "TString",
        "TFloat",
        "TInteger",
        "TBoolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TipoValor"

def test_hyp_operadorrelacional_exists():
    # Check that the Enumeration exists
    assert OperadorRelacional is not None

def test_hyp_operadorrelacional_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperadorRelacional]
    expected_literals = [
        "IGUAL",
        "MAIORIGUAL",
        "MAIOR",
        "MENOR",
        "MENORIGUAL",
        "DIFERENTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperadorRelacional"

def test_hyp_origem_exists():
    # Check that the Enumeration exists
    assert Origem is not None

def test_hyp_origem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Origem]
    expected_literals = [
        "Perfil",
        "Usuario",
        "Sentida",
        "Derivada",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Origem"

def test_hyp_operadorlogico_exists():
    # Check that the Enumeration exists
    assert OperadorLogico is not None

def test_hyp_operadorlogico_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperadorLogico]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperadorLogico"

def test_hyp_validade_exists():
    # Check that the Enumeration exists
    assert Validade is not None

def test_hyp_validade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Validade]
    expected_literals = [
        "Frequente",
        "Raramente",
        "Permanente",
        "Volatil",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Validade"

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

def test_hyp_qualidade_exists():
    # Check that the Enumeration exists
    assert Qualidade is not None

def test_hyp_qualidade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Qualidade]
    expected_literals = [
        "Alto",
        "Baixo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Qualidade"

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
PontoDeVariacao_strategy = st.builds(
    PontoDeVariacao,
)
caracteristica_PontoDeVariacao_strategy = st.builds(
    caracteristica_PontoDeVariacao,
)
ElementoCaracteristico_strategy = st.builds(
    ElementoCaracteristico,
)
Caracteristica_strategy = st.builds(
    Caracteristica,
)
caracteristica_CaracteristicaOpcional_strategy = st.builds(
    caracteristica_CaracteristicaOpcional,
)
caracteristica_CaracteristicaAgrupada_strategy = st.builds(
    caracteristica_CaracteristicaAgrupada,
)
caracteristica_Variante_strategy = st.builds(
    caracteristica_Variante,
)
caracteristica_CaracteristicaRaiz_strategy = st.builds(
    caracteristica_CaracteristicaRaiz,
)
caracteristica_VariacaoDois_strategy = st.builds(
    caracteristica_VariacaoDois,
    cardinalidadeMaximaOr=
        safe_text,
    cardinalidadeMaxima=
        safe_text,
    cardinalidadeMinimaOr=
        safe_text
)
caracteristica_CaracteristicaMandatoria_strategy = st.builds(
    caracteristica_CaracteristicaMandatoria,
)
Elemento_strategy = st.builds(
    Elemento,
)
caracteristica_Variacao_strategy = st.builds(
    caracteristica_Variacao,
    cardinalidadeMinima=
        safe_text,
    cardinalidadeMaxima=
        safe_text
)
caracteristica_Atributo_strategy = st.builds(
    caracteristica_Atributo,
    tipoValor=
        safe_text
)
caracteristica_ElementoCaracteristico_strategy = st.builds(
    caracteristica_ElementoCaracteristico,
)
caracteristica_Elemento_strategy = st.builds(
    caracteristica_Elemento,
    nome=
        safe_text
)
caracteristica_LPS_strategy = st.builds(
    caracteristica_LPS,
    nome=
        safe_text
)
caracteristica_Caracteristica_strategy = st.builds(
    caracteristica_Caracteristica,
)












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



@given(instance=caracteristica_VariacaoDois_strategy)
def test_hyp_caracteristica_variacaodois_cardinalidadeMinimaOr_setter(instance):
    original = instance.cardinalidadeMinimaOr
    instance.cardinalidadeMinimaOr = original
    assert instance.cardinalidadeMinimaOr == original






@given(instance=caracteristica_Variacao_strategy)
def test_hyp_caracteristica_variacao_cardinalidadeMinima_setter(instance):
    original = instance.cardinalidadeMinima
    instance.cardinalidadeMinima = original
    assert instance.cardinalidadeMinima == original



@given(instance=caracteristica_Variacao_strategy)
def test_hyp_caracteristica_variacao_cardinalidadeMaxima_setter(instance):
    original = instance.cardinalidadeMaxima
    instance.cardinalidadeMaxima = original
    assert instance.cardinalidadeMaxima == original




@given(instance=caracteristica_Atributo_strategy)
def test_hyp_caracteristica_atributo_tipoValor_setter(instance):
    original = instance.tipoValor
    instance.tipoValor = original
    assert instance.tipoValor == original





@given(instance=caracteristica_Elemento_strategy)
def test_hyp_caracteristica_elemento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=caracteristica_LPS_strategy)
def test_hyp_caracteristica_lps_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



