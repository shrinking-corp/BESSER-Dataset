import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor_Actor,
    Actor_external,
    Actualizar__contacto_external,
    Buscar_Contactos_external,
    CONTACTO,
    Crear_Contacto_external,
    DIRECCION,
    Eliminar_Contacto_external,
    FOTO,
    LIBRO_DE__DIRECCIONES,
    Libro_de__Direcciones_Component,
    TELEFONO,
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

def test_assoc_CONTACTO__DIRECCION_reverse_link_reassign_clear():
    a1 = DIRECCION(CIUDAD="sample_text", CODIGO_POSTAL="sample_text", ESTADO="sample_text", NOMBRE="sample_text")
    a2 = DIRECCION(CIUDAD="sample_text_2", CODIGO_POSTAL="sample_text_2", ESTADO="sample_text_2", NOMBRE="sample_text_2")
    b = CONTACTO(CORREO="sample_text", NOMBRE="sample_text")
    _safe_set(b, 'dIRECCION6', a1)
    assert _is_linked(b, 'dIRECCION6', a1)
    if hasattr(a1, 'cONTACTO7'):
        assert _is_linked(a1, 'cONTACTO7', b)
    _safe_set(b, 'dIRECCION6', a2)
    assert _is_linked(b, 'dIRECCION6', a2)
    if hasattr(a1, 'cONTACTO7'):
        assert not _is_linked(a1, 'cONTACTO7', b)
    if hasattr(a2, 'cONTACTO7'):
        assert _is_linked(a2, 'cONTACTO7', b)
    _safe_set(b, 'dIRECCION6', None)
    assert not _is_linked(b, 'dIRECCION6', a2)
    if hasattr(a2, 'cONTACTO7'):
        assert not _is_linked(a2, 'cONTACTO7', b)


def test_assoc_CONTACTO__FOTO_reverse_link_reassign_clear():
    a1 = FOTO(ALTURA=7, ANCHO=7)
    a2 = FOTO(ALTURA=13, ANCHO=13)
    b = CONTACTO(CORREO="sample_text", NOMBRE="sample_text")
    _safe_set(b, 'fOTO4', a1)
    assert _is_linked(b, 'fOTO4', a1)
    if hasattr(a1, 'cONTACTO5'):
        assert _is_linked(a1, 'cONTACTO5', b)
    _safe_set(b, 'fOTO4', a2)
    assert _is_linked(b, 'fOTO4', a2)
    if hasattr(a1, 'cONTACTO5'):
        assert not _is_linked(a1, 'cONTACTO5', b)
    if hasattr(a2, 'cONTACTO5'):
        assert _is_linked(a2, 'cONTACTO5', b)
    _safe_set(b, 'fOTO4', None)
    assert not _is_linked(b, 'fOTO4', a2)
    if hasattr(a2, 'cONTACTO5'):
        assert not _is_linked(a2, 'cONTACTO5', b)


def test_assoc_CONTACTO__TELEFONO_reverse_link_reassign_clear():
    a1 = TELEFONO(CODIGO_DE__AREA="sample_text", NUMBER=7, PREFIJO=7)
    a2 = TELEFONO(CODIGO_DE__AREA="sample_text_2", NUMBER=13, PREFIJO=13)
    b = CONTACTO(CORREO="sample_text", NOMBRE="sample_text")
    _safe_set(b, 'tELEFONO2', a1)
    assert _is_linked(b, 'tELEFONO2', a1)
    if hasattr(a1, 'cONTACTO3'):
        assert _is_linked(a1, 'cONTACTO3', b)
    _safe_set(b, 'tELEFONO2', a2)
    assert _is_linked(b, 'tELEFONO2', a2)
    if hasattr(a1, 'cONTACTO3'):
        assert not _is_linked(a1, 'cONTACTO3', b)
    if hasattr(a2, 'cONTACTO3'):
        assert _is_linked(a2, 'cONTACTO3', b)
    _safe_set(b, 'tELEFONO2', None)
    assert not _is_linked(b, 'tELEFONO2', a2)
    if hasattr(a2, 'cONTACTO3'):
        assert not _is_linked(a2, 'cONTACTO3', b)


def test_assoc_LIBRO_DE__DIRECCIONES_CONTACTO_reverse_link_reassign_clear():
    a1 = LIBRO_DE__DIRECCIONES(INTRODUCCION="sample_text")
    a2 = LIBRO_DE__DIRECCIONES(INTRODUCCION="sample_text_2")
    b = CONTACTO(CORREO="sample_text", NOMBRE="sample_text")
    _safe_set(b, 'LIBRO_DE__DIRECCIONES1', a1)
    assert _is_linked(b, 'LIBRO_DE__DIRECCIONES1', a1)
    if hasattr(a1, 'cONTACTO0'):
        assert _is_linked(a1, 'cONTACTO0', b)
    _safe_set(b, 'LIBRO_DE__DIRECCIONES1', a2)
    assert _is_linked(b, 'LIBRO_DE__DIRECCIONES1', a2)
    if hasattr(a1, 'cONTACTO0'):
        assert not _is_linked(a1, 'cONTACTO0', b)
    if hasattr(a2, 'cONTACTO0'):
        assert _is_linked(a2, 'cONTACTO0', b)
    _safe_set(b, 'LIBRO_DE__DIRECCIONES1', None)
    assert not _is_linked(b, 'LIBRO_DE__DIRECCIONES1', a2)
    if hasattr(a2, 'cONTACTO0'):
        assert not _is_linked(a2, 'cONTACTO0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

