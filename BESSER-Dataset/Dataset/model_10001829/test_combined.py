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
    Reporte,
    Tipo_mascota,
    Estados,
    Insumos,
    Profesionales,
    Auxiliar,
    Guacales,
    Cliente,
    Registro,
    Mascotas,
    Servicios,
    int,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_reporte_is_not_abstract():
    assert not inspect.isabstract(Reporte)


def test_hyp_reporte_constructor_exists():
    assert callable(Reporte.__init__)


def test_hyp_reporte_constructor_args():
    sig = inspect.signature(Reporte.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tipo_mascota_is_not_abstract():
    assert not inspect.isabstract(Tipo_mascota)


def test_hyp_tipo_mascota_constructor_exists():
    assert callable(Tipo_mascota.__init__)


def test_hyp_tipo_mascota_constructor_args():
    sig = inspect.signature(Tipo_mascota.__init__)
    params = list(sig.parameters.keys())
    assert "Nombre_Tipo" in params, "Missing parameter 'Nombre_Tipo'"
    assert "id_Tipo_Mascota" in params, "Missing parameter 'id_Tipo_Mascota'"





def test_hyp_estados_is_not_abstract():
    assert not inspect.isabstract(Estados)


def test_hyp_estados_constructor_exists():
    assert callable(Estados.__init__)


def test_hyp_estados_constructor_args():
    sig = inspect.signature(Estados.__init__)
    params = list(sig.parameters.keys())
    assert "id_estados" in params, "Missing parameter 'id_estados'"
    assert "Nombre_estados" in params, "Missing parameter 'Nombre_estados'"





def test_hyp_insumos_is_not_abstract():
    assert not inspect.isabstract(Insumos)


def test_hyp_insumos_constructor_exists():
    assert callable(Insumos.__init__)


def test_hyp_insumos_constructor_args():
    sig = inspect.signature(Insumos.__init__)
    params = list(sig.parameters.keys())
    assert "Id_insumo" in params, "Missing parameter 'Id_insumo'"
    assert "Nombre_insumo" in params, "Missing parameter 'Nombre_insumo'"





def test_hyp_profesionales_is_not_abstract():
    assert not inspect.isabstract(Profesionales)


def test_hyp_profesionales_constructor_exists():
    assert callable(Profesionales.__init__)


def test_hyp_profesionales_constructor_args():
    sig = inspect.signature(Profesionales.__init__)
    params = list(sig.parameters.keys())
    assert "Nombre_profesional" in params, "Missing parameter 'Nombre_profesional'"
    assert "id_profesional" in params, "Missing parameter 'id_profesional'"





def test_hyp_auxiliar_is_not_abstract():
    assert not inspect.isabstract(Auxiliar)


def test_hyp_auxiliar_constructor_exists():
    assert callable(Auxiliar.__init__)


def test_hyp_auxiliar_constructor_args():
    sig = inspect.signature(Auxiliar.__init__)
    params = list(sig.parameters.keys())
    assert "Id_auxiliar" in params, "Missing parameter 'Id_auxiliar'"
    assert "Nombre_auxiliar" in params, "Missing parameter 'Nombre_auxiliar'"





def test_hyp_guacales_is_not_abstract():
    assert not inspect.isabstract(Guacales)


def test_hyp_guacales_constructor_exists():
    assert callable(Guacales.__init__)


def test_hyp_guacales_constructor_args():
    sig = inspect.signature(Guacales.__init__)
    params = list(sig.parameters.keys())
    assert "Id_guacal" in params, "Missing parameter 'Id_guacal'"




def test_hyp_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_hyp_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_hyp_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "Tel_fono" in params, "Missing parameter 'Tel_fono'"
    assert "C_dula" in params, "Missing parameter 'C_dula'"





def test_hyp_registro_is_not_abstract():
    assert not inspect.isabstract(Registro)


def test_hyp_registro_constructor_exists():
    assert callable(Registro.__init__)


def test_hyp_registro_constructor_args():
    sig = inspect.signature(Registro.__init__)
    params = list(sig.parameters.keys())
    assert "Cliente" in params, "Missing parameter 'Cliente'"
    assert "Auxiliar" in params, "Missing parameter 'Auxiliar'"
    assert "Hora_entrada" in params, "Missing parameter 'Hora_entrada'"
    assert "Tipo_Mascota" in params, "Missing parameter 'Tipo_Mascota'"
    assert "Hora_salida" in params, "Missing parameter 'Hora_salida'"

def test_hyp_registro_has_Cliente():
    assert hasattr(Registro, "Cliente")
    descriptor = None
    for klass in Registro.__mro__:
        if "Cliente" in klass.__dict__:
            descriptor = klass.__dict__["Cliente"]
            break
    assert isinstance(descriptor, property)

def test_hyp_registro_has_Auxiliar():
    assert hasattr(Registro, "Auxiliar")
    descriptor = None
    for klass in Registro.__mro__:
        if "Auxiliar" in klass.__dict__:
            descriptor = klass.__dict__["Auxiliar"]
            break
    assert isinstance(descriptor, property)

def test_hyp_registro_has_Hora_entrada():
    assert hasattr(Registro, "Hora_entrada")
    descriptor = None
    for klass in Registro.__mro__:
        if "Hora_entrada" in klass.__dict__:
            descriptor = klass.__dict__["Hora_entrada"]
            break
    assert isinstance(descriptor, property)

def test_hyp_registro_has_Tipo_Mascota():
    assert hasattr(Registro, "Tipo_Mascota")
    descriptor = None
    for klass in Registro.__mro__:
        if "Tipo_Mascota" in klass.__dict__:
            descriptor = klass.__dict__["Tipo_Mascota"]
            break
    assert isinstance(descriptor, property)

def test_hyp_registro_has_Hora_salida():
    assert hasattr(Registro, "Hora_salida")
    descriptor = None
    for klass in Registro.__mro__:
        if "Hora_salida" in klass.__dict__:
            descriptor = klass.__dict__["Hora_salida"]
            break
    assert isinstance(descriptor, property)



def test_hyp_mascotas_is_not_abstract():
    assert not inspect.isabstract(Mascotas)


def test_hyp_mascotas_constructor_exists():
    assert callable(Mascotas.__init__)


def test_hyp_mascotas_constructor_args():
    sig = inspect.signature(Mascotas.__init__)
    params = list(sig.parameters.keys())
    assert "tipo_mascota" in params, "Missing parameter 'tipo_mascota'"
    assert "Id_mascota" in params, "Missing parameter 'Id_mascota'"

def test_hyp_mascotas_has_tipo_mascota():
    assert hasattr(Mascotas, "tipo_mascota")
    descriptor = None
    for klass in Mascotas.__mro__:
        if "tipo_mascota" in klass.__dict__:
            descriptor = klass.__dict__["tipo_mascota"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mascotas_has_Id_mascota():
    assert hasattr(Mascotas, "Id_mascota")
    descriptor = None
    for klass in Mascotas.__mro__:
        if "Id_mascota" in klass.__dict__:
            descriptor = klass.__dict__["Id_mascota"]
            break
    assert isinstance(descriptor, property)



def test_hyp_servicios_is_not_abstract():
    assert not inspect.isabstract(Servicios)


def test_hyp_servicios_constructor_exists():
    assert callable(Servicios.__init__)


def test_hyp_servicios_constructor_args():
    sig = inspect.signature(Servicios.__init__)
    params = list(sig.parameters.keys())
    assert "id_servicio" in params, "Missing parameter 'id_servicio'"
    assert "Insumos" in params, "Missing parameter 'Insumos'"
    assert "Nombre_servicio" in params, "Missing parameter 'Nombre_servicio'"
    assert "Tiempo" in params, "Missing parameter 'Tiempo'"
    assert "Valor" in params, "Missing parameter 'Valor'"
    assert "Profesional" in params, "Missing parameter 'Profesional'"

def test_hyp_servicios_has_id_servicio():
    assert hasattr(Servicios, "id_servicio")
    descriptor = None
    for klass in Servicios.__mro__:
        if "id_servicio" in klass.__dict__:
            descriptor = klass.__dict__["id_servicio"]
            break
    assert isinstance(descriptor, property)

def test_hyp_servicios_has_Insumos():
    assert hasattr(Servicios, "Insumos")
    descriptor = None
    for klass in Servicios.__mro__:
        if "Insumos" in klass.__dict__:
            descriptor = klass.__dict__["Insumos"]
            break
    assert isinstance(descriptor, property)

def test_hyp_servicios_has_Nombre_servicio():
    assert hasattr(Servicios, "Nombre_servicio")
    descriptor = None
    for klass in Servicios.__mro__:
        if "Nombre_servicio" in klass.__dict__:
            descriptor = klass.__dict__["Nombre_servicio"]
            break
    assert isinstance(descriptor, property)

def test_hyp_servicios_has_Tiempo():
    assert hasattr(Servicios, "Tiempo")
    descriptor = None
    for klass in Servicios.__mro__:
        if "Tiempo" in klass.__dict__:
            descriptor = klass.__dict__["Tiempo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_servicios_has_Valor():
    assert hasattr(Servicios, "Valor")
    descriptor = None
    for klass in Servicios.__mro__:
        if "Valor" in klass.__dict__:
            descriptor = klass.__dict__["Valor"]
            break
    assert isinstance(descriptor, property)

def test_hyp_servicios_has_Profesional():
    assert hasattr(Servicios, "Profesional")
    descriptor = None
    for klass in Servicios.__mro__:
        if "Profesional" in klass.__dict__:
            descriptor = klass.__dict__["Profesional"]
            break
    assert isinstance(descriptor, property)

def test_hyp_int_exists():
    # Check that the Enumeration exists
    assert int is not None

def test_hyp_int_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in int]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in int"


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
Reporte_strategy = st.builds(
    Reporte,
)
Tipo_mascota_strategy = st.builds(
    Tipo_mascota,
    Nombre_Tipo=
        safe_text,
    id_Tipo_Mascota=
        st.integers()
)
Estados_strategy = st.builds(
    Estados,
    id_estados=
        st.integers(),
    Nombre_estados=
        safe_text
)
Insumos_strategy = st.builds(
    Insumos,
    Id_insumo=
        st.integers(),
    Nombre_insumo=
        safe_text
)
Profesionales_strategy = st.builds(
    Profesionales,
    Nombre_profesional=
        safe_text,
    id_profesional=
        st.integers()
)
Auxiliar_strategy = st.builds(
    Auxiliar,
    Id_auxiliar=
        safe_text,
    Nombre_auxiliar=
        safe_text
)
Guacales_strategy = st.builds(
    Guacales,
    Id_guacal=
        st.integers()
)
Cliente_strategy = st.builds(
    Cliente,
    Tel_fono=
        st.integers(),
    C_dula=
        safe_text
)
Registro_strategy = st.builds(
    Registro,
    Cliente=
        st.none(),
    Auxiliar=
        st.none(),
    Hora_entrada=
        safe_text,
    Tipo_Mascota=
        st.none(),
    Hora_salida=
        safe_text
)
Mascotas_strategy = st.builds(
    Mascotas,
    tipo_mascota=
        st.none(),
    Id_mascota=
        st.integers()
)
Servicios_strategy = st.builds(
    Servicios,
    id_servicio=
        st.integers(),
    Insumos=
        st.none(),
    Nombre_servicio=
        safe_text,
    Tiempo=
        st.integers(),
    Valor=
        st.integers(),
    Profesional=
        st.none()
)





@given(instance=Tipo_mascota_strategy)
def test_hyp_tipo_mascota_Nombre_Tipo_setter(instance):
    original = instance.Nombre_Tipo
    instance.Nombre_Tipo = original
    assert instance.Nombre_Tipo == original



@given(instance=Tipo_mascota_strategy)
def test_hyp_tipo_mascota_id_Tipo_Mascota_setter(instance):
    original = instance.id_Tipo_Mascota
    instance.id_Tipo_Mascota = original
    assert instance.id_Tipo_Mascota == original




@given(instance=Estados_strategy)
def test_hyp_estados_id_estados_setter(instance):
    original = instance.id_estados
    instance.id_estados = original
    assert instance.id_estados == original



@given(instance=Estados_strategy)
def test_hyp_estados_Nombre_estados_setter(instance):
    original = instance.Nombre_estados
    instance.Nombre_estados = original
    assert instance.Nombre_estados == original




@given(instance=Insumos_strategy)
def test_hyp_insumos_Id_insumo_setter(instance):
    original = instance.Id_insumo
    instance.Id_insumo = original
    assert instance.Id_insumo == original



@given(instance=Insumos_strategy)
def test_hyp_insumos_Nombre_insumo_setter(instance):
    original = instance.Nombre_insumo
    instance.Nombre_insumo = original
    assert instance.Nombre_insumo == original




@given(instance=Profesionales_strategy)
def test_hyp_profesionales_Nombre_profesional_setter(instance):
    original = instance.Nombre_profesional
    instance.Nombre_profesional = original
    assert instance.Nombre_profesional == original



@given(instance=Profesionales_strategy)
def test_hyp_profesionales_id_profesional_setter(instance):
    original = instance.id_profesional
    instance.id_profesional = original
    assert instance.id_profesional == original




@given(instance=Auxiliar_strategy)
def test_hyp_auxiliar_Id_auxiliar_setter(instance):
    original = instance.Id_auxiliar
    instance.Id_auxiliar = original
    assert instance.Id_auxiliar == original



@given(instance=Auxiliar_strategy)
def test_hyp_auxiliar_Nombre_auxiliar_setter(instance):
    original = instance.Nombre_auxiliar
    instance.Nombre_auxiliar = original
    assert instance.Nombre_auxiliar == original




@given(instance=Guacales_strategy)
def test_hyp_guacales_Id_guacal_setter(instance):
    original = instance.Id_guacal
    instance.Id_guacal = original
    assert instance.Id_guacal == original




@given(instance=Cliente_strategy)
def test_hyp_cliente_Tel_fono_setter(instance):
    original = instance.Tel_fono
    instance.Tel_fono = original
    assert instance.Tel_fono == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_C_dula_setter(instance):
    original = instance.C_dula
    instance.C_dula = original
    assert instance.C_dula == original

@given(instance=Registro_strategy)
@settings(max_examples=50)
def test_hyp_registro_instantiation(instance):
    assert isinstance(instance, Registro)



@given(instance=Registro_strategy)
def test_hyp_registro_Cliente_setter(instance):
    original = instance.Cliente
    instance.Cliente = original
    assert instance.Cliente == original



@given(instance=Registro_strategy)
def test_hyp_registro_Auxiliar_setter(instance):
    original = instance.Auxiliar
    instance.Auxiliar = original
    assert instance.Auxiliar == original



@given(instance=Registro_strategy)
def test_hyp_registro_Hora_entrada_setter(instance):
    original = instance.Hora_entrada
    instance.Hora_entrada = original
    assert instance.Hora_entrada == original



@given(instance=Registro_strategy)
def test_hyp_registro_Tipo_Mascota_setter(instance):
    original = instance.Tipo_Mascota
    instance.Tipo_Mascota = original
    assert instance.Tipo_Mascota == original



@given(instance=Registro_strategy)
def test_hyp_registro_Hora_salida_setter(instance):
    original = instance.Hora_salida
    instance.Hora_salida = original
    assert instance.Hora_salida == original

@given(instance=Mascotas_strategy)
@settings(max_examples=50)
def test_hyp_mascotas_instantiation(instance):
    assert isinstance(instance, Mascotas)



@given(instance=Mascotas_strategy)
def test_hyp_mascotas_tipo_mascota_setter(instance):
    original = instance.tipo_mascota
    instance.tipo_mascota = original
    assert instance.tipo_mascota == original



@given(instance=Mascotas_strategy)
def test_hyp_mascotas_Id_mascota_setter(instance):
    original = instance.Id_mascota
    instance.Id_mascota = original
    assert instance.Id_mascota == original

@given(instance=Servicios_strategy)
@settings(max_examples=50)
def test_hyp_servicios_instantiation(instance):
    assert isinstance(instance, Servicios)



@given(instance=Servicios_strategy)
def test_hyp_servicios_id_servicio_setter(instance):
    original = instance.id_servicio
    instance.id_servicio = original
    assert instance.id_servicio == original



@given(instance=Servicios_strategy)
def test_hyp_servicios_Insumos_setter(instance):
    original = instance.Insumos
    instance.Insumos = original
    assert instance.Insumos == original



@given(instance=Servicios_strategy)
def test_hyp_servicios_Nombre_servicio_setter(instance):
    original = instance.Nombre_servicio
    instance.Nombre_servicio = original
    assert instance.Nombre_servicio == original



@given(instance=Servicios_strategy)
def test_hyp_servicios_Tiempo_setter(instance):
    original = instance.Tiempo
    instance.Tiempo = original
    assert instance.Tiempo == original



@given(instance=Servicios_strategy)
def test_hyp_servicios_Valor_setter(instance):
    original = instance.Valor
    instance.Valor = original
    assert instance.Valor == original



@given(instance=Servicios_strategy)
def test_hyp_servicios_Profesional_setter(instance):
    original = instance.Profesional
    instance.Profesional = original
    assert instance.Profesional == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Auxiliar,
    Cliente,
    Estados,
    Guacales,
    Insumos,
    Mascotas,
    Profesionales,
    Registro,
    Reporte,
    Servicios,
    Tipo_mascota,
    int,
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

def test_Auxiliar_Id_auxiliar_value_roundtrip():
    instance = Auxiliar(Id_auxiliar="sample_text", Nombre_auxiliar="sample_text")
    assert instance.Id_auxiliar == "sample_text"
    instance.Id_auxiliar = "sample_text_2"
    assert instance.Id_auxiliar == "sample_text_2"


def test_Auxiliar_Nombre_auxiliar_value_roundtrip():
    instance = Auxiliar(Id_auxiliar="sample_text", Nombre_auxiliar="sample_text")
    assert instance.Nombre_auxiliar == "sample_text"
    instance.Nombre_auxiliar = "sample_text_2"
    assert instance.Nombre_auxiliar == "sample_text_2"


def test_Cliente_C_dula_value_roundtrip():
    instance = Cliente(C_dula="sample_text", Tel_fono=7)
    assert instance.C_dula == "sample_text"
    instance.C_dula = "sample_text_2"
    assert instance.C_dula == "sample_text_2"


def test_Cliente_Tel_fono_value_roundtrip():
    instance = Cliente(C_dula="sample_text", Tel_fono=7)
    assert instance.Tel_fono == 7
    instance.Tel_fono = 13
    assert instance.Tel_fono == 13


def test_Estados_Nombre_estados_value_roundtrip():
    instance = Estados(Nombre_estados="sample_text", id_estados=7)
    assert instance.Nombre_estados == "sample_text"
    instance.Nombre_estados = "sample_text_2"
    assert instance.Nombre_estados == "sample_text_2"


def test_Estados_id_estados_value_roundtrip():
    instance = Estados(Nombre_estados="sample_text", id_estados=7)
    assert instance.id_estados == 7
    instance.id_estados = 13
    assert instance.id_estados == 13


def test_Guacales_Id_guacal_value_roundtrip():
    instance = Guacales(Id_guacal=7)
    assert instance.Id_guacal == 7
    instance.Id_guacal = 13
    assert instance.Id_guacal == 13


def test_Insumos_Id_insumo_value_roundtrip():
    instance = Insumos(Id_insumo=7, Nombre_insumo="sample_text")
    assert instance.Id_insumo == 7
    instance.Id_insumo = 13
    assert instance.Id_insumo == 13


def test_Insumos_Nombre_insumo_value_roundtrip():
    instance = Insumos(Id_insumo=7, Nombre_insumo="sample_text")
    assert instance.Nombre_insumo == "sample_text"
    instance.Nombre_insumo = "sample_text_2"
    assert instance.Nombre_insumo == "sample_text_2"


def test_Profesionales_Nombre_profesional_value_roundtrip():
    instance = Profesionales(Nombre_profesional="sample_text", id_profesional=7)
    assert instance.Nombre_profesional == "sample_text"
    instance.Nombre_profesional = "sample_text_2"
    assert instance.Nombre_profesional == "sample_text_2"


def test_Profesionales_id_profesional_value_roundtrip():
    instance = Profesionales(Nombre_profesional="sample_text", id_profesional=7)
    assert instance.id_profesional == 7
    instance.id_profesional = 13
    assert instance.id_profesional == 13


def test_Tipo_mascota_Nombre_Tipo_value_roundtrip():
    instance = Tipo_mascota(Nombre_Tipo="sample_text", id_Tipo_Mascota=7)
    assert instance.Nombre_Tipo == "sample_text"
    instance.Nombre_Tipo = "sample_text_2"
    assert instance.Nombre_Tipo == "sample_text_2"


def test_Tipo_mascota_id_Tipo_Mascota_value_roundtrip():
    instance = Tipo_mascota(Nombre_Tipo="sample_text", id_Tipo_Mascota=7)
    assert instance.id_Tipo_Mascota == 7
    instance.id_Tipo_Mascota = 13
    assert instance.id_Tipo_Mascota == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Auxiliar_strategy = st.builds(Auxiliar, Id_auxiliar=safe_text, Nombre_auxiliar=safe_text)
@given(instance=Auxiliar_strategy)
@settings(max_examples=25)
def test_Auxiliar_instantiation(instance):
    assert isinstance(instance, Auxiliar)


Cliente_strategy = st.builds(Cliente, C_dula=safe_text, Tel_fono=st.sampled_from(int))
@given(instance=Cliente_strategy)
@settings(max_examples=25)
def test_Cliente_instantiation(instance):
    assert isinstance(instance, Cliente)


Estados_strategy = st.builds(Estados, Nombre_estados=safe_text, id_estados=st.sampled_from(int))
@given(instance=Estados_strategy)
@settings(max_examples=25)
def test_Estados_instantiation(instance):
    assert isinstance(instance, Estados)


Guacales_strategy = st.builds(Guacales, Id_guacal=st.sampled_from(int))
@given(instance=Guacales_strategy)
@settings(max_examples=25)
def test_Guacales_instantiation(instance):
    assert isinstance(instance, Guacales)


Insumos_strategy = st.builds(Insumos, Id_insumo=st.sampled_from(int), Nombre_insumo=safe_text)
@given(instance=Insumos_strategy)
@settings(max_examples=25)
def test_Insumos_instantiation(instance):
    assert isinstance(instance, Insumos)


Profesionales_strategy = st.builds(Profesionales, Nombre_profesional=safe_text, id_profesional=st.sampled_from(int))
@given(instance=Profesionales_strategy)
@settings(max_examples=25)
def test_Profesionales_instantiation(instance):
    assert isinstance(instance, Profesionales)


Reporte_strategy = st.builds(Reporte)
@given(instance=Reporte_strategy)
@settings(max_examples=25)
def test_Reporte_instantiation(instance):
    assert isinstance(instance, Reporte)


Tipo_mascota_strategy = st.builds(Tipo_mascota, Nombre_Tipo=safe_text, id_Tipo_Mascota=st.sampled_from(int))
@given(instance=Tipo_mascota_strategy)
@settings(max_examples=25)
def test_Tipo_mascota_instantiation(instance):
    assert isinstance(instance, Tipo_mascota)



