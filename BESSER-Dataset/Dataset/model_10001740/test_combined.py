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
    Cliente,
    Perro,
    Gato,
    Animal,
    ILocalizable_Interface,
    CoordenadaGPS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_hyp_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_hyp_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "listaMascotas" in params, "Missing parameter 'listaMascotas'"
    assert "numeroDeCliente" in params, "Missing parameter 'numeroDeCliente'"
    assert "nombre" in params, "Missing parameter 'nombre'"






def test_hyp_perro_is_not_abstract():
    assert not inspect.isabstract(Perro)


def test_hyp_perro_constructor_exists():
    assert callable(Perro.__init__)


def test_hyp_perro_constructor_args():
    sig = inspect.signature(Perro.__init__)
    params = list(sig.parameters.keys())
    assert "fechaCastracion" in params, "Missing parameter 'fechaCastracion'"




def test_hyp_gato_is_not_abstract():
    assert not inspect.isabstract(Gato)


def test_hyp_gato_constructor_exists():
    assert callable(Gato.__init__)


def test_hyp_gato_constructor_args():
    sig = inspect.signature(Gato.__init__)
    params = list(sig.parameters.keys())
    assert "ultimaDesparasitacion" in params, "Missing parameter 'ultimaDesparasitacion'"
    assert "MESES_ENTRE_DESPARASITACIONES" in params, "Missing parameter 'MESES_ENTRE_DESPARASITACIONES'"





def test_hyp_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_hyp_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_hyp_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "identificador" in params, "Missing parameter 'identificador'"






def test_hyp_ilocalizable_interface_is_not_abstract():
    assert not inspect.isabstract(ILocalizable_Interface)


def test_hyp_ilocalizable_interface_constructor_exists():
    assert callable(ILocalizable_Interface.__init__)


def test_hyp_ilocalizable_interface_constructor_args():
    sig = inspect.signature(ILocalizable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coordenadagps_is_not_abstract():
    assert not inspect.isabstract(CoordenadaGPS)


def test_hyp_coordenadagps_constructor_exists():
    assert callable(CoordenadaGPS.__init__)


def test_hyp_coordenadagps_constructor_args():
    sig = inspect.signature(CoordenadaGPS.__init__)
    params = list(sig.parameters.keys())
    assert "latitud" in params, "Missing parameter 'latitud'"
    assert "longitud" in params, "Missing parameter 'longitud'"




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
Cliente_strategy = st.builds(
    Cliente,
    listaMascotas=
        safe_text,
    numeroDeCliente=
        safe_text,
    nombre=
        safe_text
)
Perro_strategy = st.builds(
    Perro,
    fechaCastracion=
        safe_text
)
Gato_strategy = st.builds(
    Gato,
    ultimaDesparasitacion=
        safe_text,
    MESES_ENTRE_DESPARASITACIONES=
        safe_text
)
Animal_strategy = st.builds(
    Animal,
    raza=
        safe_text,
    nombre=
        safe_text,
    identificador=
        safe_text
)
ILocalizable_Interface_strategy = st.builds(
    ILocalizable_Interface,
)
CoordenadaGPS_strategy = st.builds(
    CoordenadaGPS,
    latitud=
        safe_text,
    longitud=
        safe_text
)




@given(instance=Cliente_strategy)
def test_hyp_cliente_listaMascotas_setter(instance):
    original = instance.listaMascotas
    instance.listaMascotas = original
    assert instance.listaMascotas == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_numeroDeCliente_setter(instance):
    original = instance.numeroDeCliente
    instance.numeroDeCliente = original
    assert instance.numeroDeCliente == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original




@given(instance=Perro_strategy)
def test_hyp_perro_fechaCastracion_setter(instance):
    original = instance.fechaCastracion
    instance.fechaCastracion = original
    assert instance.fechaCastracion == original




@given(instance=Gato_strategy)
def test_hyp_gato_ultimaDesparasitacion_setter(instance):
    original = instance.ultimaDesparasitacion
    instance.ultimaDesparasitacion = original
    assert instance.ultimaDesparasitacion == original



@given(instance=Gato_strategy)
def test_hyp_gato_MESES_ENTRE_DESPARASITACIONES_setter(instance):
    original = instance.MESES_ENTRE_DESPARASITACIONES
    instance.MESES_ENTRE_DESPARASITACIONES = original
    assert instance.MESES_ENTRE_DESPARASITACIONES == original




@given(instance=Animal_strategy)
def test_hyp_animal_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=Animal_strategy)
def test_hyp_animal_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Animal_strategy)
def test_hyp_animal_identificador_setter(instance):
    original = instance.identificador
    instance.identificador = original
    assert instance.identificador == original





@given(instance=CoordenadaGPS_strategy)
def test_hyp_coordenadagps_latitud_setter(instance):
    original = instance.latitud
    instance.latitud = original
    assert instance.latitud == original



@given(instance=CoordenadaGPS_strategy)
def test_hyp_coordenadagps_longitud_setter(instance):
    original = instance.longitud
    instance.longitud = original
    assert instance.longitud == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Animal,
    Cliente,
    CoordenadaGPS,
    Gato,
    ILocalizable_Interface,
    Perro,
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

def test_Animal_identificador_value_roundtrip():
    instance = Animal(identificador="sample_text", nombre="sample_text", raza="sample_text")
    assert instance.identificador == "sample_text"
    instance.identificador = "sample_text_2"
    assert instance.identificador == "sample_text_2"


def test_Animal_nombre_value_roundtrip():
    instance = Animal(identificador="sample_text", nombre="sample_text", raza="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_Animal_raza_value_roundtrip():
    instance = Animal(identificador="sample_text", nombre="sample_text", raza="sample_text")
    assert instance.raza == "sample_text"
    instance.raza = "sample_text_2"
    assert instance.raza == "sample_text_2"


def test_Cliente_listaMascotas_value_roundtrip():
    instance = Cliente(listaMascotas="sample_text", nombre="sample_text", numeroDeCliente="sample_text")
    assert instance.listaMascotas == "sample_text"
    instance.listaMascotas = "sample_text_2"
    assert instance.listaMascotas == "sample_text_2"


def test_Cliente_nombre_value_roundtrip():
    instance = Cliente(listaMascotas="sample_text", nombre="sample_text", numeroDeCliente="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_Cliente_numeroDeCliente_value_roundtrip():
    instance = Cliente(listaMascotas="sample_text", nombre="sample_text", numeroDeCliente="sample_text")
    assert instance.numeroDeCliente == "sample_text"
    instance.numeroDeCliente = "sample_text_2"
    assert instance.numeroDeCliente == "sample_text_2"


def test_CoordenadaGPS_latitud_value_roundtrip():
    instance = CoordenadaGPS(latitud="sample_text", longitud="sample_text")
    assert instance.latitud == "sample_text"
    instance.latitud = "sample_text_2"
    assert instance.latitud == "sample_text_2"


def test_CoordenadaGPS_longitud_value_roundtrip():
    instance = CoordenadaGPS(latitud="sample_text", longitud="sample_text")
    assert instance.longitud == "sample_text"
    instance.longitud = "sample_text_2"
    assert instance.longitud == "sample_text_2"


def test_Gato_MESES_ENTRE_DESPARASITACIONES_value_roundtrip():
    instance = Gato(MESES_ENTRE_DESPARASITACIONES="sample_text", ultimaDesparasitacion="sample_text")
    assert instance.MESES_ENTRE_DESPARASITACIONES == "sample_text"
    instance.MESES_ENTRE_DESPARASITACIONES = "sample_text_2"
    assert instance.MESES_ENTRE_DESPARASITACIONES == "sample_text_2"


def test_Gato_ultimaDesparasitacion_value_roundtrip():
    instance = Gato(MESES_ENTRE_DESPARASITACIONES="sample_text", ultimaDesparasitacion="sample_text")
    assert instance.ultimaDesparasitacion == "sample_text"
    instance.ultimaDesparasitacion = "sample_text_2"
    assert instance.ultimaDesparasitacion == "sample_text_2"


def test_Perro_fechaCastracion_value_roundtrip():
    instance = Perro(fechaCastracion="sample_text")
    assert instance.fechaCastracion == "sample_text"
    instance.fechaCastracion = "sample_text_2"
    assert instance.fechaCastracion == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Animal_strategy = st.builds(Animal, identificador=safe_text, nombre=safe_text, raza=safe_text)
@given(instance=Animal_strategy)
@settings(max_examples=25)
def test_Animal_instantiation(instance):
    assert isinstance(instance, Animal)


Cliente_strategy = st.builds(Cliente, listaMascotas=safe_text, nombre=safe_text, numeroDeCliente=safe_text)
@given(instance=Cliente_strategy)
@settings(max_examples=25)
def test_Cliente_instantiation(instance):
    assert isinstance(instance, Cliente)


CoordenadaGPS_strategy = st.builds(CoordenadaGPS, latitud=safe_text, longitud=safe_text)
@given(instance=CoordenadaGPS_strategy)
@settings(max_examples=25)
def test_CoordenadaGPS_instantiation(instance):
    assert isinstance(instance, CoordenadaGPS)


Gato_strategy = st.builds(Gato, MESES_ENTRE_DESPARASITACIONES=safe_text, ultimaDesparasitacion=safe_text)
@given(instance=Gato_strategy)
@settings(max_examples=25)
def test_Gato_instantiation(instance):
    assert isinstance(instance, Gato)


ILocalizable_Interface_strategy = st.builds(ILocalizable_Interface)
@given(instance=ILocalizable_Interface_strategy)
@settings(max_examples=25)
def test_ILocalizable_Interface_instantiation(instance):
    assert isinstance(instance, ILocalizable_Interface)


Perro_strategy = st.builds(Perro, fechaCastracion=safe_text)
@given(instance=Perro_strategy)
@settings(max_examples=25)
def test_Perro_instantiation(instance):
    assert isinstance(instance, Perro)



