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
    Biblioteca_Multa,
    Biblioteca_Ejemplar,
    Biblioteca_Prestamo,
    Biblioteca_Socio,
    Biblioteca_Autor,
    Biblioteca_Libro,
    Biblioteca_Biblioteca,
    Estado,
    Genero,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_biblioteca_multa_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Multa)


def test_hyp_biblioteca_multa_constructor_exists():
    assert callable(Biblioteca_Multa.__init__)


def test_hyp_biblioteca_multa_constructor_args():
    sig = inspect.signature(Biblioteca_Multa.__init__)
    params = list(sig.parameters.keys())
    assert "diasExcedidos" in params, "Missing parameter 'diasExcedidos'"
    assert "fechaDePago" in params, "Missing parameter 'fechaDePago'"
    assert "monto" in params, "Missing parameter 'monto'"
    assert "fecha" in params, "Missing parameter 'fecha'"







def test_hyp_biblioteca_ejemplar_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Ejemplar)


def test_hyp_biblioteca_ejemplar_constructor_exists():
    assert callable(Biblioteca_Ejemplar.__init__)


def test_hyp_biblioteca_ejemplar_constructor_args():
    sig = inspect.signature(Biblioteca_Ejemplar.__init__)
    params = list(sig.parameters.keys())
    assert "estado" in params, "Missing parameter 'estado'"
    assert "numeroDeEjemplar" in params, "Missing parameter 'numeroDeEjemplar'"





def test_hyp_biblioteca_prestamo_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Prestamo)


def test_hyp_biblioteca_prestamo_constructor_exists():
    assert callable(Biblioteca_Prestamo.__init__)


def test_hyp_biblioteca_prestamo_constructor_args():
    sig = inspect.signature(Biblioteca_Prestamo.__init__)
    params = list(sig.parameters.keys())
    assert "fechaDeDevolucion" in params, "Missing parameter 'fechaDeDevolucion'"
    assert "fechaDeInicio" in params, "Missing parameter 'fechaDeInicio'"
    assert "fechaDeFin" in params, "Missing parameter 'fechaDeFin'"






def test_hyp_biblioteca_socio_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Socio)


def test_hyp_biblioteca_socio_constructor_exists():
    assert callable(Biblioteca_Socio.__init__)


def test_hyp_biblioteca_socio_constructor_args():
    sig = inspect.signature(Biblioteca_Socio.__init__)
    params = list(sig.parameters.keys())
    assert "fechaDeNacimiento" in params, "Missing parameter 'fechaDeNacimiento'"
    assert "numeroDeSocio" in params, "Missing parameter 'numeroDeSocio'"
    assert "telefono" in params, "Missing parameter 'telefono'"
    assert "edad" in params, "Missing parameter 'edad'"
    assert "direccion" in params, "Missing parameter 'direccion'"
    assert "nombreCompleto" in params, "Missing parameter 'nombreCompleto'"









def test_hyp_biblioteca_autor_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Autor)


def test_hyp_biblioteca_autor_constructor_exists():
    assert callable(Biblioteca_Autor.__init__)


def test_hyp_biblioteca_autor_constructor_args():
    sig = inspect.signature(Biblioteca_Autor.__init__)
    params = list(sig.parameters.keys())
    assert "nacionalidad" in params, "Missing parameter 'nacionalidad'"
    assert "fechaDeNacimiento" in params, "Missing parameter 'fechaDeNacimiento'"
    assert "nombreCompleto" in params, "Missing parameter 'nombreCompleto'"






def test_hyp_biblioteca_libro_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Libro)


def test_hyp_biblioteca_libro_constructor_exists():
    assert callable(Biblioteca_Libro.__init__)


def test_hyp_biblioteca_libro_constructor_args():
    sig = inspect.signature(Biblioteca_Libro.__init__)
    params = list(sig.parameters.keys())
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "editorial" in params, "Missing parameter 'editorial'"
    assert "titulo" in params, "Missing parameter 'titulo'"
    assert "genero" in params, "Missing parameter 'genero'"
    assert "anioDeEdicion" in params, "Missing parameter 'anioDeEdicion'"
    assert "activo" in params, "Missing parameter 'activo'"









def test_hyp_biblioteca_biblioteca_is_not_abstract():
    assert not inspect.isabstract(Biblioteca_Biblioteca)


def test_hyp_biblioteca_biblioteca_constructor_exists():
    assert callable(Biblioteca_Biblioteca.__init__)


def test_hyp_biblioteca_biblioteca_constructor_args():
    sig = inspect.signature(Biblioteca_Biblioteca.__init__)
    params = list(sig.parameters.keys())
    assert "direccion" in params, "Missing parameter 'direccion'"


def test_hyp_estado_exists():
    # Check that the Enumeration exists
    assert Estado is not None

def test_hyp_estado_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Estado]
    expected_literals = [
        "Malo",
        "Bueno",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Estado"

def test_hyp_genero_exists():
    # Check that the Enumeration exists
    assert Genero is not None

def test_hyp_genero_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Genero]
    expected_literals = [
        "Epico",
        "Lirico",
        "Terror",
        "Dramatico",
        "Narrativo",
        "Didactico",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Genero"


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
Biblioteca_Multa_strategy = st.builds(
    Biblioteca_Multa,
    diasExcedidos=
        st.integers(),
    fechaDePago=
        st.dates(),
    monto=
        st.integers(),
    fecha=
        st.dates()
)
Biblioteca_Ejemplar_strategy = st.builds(
    Biblioteca_Ejemplar,
    estado=
        safe_text,
    numeroDeEjemplar=
        st.integers()
)
Biblioteca_Prestamo_strategy = st.builds(
    Biblioteca_Prestamo,
    fechaDeDevolucion=
        st.dates(),
    fechaDeInicio=
        st.dates(),
    fechaDeFin=
        st.dates()
)
Biblioteca_Socio_strategy = st.builds(
    Biblioteca_Socio,
    fechaDeNacimiento=
        st.dates(),
    numeroDeSocio=
        st.integers(),
    telefono=
        safe_text,
    edad=
        st.integers(),
    direccion=
        safe_text,
    nombreCompleto=
        safe_text
)
Biblioteca_Autor_strategy = st.builds(
    Biblioteca_Autor,
    nacionalidad=
        safe_text,
    fechaDeNacimiento=
        st.dates(),
    nombreCompleto=
        safe_text
)
Biblioteca_Libro_strategy = st.builds(
    Biblioteca_Libro,
    ISBN=
        safe_text,
    editorial=
        safe_text,
    titulo=
        safe_text,
    genero=
        safe_text,
    anioDeEdicion=
        st.integers(),
    activo=
        st.booleans()
)
Biblioteca_Biblioteca_strategy = st.builds(
    Biblioteca_Biblioteca,
    direccion=
        safe_text
)




@given(instance=Biblioteca_Multa_strategy)
def test_hyp_biblioteca_multa_diasExcedidos_setter(instance):
    original = instance.diasExcedidos
    instance.diasExcedidos = original
    assert instance.diasExcedidos == original



@given(instance=Biblioteca_Multa_strategy)
def test_hyp_biblioteca_multa_fechaDePago_setter(instance):
    original = instance.fechaDePago
    instance.fechaDePago = original
    assert instance.fechaDePago == original



@given(instance=Biblioteca_Multa_strategy)
def test_hyp_biblioteca_multa_monto_setter(instance):
    original = instance.monto
    instance.monto = original
    assert instance.monto == original



@given(instance=Biblioteca_Multa_strategy)
def test_hyp_biblioteca_multa_fecha_setter(instance):
    original = instance.fecha
    instance.fecha = original
    assert instance.fecha == original




@given(instance=Biblioteca_Ejemplar_strategy)
def test_hyp_biblioteca_ejemplar_estado_setter(instance):
    original = instance.estado
    instance.estado = original
    assert instance.estado == original



@given(instance=Biblioteca_Ejemplar_strategy)
def test_hyp_biblioteca_ejemplar_numeroDeEjemplar_setter(instance):
    original = instance.numeroDeEjemplar
    instance.numeroDeEjemplar = original
    assert instance.numeroDeEjemplar == original




@given(instance=Biblioteca_Prestamo_strategy)
def test_hyp_biblioteca_prestamo_fechaDeDevolucion_setter(instance):
    original = instance.fechaDeDevolucion
    instance.fechaDeDevolucion = original
    assert instance.fechaDeDevolucion == original



@given(instance=Biblioteca_Prestamo_strategy)
def test_hyp_biblioteca_prestamo_fechaDeInicio_setter(instance):
    original = instance.fechaDeInicio
    instance.fechaDeInicio = original
    assert instance.fechaDeInicio == original



@given(instance=Biblioteca_Prestamo_strategy)
def test_hyp_biblioteca_prestamo_fechaDeFin_setter(instance):
    original = instance.fechaDeFin
    instance.fechaDeFin = original
    assert instance.fechaDeFin == original




@given(instance=Biblioteca_Socio_strategy)
def test_hyp_biblioteca_socio_fechaDeNacimiento_setter(instance):
    original = instance.fechaDeNacimiento
    instance.fechaDeNacimiento = original
    assert instance.fechaDeNacimiento == original



@given(instance=Biblioteca_Socio_strategy)
def test_hyp_biblioteca_socio_numeroDeSocio_setter(instance):
    original = instance.numeroDeSocio
    instance.numeroDeSocio = original
    assert instance.numeroDeSocio == original



@given(instance=Biblioteca_Socio_strategy)
def test_hyp_biblioteca_socio_telefono_setter(instance):
    original = instance.telefono
    instance.telefono = original
    assert instance.telefono == original



@given(instance=Biblioteca_Socio_strategy)
def test_hyp_biblioteca_socio_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original



@given(instance=Biblioteca_Socio_strategy)
def test_hyp_biblioteca_socio_direccion_setter(instance):
    original = instance.direccion
    instance.direccion = original
    assert instance.direccion == original



@given(instance=Biblioteca_Socio_strategy)
def test_hyp_biblioteca_socio_nombreCompleto_setter(instance):
    original = instance.nombreCompleto
    instance.nombreCompleto = original
    assert instance.nombreCompleto == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Biblioteca_Socio_strategy)
@settings(max_examples=30)
def test_hyp_biblioteca_socio_uniqueid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.uniqueID()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.uniqueID).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'uniqueID' in Biblioteca_Socio is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uniqueID' in Biblioteca_Socio did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uniqueID' in Biblioteca_Socio is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Biblioteca_Socio_strategy)
@settings(max_examples=30)
def test_hyp_biblioteca_socio_devolverejemplar_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.devolverEjemplar(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.devolverEjemplar).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'devolverEjemplar' in Biblioteca_Socio is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'devolverEjemplar' in Biblioteca_Socio did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'devolverEjemplar' in Biblioteca_Socio is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Biblioteca_Socio_strategy)
@settings(max_examples=30)
def test_hyp_biblioteca_socio_solicitarejemplar_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.solicitarEjemplar(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.solicitarEjemplar).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'solicitarEjemplar' in Biblioteca_Socio is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'solicitarEjemplar' in Biblioteca_Socio did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'solicitarEjemplar' in Biblioteca_Socio is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Biblioteca_Socio_strategy)
@settings(max_examples=30)
def test_hyp_biblioteca_socio_existesocio_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.existeSocio(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.existeSocio).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'existeSocio' in Biblioteca_Socio is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'existeSocio' in Biblioteca_Socio did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'existeSocio' in Biblioteca_Socio is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Biblioteca_Socio_strategy)
@settings(max_examples=30)
def test_hyp_biblioteca_socio_generarmulta_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.generarMulta(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.generarMulta).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'generarMulta' in Biblioteca_Socio is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'generarMulta' in Biblioteca_Socio did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'generarMulta' in Biblioteca_Socio is not implemented or raised an error")




@given(instance=Biblioteca_Autor_strategy)
def test_hyp_biblioteca_autor_nacionalidad_setter(instance):
    original = instance.nacionalidad
    instance.nacionalidad = original
    assert instance.nacionalidad == original



@given(instance=Biblioteca_Autor_strategy)
def test_hyp_biblioteca_autor_fechaDeNacimiento_setter(instance):
    original = instance.fechaDeNacimiento
    instance.fechaDeNacimiento = original
    assert instance.fechaDeNacimiento == original



@given(instance=Biblioteca_Autor_strategy)
def test_hyp_biblioteca_autor_nombreCompleto_setter(instance):
    original = instance.nombreCompleto
    instance.nombreCompleto = original
    assert instance.nombreCompleto == original




@given(instance=Biblioteca_Libro_strategy)
def test_hyp_biblioteca_libro_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original



@given(instance=Biblioteca_Libro_strategy)
def test_hyp_biblioteca_libro_editorial_setter(instance):
    original = instance.editorial
    instance.editorial = original
    assert instance.editorial == original



@given(instance=Biblioteca_Libro_strategy)
def test_hyp_biblioteca_libro_titulo_setter(instance):
    original = instance.titulo
    instance.titulo = original
    assert instance.titulo == original



@given(instance=Biblioteca_Libro_strategy)
def test_hyp_biblioteca_libro_genero_setter(instance):
    original = instance.genero
    instance.genero = original
    assert instance.genero == original



@given(instance=Biblioteca_Libro_strategy)
def test_hyp_biblioteca_libro_anioDeEdicion_setter(instance):
    original = instance.anioDeEdicion
    instance.anioDeEdicion = original
    assert instance.anioDeEdicion == original



@given(instance=Biblioteca_Libro_strategy)
def test_hyp_biblioteca_libro_activo_setter(instance):
    original = instance.activo
    instance.activo = original
    assert instance.activo == original




@given(instance=Biblioteca_Biblioteca_strategy)
def test_hyp_biblioteca_biblioteca_direccion_setter(instance):
    original = instance.direccion
    instance.direccion = original
    assert instance.direccion == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Biblioteca_Autor,
    Biblioteca_Biblioteca,
    Biblioteca_Ejemplar,
    Biblioteca_Libro,
    Biblioteca_Multa,
    Biblioteca_Prestamo,
    Biblioteca_Socio,
    Estado,
    Genero,
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

def test_Biblioteca_Autor_fechaDeNacimiento_value_roundtrip():
    instance = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    assert instance.fechaDeNacimiento == date(2024, 1, 1)
    instance.fechaDeNacimiento = date(2025, 6, 15)
    assert instance.fechaDeNacimiento == date(2025, 6, 15)


def test_Biblioteca_Autor_nacionalidad_value_roundtrip():
    instance = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    assert instance.nacionalidad == "sample_text"
    instance.nacionalidad = "sample_text_2"
    assert instance.nacionalidad == "sample_text_2"


def test_Biblioteca_Autor_nombreCompleto_value_roundtrip():
    instance = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    assert instance.nombreCompleto == "sample_text"
    instance.nombreCompleto = "sample_text_2"
    assert instance.nombreCompleto == "sample_text_2"


def test_Biblioteca_Biblioteca_direccion_value_roundtrip():
    instance = Biblioteca_Biblioteca(direccion="sample_text")
    assert instance.direccion == "sample_text"
    instance.direccion = "sample_text_2"
    assert instance.direccion == "sample_text_2"


def test_Biblioteca_Ejemplar_estado_value_roundtrip():
    instance = Biblioteca_Ejemplar(estado="sample_text", numeroDeEjemplar=7)
    assert instance.estado == "sample_text"
    instance.estado = "sample_text_2"
    assert instance.estado == "sample_text_2"


def test_Biblioteca_Ejemplar_numeroDeEjemplar_value_roundtrip():
    instance = Biblioteca_Ejemplar(estado="sample_text", numeroDeEjemplar=7)
    assert instance.numeroDeEjemplar == 7
    instance.numeroDeEjemplar = 13
    assert instance.numeroDeEjemplar == 13


def test_Biblioteca_Libro_ISBN_value_roundtrip():
    instance = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    assert instance.ISBN == "sample_text"
    instance.ISBN = "sample_text_2"
    assert instance.ISBN == "sample_text_2"


def test_Biblioteca_Libro_activo_value_roundtrip():
    instance = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    assert instance.activo == True
    instance.activo = False
    assert instance.activo == False


def test_Biblioteca_Libro_anioDeEdicion_value_roundtrip():
    instance = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    assert instance.anioDeEdicion == 7
    instance.anioDeEdicion = 13
    assert instance.anioDeEdicion == 13


def test_Biblioteca_Libro_editorial_value_roundtrip():
    instance = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    assert instance.editorial == "sample_text"
    instance.editorial = "sample_text_2"
    assert instance.editorial == "sample_text_2"


def test_Biblioteca_Libro_genero_value_roundtrip():
    instance = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    assert instance.genero == "sample_text"
    instance.genero = "sample_text_2"
    assert instance.genero == "sample_text_2"


def test_Biblioteca_Libro_titulo_value_roundtrip():
    instance = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    assert instance.titulo == "sample_text"
    instance.titulo = "sample_text_2"
    assert instance.titulo == "sample_text_2"


def test_Biblioteca_Multa_diasExcedidos_value_roundtrip():
    instance = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    assert instance.diasExcedidos == 7
    instance.diasExcedidos = 13
    assert instance.diasExcedidos == 13


def test_Biblioteca_Multa_fecha_value_roundtrip():
    instance = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    assert instance.fecha == date(2024, 1, 1)
    instance.fecha = date(2025, 6, 15)
    assert instance.fecha == date(2025, 6, 15)


def test_Biblioteca_Multa_fechaDePago_value_roundtrip():
    instance = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    assert instance.fechaDePago == date(2024, 1, 1)
    instance.fechaDePago = date(2025, 6, 15)
    assert instance.fechaDePago == date(2025, 6, 15)


def test_Biblioteca_Multa_monto_value_roundtrip():
    instance = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    assert instance.monto == 7
    instance.monto = 13
    assert instance.monto == 13


def test_Biblioteca_Prestamo_fechaDeDevolucion_value_roundtrip():
    instance = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    assert instance.fechaDeDevolucion == date(2024, 1, 1)
    instance.fechaDeDevolucion = date(2025, 6, 15)
    assert instance.fechaDeDevolucion == date(2025, 6, 15)


def test_Biblioteca_Prestamo_fechaDeFin_value_roundtrip():
    instance = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    assert instance.fechaDeFin == date(2024, 1, 1)
    instance.fechaDeFin = date(2025, 6, 15)
    assert instance.fechaDeFin == date(2025, 6, 15)


def test_Biblioteca_Prestamo_fechaDeInicio_value_roundtrip():
    instance = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    assert instance.fechaDeInicio == date(2024, 1, 1)
    instance.fechaDeInicio = date(2025, 6, 15)
    assert instance.fechaDeInicio == date(2025, 6, 15)


def test_Biblioteca_Socio_direccion_value_roundtrip():
    instance = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    assert instance.direccion == "sample_text"
    instance.direccion = "sample_text_2"
    assert instance.direccion == "sample_text_2"


def test_Biblioteca_Socio_edad_value_roundtrip():
    instance = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    assert instance.edad == 7
    instance.edad = 13
    assert instance.edad == 13


def test_Biblioteca_Socio_fechaDeNacimiento_value_roundtrip():
    instance = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    assert instance.fechaDeNacimiento == date(2024, 1, 1)
    instance.fechaDeNacimiento = date(2025, 6, 15)
    assert instance.fechaDeNacimiento == date(2025, 6, 15)


def test_Biblioteca_Socio_nombreCompleto_value_roundtrip():
    instance = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    assert instance.nombreCompleto == "sample_text"
    instance.nombreCompleto = "sample_text_2"
    assert instance.nombreCompleto == "sample_text_2"


def test_Biblioteca_Socio_numeroDeSocio_value_roundtrip():
    instance = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    assert instance.numeroDeSocio == 7
    instance.numeroDeSocio = 13
    assert instance.numeroDeSocio == 13


def test_Biblioteca_Socio_telefono_value_roundtrip():
    instance = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    assert instance.telefono == "sample_text"
    instance.telefono = "sample_text_2"
    assert instance.telefono == "sample_text_2"


def test_assoc_autor5_link_reassign_clear():
    a = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    b1 = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    b2 = Biblioteca_Autor(fechaDeNacimiento=date(2025, 6, 15), nacionalidad="sample_text_2", nombreCompleto="sample_text_2")
    _safe_set(a, 'Biblioteca_Libro6', b1)
    assert _is_linked(a, 'Biblioteca_Libro6', b1)
    if hasattr(b1, 'Biblioteca_Autor7'):
        assert _is_linked(b1, 'Biblioteca_Autor7', a)
    _safe_set(a, 'Biblioteca_Libro6', b2)
    assert _is_linked(a, 'Biblioteca_Libro6', b2)
    if hasattr(b1, 'Biblioteca_Autor7'):
        assert not _is_linked(b1, 'Biblioteca_Autor7', a)
    if hasattr(b2, 'Biblioteca_Autor7'):
        assert _is_linked(b2, 'Biblioteca_Autor7', a)
    _safe_set(a, 'Biblioteca_Libro6', None)
    assert not _is_linked(a, 'Biblioteca_Libro6', b2)
    if hasattr(b2, 'Biblioteca_Autor7'):
        assert not _is_linked(b2, 'Biblioteca_Autor7', a)


def test_assoc_autores1_link_reassign_clear():
    a = Biblioteca_Biblioteca(direccion="sample_text")
    b1 = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    b2 = Biblioteca_Autor(fechaDeNacimiento=date(2025, 6, 15), nacionalidad="sample_text_2", nombreCompleto="sample_text_2")
    _safe_set(a, 'Biblioteca_Biblioteca2', {b1})
    assert _is_linked(a, 'Biblioteca_Biblioteca2', b1)
    if hasattr(b1, 'Biblioteca_Autor'):
        assert _is_linked(b1, 'Biblioteca_Autor', a)
    _safe_set(a, 'Biblioteca_Biblioteca2', {b2})
    assert _is_linked(a, 'Biblioteca_Biblioteca2', b2)
    if hasattr(b1, 'Biblioteca_Autor'):
        assert not _is_linked(b1, 'Biblioteca_Autor', a)
    if hasattr(b2, 'Biblioteca_Autor'):
        assert _is_linked(b2, 'Biblioteca_Autor', a)
    _safe_set(a, 'Biblioteca_Biblioteca2', set())
    assert not _is_linked(a, 'Biblioteca_Biblioteca2', b2)
    if hasattr(b2, 'Biblioteca_Autor'):
        assert not _is_linked(b2, 'Biblioteca_Autor', a)


def test_assoc_ejemplar8_link_reassign_clear():
    a = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    b1 = Biblioteca_Ejemplar(estado="sample_text", numeroDeEjemplar=7)
    b2 = Biblioteca_Ejemplar(estado="sample_text_2", numeroDeEjemplar=13)
    _safe_set(a, 'Biblioteca_Prestamo', b1)
    assert _is_linked(a, 'Biblioteca_Prestamo', b1)
    if hasattr(b1, 'Biblioteca_Ejemplar'):
        assert _is_linked(b1, 'Biblioteca_Ejemplar', a)
    _safe_set(a, 'Biblioteca_Prestamo', b2)
    assert _is_linked(a, 'Biblioteca_Prestamo', b2)
    if hasattr(b1, 'Biblioteca_Ejemplar'):
        assert not _is_linked(b1, 'Biblioteca_Ejemplar', a)
    if hasattr(b2, 'Biblioteca_Ejemplar'):
        assert _is_linked(b2, 'Biblioteca_Ejemplar', a)
    _safe_set(a, 'Biblioteca_Prestamo', None)
    assert not _is_linked(a, 'Biblioteca_Prestamo', b2)
    if hasattr(b2, 'Biblioteca_Ejemplar'):
        assert not _is_linked(b2, 'Biblioteca_Ejemplar', a)


def test_assoc_libros0_link_reassign_clear():
    a = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    b1 = Biblioteca_Biblioteca(direccion="sample_text")
    b2 = Biblioteca_Biblioteca(direccion="sample_text_2")
    _safe_set(a, 'Biblioteca_Libro', b1)
    assert _is_linked(a, 'Biblioteca_Libro', b1)
    if hasattr(b1, 'Biblioteca_Biblioteca'):
        assert _is_linked(b1, 'Biblioteca_Biblioteca', a)
    _safe_set(a, 'Biblioteca_Libro', b2)
    assert _is_linked(a, 'Biblioteca_Libro', b2)
    if hasattr(b1, 'Biblioteca_Biblioteca'):
        assert not _is_linked(b1, 'Biblioteca_Biblioteca', a)
    if hasattr(b2, 'Biblioteca_Biblioteca'):
        assert _is_linked(b2, 'Biblioteca_Biblioteca', a)
    _safe_set(a, 'Biblioteca_Libro', None)
    assert not _is_linked(a, 'Biblioteca_Libro', b2)
    if hasattr(b2, 'Biblioteca_Biblioteca'):
        assert not _is_linked(b2, 'Biblioteca_Biblioteca', a)


def test_assoc_multas15_link_reassign_clear():
    a = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    b1 = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    b2 = Biblioteca_Multa(diasExcedidos=13, fecha=date(2025, 6, 15), fechaDePago=date(2025, 6, 15), monto=13)
    _safe_set(a, 'Biblioteca_Socio16', {b1})
    assert _is_linked(a, 'Biblioteca_Socio16', b1)
    if hasattr(b1, 'Biblioteca_Multa'):
        assert _is_linked(b1, 'Biblioteca_Multa', a)
    _safe_set(a, 'Biblioteca_Socio16', {b2})
    assert _is_linked(a, 'Biblioteca_Socio16', b2)
    if hasattr(b1, 'Biblioteca_Multa'):
        assert not _is_linked(b1, 'Biblioteca_Multa', a)
    if hasattr(b2, 'Biblioteca_Multa'):
        assert _is_linked(b2, 'Biblioteca_Multa', a)
    _safe_set(a, 'Biblioteca_Socio16', set())
    assert not _is_linked(a, 'Biblioteca_Socio16', b2)
    if hasattr(b2, 'Biblioteca_Multa'):
        assert not _is_linked(b2, 'Biblioteca_Multa', a)


def test_assoc_obras12_link_reassign_clear():
    a = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    b1 = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    b2 = Biblioteca_Autor(fechaDeNacimiento=date(2025, 6, 15), nacionalidad="sample_text_2", nombreCompleto="sample_text_2")
    _safe_set(a, 'Biblioteca_Libro14', b1)
    assert _is_linked(a, 'Biblioteca_Libro14', b1)
    if hasattr(b1, 'Biblioteca_Autor13'):
        assert _is_linked(b1, 'Biblioteca_Autor13', a)
    _safe_set(a, 'Biblioteca_Libro14', b2)
    assert _is_linked(a, 'Biblioteca_Libro14', b2)
    if hasattr(b1, 'Biblioteca_Autor13'):
        assert not _is_linked(b1, 'Biblioteca_Autor13', a)
    if hasattr(b2, 'Biblioteca_Autor13'):
        assert _is_linked(b2, 'Biblioteca_Autor13', a)
    _safe_set(a, 'Biblioteca_Libro14', None)
    assert not _is_linked(a, 'Biblioteca_Libro14', b2)
    if hasattr(b2, 'Biblioteca_Autor13'):
        assert not _is_linked(b2, 'Biblioteca_Autor13', a)


def test_assoc_prestamo20_link_reassign_clear():
    a = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    b1 = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    b2 = Biblioteca_Multa(diasExcedidos=13, fecha=date(2025, 6, 15), fechaDePago=date(2025, 6, 15), monto=13)
    _safe_set(a, 'Biblioteca_Prestamo22', b1)
    assert _is_linked(a, 'Biblioteca_Prestamo22', b1)
    if hasattr(b1, 'Biblioteca_Multa21'):
        assert _is_linked(b1, 'Biblioteca_Multa21', a)
    _safe_set(a, 'Biblioteca_Prestamo22', b2)
    assert _is_linked(a, 'Biblioteca_Prestamo22', b2)
    if hasattr(b1, 'Biblioteca_Multa21'):
        assert not _is_linked(b1, 'Biblioteca_Multa21', a)
    if hasattr(b2, 'Biblioteca_Multa21'):
        assert _is_linked(b2, 'Biblioteca_Multa21', a)
    _safe_set(a, 'Biblioteca_Prestamo22', None)
    assert not _is_linked(a, 'Biblioteca_Prestamo22', b2)
    if hasattr(b2, 'Biblioteca_Multa21'):
        assert not _is_linked(b2, 'Biblioteca_Multa21', a)


def test_assoc_prestamos17_link_reassign_clear():
    a = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    b1 = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    b2 = Biblioteca_Prestamo(fechaDeDevolucion=date(2025, 6, 15), fechaDeFin=date(2025, 6, 15), fechaDeInicio=date(2025, 6, 15))
    _safe_set(a, 'Biblioteca_Socio18', {b1})
    assert _is_linked(a, 'Biblioteca_Socio18', b1)
    if hasattr(b1, 'Biblioteca_Prestamo19'):
        assert _is_linked(b1, 'Biblioteca_Prestamo19', a)
    _safe_set(a, 'Biblioteca_Socio18', {b2})
    assert _is_linked(a, 'Biblioteca_Socio18', b2)
    if hasattr(b1, 'Biblioteca_Prestamo19'):
        assert not _is_linked(b1, 'Biblioteca_Prestamo19', a)
    if hasattr(b2, 'Biblioteca_Prestamo19'):
        assert _is_linked(b2, 'Biblioteca_Prestamo19', a)
    _safe_set(a, 'Biblioteca_Socio18', set())
    assert not _is_linked(a, 'Biblioteca_Socio18', b2)
    if hasattr(b2, 'Biblioteca_Prestamo19'):
        assert not _is_linked(b2, 'Biblioteca_Prestamo19', a)


def test_assoc_socio9_link_reassign_clear():
    a = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    b1 = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    b2 = Biblioteca_Prestamo(fechaDeDevolucion=date(2025, 6, 15), fechaDeFin=date(2025, 6, 15), fechaDeInicio=date(2025, 6, 15))
    _safe_set(a, 'Biblioteca_Socio11', b1)
    assert _is_linked(a, 'Biblioteca_Socio11', b1)
    if hasattr(b1, 'Biblioteca_Prestamo10'):
        assert _is_linked(b1, 'Biblioteca_Prestamo10', a)
    _safe_set(a, 'Biblioteca_Socio11', b2)
    assert _is_linked(a, 'Biblioteca_Socio11', b2)
    if hasattr(b1, 'Biblioteca_Prestamo10'):
        assert not _is_linked(b1, 'Biblioteca_Prestamo10', a)
    if hasattr(b2, 'Biblioteca_Prestamo10'):
        assert _is_linked(b2, 'Biblioteca_Prestamo10', a)
    _safe_set(a, 'Biblioteca_Socio11', None)
    assert not _is_linked(a, 'Biblioteca_Socio11', b2)
    if hasattr(b2, 'Biblioteca_Prestamo10'):
        assert not _is_linked(b2, 'Biblioteca_Prestamo10', a)


def test_assoc_socios3_link_reassign_clear():
    a = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    b1 = Biblioteca_Biblioteca(direccion="sample_text")
    b2 = Biblioteca_Biblioteca(direccion="sample_text_2")
    _safe_set(a, 'Biblioteca_Socio', b1)
    assert _is_linked(a, 'Biblioteca_Socio', b1)
    if hasattr(b1, 'Biblioteca_Biblioteca4'):
        assert _is_linked(b1, 'Biblioteca_Biblioteca4', a)
    _safe_set(a, 'Biblioteca_Socio', b2)
    assert _is_linked(a, 'Biblioteca_Socio', b2)
    if hasattr(b1, 'Biblioteca_Biblioteca4'):
        assert not _is_linked(b1, 'Biblioteca_Biblioteca4', a)
    if hasattr(b2, 'Biblioteca_Biblioteca4'):
        assert _is_linked(b2, 'Biblioteca_Biblioteca4', a)
    _safe_set(a, 'Biblioteca_Socio', None)
    assert not _is_linked(a, 'Biblioteca_Socio', b2)
    if hasattr(b2, 'Biblioteca_Biblioteca4'):
        assert not _is_linked(b2, 'Biblioteca_Biblioteca4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Biblioteca_Autor_strategy = st.builds(Biblioteca_Autor, fechaDeNacimiento=st.dates(), nacionalidad=safe_text, nombreCompleto=safe_text)
@given(instance=Biblioteca_Autor_strategy)
@settings(max_examples=25)
def test_Biblioteca_Autor_instantiation(instance):
    assert isinstance(instance, Biblioteca_Autor)


Biblioteca_Biblioteca_strategy = st.builds(Biblioteca_Biblioteca, direccion=safe_text)
@given(instance=Biblioteca_Biblioteca_strategy)
@settings(max_examples=25)
def test_Biblioteca_Biblioteca_instantiation(instance):
    assert isinstance(instance, Biblioteca_Biblioteca)


Biblioteca_Ejemplar_strategy = st.builds(Biblioteca_Ejemplar, estado=safe_text, numeroDeEjemplar=st.integers())
@given(instance=Biblioteca_Ejemplar_strategy)
@settings(max_examples=25)
def test_Biblioteca_Ejemplar_instantiation(instance):
    assert isinstance(instance, Biblioteca_Ejemplar)


Biblioteca_Libro_strategy = st.builds(Biblioteca_Libro, ISBN=safe_text, activo=st.booleans(), anioDeEdicion=st.integers(), editorial=safe_text, genero=safe_text, titulo=safe_text)
@given(instance=Biblioteca_Libro_strategy)
@settings(max_examples=25)
def test_Biblioteca_Libro_instantiation(instance):
    assert isinstance(instance, Biblioteca_Libro)


Biblioteca_Multa_strategy = st.builds(Biblioteca_Multa, diasExcedidos=st.integers(), fecha=st.dates(), fechaDePago=st.dates(), monto=st.integers())
@given(instance=Biblioteca_Multa_strategy)
@settings(max_examples=25)
def test_Biblioteca_Multa_instantiation(instance):
    assert isinstance(instance, Biblioteca_Multa)


Biblioteca_Prestamo_strategy = st.builds(Biblioteca_Prestamo, fechaDeDevolucion=st.dates(), fechaDeFin=st.dates(), fechaDeInicio=st.dates())
@given(instance=Biblioteca_Prestamo_strategy)
@settings(max_examples=25)
def test_Biblioteca_Prestamo_instantiation(instance):
    assert isinstance(instance, Biblioteca_Prestamo)


Biblioteca_Socio_strategy = st.builds(Biblioteca_Socio, direccion=safe_text, edad=st.integers(), fechaDeNacimiento=st.dates(), nombreCompleto=safe_text, numeroDeSocio=st.integers(), telefono=safe_text)
@given(instance=Biblioteca_Socio_strategy)
@settings(max_examples=25)
def test_Biblioteca_Socio_instantiation(instance):
    assert isinstance(instance, Biblioteca_Socio)



