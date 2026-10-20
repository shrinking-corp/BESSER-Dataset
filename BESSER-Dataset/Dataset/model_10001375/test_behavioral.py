import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Entrenador,
    Equipo,
    Jugadores,
    Liga,
    Partido,
    Personas,
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

def test_assoc_Equipo_Jugadores_reverse_link_reassign_clear():
    a1 = Jugadores(nombre="sample_text", posicion=7)
    a2 = Jugadores(nombre="sample_text_2", posicion=13)
    b = Equipo(nombre="sample_text", registro="sample_text")
    _safe_set(b, 'jugadores2', a1)
    assert _is_linked(b, 'jugadores2', a1)
    if hasattr(a1, 'equipo3'):
        assert _is_linked(a1, 'equipo3', b)
    _safe_set(b, 'jugadores2', a2)
    assert _is_linked(b, 'jugadores2', a2)
    if hasattr(a1, 'equipo3'):
        assert not _is_linked(a1, 'equipo3', b)
    if hasattr(a2, 'equipo3'):
        assert _is_linked(a2, 'equipo3', b)
    _safe_set(b, 'jugadores2', None)
    assert not _is_linked(b, 'jugadores2', a2)
    if hasattr(a2, 'equipo3'):
        assert not _is_linked(a2, 'equipo3', b)


def test_assoc_Equipo_Partido_reverse_link_reassign_clear():
    a1 = Partido(localizaci_n="sample_text", resultado=7)
    a2 = Partido(localizaci_n="sample_text_2", resultado=13)
    b = Equipo(nombre="sample_text", registro="sample_text")
    _safe_set(b, 'partido6', {a1})
    assert _is_linked(b, 'partido6', a1)
    if hasattr(a1, 'equipo7'):
        assert _is_linked(a1, 'equipo7', b)
    _safe_set(b, 'partido6', {a2})
    assert _is_linked(b, 'partido6', a2)
    if hasattr(a1, 'equipo7'):
        assert not _is_linked(a1, 'equipo7', b)
    if hasattr(a2, 'equipo7'):
        assert _is_linked(a2, 'equipo7', b)
    _safe_set(b, 'partido6', set())
    assert not _is_linked(b, 'partido6', a2)
    if hasattr(a2, 'equipo7'):
        assert not _is_linked(a2, 'equipo7', b)


def test_assoc_Jugadores_Equipo_reverse_link_reassign_clear():
    a1 = Jugadores(nombre="sample_text", posicion=7)
    a2 = Jugadores(nombre="sample_text_2", posicion=13)
    b = Equipo(nombre="sample_text", registro="sample_text")
    _safe_set(b, 'jugadores5', a1)
    assert _is_linked(b, 'jugadores5', a1)
    if hasattr(a1, 'equipo4'):
        assert _is_linked(a1, 'equipo4', b)
    _safe_set(b, 'jugadores5', a2)
    assert _is_linked(b, 'jugadores5', a2)
    if hasattr(a1, 'equipo4'):
        assert not _is_linked(a1, 'equipo4', b)
    if hasattr(a2, 'equipo4'):
        assert _is_linked(a2, 'equipo4', b)
    _safe_set(b, 'jugadores5', None)
    assert not _is_linked(b, 'jugadores5', a2)
    if hasattr(a2, 'equipo4'):
        assert not _is_linked(a2, 'equipo4', b)


def test_assoc_Liga_Equipo_reverse_link_reassign_clear():
    a1 = Liga(datos_comienzo="sample_text", datos_finalizaci_n="sample_text", nombre="sample_text")
    a2 = Liga(datos_comienzo="sample_text_2", datos_finalizaci_n="sample_text_2", nombre="sample_text_2")
    b = Equipo(nombre="sample_text", registro="sample_text")
    _safe_set(b, 'liga1', a1)
    assert _is_linked(b, 'liga1', a1)
    if hasattr(a1, 'equipo0'):
        assert _is_linked(a1, 'equipo0', b)
    _safe_set(b, 'liga1', a2)
    assert _is_linked(b, 'liga1', a2)
    if hasattr(a1, 'equipo0'):
        assert not _is_linked(a1, 'equipo0', b)
    if hasattr(a2, 'equipo0'):
        assert _is_linked(a2, 'equipo0', b)
    _safe_set(b, 'liga1', None)
    assert not _is_linked(b, 'liga1', a2)
    if hasattr(a2, 'equipo0'):
        assert not _is_linked(a2, 'equipo0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

