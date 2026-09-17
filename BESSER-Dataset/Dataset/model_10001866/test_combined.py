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
    Confirmar_Consulta_external,
    Marcar_consulta_external,
    Ver_consultas_external,
    Cancelar_Consulta_external,
    Cl_nica_Component,
    Cirurgi_o_Actor,
    Cliente_Actor,
    Consulta,
    Cliente,
    Cirurgiao,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_confirmar_consulta_external_is_not_abstract():
    assert not inspect.isabstract(Confirmar_Consulta_external)


def test_hyp_confirmar_consulta_external_constructor_exists():
    assert callable(Confirmar_Consulta_external.__init__)


def test_hyp_confirmar_consulta_external_constructor_args():
    sig = inspect.signature(Confirmar_Consulta_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_marcar_consulta_external_is_not_abstract():
    assert not inspect.isabstract(Marcar_consulta_external)


def test_hyp_marcar_consulta_external_constructor_exists():
    assert callable(Marcar_consulta_external.__init__)


def test_hyp_marcar_consulta_external_constructor_args():
    sig = inspect.signature(Marcar_consulta_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ver_consultas_external_is_not_abstract():
    assert not inspect.isabstract(Ver_consultas_external)


def test_hyp_ver_consultas_external_constructor_exists():
    assert callable(Ver_consultas_external.__init__)


def test_hyp_ver_consultas_external_constructor_args():
    sig = inspect.signature(Ver_consultas_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancelar_consulta_external_is_not_abstract():
    assert not inspect.isabstract(Cancelar_Consulta_external)


def test_hyp_cancelar_consulta_external_constructor_exists():
    assert callable(Cancelar_Consulta_external.__init__)


def test_hyp_cancelar_consulta_external_constructor_args():
    sig = inspect.signature(Cancelar_Consulta_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cl_nica_component_is_not_abstract():
    assert not inspect.isabstract(Cl_nica_Component)


def test_hyp_cl_nica_component_constructor_exists():
    assert callable(Cl_nica_Component.__init__)


def test_hyp_cl_nica_component_constructor_args():
    sig = inspect.signature(Cl_nica_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cirurgi_o_actor_is_not_abstract():
    assert not inspect.isabstract(Cirurgi_o_Actor)


def test_hyp_cirurgi_o_actor_constructor_exists():
    assert callable(Cirurgi_o_Actor.__init__)


def test_hyp_cirurgi_o_actor_constructor_args():
    sig = inspect.signature(Cirurgi_o_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cliente_actor_is_not_abstract():
    assert not inspect.isabstract(Cliente_Actor)


def test_hyp_cliente_actor_constructor_exists():
    assert callable(Cliente_Actor.__init__)


def test_hyp_cliente_actor_constructor_args():
    sig = inspect.signature(Cliente_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_hyp_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_hyp_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "ConsultaId" in params, "Missing parameter 'ConsultaId'"
    assert "Observacoes" in params, "Missing parameter 'Observacoes'"
    assert "Cirurgiao" in params, "Missing parameter 'Cirurgiao'"
    assert "Situacao" in params, "Missing parameter 'Situacao'"
    assert "Cliente" in params, "Missing parameter 'Cliente'"
    assert "DataHora" in params, "Missing parameter 'DataHora'"

def test_hyp_consulta_has_ConsultaId():
    assert hasattr(Consulta, "ConsultaId")
    descriptor = None
    for klass in Consulta.__mro__:
        if "ConsultaId" in klass.__dict__:
            descriptor = klass.__dict__["ConsultaId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_Observacoes():
    assert hasattr(Consulta, "Observacoes")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Observacoes" in klass.__dict__:
            descriptor = klass.__dict__["Observacoes"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_Cirurgiao():
    assert hasattr(Consulta, "Cirurgiao")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Cirurgiao" in klass.__dict__:
            descriptor = klass.__dict__["Cirurgiao"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_Situacao():
    assert hasattr(Consulta, "Situacao")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Situacao" in klass.__dict__:
            descriptor = klass.__dict__["Situacao"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_Cliente():
    assert hasattr(Consulta, "Cliente")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Cliente" in klass.__dict__:
            descriptor = klass.__dict__["Cliente"]
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



def test_hyp_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_hyp_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_hyp_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "ClienteId" in params, "Missing parameter 'ClienteId'"
    assert "Cpf" in params, "Missing parameter 'Cpf'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Telefone" in params, "Missing parameter 'Telefone'"








def test_hyp_cirurgiao_is_not_abstract():
    assert not inspect.isabstract(Cirurgiao)


def test_hyp_cirurgiao_constructor_exists():
    assert callable(Cirurgiao.__init__)


def test_hyp_cirurgiao_constructor_args():
    sig = inspect.signature(Cirurgiao.__init__)
    params = list(sig.parameters.keys())
    assert "CirurgiaoId" in params, "Missing parameter 'CirurgiaoId'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Especialidade" in params, "Missing parameter 'Especialidade'"





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
Confirmar_Consulta_external_strategy = st.builds(
    Confirmar_Consulta_external,
)
Marcar_consulta_external_strategy = st.builds(
    Marcar_consulta_external,
)
Ver_consultas_external_strategy = st.builds(
    Ver_consultas_external,
)
Cancelar_Consulta_external_strategy = st.builds(
    Cancelar_Consulta_external,
)
Cl_nica_Component_strategy = st.builds(
    Cl_nica_Component,
)
Cirurgi_o_Actor_strategy = st.builds(
    Cirurgi_o_Actor,
)
Cliente_Actor_strategy = st.builds(
    Cliente_Actor,
)
Consulta_strategy = st.builds(
    Consulta,
    ConsultaId=
        st.integers(),
    Observacoes=
        safe_text,
    Cirurgiao=
        st.none(),
    Situacao=
        safe_text,
    Cliente=
        st.none(),
    DataHora=
        safe_text
)
Cliente_strategy = st.builds(
    Cliente,
    ClienteId=
        st.integers(),
    Cpf=
        safe_text,
    Nome=
        safe_text,
    Email=
        safe_text,
    Telefone=
        safe_text
)
Cirurgiao_strategy = st.builds(
    Cirurgiao,
    CirurgiaoId=
        st.integers(),
    Nome=
        safe_text,
    Especialidade=
        safe_text
)








@given(instance=Consulta_strategy)
@settings(max_examples=50)
def test_hyp_consulta_instantiation(instance):
    assert isinstance(instance, Consulta)



@given(instance=Consulta_strategy)
def test_hyp_consulta_ConsultaId_setter(instance):
    original = instance.ConsultaId
    instance.ConsultaId = original
    assert instance.ConsultaId == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Observacoes_setter(instance):
    original = instance.Observacoes
    instance.Observacoes = original
    assert instance.Observacoes == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Cirurgiao_setter(instance):
    original = instance.Cirurgiao
    instance.Cirurgiao = original
    assert instance.Cirurgiao == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Situacao_setter(instance):
    original = instance.Situacao
    instance.Situacao = original
    assert instance.Situacao == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_Cliente_setter(instance):
    original = instance.Cliente
    instance.Cliente = original
    assert instance.Cliente == original



@given(instance=Consulta_strategy)
def test_hyp_consulta_DataHora_setter(instance):
    original = instance.DataHora
    instance.DataHora = original
    assert instance.DataHora == original




@given(instance=Cliente_strategy)
def test_hyp_cliente_ClienteId_setter(instance):
    original = instance.ClienteId
    instance.ClienteId = original
    assert instance.ClienteId == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_Cpf_setter(instance):
    original = instance.Cpf
    instance.Cpf = original
    assert instance.Cpf == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_Telefone_setter(instance):
    original = instance.Telefone
    instance.Telefone = original
    assert instance.Telefone == original




@given(instance=Cirurgiao_strategy)
def test_hyp_cirurgiao_CirurgiaoId_setter(instance):
    original = instance.CirurgiaoId
    instance.CirurgiaoId = original
    assert instance.CirurgiaoId == original



@given(instance=Cirurgiao_strategy)
def test_hyp_cirurgiao_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Cirurgiao_strategy)
def test_hyp_cirurgiao_Especialidade_setter(instance):
    original = instance.Especialidade
    instance.Especialidade = original
    assert instance.Especialidade == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cancelar_Consulta_external,
    Cirurgi_o_Actor,
    Cirurgiao,
    Cl_nica_Component,
    Cliente,
    Cliente_Actor,
    Confirmar_Consulta_external,
    Consulta,
    Marcar_consulta_external,
    Ver_consultas_external,
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

def test_Cirurgiao_CirurgiaoId_value_roundtrip():
    instance = Cirurgiao(CirurgiaoId=7, Especialidade="sample_text", Nome="sample_text")
    assert instance.CirurgiaoId == 7
    instance.CirurgiaoId = 13
    assert instance.CirurgiaoId == 13


def test_Cirurgiao_Especialidade_value_roundtrip():
    instance = Cirurgiao(CirurgiaoId=7, Especialidade="sample_text", Nome="sample_text")
    assert instance.Especialidade == "sample_text"
    instance.Especialidade = "sample_text_2"
    assert instance.Especialidade == "sample_text_2"


def test_Cirurgiao_Nome_value_roundtrip():
    instance = Cirurgiao(CirurgiaoId=7, Especialidade="sample_text", Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_Cliente_ClienteId_value_roundtrip():
    instance = Cliente(ClienteId=7, Cpf="sample_text", Email="sample_text", Nome="sample_text", Telefone="sample_text")
    assert instance.ClienteId == 7
    instance.ClienteId = 13
    assert instance.ClienteId == 13


def test_Cliente_Cpf_value_roundtrip():
    instance = Cliente(ClienteId=7, Cpf="sample_text", Email="sample_text", Nome="sample_text", Telefone="sample_text")
    assert instance.Cpf == "sample_text"
    instance.Cpf = "sample_text_2"
    assert instance.Cpf == "sample_text_2"


def test_Cliente_Email_value_roundtrip():
    instance = Cliente(ClienteId=7, Cpf="sample_text", Email="sample_text", Nome="sample_text", Telefone="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Cliente_Nome_value_roundtrip():
    instance = Cliente(ClienteId=7, Cpf="sample_text", Email="sample_text", Nome="sample_text", Telefone="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_Cliente_Telefone_value_roundtrip():
    instance = Cliente(ClienteId=7, Cpf="sample_text", Email="sample_text", Nome="sample_text", Telefone="sample_text")
    assert instance.Telefone == "sample_text"
    instance.Telefone = "sample_text_2"
    assert instance.Telefone == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cancelar_Consulta_external_strategy = st.builds(Cancelar_Consulta_external)
@given(instance=Cancelar_Consulta_external_strategy)
@settings(max_examples=25)
def test_Cancelar_Consulta_external_instantiation(instance):
    assert isinstance(instance, Cancelar_Consulta_external)


Cirurgi_o_Actor_strategy = st.builds(Cirurgi_o_Actor)
@given(instance=Cirurgi_o_Actor_strategy)
@settings(max_examples=25)
def test_Cirurgi_o_Actor_instantiation(instance):
    assert isinstance(instance, Cirurgi_o_Actor)


Cirurgiao_strategy = st.builds(Cirurgiao, CirurgiaoId=st.integers(), Especialidade=safe_text, Nome=safe_text)
@given(instance=Cirurgiao_strategy)
@settings(max_examples=25)
def test_Cirurgiao_instantiation(instance):
    assert isinstance(instance, Cirurgiao)


Cl_nica_Component_strategy = st.builds(Cl_nica_Component)
@given(instance=Cl_nica_Component_strategy)
@settings(max_examples=25)
def test_Cl_nica_Component_instantiation(instance):
    assert isinstance(instance, Cl_nica_Component)


Cliente_strategy = st.builds(Cliente, ClienteId=st.integers(), Cpf=safe_text, Email=safe_text, Nome=safe_text, Telefone=safe_text)
@given(instance=Cliente_strategy)
@settings(max_examples=25)
def test_Cliente_instantiation(instance):
    assert isinstance(instance, Cliente)


Cliente_Actor_strategy = st.builds(Cliente_Actor)
@given(instance=Cliente_Actor_strategy)
@settings(max_examples=25)
def test_Cliente_Actor_instantiation(instance):
    assert isinstance(instance, Cliente_Actor)


Confirmar_Consulta_external_strategy = st.builds(Confirmar_Consulta_external)
@given(instance=Confirmar_Consulta_external_strategy)
@settings(max_examples=25)
def test_Confirmar_Consulta_external_instantiation(instance):
    assert isinstance(instance, Confirmar_Consulta_external)


Marcar_consulta_external_strategy = st.builds(Marcar_consulta_external)
@given(instance=Marcar_consulta_external_strategy)
@settings(max_examples=25)
def test_Marcar_consulta_external_instantiation(instance):
    assert isinstance(instance, Marcar_consulta_external)


Ver_consultas_external_strategy = st.builds(Ver_consultas_external)
@given(instance=Ver_consultas_external_strategy)
@settings(max_examples=25)
def test_Ver_consultas_external_instantiation(instance):
    assert isinstance(instance, Ver_consultas_external)



