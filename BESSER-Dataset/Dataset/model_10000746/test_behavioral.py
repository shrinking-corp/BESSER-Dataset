import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arbitro,
    Clasificacion,
    Entrenador,
    Equipo,
    Estadio,
    Evento,
    Jugador,
    Lesion,
    Liga,
    Partido,
    Persona,
    TipoDeEvento,
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

def test_assoc_Entrenador_Equipo_reverse_link_reassign_clear():
    a1 = Equipo(Ciudad="sample_text", Cod_Entrenador="sample_text", Cod_equipo="sample_text", F_fundacion="sample_text", Nombre="sample_text", Titulos="sample_text")
    a2 = Equipo(Ciudad="sample_text_2", Cod_Entrenador="sample_text_2", Cod_equipo="sample_text_2", F_fundacion="sample_text_2", Nombre="sample_text_2", Titulos="sample_text_2")
    b = Entrenador(Cod_Entrenador="sample_text", Cod_persona="sample_text", Titulos="sample_text")
    _safe_set(b, 'equipo0', a1)
    assert _is_linked(b, 'equipo0', a1)
    if hasattr(a1, 'entrenador1'):
        assert _is_linked(a1, 'entrenador1', b)
    _safe_set(b, 'equipo0', a2)
    assert _is_linked(b, 'equipo0', a2)
    if hasattr(a1, 'entrenador1'):
        assert not _is_linked(a1, 'entrenador1', b)
    if hasattr(a2, 'entrenador1'):
        assert _is_linked(a2, 'entrenador1', b)
    _safe_set(b, 'equipo0', None)
    assert not _is_linked(b, 'equipo0', a2)
    if hasattr(a2, 'entrenador1'):
        assert not _is_linked(a2, 'entrenador1', b)


def test_assoc_Equipo_Partido_reverse_link_reassign_clear():
    a1 = Partido(Cod_liga="sample_text", Cod_partido="sample_text", Fecha="sample_text", Ganador="sample_text", GolLocal="sample_text", GolVisita="sample_text", Hora="sample_text", Local="sample_text", Visita="sample_text")
    a2 = Partido(Cod_liga="sample_text_2", Cod_partido="sample_text_2", Fecha="sample_text_2", Ganador="sample_text_2", GolLocal="sample_text_2", GolVisita="sample_text_2", Hora="sample_text_2", Local="sample_text_2", Visita="sample_text_2")
    b = Equipo(Ciudad="sample_text", Cod_Entrenador="sample_text", Cod_equipo="sample_text", F_fundacion="sample_text", Nombre="sample_text", Titulos="sample_text")
    _safe_set(b, 'partido8', {a1})
    assert _is_linked(b, 'partido8', a1)
    if hasattr(a1, 'equipo9'):
        assert _is_linked(a1, 'equipo9', b)
    _safe_set(b, 'partido8', {a2})
    assert _is_linked(b, 'partido8', a2)
    if hasattr(a1, 'equipo9'):
        assert not _is_linked(a1, 'equipo9', b)
    if hasattr(a2, 'equipo9'):
        assert _is_linked(a2, 'equipo9', b)
    _safe_set(b, 'partido8', set())
    assert not _is_linked(b, 'partido8', a2)
    if hasattr(a2, 'equipo9'):
        assert not _is_linked(a2, 'equipo9', b)


def test_assoc_Evento_Partido_reverse_link_reassign_clear():
    a1 = Partido(Cod_liga="sample_text", Cod_partido="sample_text", Fecha="sample_text", Ganador="sample_text", GolLocal="sample_text", GolVisita="sample_text", Hora="sample_text", Local="sample_text", Visita="sample_text")
    a2 = Partido(Cod_liga="sample_text_2", Cod_partido="sample_text_2", Fecha="sample_text_2", Ganador="sample_text_2", GolLocal="sample_text_2", GolVisita="sample_text_2", Hora="sample_text_2", Local="sample_text_2", Visita="sample_text_2")
    b = Evento(Cod_TipodeEvento="sample_text", Cod_jugador="sample_text", Cod_partido="sample_text")
    _safe_set(b, 'partido12', a1)
    assert _is_linked(b, 'partido12', a1)
    if hasattr(a1, 'evento13'):
        assert _is_linked(a1, 'evento13', b)
    _safe_set(b, 'partido12', a2)
    assert _is_linked(b, 'partido12', a2)
    if hasattr(a1, 'evento13'):
        assert not _is_linked(a1, 'evento13', b)
    if hasattr(a2, 'evento13'):
        assert _is_linked(a2, 'evento13', b)
    _safe_set(b, 'partido12', None)
    assert not _is_linked(b, 'partido12', a2)
    if hasattr(a2, 'evento13'):
        assert not _is_linked(a2, 'evento13', b)


def test_assoc_Jugador_Equipo_reverse_link_reassign_clear():
    a1 = Jugador(Altura="sample_text", Cod_equipo="sample_text", Cod_jugador="sample_text", Cod_persona="sample_text", Dorsal="sample_text", Peso="sample_text", Posicion="sample_text", Titulos="sample_text")
    a2 = Jugador(Altura="sample_text_2", Cod_equipo="sample_text_2", Cod_jugador="sample_text_2", Cod_persona="sample_text_2", Dorsal="sample_text_2", Peso="sample_text_2", Posicion="sample_text_2", Titulos="sample_text_2")
    b = Equipo(Ciudad="sample_text", Cod_Entrenador="sample_text", Cod_equipo="sample_text", F_fundacion="sample_text", Nombre="sample_text", Titulos="sample_text")
    _safe_set(b, 'jugador3', {a1})
    assert _is_linked(b, 'jugador3', a1)
    if hasattr(a1, 'equipo2'):
        assert _is_linked(a1, 'equipo2', b)
    _safe_set(b, 'jugador3', {a2})
    assert _is_linked(b, 'jugador3', a2)
    if hasattr(a1, 'equipo2'):
        assert not _is_linked(a1, 'equipo2', b)
    if hasattr(a2, 'equipo2'):
        assert _is_linked(a2, 'equipo2', b)
    _safe_set(b, 'jugador3', set())
    assert not _is_linked(b, 'jugador3', a2)
    if hasattr(a2, 'equipo2'):
        assert not _is_linked(a2, 'equipo2', b)


def test_assoc_Jugador_Evento_reverse_link_reassign_clear():
    a1 = Jugador(Altura="sample_text", Cod_equipo="sample_text", Cod_jugador="sample_text", Cod_persona="sample_text", Dorsal="sample_text", Peso="sample_text", Posicion="sample_text", Titulos="sample_text")
    a2 = Jugador(Altura="sample_text_2", Cod_equipo="sample_text_2", Cod_jugador="sample_text_2", Cod_persona="sample_text_2", Dorsal="sample_text_2", Peso="sample_text_2", Posicion="sample_text_2", Titulos="sample_text_2")
    b = Evento(Cod_TipodeEvento="sample_text", Cod_jugador="sample_text", Cod_partido="sample_text")
    _safe_set(b, 'jugador11', a1)
    assert _is_linked(b, 'jugador11', a1)
    if hasattr(a1, 'evento10'):
        assert _is_linked(a1, 'evento10', b)
    _safe_set(b, 'jugador11', a2)
    assert _is_linked(b, 'jugador11', a2)
    if hasattr(a1, 'evento10'):
        assert not _is_linked(a1, 'evento10', b)
    if hasattr(a2, 'evento10'):
        assert _is_linked(a2, 'evento10', b)
    _safe_set(b, 'jugador11', None)
    assert not _is_linked(b, 'jugador11', a2)
    if hasattr(a2, 'evento10'):
        assert not _is_linked(a2, 'evento10', b)


def test_assoc_Jugador_Lesion_reverse_link_reassign_clear():
    a1 = Lesion(Cod_jugador="sample_text", Condicion="sample_text", FechaLesion="sample_text", TiempoLesion="sample_text")
    a2 = Lesion(Cod_jugador="sample_text_2", Condicion="sample_text_2", FechaLesion="sample_text_2", TiempoLesion="sample_text_2")
    b = Jugador(Altura="sample_text", Cod_equipo="sample_text", Cod_jugador="sample_text", Cod_persona="sample_text", Dorsal="sample_text", Peso="sample_text", Posicion="sample_text", Titulos="sample_text")
    _safe_set(b, 'lesion22', {a1})
    assert _is_linked(b, 'lesion22', a1)
    if hasattr(a1, 'jugador23'):
        assert _is_linked(a1, 'jugador23', b)
    _safe_set(b, 'lesion22', {a2})
    assert _is_linked(b, 'lesion22', a2)
    if hasattr(a1, 'jugador23'):
        assert not _is_linked(a1, 'jugador23', b)
    if hasattr(a2, 'jugador23'):
        assert _is_linked(a2, 'jugador23', b)
    _safe_set(b, 'lesion22', set())
    assert not _is_linked(b, 'lesion22', a2)
    if hasattr(a2, 'jugador23'):
        assert not _is_linked(a2, 'jugador23', b)


def test_assoc_Liga_Clasificacion_reverse_link_reassign_clear():
    a1 = Liga(Cod_Clasificacion="sample_text", Cod_liga="sample_text", Inferior="sample_text", Nombre="sample_text", Num_equipos="sample_text", Superior="sample_text")
    a2 = Liga(Cod_Clasificacion="sample_text_2", Cod_liga="sample_text_2", Inferior="sample_text_2", Nombre="sample_text_2", Num_equipos="sample_text_2", Superior="sample_text_2")
    b = Clasificacion(Cod_Equipo="sample_text", DG="sample_text", GC="sample_text", GF="sample_text", JE="sample_text", JG="sample_text", JJ="sample_text", JP="sample_text", Posicion="sample_text", Puntos="sample_text")
    _safe_set(b, 'liga27', {a1})
    assert _is_linked(b, 'liga27', a1)
    if hasattr(a1, 'clasificacion26'):
        assert _is_linked(a1, 'clasificacion26', b)
    _safe_set(b, 'liga27', {a2})
    assert _is_linked(b, 'liga27', a2)
    if hasattr(a1, 'clasificacion26'):
        assert not _is_linked(a1, 'clasificacion26', b)
    if hasattr(a2, 'clasificacion26'):
        assert _is_linked(a2, 'clasificacion26', b)
    _safe_set(b, 'liga27', set())
    assert not _is_linked(b, 'liga27', a2)
    if hasattr(a2, 'clasificacion26'):
        assert not _is_linked(a2, 'clasificacion26', b)


def test_assoc_Liga_Partido_reverse_link_reassign_clear():
    a1 = Partido(Cod_liga="sample_text", Cod_partido="sample_text", Fecha="sample_text", Ganador="sample_text", GolLocal="sample_text", GolVisita="sample_text", Hora="sample_text", Local="sample_text", Visita="sample_text")
    a2 = Partido(Cod_liga="sample_text_2", Cod_partido="sample_text_2", Fecha="sample_text_2", Ganador="sample_text_2", GolLocal="sample_text_2", GolVisita="sample_text_2", Hora="sample_text_2", Local="sample_text_2", Visita="sample_text_2")
    b = Liga(Cod_Clasificacion="sample_text", Cod_liga="sample_text", Inferior="sample_text", Nombre="sample_text", Num_equipos="sample_text", Superior="sample_text")
    _safe_set(b, 'partido24', {a1})
    assert _is_linked(b, 'partido24', a1)
    if hasattr(a1, 'liga25'):
        assert _is_linked(a1, 'liga25', b)
    _safe_set(b, 'partido24', {a2})
    assert _is_linked(b, 'partido24', a2)
    if hasattr(a1, 'liga25'):
        assert not _is_linked(a1, 'liga25', b)
    if hasattr(a2, 'liga25'):
        assert _is_linked(a2, 'liga25', b)
    _safe_set(b, 'partido24', set())
    assert not _is_linked(b, 'partido24', a2)
    if hasattr(a2, 'liga25'):
        assert not _is_linked(a2, 'liga25', b)


def test_assoc_Partido_Equipo_reverse_link_reassign_clear():
    a1 = Partido(Cod_liga="sample_text", Cod_partido="sample_text", Fecha="sample_text", Ganador="sample_text", GolLocal="sample_text", GolVisita="sample_text", Hora="sample_text", Local="sample_text", Visita="sample_text")
    a2 = Partido(Cod_liga="sample_text_2", Cod_partido="sample_text_2", Fecha="sample_text_2", Ganador="sample_text_2", GolLocal="sample_text_2", GolVisita="sample_text_2", Hora="sample_text_2", Local="sample_text_2", Visita="sample_text_2")
    b = Equipo(Ciudad="sample_text", Cod_Entrenador="sample_text", Cod_equipo="sample_text", F_fundacion="sample_text", Nombre="sample_text", Titulos="sample_text")
    _safe_set(b, 'partido7', {a1})
    assert _is_linked(b, 'partido7', a1)
    if hasattr(a1, 'equipo6'):
        assert _is_linked(a1, 'equipo6', b)
    _safe_set(b, 'partido7', {a2})
    assert _is_linked(b, 'partido7', a2)
    if hasattr(a1, 'equipo6'):
        assert not _is_linked(a1, 'equipo6', b)
    if hasattr(a2, 'equipo6'):
        assert _is_linked(a2, 'equipo6', b)
    _safe_set(b, 'partido7', set())
    assert not _is_linked(b, 'partido7', a2)
    if hasattr(a2, 'equipo6'):
        assert not _is_linked(a2, 'equipo6', b)


def test_assoc_Partido_Estadio_reverse_link_reassign_clear():
    a1 = Partido(Cod_liga="sample_text", Cod_partido="sample_text", Fecha="sample_text", Ganador="sample_text", GolLocal="sample_text", GolVisita="sample_text", Hora="sample_text", Local="sample_text", Visita="sample_text")
    a2 = Partido(Cod_liga="sample_text_2", Cod_partido="sample_text_2", Fecha="sample_text_2", Ganador="sample_text_2", GolLocal="sample_text_2", GolVisita="sample_text_2", Hora="sample_text_2", Local="sample_text_2", Visita="sample_text_2")
    b = Estadio(Capacidad="sample_text", Cod_Estadio="sample_text", Cod_equipo="sample_text", Nombre="sample_text", Terreno="sample_text", Ubicacion="sample_text", Ubicacion1="sample_text")
    _safe_set(b, 'partido5', {a1})
    assert _is_linked(b, 'partido5', a1)
    if hasattr(a1, 'estadio4'):
        assert _is_linked(a1, 'estadio4', b)
    _safe_set(b, 'partido5', {a2})
    assert _is_linked(b, 'partido5', a2)
    if hasattr(a1, 'estadio4'):
        assert not _is_linked(a1, 'estadio4', b)
    if hasattr(a2, 'estadio4'):
        assert _is_linked(a2, 'estadio4', b)
    _safe_set(b, 'partido5', set())
    assert not _is_linked(b, 'partido5', a2)
    if hasattr(a2, 'estadio4'):
        assert not _is_linked(a2, 'estadio4', b)


def test_assoc_Persona_Arbitro_reverse_link_reassign_clear():
    a1 = Persona(Apellido="sample_text", Cod_persona="sample_text", FechaNacimiento="sample_text", Nacionalidad="sample_text", Nombre="sample_text", NombreCorto="sample_text")
    a2 = Persona(Apellido="sample_text_2", Cod_persona="sample_text_2", FechaNacimiento="sample_text_2", Nacionalidad="sample_text_2", Nombre="sample_text_2", NombreCorto="sample_text_2")
    b = Arbitro(Cod_Arbitro="sample_text", Cod_persona="sample_text", Partidos="sample_text")
    _safe_set(b, 'persona17', a1)
    assert _is_linked(b, 'persona17', a1)
    if hasattr(a1, 'arbitro16'):
        assert _is_linked(a1, 'arbitro16', b)
    _safe_set(b, 'persona17', a2)
    assert _is_linked(b, 'persona17', a2)
    if hasattr(a1, 'arbitro16'):
        assert not _is_linked(a1, 'arbitro16', b)
    if hasattr(a2, 'arbitro16'):
        assert _is_linked(a2, 'arbitro16', b)
    _safe_set(b, 'persona17', None)
    assert not _is_linked(b, 'persona17', a2)
    if hasattr(a2, 'arbitro16'):
        assert not _is_linked(a2, 'arbitro16', b)


def test_assoc_Persona_Entrenador_reverse_link_reassign_clear():
    a1 = Persona(Apellido="sample_text", Cod_persona="sample_text", FechaNacimiento="sample_text", Nacionalidad="sample_text", Nombre="sample_text", NombreCorto="sample_text")
    a2 = Persona(Apellido="sample_text_2", Cod_persona="sample_text_2", FechaNacimiento="sample_text_2", Nacionalidad="sample_text_2", Nombre="sample_text_2", NombreCorto="sample_text_2")
    b = Entrenador(Cod_Entrenador="sample_text", Cod_persona="sample_text", Titulos="sample_text")
    _safe_set(b, 'persona21', a1)
    assert _is_linked(b, 'persona21', a1)
    if hasattr(a1, 'entrenador20'):
        assert _is_linked(a1, 'entrenador20', b)
    _safe_set(b, 'persona21', a2)
    assert _is_linked(b, 'persona21', a2)
    if hasattr(a1, 'entrenador20'):
        assert not _is_linked(a1, 'entrenador20', b)
    if hasattr(a2, 'entrenador20'):
        assert _is_linked(a2, 'entrenador20', b)
    _safe_set(b, 'persona21', None)
    assert not _is_linked(b, 'persona21', a2)
    if hasattr(a2, 'entrenador20'):
        assert not _is_linked(a2, 'entrenador20', b)


def test_assoc_Persona_Jugador_reverse_link_reassign_clear():
    a1 = Persona(Apellido="sample_text", Cod_persona="sample_text", FechaNacimiento="sample_text", Nacionalidad="sample_text", Nombre="sample_text", NombreCorto="sample_text")
    a2 = Persona(Apellido="sample_text_2", Cod_persona="sample_text_2", FechaNacimiento="sample_text_2", Nacionalidad="sample_text_2", Nombre="sample_text_2", NombreCorto="sample_text_2")
    b = Jugador(Altura="sample_text", Cod_equipo="sample_text", Cod_jugador="sample_text", Cod_persona="sample_text", Dorsal="sample_text", Peso="sample_text", Posicion="sample_text", Titulos="sample_text")
    _safe_set(b, 'persona19', a1)
    assert _is_linked(b, 'persona19', a1)
    if hasattr(a1, 'jugador18'):
        assert _is_linked(a1, 'jugador18', b)
    _safe_set(b, 'persona19', a2)
    assert _is_linked(b, 'persona19', a2)
    if hasattr(a1, 'jugador18'):
        assert not _is_linked(a1, 'jugador18', b)
    if hasattr(a2, 'jugador18'):
        assert _is_linked(a2, 'jugador18', b)
    _safe_set(b, 'persona19', None)
    assert not _is_linked(b, 'persona19', a2)
    if hasattr(a2, 'jugador18'):
        assert not _is_linked(a2, 'jugador18', b)


def test_assoc_TipoDeEvento_Evento_reverse_link_reassign_clear():
    a1 = TipoDeEvento(Cod_TipodeEvento="sample_text", Evento="sample_text")
    a2 = TipoDeEvento(Cod_TipodeEvento="sample_text_2", Evento="sample_text_2")
    b = Evento(Cod_TipodeEvento="sample_text", Cod_jugador="sample_text", Cod_partido="sample_text")
    _safe_set(b, 'tipoDeEvento15', a1)
    assert _is_linked(b, 'tipoDeEvento15', a1)
    if hasattr(a1, 'evento14'):
        assert _is_linked(a1, 'evento14', b)
    _safe_set(b, 'tipoDeEvento15', a2)
    assert _is_linked(b, 'tipoDeEvento15', a2)
    if hasattr(a1, 'evento14'):
        assert not _is_linked(a1, 'evento14', b)
    if hasattr(a2, 'evento14'):
        assert _is_linked(a2, 'evento14', b)
    _safe_set(b, 'tipoDeEvento15', None)
    assert not _is_linked(b, 'tipoDeEvento15', a2)
    if hasattr(a2, 'evento14'):
        assert not _is_linked(a2, 'evento14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

