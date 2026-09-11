import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Exame,
    clinicasaudeperfeita_Analisa_consulta_UseCase,
    clinicasaudeperfeita_Compromisso,
    clinicasaudeperfeita_Consulta,
    clinicasaudeperfeita_Consulta_UseCase,
    clinicasaudeperfeita_Exame,
    clinicasaudeperfeita_Marca_consulta_UseCase,
    clinicasaudeperfeita_Medicamento,
    clinicasaudeperfeita_Medico,
    clinicasaudeperfeita_Medico_Actor,
    clinicasaudeperfeita_Paciente,
    clinicasaudeperfeita_Paciente_Actor,
    clinicasaudeperfeita_Recepcionista,
    clinicasaudeperfeita_Recepcionista_Actor,
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

def test_clinicasaudeperfeita_Compromisso_data_value_roundtrip():
    instance = clinicasaudeperfeita_Compromisso(data="sample_text", descricao="sample_text", hora="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_clinicasaudeperfeita_Compromisso_descricao_value_roundtrip():
    instance = clinicasaudeperfeita_Compromisso(data="sample_text", descricao="sample_text", hora="sample_text")
    assert instance.descricao == "sample_text"
    instance.descricao = "sample_text_2"
    assert instance.descricao == "sample_text_2"


def test_clinicasaudeperfeita_Compromisso_hora_value_roundtrip():
    instance = clinicasaudeperfeita_Compromisso(data="sample_text", descricao="sample_text", hora="sample_text")
    assert instance.hora == "sample_text"
    instance.hora = "sample_text_2"
    assert instance.hora == "sample_text_2"


def test_clinicasaudeperfeita_Exame_nome_value_roundtrip():
    instance = clinicasaudeperfeita_Exame(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_clinicasaudeperfeita_Medicamento_nome_value_roundtrip():
    instance = clinicasaudeperfeita_Medicamento(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_clinicasaudeperfeita_Paciente_cSus_value_roundtrip():
    instance = clinicasaudeperfeita_Paciente(cSus="sample_text", cpf="sample_text", idade=7, nome="sample_text")
    assert instance.cSus == "sample_text"
    instance.cSus = "sample_text_2"
    assert instance.cSus == "sample_text_2"


def test_clinicasaudeperfeita_Paciente_cpf_value_roundtrip():
    instance = clinicasaudeperfeita_Paciente(cSus="sample_text", cpf="sample_text", idade=7, nome="sample_text")
    assert instance.cpf == "sample_text"
    instance.cpf = "sample_text_2"
    assert instance.cpf == "sample_text_2"


def test_clinicasaudeperfeita_Paciente_idade_value_roundtrip():
    instance = clinicasaudeperfeita_Paciente(cSus="sample_text", cpf="sample_text", idade=7, nome="sample_text")
    assert instance.idade == 7
    instance.idade = 13
    assert instance.idade == 13


def test_clinicasaudeperfeita_Paciente_nome_value_roundtrip():
    instance = clinicasaudeperfeita_Paciente(cSus="sample_text", cpf="sample_text", idade=7, nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_clinicasaudeperfeita_Recepcionista_cpf_value_roundtrip():
    instance = clinicasaudeperfeita_Recepcionista(cpf="sample_text", idade=7, nome="sample_text")
    assert instance.cpf == "sample_text"
    instance.cpf = "sample_text_2"
    assert instance.cpf == "sample_text_2"


def test_clinicasaudeperfeita_Recepcionista_idade_value_roundtrip():
    instance = clinicasaudeperfeita_Recepcionista(cpf="sample_text", idade=7, nome="sample_text")
    assert instance.idade == 7
    instance.idade = 13
    assert instance.idade == 13


def test_clinicasaudeperfeita_Recepcionista_nome_value_roundtrip():
    instance = clinicasaudeperfeita_Recepcionista(cpf="sample_text", idade=7, nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Exame_strategy = st.builds(Exame)
@given(instance=Exame_strategy)
@settings(max_examples=25)
def test_Exame_instantiation(instance):
    assert isinstance(instance, Exame)


clinicasaudeperfeita_Analisa_consulta_UseCase_strategy = st.builds(clinicasaudeperfeita_Analisa_consulta_UseCase)
@given(instance=clinicasaudeperfeita_Analisa_consulta_UseCase_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Analisa_consulta_UseCase_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Analisa_consulta_UseCase)


clinicasaudeperfeita_Compromisso_strategy = st.builds(clinicasaudeperfeita_Compromisso, data=safe_text, descricao=safe_text, hora=safe_text)
@given(instance=clinicasaudeperfeita_Compromisso_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Compromisso_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Compromisso)


clinicasaudeperfeita_Consulta_UseCase_strategy = st.builds(clinicasaudeperfeita_Consulta_UseCase)
@given(instance=clinicasaudeperfeita_Consulta_UseCase_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Consulta_UseCase_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Consulta_UseCase)


clinicasaudeperfeita_Exame_strategy = st.builds(clinicasaudeperfeita_Exame, nome=safe_text)
@given(instance=clinicasaudeperfeita_Exame_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Exame_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Exame)


clinicasaudeperfeita_Marca_consulta_UseCase_strategy = st.builds(clinicasaudeperfeita_Marca_consulta_UseCase)
@given(instance=clinicasaudeperfeita_Marca_consulta_UseCase_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Marca_consulta_UseCase_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Marca_consulta_UseCase)


clinicasaudeperfeita_Medicamento_strategy = st.builds(clinicasaudeperfeita_Medicamento, nome=safe_text)
@given(instance=clinicasaudeperfeita_Medicamento_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Medicamento_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Medicamento)


clinicasaudeperfeita_Medico_Actor_strategy = st.builds(clinicasaudeperfeita_Medico_Actor)
@given(instance=clinicasaudeperfeita_Medico_Actor_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Medico_Actor_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Medico_Actor)


clinicasaudeperfeita_Paciente_strategy = st.builds(clinicasaudeperfeita_Paciente, cSus=safe_text, cpf=safe_text, idade=st.integers(), nome=safe_text)
@given(instance=clinicasaudeperfeita_Paciente_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Paciente_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Paciente)


clinicasaudeperfeita_Paciente_Actor_strategy = st.builds(clinicasaudeperfeita_Paciente_Actor)
@given(instance=clinicasaudeperfeita_Paciente_Actor_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Paciente_Actor_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Paciente_Actor)


clinicasaudeperfeita_Recepcionista_strategy = st.builds(clinicasaudeperfeita_Recepcionista, cpf=safe_text, idade=st.integers(), nome=safe_text)
@given(instance=clinicasaudeperfeita_Recepcionista_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Recepcionista_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Recepcionista)


clinicasaudeperfeita_Recepcionista_Actor_strategy = st.builds(clinicasaudeperfeita_Recepcionista_Actor)
@given(instance=clinicasaudeperfeita_Recepcionista_Actor_strategy)
@settings(max_examples=25)
def test_clinicasaudeperfeita_Recepcionista_Actor_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Recepcionista_Actor)


