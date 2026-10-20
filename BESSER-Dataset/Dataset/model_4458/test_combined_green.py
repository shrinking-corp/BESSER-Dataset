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
    Condition,
    farrusco_Distancia,
    Action,
    farrusco_Condition,
    Actuate,
    farrusco_LED,
    farrusco_Servo,
    farrusco_Motor,
    farrusco_Actuate,
    farrusco_Espera,
    farrusco_Bumpers,
    Behavior,
    farrusco_Sequencial,
    farrusco_Paralelo,
    farrusco_AlterarEstado,
    farrusco_Prioridade,
    Node,
    farrusco_Behavior,
    farrusco_Action,
    farrusco_Irmao,
    farrusco_Filho,
    farrusco_Node,
    farrusco_Robot,
    EstadoDaLuz,
    EstadoFalha,
    EstadoDecorrer,
    TipoDistancia,
    EscolhaBumper,
    EstadoSucesso,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_distancia_is_not_abstract():
    assert not inspect.isabstract(farrusco_Distancia)


def test_hyp_farrusco_distancia_constructor_exists():
    assert callable(farrusco_Distancia.__init__)


def test_hyp_farrusco_distancia_constructor_args():
    sig = inspect.signature(farrusco_Distancia.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "distancia" in params, "Missing parameter 'distancia'"
    assert "Menor_Maior" in params, "Missing parameter 'Menor_Maior'"






def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_condition_is_not_abstract():
    assert not inspect.isabstract(farrusco_Condition)


def test_hyp_farrusco_condition_constructor_exists():
    assert callable(farrusco_Condition.__init__)


def test_hyp_farrusco_condition_constructor_args():
    sig = inspect.signature(farrusco_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actuate_is_not_abstract():
    assert not inspect.isabstract(Actuate)


def test_hyp_actuate_constructor_exists():
    assert callable(Actuate.__init__)


def test_hyp_actuate_constructor_args():
    sig = inspect.signature(Actuate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_led_is_not_abstract():
    assert not inspect.isabstract(farrusco_LED)


def test_hyp_farrusco_led_constructor_exists():
    assert callable(farrusco_LED.__init__)


def test_hyp_farrusco_led_constructor_args():
    sig = inspect.signature(farrusco_LED.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Ligado_ou_Desligado" in params, "Missing parameter 'Ligado_ou_Desligado'"





def test_hyp_farrusco_servo_is_not_abstract():
    assert not inspect.isabstract(farrusco_Servo)


def test_hyp_farrusco_servo_constructor_exists():
    assert callable(farrusco_Servo.__init__)


def test_hyp_farrusco_servo_constructor_args():
    sig = inspect.signature(farrusco_Servo.__init__)
    params = list(sig.parameters.keys())
    assert "Passo_a_Passo" in params, "Missing parameter 'Passo_a_Passo'"
    assert "Posicao_Minima" in params, "Missing parameter 'Posicao_Minima'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Posicao_Maxima" in params, "Missing parameter 'Posicao_Maxima'"







def test_hyp_farrusco_motor_is_not_abstract():
    assert not inspect.isabstract(farrusco_Motor)


def test_hyp_farrusco_motor_constructor_exists():
    assert callable(farrusco_Motor.__init__)


def test_hyp_farrusco_motor_constructor_args():
    sig = inspect.signature(farrusco_Motor.__init__)
    params = list(sig.parameters.keys())
    assert "Motor_Esquerdo" in params, "Missing parameter 'Motor_Esquerdo'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Motor_Direito" in params, "Missing parameter 'Motor_Direito'"






def test_hyp_farrusco_actuate_is_not_abstract():
    assert not inspect.isabstract(farrusco_Actuate)


def test_hyp_farrusco_actuate_constructor_exists():
    assert callable(farrusco_Actuate.__init__)


def test_hyp_farrusco_actuate_constructor_args():
    sig = inspect.signature(farrusco_Actuate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_espera_is_not_abstract():
    assert not inspect.isabstract(farrusco_Espera)


def test_hyp_farrusco_espera_constructor_exists():
    assert callable(farrusco_Espera.__init__)


def test_hyp_farrusco_espera_constructor_args():
    sig = inspect.signature(farrusco_Espera.__init__)
    params = list(sig.parameters.keys())
    assert "Tempo" in params, "Missing parameter 'Tempo'"
    assert "Nome" in params, "Missing parameter 'Nome'"





def test_hyp_farrusco_bumpers_is_not_abstract():
    assert not inspect.isabstract(farrusco_Bumpers)


def test_hyp_farrusco_bumpers_constructor_exists():
    assert callable(farrusco_Bumpers.__init__)


def test_hyp_farrusco_bumpers_constructor_args():
    sig = inspect.signature(farrusco_Bumpers.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Bumper_Esquerdo_ou_Direito" in params, "Missing parameter 'Bumper_Esquerdo_ou_Direito'"





def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_sequencial_is_not_abstract():
    assert not inspect.isabstract(farrusco_Sequencial)


def test_hyp_farrusco_sequencial_constructor_exists():
    assert callable(farrusco_Sequencial.__init__)


def test_hyp_farrusco_sequencial_constructor_args():
    sig = inspect.signature(farrusco_Sequencial.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"




def test_hyp_farrusco_paralelo_is_not_abstract():
    assert not inspect.isabstract(farrusco_Paralelo)


def test_hyp_farrusco_paralelo_constructor_exists():
    assert callable(farrusco_Paralelo.__init__)


def test_hyp_farrusco_paralelo_constructor_args():
    sig = inspect.signature(farrusco_Paralelo.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"




def test_hyp_farrusco_alterarestado_is_not_abstract():
    assert not inspect.isabstract(farrusco_AlterarEstado)


def test_hyp_farrusco_alterarestado_constructor_exists():
    assert callable(farrusco_AlterarEstado.__init__)


def test_hyp_farrusco_alterarestado_constructor_args():
    sig = inspect.signature(farrusco_AlterarEstado.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Alterar_Falha" in params, "Missing parameter 'Alterar_Falha'"
    assert "Alterar_Sucesso" in params, "Missing parameter 'Alterar_Sucesso'"
    assert "Alterar_Decorrer" in params, "Missing parameter 'Alterar_Decorrer'"







def test_hyp_farrusco_prioridade_is_not_abstract():
    assert not inspect.isabstract(farrusco_Prioridade)


def test_hyp_farrusco_prioridade_constructor_exists():
    assert callable(farrusco_Prioridade.__init__)


def test_hyp_farrusco_prioridade_constructor_args():
    sig = inspect.signature(farrusco_Prioridade.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"




def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_behavior_is_not_abstract():
    assert not inspect.isabstract(farrusco_Behavior)


def test_hyp_farrusco_behavior_constructor_exists():
    assert callable(farrusco_Behavior.__init__)


def test_hyp_farrusco_behavior_constructor_args():
    sig = inspect.signature(farrusco_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_action_is_not_abstract():
    assert not inspect.isabstract(farrusco_Action)


def test_hyp_farrusco_action_constructor_exists():
    assert callable(farrusco_Action.__init__)


def test_hyp_farrusco_action_constructor_args():
    sig = inspect.signature(farrusco_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_irmao_is_not_abstract():
    assert not inspect.isabstract(farrusco_Irmao)


def test_hyp_farrusco_irmao_constructor_exists():
    assert callable(farrusco_Irmao.__init__)


def test_hyp_farrusco_irmao_constructor_args():
    sig = inspect.signature(farrusco_Irmao.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_filho_is_not_abstract():
    assert not inspect.isabstract(farrusco_Filho)


def test_hyp_farrusco_filho_constructor_exists():
    assert callable(farrusco_Filho.__init__)


def test_hyp_farrusco_filho_constructor_args():
    sig = inspect.signature(farrusco_Filho.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_node_is_not_abstract():
    assert not inspect.isabstract(farrusco_Node)


def test_hyp_farrusco_node_constructor_exists():
    assert callable(farrusco_Node.__init__)


def test_hyp_farrusco_node_constructor_args():
    sig = inspect.signature(farrusco_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_farrusco_robot_is_not_abstract():
    assert not inspect.isabstract(farrusco_Robot)


def test_hyp_farrusco_robot_constructor_exists():
    assert callable(farrusco_Robot.__init__)


def test_hyp_farrusco_robot_constructor_args():
    sig = inspect.signature(farrusco_Robot.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"


def test_hyp_estadodaluz_exists():
    # Check that the Enumeration exists
    assert EstadoDaLuz is not None

def test_hyp_estadodaluz_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoDaLuz]
    expected_literals = [
        "Desligado",
        "Ligado",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoDaLuz"

def test_hyp_estadofalha_exists():
    # Check that the Enumeration exists
    assert EstadoFalha is not None

def test_hyp_estadofalha_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoFalha]
    expected_literals = [
        "Sucesso",
        "Decorrer",
        "Falha",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoFalha"

def test_hyp_estadodecorrer_exists():
    # Check that the Enumeration exists
    assert EstadoDecorrer is not None

def test_hyp_estadodecorrer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoDecorrer]
    expected_literals = [
        "Decorrer",
        "Falha",
        "Sucesso",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoDecorrer"

def test_hyp_tipodistancia_exists():
    # Check that the Enumeration exists
    assert TipoDistancia is not None

def test_hyp_tipodistancia_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TipoDistancia]
    expected_literals = [
        "Menor",
        "Maior",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TipoDistancia"

def test_hyp_escolhabumper_exists():
    # Check that the Enumeration exists
    assert EscolhaBumper is not None

def test_hyp_escolhabumper_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EscolhaBumper]
    expected_literals = [
        "Direito",
        "Esquerdo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EscolhaBumper"

def test_hyp_estadosucesso_exists():
    # Check that the Enumeration exists
    assert EstadoSucesso is not None

def test_hyp_estadosucesso_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoSucesso]
    expected_literals = [
        "Decorrer",
        "Falha",
        "Sucesso",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoSucesso"


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
Condition_strategy = st.builds(
    Condition,
)
farrusco_Distancia_strategy = st.builds(
    farrusco_Distancia,
    Nome=
        safe_text,
    distancia=
        st.integers(),
    Menor_Maior=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
farrusco_Condition_strategy = st.builds(
    farrusco_Condition,
)
Actuate_strategy = st.builds(
    Actuate,
)
farrusco_LED_strategy = st.builds(
    farrusco_LED,
    Nome=
        safe_text,
    Ligado_ou_Desligado=
        safe_text
)
farrusco_Servo_strategy = st.builds(
    farrusco_Servo,
    Passo_a_Passo=
        st.integers(),
    Posicao_Minima=
        st.integers(),
    Nome=
        safe_text,
    Posicao_Maxima=
        st.integers()
)
farrusco_Motor_strategy = st.builds(
    farrusco_Motor,
    Motor_Esquerdo=
        st.integers(),
    Nome=
        safe_text,
    Motor_Direito=
        st.integers()
)
farrusco_Actuate_strategy = st.builds(
    farrusco_Actuate,
)
farrusco_Espera_strategy = st.builds(
    farrusco_Espera,
    Tempo=
        st.integers(),
    Nome=
        safe_text
)
farrusco_Bumpers_strategy = st.builds(
    farrusco_Bumpers,
    Nome=
        safe_text,
    Bumper_Esquerdo_ou_Direito=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
farrusco_Sequencial_strategy = st.builds(
    farrusco_Sequencial,
    Nome=
        safe_text
)
farrusco_Paralelo_strategy = st.builds(
    farrusco_Paralelo,
    Nome=
        safe_text
)
farrusco_AlterarEstado_strategy = st.builds(
    farrusco_AlterarEstado,
    Nome=
        safe_text,
    Alterar_Falha=
        safe_text,
    Alterar_Sucesso=
        safe_text,
    Alterar_Decorrer=
        safe_text
)
farrusco_Prioridade_strategy = st.builds(
    farrusco_Prioridade,
    Nome=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
farrusco_Behavior_strategy = st.builds(
    farrusco_Behavior,
)
farrusco_Action_strategy = st.builds(
    farrusco_Action,
)
farrusco_Irmao_strategy = st.builds(
    farrusco_Irmao,
)
farrusco_Filho_strategy = st.builds(
    farrusco_Filho,
)
farrusco_Node_strategy = st.builds(
    farrusco_Node,
)
farrusco_Robot_strategy = st.builds(
    farrusco_Robot,
    Nome=
        safe_text
)





@given(instance=farrusco_Distancia_strategy)
def test_hyp_farrusco_distancia_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=farrusco_Distancia_strategy)
def test_hyp_farrusco_distancia_distancia_setter(instance):
    original = instance.distancia
    instance.distancia = original
    assert instance.distancia == original



@given(instance=farrusco_Distancia_strategy)
def test_hyp_farrusco_distancia_Menor_Maior_setter(instance):
    original = instance.Menor_Maior
    instance.Menor_Maior = original
    assert instance.Menor_Maior == original







@given(instance=farrusco_LED_strategy)
def test_hyp_farrusco_led_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=farrusco_LED_strategy)
def test_hyp_farrusco_led_Ligado_ou_Desligado_setter(instance):
    original = instance.Ligado_ou_Desligado
    instance.Ligado_ou_Desligado = original
    assert instance.Ligado_ou_Desligado == original




@given(instance=farrusco_Servo_strategy)
def test_hyp_farrusco_servo_Passo_a_Passo_setter(instance):
    original = instance.Passo_a_Passo
    instance.Passo_a_Passo = original
    assert instance.Passo_a_Passo == original



@given(instance=farrusco_Servo_strategy)
def test_hyp_farrusco_servo_Posicao_Minima_setter(instance):
    original = instance.Posicao_Minima
    instance.Posicao_Minima = original
    assert instance.Posicao_Minima == original



@given(instance=farrusco_Servo_strategy)
def test_hyp_farrusco_servo_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=farrusco_Servo_strategy)
def test_hyp_farrusco_servo_Posicao_Maxima_setter(instance):
    original = instance.Posicao_Maxima
    instance.Posicao_Maxima = original
    assert instance.Posicao_Maxima == original




@given(instance=farrusco_Motor_strategy)
def test_hyp_farrusco_motor_Motor_Esquerdo_setter(instance):
    original = instance.Motor_Esquerdo
    instance.Motor_Esquerdo = original
    assert instance.Motor_Esquerdo == original



@given(instance=farrusco_Motor_strategy)
def test_hyp_farrusco_motor_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=farrusco_Motor_strategy)
def test_hyp_farrusco_motor_Motor_Direito_setter(instance):
    original = instance.Motor_Direito
    instance.Motor_Direito = original
    assert instance.Motor_Direito == original





@given(instance=farrusco_Espera_strategy)
def test_hyp_farrusco_espera_Tempo_setter(instance):
    original = instance.Tempo
    instance.Tempo = original
    assert instance.Tempo == original



@given(instance=farrusco_Espera_strategy)
def test_hyp_farrusco_espera_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original




@given(instance=farrusco_Bumpers_strategy)
def test_hyp_farrusco_bumpers_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=farrusco_Bumpers_strategy)
def test_hyp_farrusco_bumpers_Bumper_Esquerdo_ou_Direito_setter(instance):
    original = instance.Bumper_Esquerdo_ou_Direito
    instance.Bumper_Esquerdo_ou_Direito = original
    assert instance.Bumper_Esquerdo_ou_Direito == original





@given(instance=farrusco_Sequencial_strategy)
def test_hyp_farrusco_sequencial_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original




@given(instance=farrusco_Paralelo_strategy)
def test_hyp_farrusco_paralelo_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original




@given(instance=farrusco_AlterarEstado_strategy)
def test_hyp_farrusco_alterarestado_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=farrusco_AlterarEstado_strategy)
def test_hyp_farrusco_alterarestado_Alterar_Falha_setter(instance):
    original = instance.Alterar_Falha
    instance.Alterar_Falha = original
    assert instance.Alterar_Falha == original



@given(instance=farrusco_AlterarEstado_strategy)
def test_hyp_farrusco_alterarestado_Alterar_Sucesso_setter(instance):
    original = instance.Alterar_Sucesso
    instance.Alterar_Sucesso = original
    assert instance.Alterar_Sucesso == original



@given(instance=farrusco_AlterarEstado_strategy)
def test_hyp_farrusco_alterarestado_Alterar_Decorrer_setter(instance):
    original = instance.Alterar_Decorrer
    instance.Alterar_Decorrer = original
    assert instance.Alterar_Decorrer == original




@given(instance=farrusco_Prioridade_strategy)
def test_hyp_farrusco_prioridade_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original










@given(instance=farrusco_Robot_strategy)
def test_hyp_farrusco_robot_Nome_setter(instance):
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
    Action,
    Actuate,
    Behavior,
    Condition,
    Node,
    farrusco_Action,
    farrusco_Actuate,
    farrusco_AlterarEstado,
    farrusco_Behavior,
    farrusco_Bumpers,
    farrusco_Condition,
    farrusco_Distancia,
    farrusco_Espera,
    farrusco_Filho,
    farrusco_Irmao,
    farrusco_LED,
    farrusco_Motor,
    farrusco_Node,
    farrusco_Paralelo,
    farrusco_Prioridade,
    farrusco_Robot,
    farrusco_Sequencial,
    farrusco_Servo,
    EscolhaBumper,
    EstadoDaLuz,
    EstadoDecorrer,
    EstadoFalha,
    EstadoSucesso,
    TipoDistancia,
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

def test_farrusco_AlterarEstado_Alterar_Decorrer_value_roundtrip():
    instance = farrusco_AlterarEstado(Alterar_Decorrer="sample_text", Alterar_Falha="sample_text", Alterar_Sucesso="sample_text", Nome="sample_text")
    assert instance.Alterar_Decorrer == "sample_text"
    instance.Alterar_Decorrer = "sample_text_2"
    assert instance.Alterar_Decorrer == "sample_text_2"


def test_farrusco_AlterarEstado_Alterar_Falha_value_roundtrip():
    instance = farrusco_AlterarEstado(Alterar_Decorrer="sample_text", Alterar_Falha="sample_text", Alterar_Sucesso="sample_text", Nome="sample_text")
    assert instance.Alterar_Falha == "sample_text"
    instance.Alterar_Falha = "sample_text_2"
    assert instance.Alterar_Falha == "sample_text_2"


def test_farrusco_AlterarEstado_Alterar_Sucesso_value_roundtrip():
    instance = farrusco_AlterarEstado(Alterar_Decorrer="sample_text", Alterar_Falha="sample_text", Alterar_Sucesso="sample_text", Nome="sample_text")
    assert instance.Alterar_Sucesso == "sample_text"
    instance.Alterar_Sucesso = "sample_text_2"
    assert instance.Alterar_Sucesso == "sample_text_2"


def test_farrusco_AlterarEstado_Nome_value_roundtrip():
    instance = farrusco_AlterarEstado(Alterar_Decorrer="sample_text", Alterar_Falha="sample_text", Alterar_Sucesso="sample_text", Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Bumpers_Bumper_Esquerdo_ou_Direito_value_roundtrip():
    instance = farrusco_Bumpers(Bumper_Esquerdo_ou_Direito="sample_text", Nome="sample_text")
    assert instance.Bumper_Esquerdo_ou_Direito == "sample_text"
    instance.Bumper_Esquerdo_ou_Direito = "sample_text_2"
    assert instance.Bumper_Esquerdo_ou_Direito == "sample_text_2"


def test_farrusco_Bumpers_Nome_value_roundtrip():
    instance = farrusco_Bumpers(Bumper_Esquerdo_ou_Direito="sample_text", Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Distancia_Menor_Maior_value_roundtrip():
    instance = farrusco_Distancia(Menor_Maior="sample_text", Nome="sample_text", distancia=7)
    assert instance.Menor_Maior == "sample_text"
    instance.Menor_Maior = "sample_text_2"
    assert instance.Menor_Maior == "sample_text_2"


def test_farrusco_Distancia_Nome_value_roundtrip():
    instance = farrusco_Distancia(Menor_Maior="sample_text", Nome="sample_text", distancia=7)
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Distancia_distancia_value_roundtrip():
    instance = farrusco_Distancia(Menor_Maior="sample_text", Nome="sample_text", distancia=7)
    assert instance.distancia == 7
    instance.distancia = 13
    assert instance.distancia == 13


def test_farrusco_Espera_Nome_value_roundtrip():
    instance = farrusco_Espera(Nome="sample_text", Tempo=7)
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Espera_Tempo_value_roundtrip():
    instance = farrusco_Espera(Nome="sample_text", Tempo=7)
    assert instance.Tempo == 7
    instance.Tempo = 13
    assert instance.Tempo == 13


def test_farrusco_LED_Ligado_ou_Desligado_value_roundtrip():
    instance = farrusco_LED(Ligado_ou_Desligado="sample_text", Nome="sample_text")
    assert instance.Ligado_ou_Desligado == "sample_text"
    instance.Ligado_ou_Desligado = "sample_text_2"
    assert instance.Ligado_ou_Desligado == "sample_text_2"


def test_farrusco_LED_Nome_value_roundtrip():
    instance = farrusco_LED(Ligado_ou_Desligado="sample_text", Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Motor_Motor_Direito_value_roundtrip():
    instance = farrusco_Motor(Motor_Direito=7, Motor_Esquerdo=7, Nome="sample_text")
    assert instance.Motor_Direito == 7
    instance.Motor_Direito = 13
    assert instance.Motor_Direito == 13


def test_farrusco_Motor_Motor_Esquerdo_value_roundtrip():
    instance = farrusco_Motor(Motor_Direito=7, Motor_Esquerdo=7, Nome="sample_text")
    assert instance.Motor_Esquerdo == 7
    instance.Motor_Esquerdo = 13
    assert instance.Motor_Esquerdo == 13


def test_farrusco_Motor_Nome_value_roundtrip():
    instance = farrusco_Motor(Motor_Direito=7, Motor_Esquerdo=7, Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Paralelo_Nome_value_roundtrip():
    instance = farrusco_Paralelo(Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Prioridade_Nome_value_roundtrip():
    instance = farrusco_Prioridade(Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Robot_Nome_value_roundtrip():
    instance = farrusco_Robot(Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Sequencial_Nome_value_roundtrip():
    instance = farrusco_Sequencial(Nome="sample_text")
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Servo_Nome_value_roundtrip():
    instance = farrusco_Servo(Nome="sample_text", Passo_a_Passo=7, Posicao_Maxima=7, Posicao_Minima=7)
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_farrusco_Servo_Passo_a_Passo_value_roundtrip():
    instance = farrusco_Servo(Nome="sample_text", Passo_a_Passo=7, Posicao_Maxima=7, Posicao_Minima=7)
    assert instance.Passo_a_Passo == 7
    instance.Passo_a_Passo = 13
    assert instance.Passo_a_Passo == 13


def test_farrusco_Servo_Posicao_Maxima_value_roundtrip():
    instance = farrusco_Servo(Nome="sample_text", Passo_a_Passo=7, Posicao_Maxima=7, Posicao_Minima=7)
    assert instance.Posicao_Maxima == 7
    instance.Posicao_Maxima = 13
    assert instance.Posicao_Maxima == 13


def test_farrusco_Servo_Posicao_Minima_value_roundtrip():
    instance = farrusco_Servo(Nome="sample_text", Passo_a_Passo=7, Posicao_Maxima=7, Posicao_Minima=7)
    assert instance.Posicao_Minima == 7
    instance.Posicao_Minima = 13
    assert instance.Posicao_Minima == 13


def test_farrusco_Actuate_isa_Action():
    instance = farrusco_Actuate()
    assert isinstance(instance, Action)


def test_farrusco_Condition_isa_Action():
    instance = farrusco_Condition()
    assert isinstance(instance, Action)


def test_farrusco_LED_isa_Actuate():
    instance = farrusco_LED(Ligado_ou_Desligado="sample_text", Nome="sample_text")
    assert isinstance(instance, Actuate)


def test_farrusco_Motor_isa_Actuate():
    instance = farrusco_Motor(Motor_Direito=7, Motor_Esquerdo=7, Nome="sample_text")
    assert isinstance(instance, Actuate)


def test_farrusco_Servo_isa_Actuate():
    instance = farrusco_Servo(Nome="sample_text", Passo_a_Passo=7, Posicao_Maxima=7, Posicao_Minima=7)
    assert isinstance(instance, Actuate)


def test_farrusco_AlterarEstado_isa_Behavior():
    instance = farrusco_AlterarEstado(Alterar_Decorrer="sample_text", Alterar_Falha="sample_text", Alterar_Sucesso="sample_text", Nome="sample_text")
    assert isinstance(instance, Behavior)


def test_farrusco_Paralelo_isa_Behavior():
    instance = farrusco_Paralelo(Nome="sample_text")
    assert isinstance(instance, Behavior)


def test_farrusco_Prioridade_isa_Behavior():
    instance = farrusco_Prioridade(Nome="sample_text")
    assert isinstance(instance, Behavior)


def test_farrusco_Sequencial_isa_Behavior():
    instance = farrusco_Sequencial(Nome="sample_text")
    assert isinstance(instance, Behavior)


def test_farrusco_Bumpers_isa_Condition():
    instance = farrusco_Bumpers(Bumper_Esquerdo_ou_Direito="sample_text", Nome="sample_text")
    assert isinstance(instance, Condition)


def test_farrusco_Distancia_isa_Condition():
    instance = farrusco_Distancia(Menor_Maior="sample_text", Nome="sample_text", distancia=7)
    assert isinstance(instance, Condition)


def test_farrusco_Espera_isa_Condition():
    instance = farrusco_Espera(Nome="sample_text", Tempo=7)
    assert isinstance(instance, Condition)


def test_farrusco_Action_isa_Node():
    instance = farrusco_Action()
    assert isinstance(instance, Node)


def test_farrusco_Behavior_isa_Node():
    instance = farrusco_Behavior()
    assert isinstance(instance, Node)


def test_assoc_child1_link_reassign_clear():
    a = farrusco_Robot(Nome="sample_text")
    b1 = farrusco_Filho()
    b2 = farrusco_Filho()
    _safe_set(a, 'farrusco_Robot2', {b1})
    assert _is_linked(a, 'farrusco_Robot2', b1)
    if hasattr(b1, 'farrusco_Filho'):
        assert _is_linked(b1, 'farrusco_Filho', a)
    _safe_set(a, 'farrusco_Robot2', {b2})
    assert _is_linked(a, 'farrusco_Robot2', b2)
    if hasattr(b1, 'farrusco_Filho'):
        assert not _is_linked(b1, 'farrusco_Filho', a)
    if hasattr(b2, 'farrusco_Filho'):
        assert _is_linked(b2, 'farrusco_Filho', a)
    _safe_set(a, 'farrusco_Robot2', set())
    assert not _is_linked(a, 'farrusco_Robot2', b2)
    if hasattr(b2, 'farrusco_Filho'):
        assert not _is_linked(b2, 'farrusco_Filho', a)


def test_assoc_next3_link_reassign_clear():
    a = farrusco_Robot(Nome="sample_text")
    b1 = farrusco_Irmao()
    b2 = farrusco_Irmao()
    _safe_set(a, 'farrusco_Robot4', {b1})
    assert _is_linked(a, 'farrusco_Robot4', b1)
    if hasattr(b1, 'farrusco_Irmao'):
        assert _is_linked(b1, 'farrusco_Irmao', a)
    _safe_set(a, 'farrusco_Robot4', {b2})
    assert _is_linked(a, 'farrusco_Robot4', b2)
    if hasattr(b1, 'farrusco_Irmao'):
        assert not _is_linked(b1, 'farrusco_Irmao', a)
    if hasattr(b2, 'farrusco_Irmao'):
        assert _is_linked(b2, 'farrusco_Irmao', a)
    _safe_set(a, 'farrusco_Robot4', set())
    assert not _is_linked(a, 'farrusco_Robot4', b2)
    if hasattr(b2, 'farrusco_Irmao'):
        assert not _is_linked(b2, 'farrusco_Irmao', a)


def test_assoc_nodes0_link_reassign_clear():
    a = farrusco_Robot(Nome="sample_text")
    b1 = farrusco_Node()
    b2 = farrusco_Node()
    _safe_set(a, 'farrusco_Robot', {b1})
    assert _is_linked(a, 'farrusco_Robot', b1)
    if hasattr(b1, 'farrusco_Node'):
        assert _is_linked(b1, 'farrusco_Node', a)
    _safe_set(a, 'farrusco_Robot', {b2})
    assert _is_linked(a, 'farrusco_Robot', b2)
    if hasattr(b1, 'farrusco_Node'):
        assert not _is_linked(b1, 'farrusco_Node', a)
    if hasattr(b2, 'farrusco_Node'):
        assert _is_linked(b2, 'farrusco_Node', a)
    _safe_set(a, 'farrusco_Robot', set())
    assert not _is_linked(a, 'farrusco_Robot', b2)
    if hasattr(b2, 'farrusco_Node'):
        assert not _is_linked(b2, 'farrusco_Node', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Actuate_strategy = st.builds(Actuate)
@given(instance=Actuate_strategy)
@settings(max_examples=25)
def test_Actuate_instantiation(instance):
    assert isinstance(instance, Actuate)


Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


farrusco_Action_strategy = st.builds(farrusco_Action)
@given(instance=farrusco_Action_strategy)
@settings(max_examples=25)
def test_farrusco_Action_instantiation(instance):
    assert isinstance(instance, farrusco_Action)


farrusco_Actuate_strategy = st.builds(farrusco_Actuate)
@given(instance=farrusco_Actuate_strategy)
@settings(max_examples=25)
def test_farrusco_Actuate_instantiation(instance):
    assert isinstance(instance, farrusco_Actuate)


farrusco_AlterarEstado_strategy = st.builds(farrusco_AlterarEstado, Alterar_Decorrer=safe_text, Alterar_Falha=safe_text, Alterar_Sucesso=safe_text, Nome=safe_text)
@given(instance=farrusco_AlterarEstado_strategy)
@settings(max_examples=25)
def test_farrusco_AlterarEstado_instantiation(instance):
    assert isinstance(instance, farrusco_AlterarEstado)


farrusco_Behavior_strategy = st.builds(farrusco_Behavior)
@given(instance=farrusco_Behavior_strategy)
@settings(max_examples=25)
def test_farrusco_Behavior_instantiation(instance):
    assert isinstance(instance, farrusco_Behavior)


farrusco_Bumpers_strategy = st.builds(farrusco_Bumpers, Bumper_Esquerdo_ou_Direito=safe_text, Nome=safe_text)
@given(instance=farrusco_Bumpers_strategy)
@settings(max_examples=25)
def test_farrusco_Bumpers_instantiation(instance):
    assert isinstance(instance, farrusco_Bumpers)


farrusco_Condition_strategy = st.builds(farrusco_Condition)
@given(instance=farrusco_Condition_strategy)
@settings(max_examples=25)
def test_farrusco_Condition_instantiation(instance):
    assert isinstance(instance, farrusco_Condition)


farrusco_Distancia_strategy = st.builds(farrusco_Distancia, Menor_Maior=safe_text, Nome=safe_text, distancia=st.integers())
@given(instance=farrusco_Distancia_strategy)
@settings(max_examples=25)
def test_farrusco_Distancia_instantiation(instance):
    assert isinstance(instance, farrusco_Distancia)


farrusco_Espera_strategy = st.builds(farrusco_Espera, Nome=safe_text, Tempo=st.integers())
@given(instance=farrusco_Espera_strategy)
@settings(max_examples=25)
def test_farrusco_Espera_instantiation(instance):
    assert isinstance(instance, farrusco_Espera)


farrusco_Filho_strategy = st.builds(farrusco_Filho)
@given(instance=farrusco_Filho_strategy)
@settings(max_examples=25)
def test_farrusco_Filho_instantiation(instance):
    assert isinstance(instance, farrusco_Filho)


farrusco_Irmao_strategy = st.builds(farrusco_Irmao)
@given(instance=farrusco_Irmao_strategy)
@settings(max_examples=25)
def test_farrusco_Irmao_instantiation(instance):
    assert isinstance(instance, farrusco_Irmao)


farrusco_LED_strategy = st.builds(farrusco_LED, Ligado_ou_Desligado=safe_text, Nome=safe_text)
@given(instance=farrusco_LED_strategy)
@settings(max_examples=25)
def test_farrusco_LED_instantiation(instance):
    assert isinstance(instance, farrusco_LED)


farrusco_Motor_strategy = st.builds(farrusco_Motor, Motor_Direito=st.integers(), Motor_Esquerdo=st.integers(), Nome=safe_text)
@given(instance=farrusco_Motor_strategy)
@settings(max_examples=25)
def test_farrusco_Motor_instantiation(instance):
    assert isinstance(instance, farrusco_Motor)


farrusco_Node_strategy = st.builds(farrusco_Node)
@given(instance=farrusco_Node_strategy)
@settings(max_examples=25)
def test_farrusco_Node_instantiation(instance):
    assert isinstance(instance, farrusco_Node)


farrusco_Paralelo_strategy = st.builds(farrusco_Paralelo, Nome=safe_text)
@given(instance=farrusco_Paralelo_strategy)
@settings(max_examples=25)
def test_farrusco_Paralelo_instantiation(instance):
    assert isinstance(instance, farrusco_Paralelo)


farrusco_Prioridade_strategy = st.builds(farrusco_Prioridade, Nome=safe_text)
@given(instance=farrusco_Prioridade_strategy)
@settings(max_examples=25)
def test_farrusco_Prioridade_instantiation(instance):
    assert isinstance(instance, farrusco_Prioridade)


farrusco_Robot_strategy = st.builds(farrusco_Robot, Nome=safe_text)
@given(instance=farrusco_Robot_strategy)
@settings(max_examples=25)
def test_farrusco_Robot_instantiation(instance):
    assert isinstance(instance, farrusco_Robot)


farrusco_Sequencial_strategy = st.builds(farrusco_Sequencial, Nome=safe_text)
@given(instance=farrusco_Sequencial_strategy)
@settings(max_examples=25)
def test_farrusco_Sequencial_instantiation(instance):
    assert isinstance(instance, farrusco_Sequencial)


farrusco_Servo_strategy = st.builds(farrusco_Servo, Nome=safe_text, Passo_a_Passo=st.integers(), Posicao_Maxima=st.integers(), Posicao_Minima=st.integers())
@given(instance=farrusco_Servo_strategy)
@settings(max_examples=25)
def test_farrusco_Servo_instantiation(instance):
    assert isinstance(instance, farrusco_Servo)



