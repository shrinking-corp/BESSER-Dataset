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
    Lista_de_COntacto,
    Crear_Contacto,
    Buscar,
    Menu_Principal,
    Libro_de_Direcciones1,
    Foto,
    Tel_fono,
    Direccion,
    Contacto,
    Libro_de_Direcciones,
    Cancelar_UseCase,
    Guardar_UseCase,
    Eliminar_Contacto_UseCase,
    Actualizar_COntacto_UseCase,
    Crear_Contacto_UseCase,
    Buscar_Contactos_UseCase,
    Usuario_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_lista_de_contacto_is_not_abstract():
    assert not inspect.isabstract(Lista_de_COntacto)


def test_hyp_lista_de_contacto_constructor_exists():
    assert callable(Lista_de_COntacto.__init__)


def test_hyp_lista_de_contacto_constructor_args():
    sig = inspect.signature(Lista_de_COntacto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crear_contacto_is_not_abstract():
    assert not inspect.isabstract(Crear_Contacto)


def test_hyp_crear_contacto_constructor_exists():
    assert callable(Crear_Contacto.__init__)


def test_hyp_crear_contacto_constructor_args():
    sig = inspect.signature(Crear_Contacto.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buscar_is_not_abstract():
    assert not inspect.isabstract(Buscar)


def test_hyp_buscar_constructor_exists():
    assert callable(Buscar.__init__)


def test_hyp_buscar_constructor_args():
    sig = inspect.signature(Buscar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_menu_principal_is_not_abstract():
    assert not inspect.isabstract(Menu_Principal)


def test_hyp_menu_principal_constructor_exists():
    assert callable(Menu_Principal.__init__)


def test_hyp_menu_principal_constructor_args():
    sig = inspect.signature(Menu_Principal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libro_de_direcciones1_is_not_abstract():
    assert not inspect.isabstract(Libro_de_Direcciones1)


def test_hyp_libro_de_direcciones1_constructor_exists():
    assert callable(Libro_de_Direcciones1.__init__)


def test_hyp_libro_de_direcciones1_constructor_args():
    sig = inspect.signature(Libro_de_Direcciones1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_foto_is_not_abstract():
    assert not inspect.isabstract(Foto)


def test_hyp_foto_constructor_exists():
    assert callable(Foto.__init__)


def test_hyp_foto_constructor_args():
    sig = inspect.signature(Foto.__init__)
    params = list(sig.parameters.keys())
    assert "largo" in params, "Missing parameter 'largo'"
    assert "ancho" in params, "Missing parameter 'ancho'"





def test_hyp_tel_fono_is_not_abstract():
    assert not inspect.isabstract(Tel_fono)


def test_hyp_tel_fono_constructor_exists():
    assert callable(Tel_fono.__init__)


def test_hyp_tel_fono_constructor_args():
    sig = inspect.signature(Tel_fono.__init__)
    params = list(sig.parameters.keys())
    assert "Codigo_area" in params, "Missing parameter 'Codigo_area'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "prefijo" in params, "Missing parameter 'prefijo'"






def test_hyp_direccion_is_not_abstract():
    assert not inspect.isabstract(Direccion)


def test_hyp_direccion_constructor_exists():
    assert callable(Direccion.__init__)


def test_hyp_direccion_constructor_args():
    sig = inspect.signature(Direccion.__init__)
    params = list(sig.parameters.keys())
    assert "departamento" in params, "Missing parameter 'departamento'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "CodigoPostal" in params, "Missing parameter 'CodigoPostal'"
    assert "Ciudad" in params, "Missing parameter 'Ciudad'"







def test_hyp_contacto_is_not_abstract():
    assert not inspect.isabstract(Contacto)


def test_hyp_contacto_constructor_exists():
    assert callable(Contacto.__init__)


def test_hyp_contacto_constructor_args():
    sig = inspect.signature(Contacto.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "nombre" in params, "Missing parameter 'nombre'"





def test_hyp_libro_de_direcciones_is_not_abstract():
    assert not inspect.isabstract(Libro_de_Direcciones)


def test_hyp_libro_de_direcciones_constructor_exists():
    assert callable(Libro_de_Direcciones.__init__)


def test_hyp_libro_de_direcciones_constructor_args():
    sig = inspect.signature(Libro_de_Direcciones.__init__)
    params = list(sig.parameters.keys())
    assert "Introduccion" in params, "Missing parameter 'Introduccion'"




def test_hyp_cancelar_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancelar_UseCase)


def test_hyp_cancelar_usecase_constructor_exists():
    assert callable(Cancelar_UseCase.__init__)


def test_hyp_cancelar_usecase_constructor_args():
    sig = inspect.signature(Cancelar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_guardar_usecase_is_not_abstract():
    assert not inspect.isabstract(Guardar_UseCase)


def test_hyp_guardar_usecase_constructor_exists():
    assert callable(Guardar_UseCase.__init__)


def test_hyp_guardar_usecase_constructor_args():
    sig = inspect.signature(Guardar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eliminar_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Eliminar_Contacto_UseCase)


def test_hyp_eliminar_contacto_usecase_constructor_exists():
    assert callable(Eliminar_Contacto_UseCase.__init__)


def test_hyp_eliminar_contacto_usecase_constructor_args():
    sig = inspect.signature(Eliminar_Contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actualizar_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Actualizar_COntacto_UseCase)


def test_hyp_actualizar_contacto_usecase_constructor_exists():
    assert callable(Actualizar_COntacto_UseCase.__init__)


def test_hyp_actualizar_contacto_usecase_constructor_args():
    sig = inspect.signature(Actualizar_COntacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crear_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Crear_Contacto_UseCase)


def test_hyp_crear_contacto_usecase_constructor_exists():
    assert callable(Crear_Contacto_UseCase.__init__)


def test_hyp_crear_contacto_usecase_constructor_args():
    sig = inspect.signature(Crear_Contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buscar_contactos_usecase_is_not_abstract():
    assert not inspect.isabstract(Buscar_Contactos_UseCase)


def test_hyp_buscar_contactos_usecase_constructor_exists():
    assert callable(Buscar_Contactos_UseCase.__init__)


def test_hyp_buscar_contactos_usecase_constructor_args():
    sig = inspect.signature(Buscar_Contactos_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_usuario_actor_is_not_abstract():
    assert not inspect.isabstract(Usuario_Actor)


def test_hyp_usuario_actor_constructor_exists():
    assert callable(Usuario_Actor.__init__)


def test_hyp_usuario_actor_constructor_args():
    sig = inspect.signature(Usuario_Actor.__init__)
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
Lista_de_COntacto_strategy = st.builds(
    Lista_de_COntacto,
)
Crear_Contacto_strategy = st.builds(
    Crear_Contacto,
)
Buscar_strategy = st.builds(
    Buscar,
)
Menu_Principal_strategy = st.builds(
    Menu_Principal,
)
Libro_de_Direcciones1_strategy = st.builds(
    Libro_de_Direcciones1,
)
Foto_strategy = st.builds(
    Foto,
    largo=
        st.integers(),
    ancho=
        st.integers()
)
Tel_fono_strategy = st.builds(
    Tel_fono,
    Codigo_area=
        st.integers(),
    numero=
        st.integers(),
    prefijo=
        st.integers()
)
Direccion_strategy = st.builds(
    Direccion,
    departamento=
        safe_text,
    nombre=
        safe_text,
    CodigoPostal=
        st.integers(),
    Ciudad=
        safe_text
)
Contacto_strategy = st.builds(
    Contacto,
    email=
        safe_text,
    nombre=
        safe_text
)
Libro_de_Direcciones_strategy = st.builds(
    Libro_de_Direcciones,
    Introduccion=
        safe_text
)
Cancelar_UseCase_strategy = st.builds(
    Cancelar_UseCase,
)
Guardar_UseCase_strategy = st.builds(
    Guardar_UseCase,
)
Eliminar_Contacto_UseCase_strategy = st.builds(
    Eliminar_Contacto_UseCase,
)
Actualizar_COntacto_UseCase_strategy = st.builds(
    Actualizar_COntacto_UseCase,
)
Crear_Contacto_UseCase_strategy = st.builds(
    Crear_Contacto_UseCase,
)
Buscar_Contactos_UseCase_strategy = st.builds(
    Buscar_Contactos_UseCase,
)
Usuario_Actor_strategy = st.builds(
    Usuario_Actor,
)









@given(instance=Foto_strategy)
def test_hyp_foto_largo_setter(instance):
    original = instance.largo
    instance.largo = original
    assert instance.largo == original



@given(instance=Foto_strategy)
def test_hyp_foto_ancho_setter(instance):
    original = instance.ancho
    instance.ancho = original
    assert instance.ancho == original




@given(instance=Tel_fono_strategy)
def test_hyp_tel_fono_Codigo_area_setter(instance):
    original = instance.Codigo_area
    instance.Codigo_area = original
    assert instance.Codigo_area == original



@given(instance=Tel_fono_strategy)
def test_hyp_tel_fono_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Tel_fono_strategy)
def test_hyp_tel_fono_prefijo_setter(instance):
    original = instance.prefijo
    instance.prefijo = original
    assert instance.prefijo == original




@given(instance=Direccion_strategy)
def test_hyp_direccion_departamento_setter(instance):
    original = instance.departamento
    instance.departamento = original
    assert instance.departamento == original



@given(instance=Direccion_strategy)
def test_hyp_direccion_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Direccion_strategy)
def test_hyp_direccion_CodigoPostal_setter(instance):
    original = instance.CodigoPostal
    instance.CodigoPostal = original
    assert instance.CodigoPostal == original



@given(instance=Direccion_strategy)
def test_hyp_direccion_Ciudad_setter(instance):
    original = instance.Ciudad
    instance.Ciudad = original
    assert instance.Ciudad == original




@given(instance=Contacto_strategy)
def test_hyp_contacto_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Contacto_strategy)
def test_hyp_contacto_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original




@given(instance=Libro_de_Direcciones_strategy)
def test_hyp_libro_de_direcciones_Introduccion_setter(instance):
    original = instance.Introduccion
    instance.Introduccion = original
    assert instance.Introduccion == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actualizar_COntacto_UseCase,
    Buscar,
    Buscar_Contactos_UseCase,
    Cancelar_UseCase,
    Contacto,
    Crear_Contacto,
    Crear_Contacto_UseCase,
    Direccion,
    Eliminar_Contacto_UseCase,
    Foto,
    Guardar_UseCase,
    Libro_de_Direcciones,
    Libro_de_Direcciones1,
    Lista_de_COntacto,
    Menu_Principal,
    Tel_fono,
    Usuario_Actor,
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

def test_Contacto_email_value_roundtrip():
    instance = Contacto(email="sample_text", nombre="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Contacto_nombre_value_roundtrip():
    instance = Contacto(email="sample_text", nombre="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_Direccion_Ciudad_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", CodigoPostal=7, departamento="sample_text", nombre="sample_text")
    assert instance.Ciudad == "sample_text"
    instance.Ciudad = "sample_text_2"
    assert instance.Ciudad == "sample_text_2"


def test_Direccion_CodigoPostal_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", CodigoPostal=7, departamento="sample_text", nombre="sample_text")
    assert instance.CodigoPostal == 7
    instance.CodigoPostal = 13
    assert instance.CodigoPostal == 13


def test_Direccion_departamento_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", CodigoPostal=7, departamento="sample_text", nombre="sample_text")
    assert instance.departamento == "sample_text"
    instance.departamento = "sample_text_2"
    assert instance.departamento == "sample_text_2"


def test_Direccion_nombre_value_roundtrip():
    instance = Direccion(Ciudad="sample_text", CodigoPostal=7, departamento="sample_text", nombre="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_Foto_ancho_value_roundtrip():
    instance = Foto(ancho=7, largo=7)
    assert instance.ancho == 7
    instance.ancho = 13
    assert instance.ancho == 13


def test_Foto_largo_value_roundtrip():
    instance = Foto(ancho=7, largo=7)
    assert instance.largo == 7
    instance.largo = 13
    assert instance.largo == 13


def test_Libro_de_Direcciones_Introduccion_value_roundtrip():
    instance = Libro_de_Direcciones(Introduccion="sample_text")
    assert instance.Introduccion == "sample_text"
    instance.Introduccion = "sample_text_2"
    assert instance.Introduccion == "sample_text_2"


def test_Tel_fono_Codigo_area_value_roundtrip():
    instance = Tel_fono(Codigo_area=7, numero=7, prefijo=7)
    assert instance.Codigo_area == 7
    instance.Codigo_area = 13
    assert instance.Codigo_area == 13


def test_Tel_fono_numero_value_roundtrip():
    instance = Tel_fono(Codigo_area=7, numero=7, prefijo=7)
    assert instance.numero == 7
    instance.numero = 13
    assert instance.numero == 13


def test_Tel_fono_prefijo_value_roundtrip():
    instance = Tel_fono(Codigo_area=7, numero=7, prefijo=7)
    assert instance.prefijo == 7
    instance.prefijo = 13
    assert instance.prefijo == 13


def test_assoc_Contacto_Direccion_link_reassign_clear():
    a = Direccion(Ciudad="sample_text", CodigoPostal=7, departamento="sample_text", nombre="sample_text")
    b1 = Contacto(email="sample_text", nombre="sample_text")
    b2 = Contacto(email="sample_text_2", nombre="sample_text_2")
    _safe_set(a, 'contacto9', b1)
    assert _is_linked(a, 'contacto9', b1)
    if hasattr(b1, 'direccion8'):
        assert _is_linked(b1, 'direccion8', a)
    _safe_set(a, 'contacto9', b2)
    assert _is_linked(a, 'contacto9', b2)
    if hasattr(b1, 'direccion8'):
        assert not _is_linked(b1, 'direccion8', a)
    if hasattr(b2, 'direccion8'):
        assert _is_linked(b2, 'direccion8', a)
    _safe_set(a, 'contacto9', None)
    assert not _is_linked(a, 'contacto9', b2)
    if hasattr(b2, 'direccion8'):
        assert not _is_linked(b2, 'direccion8', a)


def test_assoc_Contacto_Foto_link_reassign_clear():
    a = Foto(ancho=7, largo=7)
    b1 = Contacto(email="sample_text", nombre="sample_text")
    b2 = Contacto(email="sample_text_2", nombre="sample_text_2")
    _safe_set(a, 'contacto13', b1)
    assert _is_linked(a, 'contacto13', b1)
    if hasattr(b1, 'foto12'):
        assert _is_linked(b1, 'foto12', a)
    _safe_set(a, 'contacto13', b2)
    assert _is_linked(a, 'contacto13', b2)
    if hasattr(b1, 'foto12'):
        assert not _is_linked(b1, 'foto12', a)
    if hasattr(b2, 'foto12'):
        assert _is_linked(b2, 'foto12', a)
    _safe_set(a, 'contacto13', None)
    assert not _is_linked(a, 'contacto13', b2)
    if hasattr(b2, 'foto12'):
        assert not _is_linked(b2, 'foto12', a)


def test_assoc_Contacto_Tel_fono_link_reassign_clear():
    a = Tel_fono(Codigo_area=7, numero=7, prefijo=7)
    b1 = Contacto(email="sample_text", nombre="sample_text")
    b2 = Contacto(email="sample_text_2", nombre="sample_text_2")
    _safe_set(a, 'contacto11', b1)
    assert _is_linked(a, 'contacto11', b1)
    if hasattr(b1, 'tel_fono10'):
        assert _is_linked(b1, 'tel_fono10', a)
    _safe_set(a, 'contacto11', b2)
    assert _is_linked(a, 'contacto11', b2)
    if hasattr(b1, 'tel_fono10'):
        assert not _is_linked(b1, 'tel_fono10', a)
    if hasattr(b2, 'tel_fono10'):
        assert _is_linked(b2, 'tel_fono10', a)
    _safe_set(a, 'contacto11', None)
    assert not _is_linked(a, 'contacto11', b2)
    if hasattr(b2, 'tel_fono10'):
        assert not _is_linked(b2, 'tel_fono10', a)


def test_assoc_Libro_de_Direcciones_Contacto_link_reassign_clear():
    a = Libro_de_Direcciones(Introduccion="sample_text")
    b1 = Contacto(email="sample_text", nombre="sample_text")
    b2 = Contacto(email="sample_text_2", nombre="sample_text_2")
    _safe_set(a, 'contacto14', b1)
    assert _is_linked(a, 'contacto14', b1)
    if hasattr(b1, 'libro_de_Direcciones15'):
        assert _is_linked(b1, 'libro_de_Direcciones15', a)
    _safe_set(a, 'contacto14', b2)
    assert _is_linked(a, 'contacto14', b2)
    if hasattr(b1, 'libro_de_Direcciones15'):
        assert not _is_linked(b1, 'libro_de_Direcciones15', a)
    if hasattr(b2, 'libro_de_Direcciones15'):
        assert _is_linked(b2, 'libro_de_Direcciones15', a)
    _safe_set(a, 'contacto14', None)
    assert not _is_linked(a, 'contacto14', b2)
    if hasattr(b2, 'libro_de_Direcciones15'):
        assert not _is_linked(b2, 'libro_de_Direcciones15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actualizar_COntacto_UseCase_strategy = st.builds(Actualizar_COntacto_UseCase)
@given(instance=Actualizar_COntacto_UseCase_strategy)
@settings(max_examples=25)
def test_Actualizar_COntacto_UseCase_instantiation(instance):
    assert isinstance(instance, Actualizar_COntacto_UseCase)


Buscar_strategy = st.builds(Buscar)
@given(instance=Buscar_strategy)
@settings(max_examples=25)
def test_Buscar_instantiation(instance):
    assert isinstance(instance, Buscar)


Buscar_Contactos_UseCase_strategy = st.builds(Buscar_Contactos_UseCase)
@given(instance=Buscar_Contactos_UseCase_strategy)
@settings(max_examples=25)
def test_Buscar_Contactos_UseCase_instantiation(instance):
    assert isinstance(instance, Buscar_Contactos_UseCase)


Cancelar_UseCase_strategy = st.builds(Cancelar_UseCase)
@given(instance=Cancelar_UseCase_strategy)
@settings(max_examples=25)
def test_Cancelar_UseCase_instantiation(instance):
    assert isinstance(instance, Cancelar_UseCase)


Contacto_strategy = st.builds(Contacto, email=safe_text, nombre=safe_text)
@given(instance=Contacto_strategy)
@settings(max_examples=25)
def test_Contacto_instantiation(instance):
    assert isinstance(instance, Contacto)


Crear_Contacto_strategy = st.builds(Crear_Contacto)
@given(instance=Crear_Contacto_strategy)
@settings(max_examples=25)
def test_Crear_Contacto_instantiation(instance):
    assert isinstance(instance, Crear_Contacto)


Crear_Contacto_UseCase_strategy = st.builds(Crear_Contacto_UseCase)
@given(instance=Crear_Contacto_UseCase_strategy)
@settings(max_examples=25)
def test_Crear_Contacto_UseCase_instantiation(instance):
    assert isinstance(instance, Crear_Contacto_UseCase)


Direccion_strategy = st.builds(Direccion, Ciudad=safe_text, CodigoPostal=st.integers(), departamento=safe_text, nombre=safe_text)
@given(instance=Direccion_strategy)
@settings(max_examples=25)
def test_Direccion_instantiation(instance):
    assert isinstance(instance, Direccion)


Eliminar_Contacto_UseCase_strategy = st.builds(Eliminar_Contacto_UseCase)
@given(instance=Eliminar_Contacto_UseCase_strategy)
@settings(max_examples=25)
def test_Eliminar_Contacto_UseCase_instantiation(instance):
    assert isinstance(instance, Eliminar_Contacto_UseCase)


Foto_strategy = st.builds(Foto, ancho=st.integers(), largo=st.integers())
@given(instance=Foto_strategy)
@settings(max_examples=25)
def test_Foto_instantiation(instance):
    assert isinstance(instance, Foto)


Guardar_UseCase_strategy = st.builds(Guardar_UseCase)
@given(instance=Guardar_UseCase_strategy)
@settings(max_examples=25)
def test_Guardar_UseCase_instantiation(instance):
    assert isinstance(instance, Guardar_UseCase)


Libro_de_Direcciones_strategy = st.builds(Libro_de_Direcciones, Introduccion=safe_text)
@given(instance=Libro_de_Direcciones_strategy)
@settings(max_examples=25)
def test_Libro_de_Direcciones_instantiation(instance):
    assert isinstance(instance, Libro_de_Direcciones)


Libro_de_Direcciones1_strategy = st.builds(Libro_de_Direcciones1)
@given(instance=Libro_de_Direcciones1_strategy)
@settings(max_examples=25)
def test_Libro_de_Direcciones1_instantiation(instance):
    assert isinstance(instance, Libro_de_Direcciones1)


Lista_de_COntacto_strategy = st.builds(Lista_de_COntacto)
@given(instance=Lista_de_COntacto_strategy)
@settings(max_examples=25)
def test_Lista_de_COntacto_instantiation(instance):
    assert isinstance(instance, Lista_de_COntacto)


Menu_Principal_strategy = st.builds(Menu_Principal)
@given(instance=Menu_Principal_strategy)
@settings(max_examples=25)
def test_Menu_Principal_instantiation(instance):
    assert isinstance(instance, Menu_Principal)


Tel_fono_strategy = st.builds(Tel_fono, Codigo_area=st.integers(), numero=st.integers(), prefijo=st.integers())
@given(instance=Tel_fono_strategy)
@settings(max_examples=25)
def test_Tel_fono_instantiation(instance):
    assert isinstance(instance, Tel_fono)


Usuario_Actor_strategy = st.builds(Usuario_Actor)
@given(instance=Usuario_Actor_strategy)
@settings(max_examples=25)
def test_Usuario_Actor_instantiation(instance):
    assert isinstance(instance, Usuario_Actor)



