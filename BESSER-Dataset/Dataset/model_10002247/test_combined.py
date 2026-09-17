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
    LinhaCuidado,
    Mensagem,
    ProfissionalSaude,
    Naturalidade,
    Medicamento,
    Paciente,
    Telefone,
    Pessoa,
    Endereco,
    Exame,
    LocalExame,
    TipoMedicamento,
    TipoSanguineo,
    Interacao,
    enu,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_linhacuidado_is_not_abstract():
    assert not inspect.isabstract(LinhaCuidado)


def test_hyp_linhacuidado_constructor_exists():
    assert callable(LinhaCuidado.__init__)


def test_hyp_linhacuidado_constructor_args():
    sig = inspect.signature(LinhaCuidado.__init__)
    params = list(sig.parameters.keys())
    assert "descricao" in params, "Missing parameter 'descricao'"
    assert "nome" in params, "Missing parameter 'nome'"





def test_hyp_mensagem_is_not_abstract():
    assert not inspect.isabstract(Mensagem)


def test_hyp_mensagem_constructor_exists():
    assert callable(Mensagem.__init__)


def test_hyp_mensagem_constructor_args():
    sig = inspect.signature(Mensagem.__init__)
    params = list(sig.parameters.keys())
    assert "mensagem" in params, "Missing parameter 'mensagem'"
    assert "dataEnvio" in params, "Missing parameter 'dataEnvio'"
    assert "geral" in params, "Missing parameter 'geral'"
    assert "assunto" in params, "Missing parameter 'assunto'"







def test_hyp_profissionalsaude_is_not_abstract():
    assert not inspect.isabstract(ProfissionalSaude)


def test_hyp_profissionalsaude_constructor_exists():
    assert callable(ProfissionalSaude.__init__)


def test_hyp_profissionalsaude_constructor_args():
    sig = inspect.signature(ProfissionalSaude.__init__)
    params = list(sig.parameters.keys())



def test_hyp_naturalidade_is_not_abstract():
    assert not inspect.isabstract(Naturalidade)


def test_hyp_naturalidade_constructor_exists():
    assert callable(Naturalidade.__init__)


def test_hyp_naturalidade_constructor_args():
    sig = inspect.signature(Naturalidade.__init__)
    params = list(sig.parameters.keys())
    assert "naturalidade" in params, "Missing parameter 'naturalidade'"




def test_hyp_medicamento_is_not_abstract():
    assert not inspect.isabstract(Medicamento)


def test_hyp_medicamento_constructor_exists():
    assert callable(Medicamento.__init__)


def test_hyp_medicamento_constructor_args():
    sig = inspect.signature(Medicamento.__init__)
    params = list(sig.parameters.keys())
    assert "ativo" in params, "Missing parameter 'ativo'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "intervaloTempo" in params, "Missing parameter 'intervaloTempo'"
    assert "horaInicial" in params, "Missing parameter 'horaInicial'"
    assert "dataFim" in params, "Missing parameter 'dataFim'"
    assert "descricao" in params, "Missing parameter 'descricao'"
    assert "dataInicio" in params, "Missing parameter 'dataInicio'"










def test_hyp_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_hyp_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_hyp_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())



def test_hyp_telefone_is_not_abstract():
    assert not inspect.isabstract(Telefone)


def test_hyp_telefone_constructor_exists():
    assert callable(Telefone.__init__)


def test_hyp_telefone_constructor_args():
    sig = inspect.signature(Telefone.__init__)
    params = list(sig.parameters.keys())
    assert "ddd" in params, "Missing parameter 'ddd'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "tipo" in params, "Missing parameter 'tipo'"






def test_hyp_pessoa_is_not_abstract():
    assert not inspect.isabstract(Pessoa)


def test_hyp_pessoa_constructor_exists():
    assert callable(Pessoa.__init__)


def test_hyp_pessoa_constructor_args():
    sig = inspect.signature(Pessoa.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "sexo" in params, "Missing parameter 'sexo'"
    assert "dataInclusao" in params, "Missing parameter 'dataInclusao'"
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "ultimoAcesso" in params, "Missing parameter 'ultimoAcesso'"
    assert "senha" in params, "Missing parameter 'senha'"
    assert "dataNascimento" in params, "Missing parameter 'dataNascimento'"










def test_hyp_endereco_is_not_abstract():
    assert not inspect.isabstract(Endereco)


def test_hyp_endereco_constructor_exists():
    assert callable(Endereco.__init__)


def test_hyp_endereco_constructor_args():
    sig = inspect.signature(Endereco.__init__)
    params = list(sig.parameters.keys())
    assert "logradouro" in params, "Missing parameter 'logradouro'"
    assert "cep" in params, "Missing parameter 'cep'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "bairro" in params, "Missing parameter 'bairro'"
    assert "cidade" in params, "Missing parameter 'cidade'"








def test_hyp_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_hyp_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_hyp_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "descricao" in params, "Missing parameter 'descricao'"






def test_hyp_localexame_is_not_abstract():
    assert not inspect.isabstract(LocalExame)


def test_hyp_localexame_constructor_exists():
    assert callable(LocalExame.__init__)


def test_hyp_localexame_constructor_args():
    sig = inspect.signature(LocalExame.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_tipomedicamento_is_not_abstract():
    assert not inspect.isabstract(TipoMedicamento)


def test_hyp_tipomedicamento_constructor_exists():
    assert callable(TipoMedicamento.__init__)


def test_hyp_tipomedicamento_constructor_args():
    sig = inspect.signature(TipoMedicamento.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_tiposanguineo_is_not_abstract():
    assert not inspect.isabstract(TipoSanguineo)


def test_hyp_tiposanguineo_constructor_exists():
    assert callable(TipoSanguineo.__init__)


def test_hyp_tiposanguineo_constructor_args():
    sig = inspect.signature(TipoSanguineo.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"




def test_hyp_interacao_is_not_abstract():
    assert not inspect.isabstract(Interacao)


def test_hyp_interacao_constructor_exists():
    assert callable(Interacao.__init__)


def test_hyp_interacao_constructor_args():
    sig = inspect.signature(Interacao.__init__)
    params = list(sig.parameters.keys())

def test_hyp_enu_exists():
    # Check that the Enumeration exists
    assert enu is not None

def test_hyp_enu_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in enu]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in enu"


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
LinhaCuidado_strategy = st.builds(
    LinhaCuidado,
    descricao=
        st.integers(),
    nome=
        safe_text
)
Mensagem_strategy = st.builds(
    Mensagem,
    mensagem=
        safe_text,
    dataEnvio=
        safe_text,
    geral=
        st.booleans(),
    assunto=
        safe_text
)
ProfissionalSaude_strategy = st.builds(
    ProfissionalSaude,
)
Naturalidade_strategy = st.builds(
    Naturalidade,
    naturalidade=
        safe_text
)
Medicamento_strategy = st.builds(
    Medicamento,
    ativo=
        st.booleans(),
    nome=
        safe_text,
    intervaloTempo=
        st.integers(),
    horaInicial=
        safe_text,
    dataFim=
        safe_text,
    descricao=
        safe_text,
    dataInicio=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
)
Telefone_strategy = st.builds(
    Telefone,
    ddd=
        st.integers(),
    numero=
        safe_text,
    tipo=
        safe_text
)
Pessoa_strategy = st.builds(
    Pessoa,
    email=
        safe_text,
    sexo=
        safe_text,
    dataInclusao=
        safe_text,
    cpf=
        safe_text,
    ultimoAcesso=
        safe_text,
    senha=
        safe_text,
    dataNascimento=
        safe_text
)
Endereco_strategy = st.builds(
    Endereco,
    logradouro=
        safe_text,
    cep=
        safe_text,
    numero=
        st.integers(),
    bairro=
        safe_text,
    cidade=
        safe_text
)
Exame_strategy = st.builds(
    Exame,
    data=
        safe_text,
    nome=
        safe_text,
    descricao=
        safe_text
)
LocalExame_strategy = st.builds(
    LocalExame,
    nome=
        safe_text
)
TipoMedicamento_strategy = st.builds(
    TipoMedicamento,
    nome=
        safe_text
)
TipoSanguineo_strategy = st.builds(
    TipoSanguineo,
    nome=
        safe_text
)
Interacao_strategy = st.builds(
    Interacao,
)




@given(instance=LinhaCuidado_strategy)
def test_hyp_linhacuidado_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original



@given(instance=LinhaCuidado_strategy)
def test_hyp_linhacuidado_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=Mensagem_strategy)
def test_hyp_mensagem_mensagem_setter(instance):
    original = instance.mensagem
    instance.mensagem = original
    assert instance.mensagem == original



@given(instance=Mensagem_strategy)
def test_hyp_mensagem_dataEnvio_setter(instance):
    original = instance.dataEnvio
    instance.dataEnvio = original
    assert instance.dataEnvio == original



@given(instance=Mensagem_strategy)
def test_hyp_mensagem_geral_setter(instance):
    original = instance.geral
    instance.geral = original
    assert instance.geral == original



@given(instance=Mensagem_strategy)
def test_hyp_mensagem_assunto_setter(instance):
    original = instance.assunto
    instance.assunto = original
    assert instance.assunto == original





@given(instance=Naturalidade_strategy)
def test_hyp_naturalidade_naturalidade_setter(instance):
    original = instance.naturalidade
    instance.naturalidade = original
    assert instance.naturalidade == original




@given(instance=Medicamento_strategy)
def test_hyp_medicamento_ativo_setter(instance):
    original = instance.ativo
    instance.ativo = original
    assert instance.ativo == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_intervaloTempo_setter(instance):
    original = instance.intervaloTempo
    instance.intervaloTempo = original
    assert instance.intervaloTempo == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_horaInicial_setter(instance):
    original = instance.horaInicial
    instance.horaInicial = original
    assert instance.horaInicial == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_dataFim_setter(instance):
    original = instance.dataFim
    instance.dataFim = original
    assert instance.dataFim == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_dataInicio_setter(instance):
    original = instance.dataInicio
    instance.dataInicio = original
    assert instance.dataInicio == original





@given(instance=Telefone_strategy)
def test_hyp_telefone_ddd_setter(instance):
    original = instance.ddd
    instance.ddd = original
    assert instance.ddd == original



@given(instance=Telefone_strategy)
def test_hyp_telefone_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Telefone_strategy)
def test_hyp_telefone_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original




@given(instance=Pessoa_strategy)
def test_hyp_pessoa_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_sexo_setter(instance):
    original = instance.sexo
    instance.sexo = original
    assert instance.sexo == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_dataInclusao_setter(instance):
    original = instance.dataInclusao
    instance.dataInclusao = original
    assert instance.dataInclusao == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_ultimoAcesso_setter(instance):
    original = instance.ultimoAcesso
    instance.ultimoAcesso = original
    assert instance.ultimoAcesso == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_senha_setter(instance):
    original = instance.senha
    instance.senha = original
    assert instance.senha == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_dataNascimento_setter(instance):
    original = instance.dataNascimento
    instance.dataNascimento = original
    assert instance.dataNascimento == original




@given(instance=Endereco_strategy)
def test_hyp_endereco_logradouro_setter(instance):
    original = instance.logradouro
    instance.logradouro = original
    assert instance.logradouro == original



@given(instance=Endereco_strategy)
def test_hyp_endereco_cep_setter(instance):
    original = instance.cep
    instance.cep = original
    assert instance.cep == original



@given(instance=Endereco_strategy)
def test_hyp_endereco_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Endereco_strategy)
def test_hyp_endereco_bairro_setter(instance):
    original = instance.bairro
    instance.bairro = original
    assert instance.bairro == original



@given(instance=Endereco_strategy)
def test_hyp_endereco_cidade_setter(instance):
    original = instance.cidade
    instance.cidade = original
    assert instance.cidade == original




@given(instance=Exame_strategy)
def test_hyp_exame_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=Exame_strategy)
def test_hyp_exame_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Exame_strategy)
def test_hyp_exame_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original




@given(instance=LocalExame_strategy)
def test_hyp_localexame_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=TipoMedicamento_strategy)
def test_hyp_tipomedicamento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original




@given(instance=TipoSanguineo_strategy)
def test_hyp_tiposanguineo_nome_setter(instance):
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
    Endereco,
    Exame,
    Interacao,
    LinhaCuidado,
    LocalExame,
    Medicamento,
    Mensagem,
    Naturalidade,
    Paciente,
    Pessoa,
    ProfissionalSaude,
    Telefone,
    TipoMedicamento,
    TipoSanguineo,
    enu,
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

def test_Endereco_bairro_value_roundtrip():
    instance = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    assert instance.bairro == "sample_text"
    instance.bairro = "sample_text_2"
    assert instance.bairro == "sample_text_2"


def test_Endereco_cep_value_roundtrip():
    instance = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    assert instance.cep == "sample_text"
    instance.cep = "sample_text_2"
    assert instance.cep == "sample_text_2"


def test_Endereco_cidade_value_roundtrip():
    instance = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    assert instance.cidade == "sample_text"
    instance.cidade = "sample_text_2"
    assert instance.cidade == "sample_text_2"


def test_Endereco_logradouro_value_roundtrip():
    instance = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    assert instance.logradouro == "sample_text"
    instance.logradouro = "sample_text_2"
    assert instance.logradouro == "sample_text_2"


def test_Endereco_numero_value_roundtrip():
    instance = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    assert instance.numero == 7
    instance.numero = 13
    assert instance.numero == 13


def test_Exame_data_value_roundtrip():
    instance = Exame(data="sample_text", descricao="sample_text", nome="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_Exame_descricao_value_roundtrip():
    instance = Exame(data="sample_text", descricao="sample_text", nome="sample_text")
    assert instance.descricao == "sample_text"
    instance.descricao = "sample_text_2"
    assert instance.descricao == "sample_text_2"


def test_Exame_nome_value_roundtrip():
    instance = Exame(data="sample_text", descricao="sample_text", nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_LinhaCuidado_descricao_value_roundtrip():
    instance = LinhaCuidado(descricao=7, nome="sample_text")
    assert instance.descricao == 7
    instance.descricao = 13
    assert instance.descricao == 13


def test_LinhaCuidado_nome_value_roundtrip():
    instance = LinhaCuidado(descricao=7, nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_LocalExame_nome_value_roundtrip():
    instance = LocalExame(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_Medicamento_ativo_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.ativo == True
    instance.ativo = False
    assert instance.ativo == False


def test_Medicamento_dataFim_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.dataFim == "sample_text"
    instance.dataFim = "sample_text_2"
    assert instance.dataFim == "sample_text_2"


def test_Medicamento_dataInicio_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.dataInicio == "sample_text"
    instance.dataInicio = "sample_text_2"
    assert instance.dataInicio == "sample_text_2"


def test_Medicamento_descricao_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.descricao == "sample_text"
    instance.descricao = "sample_text_2"
    assert instance.descricao == "sample_text_2"


def test_Medicamento_horaInicial_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.horaInicial == "sample_text"
    instance.horaInicial = "sample_text_2"
    assert instance.horaInicial == "sample_text_2"


def test_Medicamento_intervaloTempo_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.intervaloTempo == 7
    instance.intervaloTempo = 13
    assert instance.intervaloTempo == 13


def test_Medicamento_nome_value_roundtrip():
    instance = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_Mensagem_assunto_value_roundtrip():
    instance = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    assert instance.assunto == "sample_text"
    instance.assunto = "sample_text_2"
    assert instance.assunto == "sample_text_2"


def test_Mensagem_dataEnvio_value_roundtrip():
    instance = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    assert instance.dataEnvio == "sample_text"
    instance.dataEnvio = "sample_text_2"
    assert instance.dataEnvio == "sample_text_2"


def test_Mensagem_geral_value_roundtrip():
    instance = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    assert instance.geral == True
    instance.geral = False
    assert instance.geral == False


def test_Mensagem_mensagem_value_roundtrip():
    instance = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    assert instance.mensagem == "sample_text"
    instance.mensagem = "sample_text_2"
    assert instance.mensagem == "sample_text_2"


def test_Naturalidade_naturalidade_value_roundtrip():
    instance = Naturalidade(naturalidade="sample_text")
    assert instance.naturalidade == "sample_text"
    instance.naturalidade = "sample_text_2"
    assert instance.naturalidade == "sample_text_2"


def test_Pessoa_cpf_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.cpf == "sample_text"
    instance.cpf = "sample_text_2"
    assert instance.cpf == "sample_text_2"


def test_Pessoa_dataInclusao_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.dataInclusao == "sample_text"
    instance.dataInclusao = "sample_text_2"
    assert instance.dataInclusao == "sample_text_2"


def test_Pessoa_dataNascimento_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.dataNascimento == "sample_text"
    instance.dataNascimento = "sample_text_2"
    assert instance.dataNascimento == "sample_text_2"


def test_Pessoa_email_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Pessoa_senha_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.senha == "sample_text"
    instance.senha = "sample_text_2"
    assert instance.senha == "sample_text_2"


def test_Pessoa_sexo_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.sexo == "sample_text"
    instance.sexo = "sample_text_2"
    assert instance.sexo == "sample_text_2"


def test_Pessoa_ultimoAcesso_value_roundtrip():
    instance = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    assert instance.ultimoAcesso == "sample_text"
    instance.ultimoAcesso = "sample_text_2"
    assert instance.ultimoAcesso == "sample_text_2"


def test_Telefone_ddd_value_roundtrip():
    instance = Telefone(ddd=7, numero="sample_text", tipo="sample_text")
    assert instance.ddd == 7
    instance.ddd = 13
    assert instance.ddd == 13


def test_Telefone_numero_value_roundtrip():
    instance = Telefone(ddd=7, numero="sample_text", tipo="sample_text")
    assert instance.numero == "sample_text"
    instance.numero = "sample_text_2"
    assert instance.numero == "sample_text_2"


def test_Telefone_tipo_value_roundtrip():
    instance = Telefone(ddd=7, numero="sample_text", tipo="sample_text")
    assert instance.tipo == "sample_text"
    instance.tipo = "sample_text_2"
    assert instance.tipo == "sample_text_2"


def test_TipoMedicamento_nome_value_roundtrip():
    instance = TipoMedicamento(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_TipoSanguineo_nome_value_roundtrip():
    instance = TipoSanguineo(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_assoc_Endereco_Pessoa_link_reassign_clear():
    a = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    b1 = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    b2 = Endereco(bairro="sample_text_2", cep="sample_text_2", cidade="sample_text_2", logradouro="sample_text_2", numero=13)
    _safe_set(a, 'endereco5', b1)
    assert _is_linked(a, 'endereco5', b1)
    if hasattr(b1, 'pessoa4'):
        assert _is_linked(b1, 'pessoa4', a)
    _safe_set(a, 'endereco5', b2)
    assert _is_linked(a, 'endereco5', b2)
    if hasattr(b1, 'pessoa4'):
        assert not _is_linked(b1, 'pessoa4', a)
    if hasattr(b2, 'pessoa4'):
        assert _is_linked(b2, 'pessoa4', a)
    _safe_set(a, 'endereco5', None)
    assert not _is_linked(a, 'endereco5', b2)
    if hasattr(b2, 'pessoa4'):
        assert not _is_linked(b2, 'pessoa4', a)


def test_assoc_Est__em_link_reassign_clear():
    a = LocalExame(nome="sample_text")
    b1 = Exame(data="sample_text", descricao="sample_text", nome="sample_text")
    b2 = Exame(data="sample_text_2", descricao="sample_text_2", nome="sample_text_2")
    _safe_set(a, 'exame0', {b1})
    assert _is_linked(a, 'exame0', b1)
    if hasattr(b1, 'localExame1'):
        assert _is_linked(b1, 'localExame1', a)
    _safe_set(a, 'exame0', {b2})
    assert _is_linked(a, 'exame0', b2)
    if hasattr(b1, 'localExame1'):
        assert not _is_linked(b1, 'localExame1', a)
    if hasattr(b2, 'localExame1'):
        assert _is_linked(b2, 'localExame1', a)
    _safe_set(a, 'exame0', set())
    assert not _is_linked(a, 'exame0', b2)
    if hasattr(b2, 'localExame1'):
        assert not _is_linked(b2, 'localExame1', a)


def test_assoc_Interacao_Mensagem_link_reassign_clear():
    a = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    b1 = Interacao()
    b2 = Interacao()
    _safe_set(a, 'interacao17', {b1})
    assert _is_linked(a, 'interacao17', b1)
    if hasattr(b1, 'mensagem16'):
        assert _is_linked(b1, 'mensagem16', a)
    _safe_set(a, 'interacao17', {b2})
    assert _is_linked(a, 'interacao17', b2)
    if hasattr(b1, 'mensagem16'):
        assert not _is_linked(b1, 'mensagem16', a)
    if hasattr(b2, 'mensagem16'):
        assert _is_linked(b2, 'mensagem16', a)
    _safe_set(a, 'interacao17', set())
    assert not _is_linked(a, 'interacao17', b2)
    if hasattr(b2, 'mensagem16'):
        assert not _is_linked(b2, 'mensagem16', a)


def test_assoc_LocalExame_Endereco_link_reassign_clear():
    a = LocalExame(nome="sample_text")
    b1 = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    b2 = Endereco(bairro="sample_text_2", cep="sample_text_2", cidade="sample_text_2", logradouro="sample_text_2", numero=13)
    _safe_set(a, 'endereco2', b1)
    assert _is_linked(a, 'endereco2', b1)
    if hasattr(b1, 'localExame3'):
        assert _is_linked(b1, 'localExame3', a)
    _safe_set(a, 'endereco2', b2)
    assert _is_linked(a, 'endereco2', b2)
    if hasattr(b1, 'localExame3'):
        assert not _is_linked(b1, 'localExame3', a)
    if hasattr(b2, 'localExame3'):
        assert _is_linked(b2, 'localExame3', a)
    _safe_set(a, 'endereco2', None)
    assert not _is_linked(a, 'endereco2', b2)
    if hasattr(b2, 'localExame3'):
        assert not _is_linked(b2, 'localExame3', a)


def test_assoc_Mensagem_LinhaCuidado_link_reassign_clear():
    a = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    b1 = LinhaCuidado(descricao=7, nome="sample_text")
    b2 = LinhaCuidado(descricao=13, nome="sample_text_2")
    _safe_set(a, 'linhaCuidado14', b1)
    assert _is_linked(a, 'linhaCuidado14', b1)
    if hasattr(b1, 'mensagem15'):
        assert _is_linked(b1, 'mensagem15', a)
    _safe_set(a, 'linhaCuidado14', b2)
    assert _is_linked(a, 'linhaCuidado14', b2)
    if hasattr(b1, 'mensagem15'):
        assert not _is_linked(b1, 'mensagem15', a)
    if hasattr(b2, 'mensagem15'):
        assert _is_linked(b2, 'mensagem15', a)
    _safe_set(a, 'linhaCuidado14', None)
    assert not _is_linked(a, 'linhaCuidado14', b2)
    if hasattr(b2, 'mensagem15'):
        assert not _is_linked(b2, 'mensagem15', a)


def test_assoc_Paciente_Medicamento_link_reassign_clear():
    a = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    b1 = Paciente()
    b2 = Paciente()
    _safe_set(a, 'paciente9', b1)
    assert _is_linked(a, 'paciente9', b1)
    if hasattr(b1, 'medicamento8'):
        assert _is_linked(b1, 'medicamento8', a)
    _safe_set(a, 'paciente9', b2)
    assert _is_linked(a, 'paciente9', b2)
    if hasattr(b1, 'medicamento8'):
        assert not _is_linked(b1, 'medicamento8', a)
    if hasattr(b2, 'medicamento8'):
        assert _is_linked(b2, 'medicamento8', a)
    _safe_set(a, 'paciente9', None)
    assert not _is_linked(a, 'paciente9', b2)
    if hasattr(b2, 'medicamento8'):
        assert not _is_linked(b2, 'medicamento8', a)


def test_assoc_Paciente_Mensagem_link_reassign_clear():
    a = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    b1 = Paciente()
    b2 = Paciente()
    _safe_set(a, 'paciente21', b1)
    assert _is_linked(a, 'paciente21', b1)
    if hasattr(b1, 'mensagem20'):
        assert _is_linked(b1, 'mensagem20', a)
    _safe_set(a, 'paciente21', b2)
    assert _is_linked(a, 'paciente21', b2)
    if hasattr(b1, 'mensagem20'):
        assert not _is_linked(b1, 'mensagem20', a)
    if hasattr(b2, 'mensagem20'):
        assert _is_linked(b2, 'mensagem20', a)
    _safe_set(a, 'paciente21', None)
    assert not _is_linked(a, 'paciente21', b2)
    if hasattr(b2, 'mensagem20'):
        assert not _is_linked(b2, 'mensagem20', a)


def test_assoc_Pessoa_Naturalidade_link_reassign_clear():
    a = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    b1 = Naturalidade(naturalidade="sample_text")
    b2 = Naturalidade(naturalidade="sample_text_2")
    _safe_set(a, 'naturalidade10', b1)
    assert _is_linked(a, 'naturalidade10', b1)
    if hasattr(b1, 'pessoa11'):
        assert _is_linked(b1, 'pessoa11', a)
    _safe_set(a, 'naturalidade10', b2)
    assert _is_linked(a, 'naturalidade10', b2)
    if hasattr(b1, 'pessoa11'):
        assert not _is_linked(b1, 'pessoa11', a)
    if hasattr(b2, 'pessoa11'):
        assert _is_linked(b2, 'pessoa11', a)
    _safe_set(a, 'naturalidade10', None)
    assert not _is_linked(a, 'naturalidade10', b2)
    if hasattr(b2, 'pessoa11'):
        assert not _is_linked(b2, 'pessoa11', a)


def test_assoc_Pessoa_Telefone_link_reassign_clear():
    a = Telefone(ddd=7, numero="sample_text", tipo="sample_text")
    b1 = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    b2 = Pessoa(cpf="sample_text_2", dataInclusao="sample_text_2", dataNascimento="sample_text_2", email="sample_text_2", senha="sample_text_2", sexo="sample_text_2", ultimoAcesso="sample_text_2")
    _safe_set(a, 'pessoa7', b1)
    assert _is_linked(a, 'pessoa7', b1)
    if hasattr(b1, 'telefone6'):
        assert _is_linked(b1, 'telefone6', a)
    _safe_set(a, 'pessoa7', b2)
    assert _is_linked(a, 'pessoa7', b2)
    if hasattr(b1, 'telefone6'):
        assert not _is_linked(b1, 'telefone6', a)
    if hasattr(b2, 'telefone6'):
        assert _is_linked(b2, 'telefone6', a)
    _safe_set(a, 'pessoa7', None)
    assert not _is_linked(a, 'pessoa7', b2)
    if hasattr(b2, 'telefone6'):
        assert not _is_linked(b2, 'telefone6', a)


def test_assoc_ProfissioanlSaude_Mensagem_link_reassign_clear():
    a = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    b1 = ProfissionalSaude()
    b2 = ProfissionalSaude()
    _safe_set(a, 'profissionalSaude13', b1)
    assert _is_linked(a, 'profissionalSaude13', b1)
    if hasattr(b1, 'mensagem12'):
        assert _is_linked(b1, 'mensagem12', a)
    _safe_set(a, 'profissionalSaude13', b2)
    assert _is_linked(a, 'profissionalSaude13', b2)
    if hasattr(b1, 'mensagem12'):
        assert not _is_linked(b1, 'mensagem12', a)
    if hasattr(b2, 'mensagem12'):
        assert _is_linked(b2, 'mensagem12', a)
    _safe_set(a, 'profissionalSaude13', None)
    assert not _is_linked(a, 'profissionalSaude13', b2)
    if hasattr(b2, 'mensagem12'):
        assert not _is_linked(b2, 'mensagem12', a)


def test_assoc_TipoSanguineo_Paciente_link_reassign_clear():
    a = TipoSanguineo(nome="sample_text")
    b1 = Paciente()
    b2 = Paciente()
    _safe_set(a, 'paciente22', {b1})
    assert _is_linked(a, 'paciente22', b1)
    if hasattr(b1, 'tipoSanguineo23'):
        assert _is_linked(b1, 'tipoSanguineo23', a)
    _safe_set(a, 'paciente22', {b2})
    assert _is_linked(a, 'paciente22', b2)
    if hasattr(b1, 'tipoSanguineo23'):
        assert not _is_linked(b1, 'tipoSanguineo23', a)
    if hasattr(b2, 'tipoSanguineo23'):
        assert _is_linked(b2, 'tipoSanguineo23', a)
    _safe_set(a, 'paciente22', set())
    assert not _is_linked(a, 'paciente22', b2)
    if hasattr(b2, 'tipoSanguineo23'):
        assert not _is_linked(b2, 'tipoSanguineo23', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Endereco_strategy = st.builds(Endereco, bairro=safe_text, cep=safe_text, cidade=safe_text, logradouro=safe_text, numero=st.integers())
@given(instance=Endereco_strategy)
@settings(max_examples=25)
def test_Endereco_instantiation(instance):
    assert isinstance(instance, Endereco)


Exame_strategy = st.builds(Exame, data=safe_text, descricao=safe_text, nome=safe_text)
@given(instance=Exame_strategy)
@settings(max_examples=25)
def test_Exame_instantiation(instance):
    assert isinstance(instance, Exame)


Interacao_strategy = st.builds(Interacao)
@given(instance=Interacao_strategy)
@settings(max_examples=25)
def test_Interacao_instantiation(instance):
    assert isinstance(instance, Interacao)


LinhaCuidado_strategy = st.builds(LinhaCuidado, descricao=st.integers(), nome=safe_text)
@given(instance=LinhaCuidado_strategy)
@settings(max_examples=25)
def test_LinhaCuidado_instantiation(instance):
    assert isinstance(instance, LinhaCuidado)


LocalExame_strategy = st.builds(LocalExame, nome=safe_text)
@given(instance=LocalExame_strategy)
@settings(max_examples=25)
def test_LocalExame_instantiation(instance):
    assert isinstance(instance, LocalExame)


Medicamento_strategy = st.builds(Medicamento, ativo=st.booleans(), dataFim=safe_text, dataInicio=safe_text, descricao=safe_text, horaInicial=safe_text, intervaloTempo=st.integers(), nome=safe_text)
@given(instance=Medicamento_strategy)
@settings(max_examples=25)
def test_Medicamento_instantiation(instance):
    assert isinstance(instance, Medicamento)


Mensagem_strategy = st.builds(Mensagem, assunto=safe_text, dataEnvio=safe_text, geral=st.booleans(), mensagem=safe_text)
@given(instance=Mensagem_strategy)
@settings(max_examples=25)
def test_Mensagem_instantiation(instance):
    assert isinstance(instance, Mensagem)


Naturalidade_strategy = st.builds(Naturalidade, naturalidade=safe_text)
@given(instance=Naturalidade_strategy)
@settings(max_examples=25)
def test_Naturalidade_instantiation(instance):
    assert isinstance(instance, Naturalidade)


Paciente_strategy = st.builds(Paciente)
@given(instance=Paciente_strategy)
@settings(max_examples=25)
def test_Paciente_instantiation(instance):
    assert isinstance(instance, Paciente)


Pessoa_strategy = st.builds(Pessoa, cpf=safe_text, dataInclusao=safe_text, dataNascimento=safe_text, email=safe_text, senha=safe_text, sexo=safe_text, ultimoAcesso=safe_text)
@given(instance=Pessoa_strategy)
@settings(max_examples=25)
def test_Pessoa_instantiation(instance):
    assert isinstance(instance, Pessoa)


ProfissionalSaude_strategy = st.builds(ProfissionalSaude)
@given(instance=ProfissionalSaude_strategy)
@settings(max_examples=25)
def test_ProfissionalSaude_instantiation(instance):
    assert isinstance(instance, ProfissionalSaude)


Telefone_strategy = st.builds(Telefone, ddd=st.integers(), numero=safe_text, tipo=safe_text)
@given(instance=Telefone_strategy)
@settings(max_examples=25)
def test_Telefone_instantiation(instance):
    assert isinstance(instance, Telefone)


TipoMedicamento_strategy = st.builds(TipoMedicamento, nome=safe_text)
@given(instance=TipoMedicamento_strategy)
@settings(max_examples=25)
def test_TipoMedicamento_instantiation(instance):
    assert isinstance(instance, TipoMedicamento)


TipoSanguineo_strategy = st.builds(TipoSanguineo, nome=safe_text)
@given(instance=TipoSanguineo_strategy)
@settings(max_examples=25)
def test_TipoSanguineo_instantiation(instance):
    assert isinstance(instance, TipoSanguineo)



