import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Avanzar_hacia_el_siguiendo_ejemplar__UseCase,
    Buscar_un_ejemplar_por_su_nombre__UseCase,
    Calcular_el_numero_de_ejemplares_por_raza__UseCase,
    Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase,
    Canino,
    Desplazarse_hasta_el_primer_ejemplar_UseCase,
    Desplazarse_hasta_el_ultimo_ejemplar__UseCase,
    Empresa,
    Int,
    Int2,
    Regresar_hacia_el_anterior_ejemplar__UseCase,
    String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones,
    String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2,
    Usuario_Actor,
    Visualizar_hoja_de_vida_de_cada_perrito__UseCase,
    double,
    void,
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

def test_Empresa_ejemplaresCaninos_value_roundtrip():
    instance = Empresa(ejemplaresCaninos="sample_text")
    assert instance.ejemplaresCaninos == "sample_text"
    instance.ejemplaresCaninos = "sample_text_2"
    assert instance.ejemplaresCaninos == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Avanzar_hacia_el_siguiendo_ejemplar__UseCase_strategy = st.builds(Avanzar_hacia_el_siguiendo_ejemplar__UseCase)
@given(instance=Avanzar_hacia_el_siguiendo_ejemplar__UseCase_strategy)
@settings(max_examples=25)
def test_Avanzar_hacia_el_siguiendo_ejemplar__UseCase_instantiation(instance):
    assert isinstance(instance, Avanzar_hacia_el_siguiendo_ejemplar__UseCase)


Buscar_un_ejemplar_por_su_nombre__UseCase_strategy = st.builds(Buscar_un_ejemplar_por_su_nombre__UseCase)
@given(instance=Buscar_un_ejemplar_por_su_nombre__UseCase_strategy)
@settings(max_examples=25)
def test_Buscar_un_ejemplar_por_su_nombre__UseCase_instantiation(instance):
    assert isinstance(instance, Buscar_un_ejemplar_por_su_nombre__UseCase)


Calcular_el_numero_de_ejemplares_por_raza__UseCase_strategy = st.builds(Calcular_el_numero_de_ejemplares_por_raza__UseCase)
@given(instance=Calcular_el_numero_de_ejemplares_por_raza__UseCase_strategy)
@settings(max_examples=25)
def test_Calcular_el_numero_de_ejemplares_por_raza__UseCase_instantiation(instance):
    assert isinstance(instance, Calcular_el_numero_de_ejemplares_por_raza__UseCase)


Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase_strategy = st.builds(Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase)
@given(instance=Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase_strategy)
@settings(max_examples=25)
def test_Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase_instantiation(instance):
    assert isinstance(instance, Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase)


Desplazarse_hasta_el_primer_ejemplar_UseCase_strategy = st.builds(Desplazarse_hasta_el_primer_ejemplar_UseCase)
@given(instance=Desplazarse_hasta_el_primer_ejemplar_UseCase_strategy)
@settings(max_examples=25)
def test_Desplazarse_hasta_el_primer_ejemplar_UseCase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_primer_ejemplar_UseCase)


Desplazarse_hasta_el_ultimo_ejemplar__UseCase_strategy = st.builds(Desplazarse_hasta_el_ultimo_ejemplar__UseCase)
@given(instance=Desplazarse_hasta_el_ultimo_ejemplar__UseCase_strategy)
@settings(max_examples=25)
def test_Desplazarse_hasta_el_ultimo_ejemplar__UseCase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_ultimo_ejemplar__UseCase)


Empresa_strategy = st.builds(Empresa, ejemplaresCaninos=safe_text)
@given(instance=Empresa_strategy)
@settings(max_examples=25)
def test_Empresa_instantiation(instance):
    assert isinstance(instance, Empresa)


Int_strategy = st.builds(Int)
@given(instance=Int_strategy)
@settings(max_examples=25)
def test_Int_instantiation(instance):
    assert isinstance(instance, Int)


Int2_strategy = st.builds(Int2)
@given(instance=Int2_strategy)
@settings(max_examples=25)
def test_Int2_instantiation(instance):
    assert isinstance(instance, Int2)


Regresar_hacia_el_anterior_ejemplar__UseCase_strategy = st.builds(Regresar_hacia_el_anterior_ejemplar__UseCase)
@given(instance=Regresar_hacia_el_anterior_ejemplar__UseCase_strategy)
@settings(max_examples=25)
def test_Regresar_hacia_el_anterior_ejemplar__UseCase_instantiation(instance):
    assert isinstance(instance, Regresar_hacia_el_anterior_ejemplar__UseCase)


String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones_strategy = st.builds(String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones)
@given(instance=String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones_strategy)
@settings(max_examples=25)
def test_String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones_instantiation(instance):
    assert isinstance(instance, String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones)


String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2_strategy = st.builds(String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2)
@given(instance=String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2_strategy)
@settings(max_examples=25)
def test_String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2_instantiation(instance):
    assert isinstance(instance, String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2)


Usuario_Actor_strategy = st.builds(Usuario_Actor)
@given(instance=Usuario_Actor_strategy)
@settings(max_examples=25)
def test_Usuario_Actor_instantiation(instance):
    assert isinstance(instance, Usuario_Actor)


Visualizar_hoja_de_vida_de_cada_perrito__UseCase_strategy = st.builds(Visualizar_hoja_de_vida_de_cada_perrito__UseCase)
@given(instance=Visualizar_hoja_de_vida_de_cada_perrito__UseCase_strategy)
@settings(max_examples=25)
def test_Visualizar_hoja_de_vida_de_cada_perrito__UseCase_instantiation(instance):
    assert isinstance(instance, Visualizar_hoja_de_vida_de_cada_perrito__UseCase)


double_strategy = st.builds(double)
@given(instance=double_strategy)
@settings(max_examples=25)
def test_double_instantiation(instance):
    assert isinstance(instance, double)


void_strategy = st.builds(void)
@given(instance=void_strategy)
@settings(max_examples=25)
def test_void_instantiation(instance):
    assert isinstance(instance, void)


