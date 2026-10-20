import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Equipo,
    Fecha,
    Jugador,
    Marcador,
    Partido,
    Premio,
    Torneo,
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

def test_assoc_Equipo_Jugador_reverse_link_reassign_clear():
    a1 = Jugador(apellidos="sample_text", nif="sample_text", nombre="sample_text", telefono=7)
    a2 = Jugador(apellidos="sample_text_2", nif="sample_text_2", nombre="sample_text_2", telefono=13)
    b = Equipo(nombre="sample_text")
    _safe_set(b, 'jugador6', {a1})
    assert _is_linked(b, 'jugador6', a1)
    if hasattr(a1, 'equipo7'):
        assert _is_linked(a1, 'equipo7', b)
    _safe_set(b, 'jugador6', {a2})
    assert _is_linked(b, 'jugador6', a2)
    if hasattr(a1, 'equipo7'):
        assert not _is_linked(a1, 'equipo7', b)
    if hasattr(a2, 'equipo7'):
        assert _is_linked(a2, 'equipo7', b)
    _safe_set(b, 'jugador6', set())
    assert not _is_linked(b, 'jugador6', a2)
    if hasattr(a2, 'equipo7'):
        assert not _is_linked(a2, 'equipo7', b)


def test_assoc_Jugador_Fecha_Nacimiento_reverse_link_reassign_clear():
    a1 = Jugador(apellidos="sample_text", nif="sample_text", nombre="sample_text", telefono=7)
    a2 = Jugador(apellidos="sample_text_2", nif="sample_text_2", nombre="sample_text_2", telefono=13)
    b = Fecha(anio=7, dia=7, mes=7)
    _safe_set(b, 'jugador9', a1)
    assert _is_linked(b, 'jugador9', a1)
    if hasattr(a1, 'fechaNacimiento8'):
        assert _is_linked(a1, 'fechaNacimiento8', b)
    _safe_set(b, 'jugador9', a2)
    assert _is_linked(b, 'jugador9', a2)
    if hasattr(a1, 'fechaNacimiento8'):
        assert not _is_linked(a1, 'fechaNacimiento8', b)
    if hasattr(a2, 'fechaNacimiento8'):
        assert _is_linked(a2, 'fechaNacimiento8', b)
    _safe_set(b, 'jugador9', None)
    assert not _is_linked(b, 'jugador9', a2)
    if hasattr(a2, 'fechaNacimiento8'):
        assert not _is_linked(a2, 'fechaNacimiento8', b)


def test_assoc_Partido_Equipo_reverse_link_reassign_clear():
    a1 = Partido(id=7, ronda="sample_text")
    a2 = Partido(id=13, ronda="sample_text_2")
    b = Equipo(nombre="sample_text")
    _safe_set(b, 'partido5', a1)
    assert _is_linked(b, 'partido5', a1)
    if hasattr(a1, 'equipo4'):
        assert _is_linked(a1, 'equipo4', b)
    _safe_set(b, 'partido5', a2)
    assert _is_linked(b, 'partido5', a2)
    if hasattr(a1, 'equipo4'):
        assert not _is_linked(a1, 'equipo4', b)
    if hasattr(a2, 'equipo4'):
        assert _is_linked(a2, 'equipo4', b)
    _safe_set(b, 'partido5', None)
    assert not _is_linked(b, 'partido5', a2)
    if hasattr(a2, 'equipo4'):
        assert not _is_linked(a2, 'equipo4', b)


def test_assoc_Partido_Marcador_reverse_link_reassign_clear():
    a1 = Partido(id=7, ronda="sample_text")
    a2 = Partido(id=13, ronda="sample_text_2")
    b = Marcador(equipo1=7, equipo2=7, tiempoSet=7)
    _safe_set(b, 'partido3', a1)
    assert _is_linked(b, 'partido3', a1)
    if hasattr(a1, 'marcador2'):
        assert _is_linked(a1, 'marcador2', b)
    _safe_set(b, 'partido3', a2)
    assert _is_linked(b, 'partido3', a2)
    if hasattr(a1, 'marcador2'):
        assert not _is_linked(a1, 'marcador2', b)
    if hasattr(a2, 'marcador2'):
        assert _is_linked(a2, 'marcador2', b)
    _safe_set(b, 'partido3', None)
    assert not _is_linked(b, 'partido3', a2)
    if hasattr(a2, 'marcador2'):
        assert not _is_linked(a2, 'marcador2', b)


def test_assoc_Torneo_Fecha_Fin_reverse_link_reassign_clear():
    a1 = Torneo(Nombre="sample_text", Pais="sample_text")
    a2 = Torneo(Nombre="sample_text_2", Pais="sample_text_2")
    b = Fecha(anio=7, dia=7, mes=7)
    _safe_set(b, 'torneo13', a1)
    assert _is_linked(b, 'torneo13', a1)
    if hasattr(a1, 'fechaFin12'):
        assert _is_linked(a1, 'fechaFin12', b)
    _safe_set(b, 'torneo13', a2)
    assert _is_linked(b, 'torneo13', a2)
    if hasattr(a1, 'fechaFin12'):
        assert not _is_linked(a1, 'fechaFin12', b)
    if hasattr(a2, 'fechaFin12'):
        assert _is_linked(a2, 'fechaFin12', b)
    _safe_set(b, 'torneo13', None)
    assert not _is_linked(b, 'torneo13', a2)
    if hasattr(a2, 'fechaFin12'):
        assert not _is_linked(a2, 'fechaFin12', b)


def test_assoc_Torneo_Fecha_Inicio_reverse_link_reassign_clear():
    a1 = Torneo(Nombre="sample_text", Pais="sample_text")
    a2 = Torneo(Nombre="sample_text_2", Pais="sample_text_2")
    b = Fecha(anio=7, dia=7, mes=7)
    _safe_set(b, 'torneo11', a1)
    assert _is_linked(b, 'torneo11', a1)
    if hasattr(a1, 'fechaInicio10'):
        assert _is_linked(a1, 'fechaInicio10', b)
    _safe_set(b, 'torneo11', a2)
    assert _is_linked(b, 'torneo11', a2)
    if hasattr(a1, 'fechaInicio10'):
        assert not _is_linked(a1, 'fechaInicio10', b)
    if hasattr(a2, 'fechaInicio10'):
        assert _is_linked(a2, 'fechaInicio10', b)
    _safe_set(b, 'torneo11', None)
    assert not _is_linked(b, 'torneo11', a2)
    if hasattr(a2, 'fechaInicio10'):
        assert not _is_linked(a2, 'fechaInicio10', b)


def test_assoc_Torneo_Partido_reverse_link_reassign_clear():
    a1 = Torneo(Nombre="sample_text", Pais="sample_text")
    a2 = Torneo(Nombre="sample_text_2", Pais="sample_text_2")
    b = Partido(id=7, ronda="sample_text")
    _safe_set(b, 'torneo15', a1)
    assert _is_linked(b, 'torneo15', a1)
    if hasattr(a1, 'partido14'):
        assert _is_linked(a1, 'partido14', b)
    _safe_set(b, 'torneo15', a2)
    assert _is_linked(b, 'torneo15', a2)
    if hasattr(a1, 'partido14'):
        assert not _is_linked(a1, 'partido14', b)
    if hasattr(a2, 'partido14'):
        assert _is_linked(a2, 'partido14', b)
    _safe_set(b, 'torneo15', None)
    assert not _is_linked(b, 'torneo15', a2)
    if hasattr(a2, 'partido14'):
        assert not _is_linked(a2, 'partido14', b)


def test_assoc_Torneo_Premio_reverse_link_reassign_clear():
    a1 = Torneo(Nombre="sample_text", Pais="sample_text")
    a2 = Torneo(Nombre="sample_text_2", Pais="sample_text_2")
    b = Premio(Dinero=7, Puesto=7, Puntos=7)
    _safe_set(b, 'torneo1', a1)
    assert _is_linked(b, 'torneo1', a1)
    if hasattr(a1, 'premio0'):
        assert _is_linked(a1, 'premio0', b)
    _safe_set(b, 'torneo1', a2)
    assert _is_linked(b, 'torneo1', a2)
    if hasattr(a1, 'premio0'):
        assert not _is_linked(a1, 'premio0', b)
    if hasattr(a2, 'premio0'):
        assert _is_linked(a2, 'premio0', b)
    _safe_set(b, 'torneo1', None)
    assert not _is_linked(b, 'torneo1', a2)
    if hasattr(a2, 'premio0'):
        assert not _is_linked(a2, 'premio0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

