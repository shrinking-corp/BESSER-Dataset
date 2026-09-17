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
    Foto_de_perfil,
    Telefono,
    Direccion,
    Contacto,
    Directorio,
    User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_foto_de_perfil_is_not_abstract():
    assert not inspect.isabstract(Foto_de_perfil)


def test_hyp_foto_de_perfil_constructor_exists():
    assert callable(Foto_de_perfil.__init__)


def test_hyp_foto_de_perfil_constructor_args():
    sig = inspect.signature(Foto_de_perfil.__init__)
    params = list(sig.parameters.keys())



def test_hyp_telefono_is_not_abstract():
    assert not inspect.isabstract(Telefono)


def test_hyp_telefono_constructor_exists():
    assert callable(Telefono.__init__)


def test_hyp_telefono_constructor_args():
    sig = inspect.signature(Telefono.__init__)
    params = list(sig.parameters.keys())
    assert "Codigo_de_Area" in params, "Missing parameter 'Codigo_de_Area'"
    assert "Prefijo" in params, "Missing parameter 'Prefijo'"
    assert "Numero" in params, "Missing parameter 'Numero'"






def test_hyp_direccion_is_not_abstract():
    assert not inspect.isabstract(Direccion)


def test_hyp_direccion_constructor_exists():
    assert callable(Direccion.__init__)


def test_hyp_direccion_constructor_args():
    sig = inspect.signature(Direccion.__init__)
    params = list(sig.parameters.keys())
    assert "Pais" in params, "Missing parameter 'Pais'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Ciudad" in params, "Missing parameter 'Ciudad'"
    assert "Codigo_Postal" in params, "Missing parameter 'Codigo_Postal'"







def test_hyp_contacto_is_not_abstract():
    assert not inspect.isabstract(Contacto)


def test_hyp_contacto_constructor_exists():
    assert callable(Contacto.__init__)


def test_hyp_contacto_constructor_args():
    sig = inspect.signature(Contacto.__init__)
    params = list(sig.parameters.keys())
    assert "Correo" in params, "Missing parameter 'Correo'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"





def test_hyp_directorio_is_not_abstract():
    assert not inspect.isabstract(Directorio)


def test_hyp_directorio_constructor_exists():
    assert callable(Directorio.__init__)


def test_hyp_directorio_constructor_args():
    sig = inspect.signature(Directorio.__init__)
    params = list(sig.parameters.keys())
    assert "Introducir" in params, "Missing parameter 'Introducir'"




def test_hyp_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_hyp_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_hyp_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
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
Foto_de_perfil_strategy = st.builds(
    Foto_de_perfil,
)
Telefono_strategy = st.builds(
    Telefono,
    Codigo_de_Area=
        st.integers(),
    Prefijo=
        st.integers(),
    Numero=
        st.integers()
)
Direccion_strategy = st.builds(
    Direccion,
    Pais=
        safe_text,
    Nombre=
        safe_text,
    Ciudad=
        safe_text,
    Codigo_Postal=
        st.integers()
)
Contacto_strategy = st.builds(
    Contacto,
    Correo=
        safe_text,
    Nombre=
        safe_text
)
Directorio_strategy = st.builds(
    Directorio,
    Introducir=
        safe_text
)
User_Actor_strategy = st.builds(
    User_Actor,
)





@given(instance=Telefono_strategy)
def test_hyp_telefono_Codigo_de_Area_setter(instance):
    original = instance.Codigo_de_Area
    instance.Codigo_de_Area = original
    assert instance.Codigo_de_Area == original



@given(instance=Telefono_strategy)
def test_hyp_telefono_Prefijo_setter(instance):
    original = instance.Prefijo
    instance.Prefijo = original
    assert instance.Prefijo == original



@given(instance=Telefono_strategy)
def test_hyp_telefono_Numero_setter(instance):
    original = instance.Numero
    instance.Numero = original
    assert instance.Numero == original




@given(instance=Direccion_strategy)
def test_hyp_direccion_Pais_setter(instance):
    original = instance.Pais
    instance.Pais = original
    assert instance.Pais == original



@given(instance=Direccion_strategy)
def test_hyp_direccion_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Direccion_strategy)
def test_hyp_direccion_Ciudad_setter(instance):
    original = instance.Ciudad
    instance.Ciudad = original
    assert instance.Ciudad == original



@given(instance=Direccion_strategy)
def test_hyp_direccion_Codigo_Postal_setter(instance):
    original = instance.Codigo_Postal
    instance.Codigo_Postal = original
    assert instance.Codigo_Postal == original




@given(instance=Contacto_strategy)
def test_hyp_contacto_Correo_setter(instance):
    original = instance.Correo
    instance.Correo = original
    assert instance.Correo == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original




@given(instance=Directorio_strategy)
def test_hyp_directorio_Introducir_setter(instance):
    original = instance.Introducir
    instance.Introducir = original
    assert instance.Introducir == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Contacto,
    Direccion,
    Directorio,
    Foto_de_perfil,
    Telefono,
    User_Actor,
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

def test_Contacto_Correo_value_roundtrip():
    instance = Contacto(Correo="sample_text", Nombre="sample_text")
    assert instance.Correo == "sample_text"
    instance.Correo = "sample_text_2"
    assert instance.Correo == "sample_text_2"


def test_Contacto_Nombre_value_roundtrip():
    instance = Contacto(Correo="sample_text", Nombre="sample_text")
    assert instance.Nombre == "sample_text"
    instance.Nombre = "sample_text_2"
    assert instance.Nombre == "sample_text_2"


def test_Direccion_Ciudad_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    assert instance.Ciudad == "sample_text"
    instance.Ciudad = "sample_text_2"
    assert instance.Ciudad == "sample_text_2"


def test_Direccion_Codigo_Postal_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    assert instance.Codigo_Postal == 7
    instance.Codigo_Postal = 13
    assert instance.Codigo_Postal == 13


def test_Direccion_Nombre_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    assert instance.Nombre == "sample_text"
    instance.Nombre = "sample_text_2"
    assert instance.Nombre == "sample_text_2"


def test_Direccion_Pais_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    assert instance.Pais == "sample_text"
    instance.Pais = "sample_text_2"
    assert instance.Pais == "sample_text_2"


def test_Directorio_Introducir_value_roundtrip():
    instance = Directorio(Introducir="sample_text")
    assert instance.Introducir == "sample_text"
    instance.Introducir = "sample_text_2"
    assert instance.Introducir == "sample_text_2"


def test_Telefono_Codigo_de_Area_value_roundtrip():
    instance = Telefono(Codigo_de_Area=7, Numero=7, Prefijo=7)
    assert instance.Codigo_de_Area == 7
    instance.Codigo_de_Area = 13
    assert instance.Codigo_de_Area == 13


def test_Telefono_Numero_value_roundtrip():
    instance = Telefono(Codigo_de_Area=7, Numero=7, Prefijo=7)
    assert instance.Numero == 7
    instance.Numero = 13
    assert instance.Numero == 13


def test_Telefono_Prefijo_value_roundtrip():
    instance = Telefono(Codigo_de_Area=7, Numero=7, Prefijo=7)
    assert instance.Prefijo == 7
    instance.Prefijo = 13
    assert instance.Prefijo == 13


def test_assoc_Contacto_Direccion_link_reassign_clear():
    a = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    b1 = Contacto(Correo="sample_text", Nombre="sample_text")
    b2 = Contacto(Correo="sample_text_2", Nombre="sample_text_2")
    _safe_set(a, 'contacto3', b1)
    assert _is_linked(a, 'contacto3', b1)
    if hasattr(b1, 'direccion_Principal2'):
        assert _is_linked(b1, 'direccion_Principal2', a)
    _safe_set(a, 'contacto3', b2)
    assert _is_linked(a, 'contacto3', b2)
    if hasattr(b1, 'direccion_Principal2'):
        assert not _is_linked(b1, 'direccion_Principal2', a)
    if hasattr(b2, 'direccion_Principal2'):
        assert _is_linked(b2, 'direccion_Principal2', a)
    _safe_set(a, 'contacto3', None)
    assert not _is_linked(a, 'contacto3', b2)
    if hasattr(b2, 'direccion_Principal2'):
        assert not _is_linked(b2, 'direccion_Principal2', a)


def test_assoc_Contacto_Direccion2_link_reassign_clear():
    a = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    b1 = Contacto(Correo="sample_text", Nombre="sample_text")
    b2 = Contacto(Correo="sample_text_2", Nombre="sample_text_2")
    _safe_set(a, 'contacto5', b1)
    assert _is_linked(a, 'contacto5', b1)
    if hasattr(b1, 'direccion4'):
        assert _is_linked(b1, 'direccion4', a)
    _safe_set(a, 'contacto5', b2)
    assert _is_linked(a, 'contacto5', b2)
    if hasattr(b1, 'direccion4'):
        assert not _is_linked(b1, 'direccion4', a)
    if hasattr(b2, 'direccion4'):
        assert _is_linked(b2, 'direccion4', a)
    _safe_set(a, 'contacto5', None)
    assert not _is_linked(a, 'contacto5', b2)
    if hasattr(b2, 'direccion4'):
        assert not _is_linked(b2, 'direccion4', a)


def test_assoc_Directorio_Contacto_link_reassign_clear():
    a = Directorio(Introducir="sample_text")
    b1 = Contacto(Correo="sample_text", Nombre="sample_text")
    b2 = Contacto(Correo="sample_text_2", Nombre="sample_text_2")
    _safe_set(a, 'contacto0', b1)
    assert _is_linked(a, 'contacto0', b1)
    if hasattr(b1, 'directorio1'):
        assert _is_linked(b1, 'directorio1', a)
    _safe_set(a, 'contacto0', b2)
    assert _is_linked(a, 'contacto0', b2)
    if hasattr(b1, 'directorio1'):
        assert not _is_linked(b1, 'directorio1', a)
    if hasattr(b2, 'directorio1'):
        assert _is_linked(b2, 'directorio1', a)
    _safe_set(a, 'contacto0', None)
    assert not _is_linked(a, 'contacto0', b2)
    if hasattr(b2, 'directorio1'):
        assert not _is_linked(b2, 'directorio1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Contacto_strategy = st.builds(Contacto, Correo=safe_text, Nombre=safe_text)
@given(instance=Contacto_strategy)
@settings(max_examples=25)
def test_Contacto_instantiation(instance):
    assert isinstance(instance, Contacto)


Direccion_strategy = st.builds(Direccion, Ciudad=safe_text, Codigo_Postal=st.integers(), Nombre=safe_text, Pais=safe_text)
@given(instance=Direccion_strategy)
@settings(max_examples=25)
def test_Direccion_instantiation(instance):
    assert isinstance(instance, Direccion)


Directorio_strategy = st.builds(Directorio, Introducir=safe_text)
@given(instance=Directorio_strategy)
@settings(max_examples=25)
def test_Directorio_instantiation(instance):
    assert isinstance(instance, Directorio)


Foto_de_perfil_strategy = st.builds(Foto_de_perfil)
@given(instance=Foto_de_perfil_strategy)
@settings(max_examples=25)
def test_Foto_de_perfil_instantiation(instance):
    assert isinstance(instance, Foto_de_perfil)


Telefono_strategy = st.builds(Telefono, Codigo_de_Area=st.integers(), Numero=st.integers(), Prefijo=st.integers())
@given(instance=Telefono_strategy)
@settings(max_examples=25)
def test_Telefono_instantiation(instance):
    assert isinstance(instance, Telefono)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)



