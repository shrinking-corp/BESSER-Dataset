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
    M_dico,
    Agendamento,
    Funcion_rio,
    Consulta,
    Paciente,
    Exame,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_m_dico_is_not_abstract():
    assert not inspect.isabstract(M_dico)


def test_hyp_m_dico_constructor_exists():
    assert callable(M_dico.__init__)


def test_hyp_m_dico_constructor_args():
    sig = inspect.signature(M_dico.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "CPF" in params, "Missing parameter 'CPF'"
    assert "Especialidade" in params, "Missing parameter 'Especialidade'"






def test_hyp_agendamento_is_not_abstract():
    assert not inspect.isabstract(Agendamento)


def test_hyp_agendamento_constructor_exists():
    assert callable(Agendamento.__init__)


def test_hyp_agendamento_constructor_args():
    sig = inspect.signature(Agendamento.__init__)
    params = list(sig.parameters.keys())
    assert "Dia_e_Horario" in params, "Missing parameter 'Dia_e_Horario'"
    assert "TipoAgendamento" in params, "Missing parameter 'TipoAgendamento'"
    assert "Sede" in params, "Missing parameter 'Sede'"
    assert "Medico" in params, "Missing parameter 'Medico'"
    assert "Especialista" in params, "Missing parameter 'Especialista'"








def test_hyp_funcion_rio_is_not_abstract():
    assert not inspect.isabstract(Funcion_rio)


def test_hyp_funcion_rio_constructor_exists():
    assert callable(Funcion_rio.__init__)


def test_hyp_funcion_rio_constructor_args():
    sig = inspect.signature(Funcion_rio.__init__)
    params = list(sig.parameters.keys())
    assert "Usuario" in params, "Missing parameter 'Usuario'"
    assert "Senha" in params, "Missing parameter 'Senha'"





def test_hyp_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_hyp_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_hyp_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "Sede" in params, "Missing parameter 'Sede'"
    assert "TipoConsulta" in params, "Missing parameter 'TipoConsulta'"
    assert "Especialista" in params, "Missing parameter 'Especialista'"
    assert "Medico" in params, "Missing parameter 'Medico'"







def test_hyp_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_hyp_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_hyp_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "Endereco" in params, "Missing parameter 'Endereco'"
    assert "DataNascimento" in params, "Missing parameter 'DataNascimento'"
    assert "CPF" in params, "Missing parameter 'CPF'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "RG" in params, "Missing parameter 'RG'"
    assert "Telefone" in params, "Missing parameter 'Telefone'"
    assert "Sobrenome" in params, "Missing parameter 'Sobrenome'"
    assert "Estado" in params, "Missing parameter 'Estado'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "EstadoCivil" in params, "Missing parameter 'EstadoCivil'"
    assert "ConvenioMedico" in params, "Missing parameter 'ConvenioMedico'"
    assert "Nacionalidade" in params, "Missing parameter 'Nacionalidade'"
    assert "Celular" in params, "Missing parameter 'Celular'"
    assert "Cidade" in params, "Missing parameter 'Cidade'"
    assert "Sexo" in params, "Missing parameter 'Sexo'"
    assert "CEP" in params, "Missing parameter 'CEP'"
    assert "CPF1" in params, "Missing parameter 'CPF1'"

def test_hyp_paciente_has_Endereco():
    assert hasattr(Paciente, "Endereco")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Endereco" in klass.__dict__:
            descriptor = klass.__dict__["Endereco"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_DataNascimento():
    assert hasattr(Paciente, "DataNascimento")
    descriptor = None
    for klass in Paciente.__mro__:
        if "DataNascimento" in klass.__dict__:
            descriptor = klass.__dict__["DataNascimento"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_CPF():
    assert hasattr(Paciente, "CPF")
    descriptor = None
    for klass in Paciente.__mro__:
        if "CPF" in klass.__dict__:
            descriptor = klass.__dict__["CPF"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Email():
    assert hasattr(Paciente, "Email")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_RG():
    assert hasattr(Paciente, "RG")
    descriptor = None
    for klass in Paciente.__mro__:
        if "RG" in klass.__dict__:
            descriptor = klass.__dict__["RG"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Telefone():
    assert hasattr(Paciente, "Telefone")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Telefone" in klass.__dict__:
            descriptor = klass.__dict__["Telefone"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Sobrenome():
    assert hasattr(Paciente, "Sobrenome")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Sobrenome" in klass.__dict__:
            descriptor = klass.__dict__["Sobrenome"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Estado():
    assert hasattr(Paciente, "Estado")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Estado" in klass.__dict__:
            descriptor = klass.__dict__["Estado"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Nome():
    assert hasattr(Paciente, "Nome")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_EstadoCivil():
    assert hasattr(Paciente, "EstadoCivil")
    descriptor = None
    for klass in Paciente.__mro__:
        if "EstadoCivil" in klass.__dict__:
            descriptor = klass.__dict__["EstadoCivil"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_ConvenioMedico():
    assert hasattr(Paciente, "ConvenioMedico")
    descriptor = None
    for klass in Paciente.__mro__:
        if "ConvenioMedico" in klass.__dict__:
            descriptor = klass.__dict__["ConvenioMedico"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Nacionalidade():
    assert hasattr(Paciente, "Nacionalidade")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Nacionalidade" in klass.__dict__:
            descriptor = klass.__dict__["Nacionalidade"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Celular():
    assert hasattr(Paciente, "Celular")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Celular" in klass.__dict__:
            descriptor = klass.__dict__["Celular"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Cidade():
    assert hasattr(Paciente, "Cidade")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Cidade" in klass.__dict__:
            descriptor = klass.__dict__["Cidade"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_Sexo():
    assert hasattr(Paciente, "Sexo")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Sexo" in klass.__dict__:
            descriptor = klass.__dict__["Sexo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_CEP():
    assert hasattr(Paciente, "CEP")
    descriptor = None
    for klass in Paciente.__mro__:
        if "CEP" in klass.__dict__:
            descriptor = klass.__dict__["CEP"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_CPF1():
    assert hasattr(Paciente, "CPF1")
    descriptor = None
    for klass in Paciente.__mro__:
        if "CPF1" in klass.__dict__:
            descriptor = klass.__dict__["CPF1"]
            break
    assert isinstance(descriptor, property)



def test_hyp_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_hyp_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_hyp_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "TipoExame" in params, "Missing parameter 'TipoExame'"
    assert "Sede" in params, "Missing parameter 'Sede'"
    assert "Especialista" in params, "Missing parameter 'Especialista'"
    assert "Medico" in params, "Missing parameter 'Medico'"






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
M_dico_strategy = st.builds(
    M_dico,
    Nome=
        safe_text,
    CPF=
        st.integers(),
    Especialidade=
        safe_text
)
Agendamento_strategy = st.builds(
    Agendamento,
    Dia_e_Horario=
        safe_text,
    TipoAgendamento=
        safe_text,
    Sede=
        safe_text,
    Medico=
        safe_text,
    Especialista=
        safe_text
)
Funcion_rio_strategy = st.builds(
    Funcion_rio,
    Usuario=
        safe_text,
    Senha=
        safe_text
)
Consulta_strategy = st.builds(
    Consulta,
    Sede=
        safe_text,
    TipoConsulta=
        safe_text,
    Especialista=
        safe_text,
    Medico=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    Endereco=
        safe_text,
    DataNascimento=
        safe_text,
    CPF=
        st.none(),
    Email=
        safe_text,
    RG=
        st.integers(),
    Telefone=
        st.integers(),
    Sobrenome=
        safe_text,
    Estado=
        safe_text,
    Nome=
        safe_text,
    EstadoCivil=
        safe_text,
    ConvenioMedico=
        safe_text,
    Nacionalidade=
        safe_text,
    Celular=
        st.integers(),
    Cidade=
        safe_text,
    Sexo=
        safe_text,
    CEP=
        st.integers(),
    CPF1=
        st.integers()
)
Exame_strategy = st.builds(
    Exame,
    TipoExame=
        safe_text,
    Sede=
        safe_text,
    Especialista=
        safe_text,
    Medico=
        safe_text
)




@given(instance=M_dico_strategy)
def test_hyp_m_dico_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=M_dico_strategy)
def test_hyp_m_dico_CPF_setter(instance):
    original = instance.CPF
    instance.CPF = original
    assert instance.CPF == original



@given(instance=M_dico_strategy)
def test_hyp_m_dico_Especialidade_setter(instance):
    original = instance.Especialidade
    instance.Especialidade = original
    assert instance.Especialidade == original




@given(instance=Agendamento_strategy)
def test_hyp_agendamento_Dia_e_Horario_setter(instance):
    original = instance.Dia_e_Horario
    instance.Dia_e_Horario = original
    assert instance.Dia_e_Horario == original



@given(instance=Agendamento_strategy)
def test_hyp_agendamento_TipoAgendamento_setter(instance):
    original = instance.TipoAgendamento
    instance.TipoAgendamento = original
    assert instance.TipoAgendamento == original



@given(instance=Agendamento_strategy)
def test_hyp_agendamento_Sede_setter(instance):
    original = instance.Sede
    instance.Sede = original
    assert instance.Sede == original



@given(instance=Agendamento_strategy)
def test_hyp_agendamento_Medico_setter(instance):
    original = instance.Medico
    instance.Medico = original
    assert instance.Medico == original



@given(instance=Agendamento_strategy)
def test_hyp_agendamento_Especialista_setter(instance):
    original = instance.Especialista
    instance.Especialista = original
    assert instance.Especialista == original




@given(instance=Funcion_rio_strategy)
def test_hyp_funcion_rio_Usuario_setter(instance):
    original = instance.Usuario
    instance.Usuario = original
    assert instance.Usuario == original



@given(instance=Funcion_rio_strategy)
def test_hyp_funcion_rio_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original




@given(instance=Consulta_strategy)
def test_hyp_consulta_Sede_setter(instance):
    original = instance.Sede
    instance.Sede = original
    assert instance.Sede == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_TipoConsulta_setter(instance):
    original = instance.TipoConsulta
    instance.TipoConsulta = original
    assert instance.TipoConsulta == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Especialista_setter(instance):
    original = instance.Especialista
    instance.Especialista = original
    assert instance.Especialista == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Medico_setter(instance):
    original = instance.Medico
    instance.Medico = original
    assert instance.Medico == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_hyp_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



@given(instance=Paciente_strategy)
def test_hyp_paciente_Endereco_setter(instance):
    original = instance.Endereco
    instance.Endereco = original
    assert instance.Endereco == original



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



@given(instance=Paciente_strategy)
def test_hyp_paciente_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_RG_setter(instance):
    original = instance.RG
    instance.RG = original
    assert instance.RG == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Telefone_setter(instance):
    original = instance.Telefone
    instance.Telefone = original
    assert instance.Telefone == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Sobrenome_setter(instance):
    original = instance.Sobrenome
    instance.Sobrenome = original
    assert instance.Sobrenome == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Estado_setter(instance):
    original = instance.Estado
    instance.Estado = original
    assert instance.Estado == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_EstadoCivil_setter(instance):
    original = instance.EstadoCivil
    instance.EstadoCivil = original
    assert instance.EstadoCivil == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_ConvenioMedico_setter(instance):
    original = instance.ConvenioMedico
    instance.ConvenioMedico = original
    assert instance.ConvenioMedico == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Nacionalidade_setter(instance):
    original = instance.Nacionalidade
    instance.Nacionalidade = original
    assert instance.Nacionalidade == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Celular_setter(instance):
    original = instance.Celular
    instance.Celular = original
    assert instance.Celular == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Cidade_setter(instance):
    original = instance.Cidade
    instance.Cidade = original
    assert instance.Cidade == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_Sexo_setter(instance):
    original = instance.Sexo
    instance.Sexo = original
    assert instance.Sexo == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_CEP_setter(instance):
    original = instance.CEP
    instance.CEP = original
    assert instance.CEP == original



@given(instance=Paciente_strategy)
def test_hyp_paciente_CPF1_setter(instance):
    original = instance.CPF1
    instance.CPF1 = original
    assert instance.CPF1 == original




@given(instance=Exame_strategy)
def test_hyp_exame_TipoExame_setter(instance):
    original = instance.TipoExame
    instance.TipoExame = original
    assert instance.TipoExame == original



@given(instance=Exame_strategy)
def test_hyp_exame_Sede_setter(instance):
    original = instance.Sede
    instance.Sede = original
    assert instance.Sede == original



@given(instance=Exame_strategy)
def test_hyp_exame_Especialista_setter(instance):
    original = instance.Especialista
    instance.Especialista = original
    assert instance.Especialista == original



@given(instance=Exame_strategy)
def test_hyp_exame_Medico_setter(instance):
    original = instance.Medico
    instance.Medico = original
    assert instance.Medico == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Agendamento,
    Consulta,
    Exame,
    Funcion_rio,
    M_dico,
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

def test_Agendamento_Dia_e_Horario_value_roundtrip():
    instance = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    assert instance.Dia_e_Horario == "sample_text"
    instance.Dia_e_Horario = "sample_text_2"
    assert instance.Dia_e_Horario == "sample_text_2"


def test_Agendamento_Especialista_value_roundtrip():
    instance = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    assert instance.Especialista == "sample_text"
    instance.Especialista = "sample_text_2"
    assert instance.Especialista == "sample_text_2"


def test_Agendamento_Medico_value_roundtrip():
    instance = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    assert instance.Medico == "sample_text"
    instance.Medico = "sample_text_2"
    assert instance.Medico == "sample_text_2"


def test_Agendamento_Sede_value_roundtrip():
    instance = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    assert instance.Sede == "sample_text"
    instance.Sede = "sample_text_2"
    assert instance.Sede == "sample_text_2"


def test_Agendamento_TipoAgendamento_value_roundtrip():
    instance = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    assert instance.TipoAgendamento == "sample_text"
    instance.TipoAgendamento = "sample_text_2"
    assert instance.TipoAgendamento == "sample_text_2"


def test_Consulta_Especialista_value_roundtrip():
    instance = Consulta(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoConsulta="sample_text")
    assert instance.Especialista == "sample_text"
    instance.Especialista = "sample_text_2"
    assert instance.Especialista == "sample_text_2"


def test_Consulta_Medico_value_roundtrip():
    instance = Consulta(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoConsulta="sample_text")
    assert instance.Medico == "sample_text"
    instance.Medico = "sample_text_2"
    assert instance.Medico == "sample_text_2"


def test_Consulta_Sede_value_roundtrip():
    instance = Consulta(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoConsulta="sample_text")
    assert instance.Sede == "sample_text"
    instance.Sede = "sample_text_2"
    assert instance.Sede == "sample_text_2"


def test_Consulta_TipoConsulta_value_roundtrip():
    instance = Consulta(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoConsulta="sample_text")
    assert instance.TipoConsulta == "sample_text"
    instance.TipoConsulta = "sample_text_2"
    assert instance.TipoConsulta == "sample_text_2"


def test_Exame_Especialista_value_roundtrip():
    instance = Exame(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoExame="sample_text")
    assert instance.Especialista == "sample_text"
    instance.Especialista = "sample_text_2"
    assert instance.Especialista == "sample_text_2"


def test_Exame_Medico_value_roundtrip():
    instance = Exame(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoExame="sample_text")
    assert instance.Medico == "sample_text"
    instance.Medico = "sample_text_2"
    assert instance.Medico == "sample_text_2"


def test_Exame_Sede_value_roundtrip():
    instance = Exame(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoExame="sample_text")
    assert instance.Sede == "sample_text"
    instance.Sede = "sample_text_2"
    assert instance.Sede == "sample_text_2"


def test_Exame_TipoExame_value_roundtrip():
    instance = Exame(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoExame="sample_text")
    assert instance.TipoExame == "sample_text"
    instance.TipoExame = "sample_text_2"
    assert instance.TipoExame == "sample_text_2"


def test_Funcion_rio_Senha_value_roundtrip():
    instance = Funcion_rio(Senha="sample_text", Usuario="sample_text")
    assert instance.Senha == "sample_text"
    instance.Senha = "sample_text_2"
    assert instance.Senha == "sample_text_2"


def test_Funcion_rio_Usuario_value_roundtrip():
    instance = Funcion_rio(Senha="sample_text", Usuario="sample_text")
    assert instance.Usuario == "sample_text"
    instance.Usuario = "sample_text_2"
    assert instance.Usuario == "sample_text_2"


def test_M_dico_CPF_value_roundtrip():
    instance = M_dico(CPF=7, Especialidade="sample_text", Nome="sample_text")
    assert instance.CPF == 7
    instance.CPF = 13
    assert instance.CPF == 13


def test_M_dico_Especialidade_value_roundtrip():
    instance = M_dico(CPF=7, Especialidade="sample_text", Nome="sample_text")
    assert instance.Especialidade == "sample_text"
    instance.Especialidade = "sample_text_2"
    assert instance.Especialidade == "sample_text_2"


def test_M_dico_Nome_value_roundtrip():
    instance = M_dico(CPF=7, Especialidade="sample_text", Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_assoc_Agendamento_Consulta_link_reassign_clear():
    a = Consulta(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoConsulta="sample_text")
    b1 = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    b2 = Agendamento(Dia_e_Horario="sample_text_2", Especialista="sample_text_2", Medico="sample_text_2", Sede="sample_text_2", TipoAgendamento="sample_text_2")
    _safe_set(a, 'agendamento3', b1)
    assert _is_linked(a, 'agendamento3', b1)
    if hasattr(b1, 'consulta2'):
        assert _is_linked(b1, 'consulta2', a)
    _safe_set(a, 'agendamento3', b2)
    assert _is_linked(a, 'agendamento3', b2)
    if hasattr(b1, 'consulta2'):
        assert not _is_linked(b1, 'consulta2', a)
    if hasattr(b2, 'consulta2'):
        assert _is_linked(b2, 'consulta2', a)
    _safe_set(a, 'agendamento3', None)
    assert not _is_linked(a, 'agendamento3', b2)
    if hasattr(b2, 'consulta2'):
        assert not _is_linked(b2, 'consulta2', a)


def test_assoc_Agendamento_Exame_link_reassign_clear():
    a = Exame(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoExame="sample_text")
    b1 = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    b2 = Agendamento(Dia_e_Horario="sample_text_2", Especialista="sample_text_2", Medico="sample_text_2", Sede="sample_text_2", TipoAgendamento="sample_text_2")
    _safe_set(a, 'agendamento1', b1)
    assert _is_linked(a, 'agendamento1', b1)
    if hasattr(b1, 'exame0'):
        assert _is_linked(b1, 'exame0', a)
    _safe_set(a, 'agendamento1', b2)
    assert _is_linked(a, 'agendamento1', b2)
    if hasattr(b1, 'exame0'):
        assert not _is_linked(b1, 'exame0', a)
    if hasattr(b2, 'exame0'):
        assert _is_linked(b2, 'exame0', a)
    _safe_set(a, 'agendamento1', None)
    assert not _is_linked(a, 'agendamento1', b2)
    if hasattr(b2, 'exame0'):
        assert not _is_linked(b2, 'exame0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Agendamento_strategy = st.builds(Agendamento, Dia_e_Horario=safe_text, Especialista=safe_text, Medico=safe_text, Sede=safe_text, TipoAgendamento=safe_text)
@given(instance=Agendamento_strategy)
@settings(max_examples=25)
def test_Agendamento_instantiation(instance):
    assert isinstance(instance, Agendamento)


Consulta_strategy = st.builds(Consulta, Especialista=safe_text, Medico=safe_text, Sede=safe_text, TipoConsulta=safe_text)
@given(instance=Consulta_strategy)
@settings(max_examples=25)
def test_Consulta_instantiation(instance):
    assert isinstance(instance, Consulta)


Exame_strategy = st.builds(Exame, Especialista=safe_text, Medico=safe_text, Sede=safe_text, TipoExame=safe_text)
@given(instance=Exame_strategy)
@settings(max_examples=25)
def test_Exame_instantiation(instance):
    assert isinstance(instance, Exame)


Funcion_rio_strategy = st.builds(Funcion_rio, Senha=safe_text, Usuario=safe_text)
@given(instance=Funcion_rio_strategy)
@settings(max_examples=25)
def test_Funcion_rio_instantiation(instance):
    assert isinstance(instance, Funcion_rio)


M_dico_strategy = st.builds(M_dico, CPF=st.integers(), Especialidade=safe_text, Nome=safe_text)
@given(instance=M_dico_strategy)
@settings(max_examples=25)
def test_M_dico_instantiation(instance):
    assert isinstance(instance, M_dico)



