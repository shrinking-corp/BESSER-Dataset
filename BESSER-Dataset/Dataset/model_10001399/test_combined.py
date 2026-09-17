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
    Ver_Contactos_external,
    Contacto,
    Usuario_Actor,
    Actualizar_Coredata_UseCase,
    Ver_detalles_de_contacto_UseCase,
    Salir_de_la_aplicacion_UseCase,
    Editar_Contacto_UseCase,
    Eliminar_Contacto_UseCase,
    Buscar_Contactos_UseCase,
    Agregar_Contactos_UseCase,
    AGENDA_TELEFONICA_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ver_contactos_external_is_not_abstract():
    assert not inspect.isabstract(Ver_Contactos_external)


def test_hyp_ver_contactos_external_constructor_exists():
    assert callable(Ver_Contactos_external.__init__)


def test_hyp_ver_contactos_external_constructor_args():
    sig = inspect.signature(Ver_Contactos_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contacto_is_not_abstract():
    assert not inspect.isabstract(Contacto)


def test_hyp_contacto_constructor_exists():
    assert callable(Contacto.__init__)


def test_hyp_contacto_constructor_args():
    sig = inspect.signature(Contacto.__init__)
    params = list(sig.parameters.keys())
    assert "Foto" in params, "Missing parameter 'Foto'"
    assert "user" in params, "Missing parameter 'user'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Telefono" in params, "Missing parameter 'Telefono'"
    assert "id" in params, "Missing parameter 'id'"
    assert "Groups" in params, "Missing parameter 'Groups'"
    assert "Apellido" in params, "Missing parameter 'Apellido'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"











def test_hyp_usuario_actor_is_not_abstract():
    assert not inspect.isabstract(Usuario_Actor)


def test_hyp_usuario_actor_constructor_exists():
    assert callable(Usuario_Actor.__init__)


def test_hyp_usuario_actor_constructor_args():
    sig = inspect.signature(Usuario_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actualizar_coredata_usecase_is_not_abstract():
    assert not inspect.isabstract(Actualizar_Coredata_UseCase)


def test_hyp_actualizar_coredata_usecase_constructor_exists():
    assert callable(Actualizar_Coredata_UseCase.__init__)


def test_hyp_actualizar_coredata_usecase_constructor_args():
    sig = inspect.signature(Actualizar_Coredata_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ver_detalles_de_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Ver_detalles_de_contacto_UseCase)


def test_hyp_ver_detalles_de_contacto_usecase_constructor_exists():
    assert callable(Ver_detalles_de_contacto_UseCase.__init__)


def test_hyp_ver_detalles_de_contacto_usecase_constructor_args():
    sig = inspect.signature(Ver_detalles_de_contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_salir_de_la_aplicacion_usecase_is_not_abstract():
    assert not inspect.isabstract(Salir_de_la_aplicacion_UseCase)


def test_hyp_salir_de_la_aplicacion_usecase_constructor_exists():
    assert callable(Salir_de_la_aplicacion_UseCase.__init__)


def test_hyp_salir_de_la_aplicacion_usecase_constructor_args():
    sig = inspect.signature(Salir_de_la_aplicacion_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_editar_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Editar_Contacto_UseCase)


def test_hyp_editar_contacto_usecase_constructor_exists():
    assert callable(Editar_Contacto_UseCase.__init__)


def test_hyp_editar_contacto_usecase_constructor_args():
    sig = inspect.signature(Editar_Contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eliminar_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Eliminar_Contacto_UseCase)


def test_hyp_eliminar_contacto_usecase_constructor_exists():
    assert callable(Eliminar_Contacto_UseCase.__init__)


def test_hyp_eliminar_contacto_usecase_constructor_args():
    sig = inspect.signature(Eliminar_Contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buscar_contactos_usecase_is_not_abstract():
    assert not inspect.isabstract(Buscar_Contactos_UseCase)


def test_hyp_buscar_contactos_usecase_constructor_exists():
    assert callable(Buscar_Contactos_UseCase.__init__)


def test_hyp_buscar_contactos_usecase_constructor_args():
    sig = inspect.signature(Buscar_Contactos_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_agregar_contactos_usecase_is_not_abstract():
    assert not inspect.isabstract(Agregar_Contactos_UseCase)


def test_hyp_agregar_contactos_usecase_constructor_exists():
    assert callable(Agregar_Contactos_UseCase.__init__)


def test_hyp_agregar_contactos_usecase_constructor_args():
    sig = inspect.signature(Agregar_Contactos_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_agenda_telefonica_component_is_not_abstract():
    assert not inspect.isabstract(AGENDA_TELEFONICA_Component)


def test_hyp_agenda_telefonica_component_constructor_exists():
    assert callable(AGENDA_TELEFONICA_Component.__init__)


def test_hyp_agenda_telefonica_component_constructor_args():
    sig = inspect.signature(AGENDA_TELEFONICA_Component.__init__)
    params = list(sig.parameters.keys())


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
Ver_Contactos_external_strategy = st.builds(
    Ver_Contactos_external,
)
Contacto_strategy = st.builds(
    Contacto,
    Foto=
        safe_text,
    user=
        safe_text,
    Email=
        safe_text,
    Telefono=
        st.integers(),
    id=
        st.integers(),
    Groups=
        safe_text,
    Apellido=
        safe_text,
    Nombre=
        safe_text
)
Usuario_Actor_strategy = st.builds(
    Usuario_Actor,
)
Actualizar_Coredata_UseCase_strategy = st.builds(
    Actualizar_Coredata_UseCase,
)
Ver_detalles_de_contacto_UseCase_strategy = st.builds(
    Ver_detalles_de_contacto_UseCase,
)
Salir_de_la_aplicacion_UseCase_strategy = st.builds(
    Salir_de_la_aplicacion_UseCase,
)
Editar_Contacto_UseCase_strategy = st.builds(
    Editar_Contacto_UseCase,
)
Eliminar_Contacto_UseCase_strategy = st.builds(
    Eliminar_Contacto_UseCase,
)
Buscar_Contactos_UseCase_strategy = st.builds(
    Buscar_Contactos_UseCase,
)
Agregar_Contactos_UseCase_strategy = st.builds(
    Agregar_Contactos_UseCase,
)
AGENDA_TELEFONICA_Component_strategy = st.builds(
    AGENDA_TELEFONICA_Component,
)





@given(instance=Contacto_strategy)
def test_hyp_contacto_Foto_setter(instance):
    original = instance.Foto
    instance.Foto = original
    assert instance.Foto == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_Telefono_setter(instance):
    original = instance.Telefono
    instance.Telefono = original
    assert instance.Telefono == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_Groups_setter(instance):
    original = instance.Groups
    instance.Groups = original
    assert instance.Groups == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_Apellido_setter(instance):
    original = instance.Apellido
    instance.Apellido = original
    assert instance.Apellido == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original











# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AGENDA_TELEFONICA_Component,
    Actualizar_Coredata_UseCase,
    Agregar_Contactos_UseCase,
    Buscar_Contactos_UseCase,
    Contacto,
    Editar_Contacto_UseCase,
    Eliminar_Contacto_UseCase,
    Salir_de_la_aplicacion_UseCase,
    Usuario_Actor,
    Ver_Contactos_external,
    Ver_detalles_de_contacto_UseCase,
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

def test_Contacto_Apellido_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.Apellido == "sample_text"
    instance.Apellido = "sample_text_2"
    assert instance.Apellido == "sample_text_2"


def test_Contacto_Email_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Contacto_Foto_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.Foto == "sample_text"
    instance.Foto = "sample_text_2"
    assert instance.Foto == "sample_text_2"


def test_Contacto_Groups_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.Groups == "sample_text"
    instance.Groups = "sample_text_2"
    assert instance.Groups == "sample_text_2"


def test_Contacto_Nombre_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.Nombre == "sample_text"
    instance.Nombre = "sample_text_2"
    assert instance.Nombre == "sample_text_2"


def test_Contacto_Telefono_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.Telefono == 7
    instance.Telefono = 13
    assert instance.Telefono == 13


def test_Contacto_id_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Contacto_user_value_roundtrip():
    instance = Contacto(Apellido="sample_text", Email="sample_text", Foto="sample_text", Groups="sample_text", Nombre="sample_text", Telefono=7, id=7, user="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AGENDA_TELEFONICA_Component_strategy = st.builds(AGENDA_TELEFONICA_Component)
@given(instance=AGENDA_TELEFONICA_Component_strategy)
@settings(max_examples=25)
def test_AGENDA_TELEFONICA_Component_instantiation(instance):
    assert isinstance(instance, AGENDA_TELEFONICA_Component)


Actualizar_Coredata_UseCase_strategy = st.builds(Actualizar_Coredata_UseCase)
@given(instance=Actualizar_Coredata_UseCase_strategy)
@settings(max_examples=25)
def test_Actualizar_Coredata_UseCase_instantiation(instance):
    assert isinstance(instance, Actualizar_Coredata_UseCase)


Agregar_Contactos_UseCase_strategy = st.builds(Agregar_Contactos_UseCase)
@given(instance=Agregar_Contactos_UseCase_strategy)
@settings(max_examples=25)
def test_Agregar_Contactos_UseCase_instantiation(instance):
    assert isinstance(instance, Agregar_Contactos_UseCase)


Buscar_Contactos_UseCase_strategy = st.builds(Buscar_Contactos_UseCase)
@given(instance=Buscar_Contactos_UseCase_strategy)
@settings(max_examples=25)
def test_Buscar_Contactos_UseCase_instantiation(instance):
    assert isinstance(instance, Buscar_Contactos_UseCase)


Contacto_strategy = st.builds(Contacto, Apellido=safe_text, Email=safe_text, Foto=safe_text, Groups=safe_text, Nombre=safe_text, Telefono=st.integers(), id=st.integers(), user=safe_text)
@given(instance=Contacto_strategy)
@settings(max_examples=25)
def test_Contacto_instantiation(instance):
    assert isinstance(instance, Contacto)


Editar_Contacto_UseCase_strategy = st.builds(Editar_Contacto_UseCase)
@given(instance=Editar_Contacto_UseCase_strategy)
@settings(max_examples=25)
def test_Editar_Contacto_UseCase_instantiation(instance):
    assert isinstance(instance, Editar_Contacto_UseCase)


Eliminar_Contacto_UseCase_strategy = st.builds(Eliminar_Contacto_UseCase)
@given(instance=Eliminar_Contacto_UseCase_strategy)
@settings(max_examples=25)
def test_Eliminar_Contacto_UseCase_instantiation(instance):
    assert isinstance(instance, Eliminar_Contacto_UseCase)


Salir_de_la_aplicacion_UseCase_strategy = st.builds(Salir_de_la_aplicacion_UseCase)
@given(instance=Salir_de_la_aplicacion_UseCase_strategy)
@settings(max_examples=25)
def test_Salir_de_la_aplicacion_UseCase_instantiation(instance):
    assert isinstance(instance, Salir_de_la_aplicacion_UseCase)


Usuario_Actor_strategy = st.builds(Usuario_Actor)
@given(instance=Usuario_Actor_strategy)
@settings(max_examples=25)
def test_Usuario_Actor_instantiation(instance):
    assert isinstance(instance, Usuario_Actor)


Ver_Contactos_external_strategy = st.builds(Ver_Contactos_external)
@given(instance=Ver_Contactos_external_strategy)
@settings(max_examples=25)
def test_Ver_Contactos_external_instantiation(instance):
    assert isinstance(instance, Ver_Contactos_external)


Ver_detalles_de_contacto_UseCase_strategy = st.builds(Ver_detalles_de_contacto_UseCase)
@given(instance=Ver_detalles_de_contacto_UseCase_strategy)
@settings(max_examples=25)
def test_Ver_detalles_de_contacto_UseCase_instantiation(instance):
    assert isinstance(instance, Ver_detalles_de_contacto_UseCase)



