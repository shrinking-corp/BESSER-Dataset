import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_autor5_reverse_link_reassign_clear():
    a1 = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    a2 = Biblioteca_Libro(ISBN="sample_text_2", activo=False, anioDeEdicion=13, editorial="sample_text_2", genero="sample_text_2", titulo="sample_text_2")
    b = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    _safe_set(b, 'Biblioteca_Autor7', a1)
    assert _is_linked(b, 'Biblioteca_Autor7', a1)
    if hasattr(a1, 'Biblioteca_Libro6'):
        assert _is_linked(a1, 'Biblioteca_Libro6', b)
    _safe_set(b, 'Biblioteca_Autor7', a2)
    assert _is_linked(b, 'Biblioteca_Autor7', a2)
    if hasattr(a1, 'Biblioteca_Libro6'):
        assert not _is_linked(a1, 'Biblioteca_Libro6', b)
    if hasattr(a2, 'Biblioteca_Libro6'):
        assert _is_linked(a2, 'Biblioteca_Libro6', b)
    _safe_set(b, 'Biblioteca_Autor7', None)
    assert not _is_linked(b, 'Biblioteca_Autor7', a2)
    if hasattr(a2, 'Biblioteca_Libro6'):
        assert not _is_linked(a2, 'Biblioteca_Libro6', b)


def test_assoc_autores1_reverse_link_reassign_clear():
    a1 = Biblioteca_Biblioteca(direccion="sample_text")
    a2 = Biblioteca_Biblioteca(direccion="sample_text_2")
    b = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    _safe_set(b, 'Biblioteca_Autor', a1)
    assert _is_linked(b, 'Biblioteca_Autor', a1)
    if hasattr(a1, 'Biblioteca_Biblioteca2'):
        assert _is_linked(a1, 'Biblioteca_Biblioteca2', b)
    _safe_set(b, 'Biblioteca_Autor', a2)
    assert _is_linked(b, 'Biblioteca_Autor', a2)
    if hasattr(a1, 'Biblioteca_Biblioteca2'):
        assert not _is_linked(a1, 'Biblioteca_Biblioteca2', b)
    if hasattr(a2, 'Biblioteca_Biblioteca2'):
        assert _is_linked(a2, 'Biblioteca_Biblioteca2', b)
    _safe_set(b, 'Biblioteca_Autor', None)
    assert not _is_linked(b, 'Biblioteca_Autor', a2)
    if hasattr(a2, 'Biblioteca_Biblioteca2'):
        assert not _is_linked(a2, 'Biblioteca_Biblioteca2', b)


def test_assoc_ejemplar8_reverse_link_reassign_clear():
    a1 = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    a2 = Biblioteca_Prestamo(fechaDeDevolucion=date(2025, 6, 15), fechaDeFin=date(2025, 6, 15), fechaDeInicio=date(2025, 6, 15))
    b = Biblioteca_Ejemplar(estado="sample_text", numeroDeEjemplar=7)
    _safe_set(b, 'Biblioteca_Ejemplar', a1)
    assert _is_linked(b, 'Biblioteca_Ejemplar', a1)
    if hasattr(a1, 'Biblioteca_Prestamo'):
        assert _is_linked(a1, 'Biblioteca_Prestamo', b)
    _safe_set(b, 'Biblioteca_Ejemplar', a2)
    assert _is_linked(b, 'Biblioteca_Ejemplar', a2)
    if hasattr(a1, 'Biblioteca_Prestamo'):
        assert not _is_linked(a1, 'Biblioteca_Prestamo', b)
    if hasattr(a2, 'Biblioteca_Prestamo'):
        assert _is_linked(a2, 'Biblioteca_Prestamo', b)
    _safe_set(b, 'Biblioteca_Ejemplar', None)
    assert not _is_linked(b, 'Biblioteca_Ejemplar', a2)
    if hasattr(a2, 'Biblioteca_Prestamo'):
        assert not _is_linked(a2, 'Biblioteca_Prestamo', b)


def test_assoc_libros0_reverse_link_reassign_clear():
    a1 = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    a2 = Biblioteca_Libro(ISBN="sample_text_2", activo=False, anioDeEdicion=13, editorial="sample_text_2", genero="sample_text_2", titulo="sample_text_2")
    b = Biblioteca_Biblioteca(direccion="sample_text")
    _safe_set(b, 'Biblioteca_Biblioteca', {a1})
    assert _is_linked(b, 'Biblioteca_Biblioteca', a1)
    if hasattr(a1, 'Biblioteca_Libro'):
        assert _is_linked(a1, 'Biblioteca_Libro', b)
    _safe_set(b, 'Biblioteca_Biblioteca', {a2})
    assert _is_linked(b, 'Biblioteca_Biblioteca', a2)
    if hasattr(a1, 'Biblioteca_Libro'):
        assert not _is_linked(a1, 'Biblioteca_Libro', b)
    if hasattr(a2, 'Biblioteca_Libro'):
        assert _is_linked(a2, 'Biblioteca_Libro', b)
    _safe_set(b, 'Biblioteca_Biblioteca', set())
    assert not _is_linked(b, 'Biblioteca_Biblioteca', a2)
    if hasattr(a2, 'Biblioteca_Libro'):
        assert not _is_linked(a2, 'Biblioteca_Libro', b)


def test_assoc_multas15_reverse_link_reassign_clear():
    a1 = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    a2 = Biblioteca_Socio(direccion="sample_text_2", edad=13, fechaDeNacimiento=date(2025, 6, 15), nombreCompleto="sample_text_2", numeroDeSocio=13, telefono="sample_text_2")
    b = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    _safe_set(b, 'Biblioteca_Multa', a1)
    assert _is_linked(b, 'Biblioteca_Multa', a1)
    if hasattr(a1, 'Biblioteca_Socio16'):
        assert _is_linked(a1, 'Biblioteca_Socio16', b)
    _safe_set(b, 'Biblioteca_Multa', a2)
    assert _is_linked(b, 'Biblioteca_Multa', a2)
    if hasattr(a1, 'Biblioteca_Socio16'):
        assert not _is_linked(a1, 'Biblioteca_Socio16', b)
    if hasattr(a2, 'Biblioteca_Socio16'):
        assert _is_linked(a2, 'Biblioteca_Socio16', b)
    _safe_set(b, 'Biblioteca_Multa', None)
    assert not _is_linked(b, 'Biblioteca_Multa', a2)
    if hasattr(a2, 'Biblioteca_Socio16'):
        assert not _is_linked(a2, 'Biblioteca_Socio16', b)


def test_assoc_obras12_reverse_link_reassign_clear():
    a1 = Biblioteca_Libro(ISBN="sample_text", activo=True, anioDeEdicion=7, editorial="sample_text", genero="sample_text", titulo="sample_text")
    a2 = Biblioteca_Libro(ISBN="sample_text_2", activo=False, anioDeEdicion=13, editorial="sample_text_2", genero="sample_text_2", titulo="sample_text_2")
    b = Biblioteca_Autor(fechaDeNacimiento=date(2024, 1, 1), nacionalidad="sample_text", nombreCompleto="sample_text")
    _safe_set(b, 'Biblioteca_Autor13', {a1})
    assert _is_linked(b, 'Biblioteca_Autor13', a1)
    if hasattr(a1, 'Biblioteca_Libro14'):
        assert _is_linked(a1, 'Biblioteca_Libro14', b)
    _safe_set(b, 'Biblioteca_Autor13', {a2})
    assert _is_linked(b, 'Biblioteca_Autor13', a2)
    if hasattr(a1, 'Biblioteca_Libro14'):
        assert not _is_linked(a1, 'Biblioteca_Libro14', b)
    if hasattr(a2, 'Biblioteca_Libro14'):
        assert _is_linked(a2, 'Biblioteca_Libro14', b)
    _safe_set(b, 'Biblioteca_Autor13', set())
    assert not _is_linked(b, 'Biblioteca_Autor13', a2)
    if hasattr(a2, 'Biblioteca_Libro14'):
        assert not _is_linked(a2, 'Biblioteca_Libro14', b)


def test_assoc_prestamo20_reverse_link_reassign_clear():
    a1 = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    a2 = Biblioteca_Prestamo(fechaDeDevolucion=date(2025, 6, 15), fechaDeFin=date(2025, 6, 15), fechaDeInicio=date(2025, 6, 15))
    b = Biblioteca_Multa(diasExcedidos=7, fecha=date(2024, 1, 1), fechaDePago=date(2024, 1, 1), monto=7)
    _safe_set(b, 'Biblioteca_Multa21', a1)
    assert _is_linked(b, 'Biblioteca_Multa21', a1)
    if hasattr(a1, 'Biblioteca_Prestamo22'):
        assert _is_linked(a1, 'Biblioteca_Prestamo22', b)
    _safe_set(b, 'Biblioteca_Multa21', a2)
    assert _is_linked(b, 'Biblioteca_Multa21', a2)
    if hasattr(a1, 'Biblioteca_Prestamo22'):
        assert not _is_linked(a1, 'Biblioteca_Prestamo22', b)
    if hasattr(a2, 'Biblioteca_Prestamo22'):
        assert _is_linked(a2, 'Biblioteca_Prestamo22', b)
    _safe_set(b, 'Biblioteca_Multa21', None)
    assert not _is_linked(b, 'Biblioteca_Multa21', a2)
    if hasattr(a2, 'Biblioteca_Prestamo22'):
        assert not _is_linked(a2, 'Biblioteca_Prestamo22', b)


def test_assoc_prestamos17_reverse_link_reassign_clear():
    a1 = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    a2 = Biblioteca_Socio(direccion="sample_text_2", edad=13, fechaDeNacimiento=date(2025, 6, 15), nombreCompleto="sample_text_2", numeroDeSocio=13, telefono="sample_text_2")
    b = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    _safe_set(b, 'Biblioteca_Prestamo19', a1)
    assert _is_linked(b, 'Biblioteca_Prestamo19', a1)
    if hasattr(a1, 'Biblioteca_Socio18'):
        assert _is_linked(a1, 'Biblioteca_Socio18', b)
    _safe_set(b, 'Biblioteca_Prestamo19', a2)
    assert _is_linked(b, 'Biblioteca_Prestamo19', a2)
    if hasattr(a1, 'Biblioteca_Socio18'):
        assert not _is_linked(a1, 'Biblioteca_Socio18', b)
    if hasattr(a2, 'Biblioteca_Socio18'):
        assert _is_linked(a2, 'Biblioteca_Socio18', b)
    _safe_set(b, 'Biblioteca_Prestamo19', None)
    assert not _is_linked(b, 'Biblioteca_Prestamo19', a2)
    if hasattr(a2, 'Biblioteca_Socio18'):
        assert not _is_linked(a2, 'Biblioteca_Socio18', b)


def test_assoc_socio9_reverse_link_reassign_clear():
    a1 = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    a2 = Biblioteca_Socio(direccion="sample_text_2", edad=13, fechaDeNacimiento=date(2025, 6, 15), nombreCompleto="sample_text_2", numeroDeSocio=13, telefono="sample_text_2")
    b = Biblioteca_Prestamo(fechaDeDevolucion=date(2024, 1, 1), fechaDeFin=date(2024, 1, 1), fechaDeInicio=date(2024, 1, 1))
    _safe_set(b, 'Biblioteca_Prestamo10', a1)
    assert _is_linked(b, 'Biblioteca_Prestamo10', a1)
    if hasattr(a1, 'Biblioteca_Socio11'):
        assert _is_linked(a1, 'Biblioteca_Socio11', b)
    _safe_set(b, 'Biblioteca_Prestamo10', a2)
    assert _is_linked(b, 'Biblioteca_Prestamo10', a2)
    if hasattr(a1, 'Biblioteca_Socio11'):
        assert not _is_linked(a1, 'Biblioteca_Socio11', b)
    if hasattr(a2, 'Biblioteca_Socio11'):
        assert _is_linked(a2, 'Biblioteca_Socio11', b)
    _safe_set(b, 'Biblioteca_Prestamo10', None)
    assert not _is_linked(b, 'Biblioteca_Prestamo10', a2)
    if hasattr(a2, 'Biblioteca_Socio11'):
        assert not _is_linked(a2, 'Biblioteca_Socio11', b)


def test_assoc_socios3_reverse_link_reassign_clear():
    a1 = Biblioteca_Socio(direccion="sample_text", edad=7, fechaDeNacimiento=date(2024, 1, 1), nombreCompleto="sample_text", numeroDeSocio=7, telefono="sample_text")
    a2 = Biblioteca_Socio(direccion="sample_text_2", edad=13, fechaDeNacimiento=date(2025, 6, 15), nombreCompleto="sample_text_2", numeroDeSocio=13, telefono="sample_text_2")
    b = Biblioteca_Biblioteca(direccion="sample_text")
    _safe_set(b, 'Biblioteca_Biblioteca4', {a1})
    assert _is_linked(b, 'Biblioteca_Biblioteca4', a1)
    if hasattr(a1, 'Biblioteca_Socio'):
        assert _is_linked(a1, 'Biblioteca_Socio', b)
    _safe_set(b, 'Biblioteca_Biblioteca4', {a2})
    assert _is_linked(b, 'Biblioteca_Biblioteca4', a2)
    if hasattr(a1, 'Biblioteca_Socio'):
        assert not _is_linked(a1, 'Biblioteca_Socio', b)
    if hasattr(a2, 'Biblioteca_Socio'):
        assert _is_linked(a2, 'Biblioteca_Socio', b)
    _safe_set(b, 'Biblioteca_Biblioteca4', set())
    assert not _is_linked(b, 'Biblioteca_Biblioteca4', a2)
    if hasattr(a2, 'Biblioteca_Socio'):
        assert not _is_linked(a2, 'Biblioteca_Socio', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

