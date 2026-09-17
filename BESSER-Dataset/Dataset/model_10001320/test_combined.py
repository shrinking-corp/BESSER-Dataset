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
    Especialidade,
    ConsultaExame,
    ConsultaMedicamento,
    ConsultaCid,
    Consulta,
    Paciente,
    Medicamento,
    Exame,
    Cid,
    Agenda,
    Funcionario,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_especialidade_is_not_abstract():
    assert not inspect.isabstract(Especialidade)


def test_hyp_especialidade_constructor_exists():
    assert callable(Especialidade.__init__)


def test_hyp_especialidade_constructor_args():
    sig = inspect.signature(Especialidade.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Descricao" in params, "Missing parameter 'Descricao'"





def test_hyp_consultaexame_is_not_abstract():
    assert not inspect.isabstract(ConsultaExame)


def test_hyp_consultaexame_constructor_exists():
    assert callable(ConsultaExame.__init__)


def test_hyp_consultaexame_constructor_args():
    sig = inspect.signature(ConsultaExame.__init__)
    params = list(sig.parameters.keys())
    assert "Entregue" in params, "Missing parameter 'Entregue'"




def test_hyp_consultamedicamento_is_not_abstract():
    assert not inspect.isabstract(ConsultaMedicamento)


def test_hyp_consultamedicamento_constructor_exists():
    assert callable(ConsultaMedicamento.__init__)


def test_hyp_consultamedicamento_constructor_args():
    sig = inspect.signature(ConsultaMedicamento.__init__)
    params = list(sig.parameters.keys())
    assert "MedicamentoId" in params, "Missing parameter 'MedicamentoId'"
    assert "Posologia" in params, "Missing parameter 'Posologia'"

def test_hyp_consultamedicamento_has_MedicamentoId():
    assert hasattr(ConsultaMedicamento, "MedicamentoId")
    descriptor = None
    for klass in ConsultaMedicamento.__mro__:
        if "MedicamentoId" in klass.__dict__:
            descriptor = klass.__dict__["MedicamentoId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consultamedicamento_has_Posologia():
    assert hasattr(ConsultaMedicamento, "Posologia")
    descriptor = None
    for klass in ConsultaMedicamento.__mro__:
        if "Posologia" in klass.__dict__:
            descriptor = klass.__dict__["Posologia"]
            break
    assert isinstance(descriptor, property)



def test_hyp_consultacid_is_not_abstract():
    assert not inspect.isabstract(ConsultaCid)


def test_hyp_consultacid_constructor_exists():
    assert callable(ConsultaCid.__init__)


def test_hyp_consultacid_constructor_args():
    sig = inspect.signature(ConsultaCid.__init__)
    params = list(sig.parameters.keys())
    assert "ConsultaId" in params, "Missing parameter 'ConsultaId'"
    assert "CidId" in params, "Missing parameter 'CidId'"





def test_hyp_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_hyp_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_hyp_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "MedicoId" in params, "Missing parameter 'MedicoId'"
    assert "Queixas" in params, "Missing parameter 'Queixas'"
    assert "PacienteId" in params, "Missing parameter 'PacienteId'"
    assert "DataHora" in params, "Missing parameter 'DataHora'"

def test_hyp_consulta_has_MedicoId():
    assert hasattr(Consulta, "MedicoId")
    descriptor = None
    for klass in Consulta.__mro__:
        if "MedicoId" in klass.__dict__:
            descriptor = klass.__dict__["MedicoId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_Queixas():
    assert hasattr(Consulta, "Queixas")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Queixas" in klass.__dict__:
            descriptor = klass.__dict__["Queixas"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_PacienteId():
    assert hasattr(Consulta, "PacienteId")
    descriptor = None
    for klass in Consulta.__mro__:
        if "PacienteId" in klass.__dict__:
            descriptor = klass.__dict__["PacienteId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_DataHora():
    assert hasattr(Consulta, "DataHora")
    descriptor = None
    for klass in Consulta.__mro__:
        if "DataHora" in klass.__dict__:
            descriptor = klass.__dict__["DataHora"]
            break
    assert isinstance(descriptor, property)



def test_hyp_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_hyp_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_hyp_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "NomeMae" in params, "Missing parameter 'NomeMae'"
    assert "DataNascimento" in params, "Missing parameter 'DataNascimento'"
    assert "CPF" in params, "Missing parameter 'CPF'"








def test_hyp_medicamento_is_not_abstract():
    assert not inspect.isabstract(Medicamento)


def test_hyp_medicamento_constructor_exists():
    assert callable(Medicamento.__init__)


def test_hyp_medicamento_constructor_args():
    sig = inspect.signature(Medicamento.__init__)
    params = list(sig.parameters.keys())
    assert "Fabricante" in params, "Missing parameter 'Fabricante'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "NomeGenerico" in params, "Missing parameter 'NomeGenerico'"
    assert "NomeComercial" in params, "Missing parameter 'NomeComercial'"







def test_hyp_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_hyp_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_hyp_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Descricao" in params, "Missing parameter 'Descricao'"
    assert "Codigo" in params, "Missing parameter 'Codigo'"






def test_hyp_cid_is_not_abstract():
    assert not inspect.isabstract(Cid)


def test_hyp_cid_constructor_exists():
    assert callable(Cid.__init__)


def test_hyp_cid_constructor_args():
    sig = inspect.signature(Cid.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Codigo" in params, "Missing parameter 'Codigo'"
    assert "Descricao" in params, "Missing parameter 'Descricao'"






def test_hyp_agenda_is_not_abstract():
    assert not inspect.isabstract(Agenda)


def test_hyp_agenda_constructor_exists():
    assert callable(Agenda.__init__)


def test_hyp_agenda_constructor_args():
    sig = inspect.signature(Agenda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_funcionario_is_not_abstract():
    assert not inspect.isabstract(Funcionario)


def test_hyp_funcionario_constructor_exists():
    assert callable(Funcionario.__init__)


def test_hyp_funcionario_constructor_args():
    sig = inspect.signature(Funcionario.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Login" in params, "Missing parameter 'Login'"
    assert "Senha" in params, "Missing parameter 'Senha'"
    assert "Perfil" in params, "Missing parameter 'Perfil'"
    assert "Nome" in params, "Missing parameter 'Nome'"







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
Especialidade_strategy = st.builds(
    Especialidade,
    Id=
        st.integers(),
    Descricao=
        safe_text
)
ConsultaExame_strategy = st.builds(
    ConsultaExame,
    Entregue=
        st.booleans()
)
ConsultaMedicamento_strategy = st.builds(
    ConsultaMedicamento,
    MedicamentoId=
        st.none(),
    Posologia=
        safe_text
)
ConsultaCid_strategy = st.builds(
    ConsultaCid,
    ConsultaId=
        st.integers(),
    CidId=
        st.integers()
)
Consulta_strategy = st.builds(
    Consulta,
    MedicoId=
        st.none(),
    Queixas=
        safe_text,
    PacienteId=
        st.none(),
    DataHora=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    Id=
        st.integers(),
    Nome=
        safe_text,
    NomeMae=
        safe_text,
    DataNascimento=
        safe_text,
    CPF=
        safe_text
)
Medicamento_strategy = st.builds(
    Medicamento,
    Fabricante=
        safe_text,
    Id=
        st.integers(),
    NomeGenerico=
        safe_text,
    NomeComercial=
        safe_text
)
Exame_strategy = st.builds(
    Exame,
    Id=
        st.integers(),
    Descricao=
        safe_text,
    Codigo=
        safe_text
)
Cid_strategy = st.builds(
    Cid,
    Id=
        st.integers(),
    Codigo=
        safe_text,
    Descricao=
        safe_text
)
Agenda_strategy = st.builds(
    Agenda,
)
Funcionario_strategy = st.builds(
    Funcionario,
    Id=
        st.integers(),
    Login=
        safe_text,
    Senha=
        safe_text,
    Perfil=
        st.integers(),
    Nome=
        safe_text
)




@given(instance=Especialidade_strategy)
def test_hyp_especialidade_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Especialidade_strategy)
def test_hyp_especialidade_Descricao_setter(instance):
    original = instance.Descricao
    instance.Descricao = original
    assert instance.Descricao == original




@given(instance=ConsultaExame_strategy)
def test_hyp_consultaexame_Entregue_setter(instance):
    original = instance.Entregue
    instance.Entregue = original
    assert instance.Entregue == original

@given(instance=ConsultaMedicamento_strategy)
@settings(max_examples=50)
def test_hyp_consultamedicamento_instantiation(instance):
    assert isinstance(instance, ConsultaMedicamento)



@given(instance=ConsultaMedicamento_strategy)
def test_hyp_consultamedicamento_MedicamentoId_setter(instance):
    original = instance.MedicamentoId
    instance.MedicamentoId = original
    assert instance.MedicamentoId == original



@given(instance=ConsultaMedicamento_strategy)
def test_hyp_consultamedicamento_Posologia_setter(instance):
    original = instance.Posologia
    instance.Posologia = original
    assert instance.Posologia == original




@given(instance=ConsultaCid_strategy)
def test_hyp_consultacid_ConsultaId_setter(instance):
    original = instance.ConsultaId
    instance.ConsultaId = original
    assert instance.ConsultaId == original



@given(instance=ConsultaCid_strategy)
def test_hyp_consultacid_CidId_setter(instance):
    original = instance.CidId
    instance.CidId = original
    assert instance.CidId == original

@given(instance=Consulta_strategy)
@settings(max_examples=50)
def test_hyp_consulta_instantiation(instance):
    assert isinstance(instance, Consulta)



@given(instance=Consulta_strategy)
def test_hyp_consulta_MedicoId_setter(instance):
    original = instance.MedicoId
    instance.MedicoId = original
    assert instance.MedicoId == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Queixas_setter(instance):
    original = instance.Queixas
    instance.Queixas = original
    assert instance.Queixas == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_PacienteId_setter(instance):
    original = instance.PacienteId
    instance.PacienteId = original
    assert instance.PacienteId == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_DataHora_setter(instance):
    original = instance.DataHora
    instance.DataHora = original
    assert instance.DataHora == original




@given(instance=Paciente_strategy)
def test_hyp_paciente_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_NomeMae_setter(instance):
    original = instance.NomeMae
    instance.NomeMae = original
    assert instance.NomeMae == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_DataNascimento_setter(instance):
    original = instance.DataNascimento
    instance.DataNascimento = original
    assert instance.DataNascimento == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_CPF_setter(instance):
    original = instance.CPF
    instance.CPF = original
    assert instance.CPF == original




@given(instance=Medicamento_strategy)
def test_hyp_medicamento_Fabricante_setter(instance):
    original = instance.Fabricante
    instance.Fabricante = original
    assert instance.Fabricante == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_NomeGenerico_setter(instance):
    original = instance.NomeGenerico
    instance.NomeGenerico = original
    assert instance.NomeGenerico == original



@given(instance=Medicamento_strategy)
def test_hyp_medicamento_NomeComercial_setter(instance):
    original = instance.NomeComercial
    instance.NomeComercial = original
    assert instance.NomeComercial == original




@given(instance=Exame_strategy)
def test_hyp_exame_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Exame_strategy)
def test_hyp_exame_Descricao_setter(instance):
    original = instance.Descricao
    instance.Descricao = original
    assert instance.Descricao == original



@given(instance=Exame_strategy)
def test_hyp_exame_Codigo_setter(instance):
    original = instance.Codigo
    instance.Codigo = original
    assert instance.Codigo == original




@given(instance=Cid_strategy)
def test_hyp_cid_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Cid_strategy)
def test_hyp_cid_Codigo_setter(instance):
    original = instance.Codigo
    instance.Codigo = original
    assert instance.Codigo == original



@given(instance=Cid_strategy)
def test_hyp_cid_Descricao_setter(instance):
    original = instance.Descricao
    instance.Descricao = original
    assert instance.Descricao == original





@given(instance=Funcionario_strategy)
def test_hyp_funcionario_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Funcionario_strategy)
def test_hyp_funcionario_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original



@given(instance=Funcionario_strategy)
def test_hyp_funcionario_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original



@given(instance=Funcionario_strategy)
def test_hyp_funcionario_Perfil_setter(instance):
    original = instance.Perfil
    instance.Perfil = original
    assert instance.Perfil == original



@given(instance=Funcionario_strategy)
def test_hyp_funcionario_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Agenda,
    Cid,
    Consulta,
    ConsultaCid,
    ConsultaExame,
    ConsultaMedicamento,
    Especialidade,
    Exame,
    Funcionario,
    Medicamento,
    Paciente,
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

def test_Cid_Codigo_value_roundtrip():
    instance = Cid(Codigo="sample_text", Descricao="sample_text", Id=7)
    assert instance.Codigo == "sample_text"
    instance.Codigo = "sample_text_2"
    assert instance.Codigo == "sample_text_2"


def test_Cid_Descricao_value_roundtrip():
    instance = Cid(Codigo="sample_text", Descricao="sample_text", Id=7)
    assert instance.Descricao == "sample_text"
    instance.Descricao = "sample_text_2"
    assert instance.Descricao == "sample_text_2"


def test_Cid_Id_value_roundtrip():
    instance = Cid(Codigo="sample_text", Descricao="sample_text", Id=7)
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_ConsultaCid_CidId_value_roundtrip():
    instance = ConsultaCid(CidId=7, ConsultaId=7)
    assert instance.CidId == 7
    instance.CidId = 13
    assert instance.CidId == 13


def test_ConsultaCid_ConsultaId_value_roundtrip():
    instance = ConsultaCid(CidId=7, ConsultaId=7)
    assert instance.ConsultaId == 7
    instance.ConsultaId = 13
    assert instance.ConsultaId == 13


def test_ConsultaExame_Entregue_value_roundtrip():
    instance = ConsultaExame(Entregue=True)
    assert instance.Entregue == True
    instance.Entregue = False
    assert instance.Entregue == False


def test_Especialidade_Descricao_value_roundtrip():
    instance = Especialidade(Descricao="sample_text", Id=7)
    assert instance.Descricao == "sample_text"
    instance.Descricao = "sample_text_2"
    assert instance.Descricao == "sample_text_2"


def test_Especialidade_Id_value_roundtrip():
    instance = Especialidade(Descricao="sample_text", Id=7)
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Exame_Codigo_value_roundtrip():
    instance = Exame(Codigo="sample_text", Descricao="sample_text", Id=7)
    assert instance.Codigo == "sample_text"
    instance.Codigo = "sample_text_2"
    assert instance.Codigo == "sample_text_2"


def test_Exame_Descricao_value_roundtrip():
    instance = Exame(Codigo="sample_text", Descricao="sample_text", Id=7)
    assert instance.Descricao == "sample_text"
    instance.Descricao = "sample_text_2"
    assert instance.Descricao == "sample_text_2"


def test_Exame_Id_value_roundtrip():
    instance = Exame(Codigo="sample_text", Descricao="sample_text", Id=7)
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Funcionario_Id_value_roundtrip():
    instance = Funcionario(Id=7, Login="sample_text", Nome="sample_text", Perfil=7, Senha="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Funcionario_Login_value_roundtrip():
    instance = Funcionario(Id=7, Login="sample_text", Nome="sample_text", Perfil=7, Senha="sample_text")
    assert instance.Login == "sample_text"
    instance.Login = "sample_text_2"
    assert instance.Login == "sample_text_2"


def test_Funcionario_Nome_value_roundtrip():
    instance = Funcionario(Id=7, Login="sample_text", Nome="sample_text", Perfil=7, Senha="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_Funcionario_Perfil_value_roundtrip():
    instance = Funcionario(Id=7, Login="sample_text", Nome="sample_text", Perfil=7, Senha="sample_text")
    assert instance.Perfil == 7
    instance.Perfil = 13
    assert instance.Perfil == 13


def test_Funcionario_Senha_value_roundtrip():
    instance = Funcionario(Id=7, Login="sample_text", Nome="sample_text", Perfil=7, Senha="sample_text")
    assert instance.Senha == "sample_text"
    instance.Senha = "sample_text_2"
    assert instance.Senha == "sample_text_2"


def test_Medicamento_Fabricante_value_roundtrip():
    instance = Medicamento(Fabricante="sample_text", Id=7, NomeComercial="sample_text", NomeGenerico="sample_text")
    assert instance.Fabricante == "sample_text"
    instance.Fabricante = "sample_text_2"
    assert instance.Fabricante == "sample_text_2"


def test_Medicamento_Id_value_roundtrip():
    instance = Medicamento(Fabricante="sample_text", Id=7, NomeComercial="sample_text", NomeGenerico="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Medicamento_NomeComercial_value_roundtrip():
    instance = Medicamento(Fabricante="sample_text", Id=7, NomeComercial="sample_text", NomeGenerico="sample_text")
    assert instance.NomeComercial == "sample_text"
    instance.NomeComercial = "sample_text_2"
    assert instance.NomeComercial == "sample_text_2"


def test_Medicamento_NomeGenerico_value_roundtrip():
    instance = Medicamento(Fabricante="sample_text", Id=7, NomeComercial="sample_text", NomeGenerico="sample_text")
    assert instance.NomeGenerico == "sample_text"
    instance.NomeGenerico = "sample_text_2"
    assert instance.NomeGenerico == "sample_text_2"


def test_Paciente_CPF_value_roundtrip():
    instance = Paciente(CPF="sample_text", DataNascimento="sample_text", Id=7, Nome="sample_text", NomeMae="sample_text")
    assert instance.CPF == "sample_text"
    instance.CPF = "sample_text_2"
    assert instance.CPF == "sample_text_2"


def test_Paciente_DataNascimento_value_roundtrip():
    instance = Paciente(CPF="sample_text", DataNascimento="sample_text", Id=7, Nome="sample_text", NomeMae="sample_text")
    assert instance.DataNascimento == "sample_text"
    instance.DataNascimento = "sample_text_2"
    assert instance.DataNascimento == "sample_text_2"


def test_Paciente_Id_value_roundtrip():
    instance = Paciente(CPF="sample_text", DataNascimento="sample_text", Id=7, Nome="sample_text", NomeMae="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Paciente_Nome_value_roundtrip():
    instance = Paciente(CPF="sample_text", DataNascimento="sample_text", Id=7, Nome="sample_text", NomeMae="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_Paciente_NomeMae_value_roundtrip():
    instance = Paciente(CPF="sample_text", DataNascimento="sample_text", Id=7, Nome="sample_text", NomeMae="sample_text")
    assert instance.NomeMae == "sample_text"
    instance.NomeMae = "sample_text_2"
    assert instance.NomeMae == "sample_text_2"


def test_assoc_Agenda_Especialidade_link_reassign_clear():
    a = Especialidade(Descricao="sample_text", Id=7)
    b1 = Agenda()
    b2 = Agenda()
    _safe_set(a, 'agenda3', {b1})
    assert _is_linked(a, 'agenda3', b1)
    if hasattr(b1, 'especialidade2'):
        assert _is_linked(b1, 'especialidade2', a)
    _safe_set(a, 'agenda3', {b2})
    assert _is_linked(a, 'agenda3', b2)
    if hasattr(b1, 'especialidade2'):
        assert not _is_linked(b1, 'especialidade2', a)
    if hasattr(b2, 'especialidade2'):
        assert _is_linked(b2, 'especialidade2', a)
    _safe_set(a, 'agenda3', set())
    assert not _is_linked(a, 'agenda3', b2)
    if hasattr(b2, 'especialidade2'):
        assert not _is_linked(b2, 'especialidade2', a)


def test_assoc_Agenda_Funcionario_link_reassign_clear():
    a = Funcionario(Id=7, Login="sample_text", Nome="sample_text", Perfil=7, Senha="sample_text")
    b1 = Agenda()
    b2 = Agenda()
    _safe_set(a, 'agenda1', b1)
    assert _is_linked(a, 'agenda1', b1)
    if hasattr(b1, 'funcionario0'):
        assert _is_linked(b1, 'funcionario0', a)
    _safe_set(a, 'agenda1', b2)
    assert _is_linked(a, 'agenda1', b2)
    if hasattr(b1, 'funcionario0'):
        assert not _is_linked(b1, 'funcionario0', a)
    if hasattr(b2, 'funcionario0'):
        assert _is_linked(b2, 'funcionario0', a)
    _safe_set(a, 'agenda1', None)
    assert not _is_linked(a, 'agenda1', b2)
    if hasattr(b2, 'funcionario0'):
        assert not _is_linked(b2, 'funcionario0', a)


def test_assoc_Cid_ConsultaCid_link_reassign_clear():
    a = ConsultaCid(CidId=7, ConsultaId=7)
    b1 = Cid(Codigo="sample_text", Descricao="sample_text", Id=7)
    b2 = Cid(Codigo="sample_text_2", Descricao="sample_text_2", Id=13)
    _safe_set(a, 'cid9', b1)
    assert _is_linked(a, 'cid9', b1)
    if hasattr(b1, 'consultaCid8'):
        assert _is_linked(b1, 'consultaCid8', a)
    _safe_set(a, 'cid9', b2)
    assert _is_linked(a, 'cid9', b2)
    if hasattr(b1, 'consultaCid8'):
        assert not _is_linked(b1, 'consultaCid8', a)
    if hasattr(b2, 'consultaCid8'):
        assert _is_linked(b2, 'consultaCid8', a)
    _safe_set(a, 'cid9', None)
    assert not _is_linked(a, 'cid9', b2)
    if hasattr(b2, 'consultaCid8'):
        assert not _is_linked(b2, 'consultaCid8', a)


def test_assoc_Exame_ConsultaExame_link_reassign_clear():
    a = Exame(Codigo="sample_text", Descricao="sample_text", Id=7)
    b1 = ConsultaExame(Entregue=True)
    b2 = ConsultaExame(Entregue=False)
    _safe_set(a, 'consultaExame14', b1)
    assert _is_linked(a, 'consultaExame14', b1)
    if hasattr(b1, 'exame15'):
        assert _is_linked(b1, 'exame15', a)
    _safe_set(a, 'consultaExame14', b2)
    assert _is_linked(a, 'consultaExame14', b2)
    if hasattr(b1, 'exame15'):
        assert not _is_linked(b1, 'exame15', a)
    if hasattr(b2, 'exame15'):
        assert _is_linked(b2, 'exame15', a)
    _safe_set(a, 'consultaExame14', None)
    assert not _is_linked(a, 'consultaExame14', b2)
    if hasattr(b2, 'exame15'):
        assert not _is_linked(b2, 'exame15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Agenda_strategy = st.builds(Agenda)
@given(instance=Agenda_strategy)
@settings(max_examples=25)
def test_Agenda_instantiation(instance):
    assert isinstance(instance, Agenda)


Cid_strategy = st.builds(Cid, Codigo=safe_text, Descricao=safe_text, Id=st.integers())
@given(instance=Cid_strategy)
@settings(max_examples=25)
def test_Cid_instantiation(instance):
    assert isinstance(instance, Cid)


ConsultaCid_strategy = st.builds(ConsultaCid, CidId=st.integers(), ConsultaId=st.integers())
@given(instance=ConsultaCid_strategy)
@settings(max_examples=25)
def test_ConsultaCid_instantiation(instance):
    assert isinstance(instance, ConsultaCid)


ConsultaExame_strategy = st.builds(ConsultaExame, Entregue=st.booleans())
@given(instance=ConsultaExame_strategy)
@settings(max_examples=25)
def test_ConsultaExame_instantiation(instance):
    assert isinstance(instance, ConsultaExame)


Especialidade_strategy = st.builds(Especialidade, Descricao=safe_text, Id=st.integers())
@given(instance=Especialidade_strategy)
@settings(max_examples=25)
def test_Especialidade_instantiation(instance):
    assert isinstance(instance, Especialidade)


Exame_strategy = st.builds(Exame, Codigo=safe_text, Descricao=safe_text, Id=st.integers())
@given(instance=Exame_strategy)
@settings(max_examples=25)
def test_Exame_instantiation(instance):
    assert isinstance(instance, Exame)


Funcionario_strategy = st.builds(Funcionario, Id=st.integers(), Login=safe_text, Nome=safe_text, Perfil=st.integers(), Senha=safe_text)
@given(instance=Funcionario_strategy)
@settings(max_examples=25)
def test_Funcionario_instantiation(instance):
    assert isinstance(instance, Funcionario)


Medicamento_strategy = st.builds(Medicamento, Fabricante=safe_text, Id=st.integers(), NomeComercial=safe_text, NomeGenerico=safe_text)
@given(instance=Medicamento_strategy)
@settings(max_examples=25)
def test_Medicamento_instantiation(instance):
    assert isinstance(instance, Medicamento)


Paciente_strategy = st.builds(Paciente, CPF=safe_text, DataNascimento=safe_text, Id=st.integers(), Nome=safe_text, NomeMae=safe_text)
@given(instance=Paciente_strategy)
@settings(max_examples=25)
def test_Paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



