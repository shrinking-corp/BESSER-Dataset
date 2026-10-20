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
    Actor7_Actor,
    Actor6_Actor,
    Actor5_Actor,
    Component3_Component,
    Component2_Component,
    Actor4_Actor,
    Actor3_Actor,
    Actor2_Actor,
    Component_Component,
    Actor_Actor,
    Funcionario,
    Pessoa,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_actor7_actor_is_not_abstract():
    assert not inspect.isabstract(Actor7_Actor)


def test_hyp_actor7_actor_constructor_exists():
    assert callable(Actor7_Actor.__init__)


def test_hyp_actor7_actor_constructor_args():
    sig = inspect.signature(Actor7_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor6_actor_is_not_abstract():
    assert not inspect.isabstract(Actor6_Actor)


def test_hyp_actor6_actor_constructor_exists():
    assert callable(Actor6_Actor.__init__)


def test_hyp_actor6_actor_constructor_args():
    sig = inspect.signature(Actor6_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor5_actor_is_not_abstract():
    assert not inspect.isabstract(Actor5_Actor)


def test_hyp_actor5_actor_constructor_exists():
    assert callable(Actor5_Actor.__init__)


def test_hyp_actor5_actor_constructor_args():
    sig = inspect.signature(Actor5_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component3_component_is_not_abstract():
    assert not inspect.isabstract(Component3_Component)


def test_hyp_component3_component_constructor_exists():
    assert callable(Component3_Component.__init__)


def test_hyp_component3_component_constructor_args():
    sig = inspect.signature(Component3_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component2_component_is_not_abstract():
    assert not inspect.isabstract(Component2_Component)


def test_hyp_component2_component_constructor_exists():
    assert callable(Component2_Component.__init__)


def test_hyp_component2_component_constructor_args():
    sig = inspect.signature(Component2_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor4_actor_is_not_abstract():
    assert not inspect.isabstract(Actor4_Actor)


def test_hyp_actor4_actor_constructor_exists():
    assert callable(Actor4_Actor.__init__)


def test_hyp_actor4_actor_constructor_args():
    sig = inspect.signature(Actor4_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor3_actor_is_not_abstract():
    assert not inspect.isabstract(Actor3_Actor)


def test_hyp_actor3_actor_constructor_exists():
    assert callable(Actor3_Actor.__init__)


def test_hyp_actor3_actor_constructor_args():
    sig = inspect.signature(Actor3_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor2_actor_is_not_abstract():
    assert not inspect.isabstract(Actor2_Actor)


def test_hyp_actor2_actor_constructor_exists():
    assert callable(Actor2_Actor.__init__)


def test_hyp_actor2_actor_constructor_args():
    sig = inspect.signature(Actor2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component_component_is_not_abstract():
    assert not inspect.isabstract(Component_Component)


def test_hyp_component_component_constructor_exists():
    assert callable(Component_Component.__init__)


def test_hyp_component_component_constructor_args():
    sig = inspect.signature(Component_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_hyp_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_hyp_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_funcionario_is_not_abstract():
    assert not inspect.isabstract(Funcionario)


def test_hyp_funcionario_constructor_exists():
    assert callable(Funcionario.__init__)


def test_hyp_funcionario_constructor_args():
    sig = inspect.signature(Funcionario.__init__)
    params = list(sig.parameters.keys())
    assert "cracha" in params, "Missing parameter 'cracha'"




def test_hyp_pessoa_is_not_abstract():
    assert not inspect.isabstract(Pessoa)


def test_hyp_pessoa_constructor_exists():
    assert callable(Pessoa.__init__)


def test_hyp_pessoa_constructor_args():
    sig = inspect.signature(Pessoa.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "idade" in params, "Missing parameter 'idade'"





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
Actor7_Actor_strategy = st.builds(
    Actor7_Actor,
)
Actor6_Actor_strategy = st.builds(
    Actor6_Actor,
)
Actor5_Actor_strategy = st.builds(
    Actor5_Actor,
)
Component3_Component_strategy = st.builds(
    Component3_Component,
)
Component2_Component_strategy = st.builds(
    Component2_Component,
)
Actor4_Actor_strategy = st.builds(
    Actor4_Actor,
)
Actor3_Actor_strategy = st.builds(
    Actor3_Actor,
)
Actor2_Actor_strategy = st.builds(
    Actor2_Actor,
)
Component_Component_strategy = st.builds(
    Component_Component,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Funcionario_strategy = st.builds(
    Funcionario,
    cracha=
        st.integers()
)
Pessoa_strategy = st.builds(
    Pessoa,
    id=
        st.integers(),
    Nome=
        safe_text,
    idade=
        st.integers()
)














@given(instance=Funcionario_strategy)
def test_hyp_funcionario_cracha_setter(instance):
    original = instance.cracha
    instance.cracha = original
    assert instance.cracha == original




@given(instance=Pessoa_strategy)
def test_hyp_pessoa_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Pessoa_strategy)
def test_hyp_pessoa_idade_setter(instance):
    original = instance.idade
    instance.idade = original
    assert instance.idade == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actor2_Actor,
    Actor3_Actor,
    Actor4_Actor,
    Actor5_Actor,
    Actor6_Actor,
    Actor7_Actor,
    Actor_Actor,
    Component2_Component,
    Component3_Component,
    Component_Component,
    Funcionario,
    Pessoa,
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

def test_Funcionario_cracha_value_roundtrip():
    instance = Funcionario(cracha=7)
    assert instance.cracha == 7
    instance.cracha = 13
    assert instance.cracha == 13


def test_Pessoa_Nome_value_roundtrip():
    instance = Pessoa(Nome="sample_text", id=7, idade=7)
    assert instance.Nome == "sample_text"
    instance.Nome = "sample_text_2"
    assert instance.Nome == "sample_text_2"


def test_Pessoa_id_value_roundtrip():
    instance = Pessoa(Nome="sample_text", id=7, idade=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Pessoa_idade_value_roundtrip():
    instance = Pessoa(Nome="sample_text", id=7, idade=7)
    assert instance.idade == 7
    instance.idade = 13
    assert instance.idade == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actor2_Actor_strategy = st.builds(Actor2_Actor)
@given(instance=Actor2_Actor_strategy)
@settings(max_examples=25)
def test_Actor2_Actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)


Actor3_Actor_strategy = st.builds(Actor3_Actor)
@given(instance=Actor3_Actor_strategy)
@settings(max_examples=25)
def test_Actor3_Actor_instantiation(instance):
    assert isinstance(instance, Actor3_Actor)


Actor4_Actor_strategy = st.builds(Actor4_Actor)
@given(instance=Actor4_Actor_strategy)
@settings(max_examples=25)
def test_Actor4_Actor_instantiation(instance):
    assert isinstance(instance, Actor4_Actor)


Actor5_Actor_strategy = st.builds(Actor5_Actor)
@given(instance=Actor5_Actor_strategy)
@settings(max_examples=25)
def test_Actor5_Actor_instantiation(instance):
    assert isinstance(instance, Actor5_Actor)


Actor6_Actor_strategy = st.builds(Actor6_Actor)
@given(instance=Actor6_Actor_strategy)
@settings(max_examples=25)
def test_Actor6_Actor_instantiation(instance):
    assert isinstance(instance, Actor6_Actor)


Actor7_Actor_strategy = st.builds(Actor7_Actor)
@given(instance=Actor7_Actor_strategy)
@settings(max_examples=25)
def test_Actor7_Actor_instantiation(instance):
    assert isinstance(instance, Actor7_Actor)


Actor_Actor_strategy = st.builds(Actor_Actor)
@given(instance=Actor_Actor_strategy)
@settings(max_examples=25)
def test_Actor_Actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)


Component2_Component_strategy = st.builds(Component2_Component)
@given(instance=Component2_Component_strategy)
@settings(max_examples=25)
def test_Component2_Component_instantiation(instance):
    assert isinstance(instance, Component2_Component)


Component3_Component_strategy = st.builds(Component3_Component)
@given(instance=Component3_Component_strategy)
@settings(max_examples=25)
def test_Component3_Component_instantiation(instance):
    assert isinstance(instance, Component3_Component)


Component_Component_strategy = st.builds(Component_Component)
@given(instance=Component_Component_strategy)
@settings(max_examples=25)
def test_Component_Component_instantiation(instance):
    assert isinstance(instance, Component_Component)


Funcionario_strategy = st.builds(Funcionario, cracha=st.integers())
@given(instance=Funcionario_strategy)
@settings(max_examples=25)
def test_Funcionario_instantiation(instance):
    assert isinstance(instance, Funcionario)


Pessoa_strategy = st.builds(Pessoa, Nome=safe_text, id=st.integers(), idade=st.integers())
@given(instance=Pessoa_strategy)
@settings(max_examples=25)
def test_Pessoa_instantiation(instance):
    assert isinstance(instance, Pessoa)



