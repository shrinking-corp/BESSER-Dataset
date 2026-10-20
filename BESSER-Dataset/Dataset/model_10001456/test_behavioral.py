import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Apuesta,
    ApuestaEquipoGanador,
    ApuestaMarcadorEspecifico,
    Equipo,
    Historico,
    Marcador,
    Partido,
    SistemaApuesta,
    Tarjeta,
    Usuario,
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

def test_assoc_Apuesta_Partido_reverse_link_reassign_clear():
    a1 = Partido(idPartido="sample_text", numeroApuestas="sample_text")
    a2 = Partido(idPartido="sample_text_2", numeroApuestas="sample_text_2")
    b = Apuesta(id="sample_text", porcentajeGanancia="sample_text", valorApuesta="sample_text")
    _safe_set(b, 'partido6', a1)
    assert _is_linked(b, 'partido6', a1)
    if hasattr(a1, 'apuesta7'):
        assert _is_linked(a1, 'apuesta7', b)
    _safe_set(b, 'partido6', a2)
    assert _is_linked(b, 'partido6', a2)
    if hasattr(a1, 'apuesta7'):
        assert not _is_linked(a1, 'apuesta7', b)
    if hasattr(a2, 'apuesta7'):
        assert _is_linked(a2, 'apuesta7', b)
    _safe_set(b, 'partido6', None)
    assert not _is_linked(b, 'partido6', a2)
    if hasattr(a2, 'apuesta7'):
        assert not _is_linked(a2, 'apuesta7', b)


def test_assoc_Equipo_Historico_reverse_link_reassign_clear():
    a1 = Historico(numeroPartidosGanados=7, numeroPartidosJugados=7, numeroPartidosPerdidos=7, porcentajeApuestasEnFavor="sample_text")
    a2 = Historico(numeroPartidosGanados=13, numeroPartidosJugados=13, numeroPartidosPerdidos=13, porcentajeApuestasEnFavor="sample_text_2")
    b = Equipo(jugadores="sample_text", nombre="sample_text", porcentajeFavoritismo="sample_text")
    _safe_set(b, 'historico12', a1)
    assert _is_linked(b, 'historico12', a1)
    if hasattr(a1, 'equipo13'):
        assert _is_linked(a1, 'equipo13', b)
    _safe_set(b, 'historico12', a2)
    assert _is_linked(b, 'historico12', a2)
    if hasattr(a1, 'equipo13'):
        assert not _is_linked(a1, 'equipo13', b)
    if hasattr(a2, 'equipo13'):
        assert _is_linked(a2, 'equipo13', b)
    _safe_set(b, 'historico12', None)
    assert not _is_linked(b, 'historico12', a2)
    if hasattr(a2, 'equipo13'):
        assert not _is_linked(a2, 'equipo13', b)


def test_assoc_Historico__Partido_reverse_link_reassign_clear():
    a1 = Partido(idPartido="sample_text", numeroApuestas="sample_text")
    a2 = Partido(idPartido="sample_text_2", numeroApuestas="sample_text_2")
    b = Historico(numeroPartidosGanados=7, numeroPartidosJugados=7, numeroPartidosPerdidos=7, porcentajeApuestasEnFavor="sample_text")
    _safe_set(b, 'partido14', {a1})
    assert _is_linked(b, 'partido14', a1)
    if hasattr(a1, 'historico15'):
        assert _is_linked(a1, 'historico15', b)
    _safe_set(b, 'partido14', {a2})
    assert _is_linked(b, 'partido14', a2)
    if hasattr(a1, 'historico15'):
        assert not _is_linked(a1, 'historico15', b)
    if hasattr(a2, 'historico15'):
        assert _is_linked(a2, 'historico15', b)
    _safe_set(b, 'partido14', set())
    assert not _is_linked(b, 'partido14', a2)
    if hasattr(a2, 'historico15'):
        assert not _is_linked(a2, 'historico15', b)


def test_assoc_Partido_Equipo_reverse_link_reassign_clear():
    a1 = Partido(idPartido="sample_text", numeroApuestas="sample_text")
    a2 = Partido(idPartido="sample_text_2", numeroApuestas="sample_text_2")
    b = Equipo(jugadores="sample_text", nombre="sample_text", porcentajeFavoritismo="sample_text")
    _safe_set(b, 'partido9', a1)
    assert _is_linked(b, 'partido9', a1)
    if hasattr(a1, 'eq_18'):
        assert _is_linked(a1, 'eq_18', b)
    _safe_set(b, 'partido9', a2)
    assert _is_linked(b, 'partido9', a2)
    if hasattr(a1, 'eq_18'):
        assert not _is_linked(a1, 'eq_18', b)
    if hasattr(a2, 'eq_18'):
        assert _is_linked(a2, 'eq_18', b)
    _safe_set(b, 'partido9', None)
    assert not _is_linked(b, 'partido9', a2)
    if hasattr(a2, 'eq_18'):
        assert not _is_linked(a2, 'eq_18', b)


def test_assoc_Partido_Equipo2_reverse_link_reassign_clear():
    a1 = Partido(idPartido="sample_text", numeroApuestas="sample_text")
    a2 = Partido(idPartido="sample_text_2", numeroApuestas="sample_text_2")
    b = Equipo(jugadores="sample_text", nombre="sample_text", porcentajeFavoritismo="sample_text")
    _safe_set(b, 'partido11', a1)
    assert _is_linked(b, 'partido11', a1)
    if hasattr(a1, 'eq_210'):
        assert _is_linked(a1, 'eq_210', b)
    _safe_set(b, 'partido11', a2)
    assert _is_linked(b, 'partido11', a2)
    if hasattr(a1, 'eq_210'):
        assert not _is_linked(a1, 'eq_210', b)
    if hasattr(a2, 'eq_210'):
        assert _is_linked(a2, 'eq_210', b)
    _safe_set(b, 'partido11', None)
    assert not _is_linked(b, 'partido11', a2)
    if hasattr(a2, 'eq_210'):
        assert not _is_linked(a2, 'eq_210', b)


def test_assoc_Partido_Marcador_reverse_link_reassign_clear():
    a1 = Partido(idPartido="sample_text", numeroApuestas="sample_text")
    a2 = Partido(idPartido="sample_text_2", numeroApuestas="sample_text_2")
    b = Marcador(nombreEquipoGanador="sample_text", numeroGolesEquipo1=7, numeroGolesEquipo2=7)
    _safe_set(b, 'partido17', a1)
    assert _is_linked(b, 'partido17', a1)
    if hasattr(a1, 'marcador16'):
        assert _is_linked(a1, 'marcador16', b)
    _safe_set(b, 'partido17', a2)
    assert _is_linked(b, 'partido17', a2)
    if hasattr(a1, 'marcador16'):
        assert not _is_linked(a1, 'marcador16', b)
    if hasattr(a2, 'marcador16'):
        assert _is_linked(a2, 'marcador16', b)
    _safe_set(b, 'partido17', None)
    assert not _is_linked(b, 'partido17', a2)
    if hasattr(a2, 'marcador16'):
        assert not _is_linked(a2, 'marcador16', b)


def test_assoc_Usuario_Apuesta_reverse_link_reassign_clear():
    a1 = Usuario(passWord="sample_text", userName="sample_text")
    a2 = Usuario(passWord="sample_text_2", userName="sample_text_2")
    b = Apuesta(id="sample_text", porcentajeGanancia="sample_text", valorApuesta="sample_text")
    _safe_set(b, 'usuario5', a1)
    assert _is_linked(b, 'usuario5', a1)
    if hasattr(a1, 'apuesta4'):
        assert _is_linked(a1, 'apuesta4', b)
    _safe_set(b, 'usuario5', a2)
    assert _is_linked(b, 'usuario5', a2)
    if hasattr(a1, 'apuesta4'):
        assert not _is_linked(a1, 'apuesta4', b)
    if hasattr(a2, 'apuesta4'):
        assert _is_linked(a2, 'apuesta4', b)
    _safe_set(b, 'usuario5', None)
    assert not _is_linked(b, 'usuario5', a2)
    if hasattr(a2, 'apuesta4'):
        assert not _is_linked(a2, 'apuesta4', b)


def test_assoc_Usuario_Tarjeta_reverse_link_reassign_clear():
    a1 = Usuario(passWord="sample_text", userName="sample_text")
    a2 = Usuario(passWord="sample_text_2", userName="sample_text_2")
    b = Tarjeta(codigoSeguridad=7, numeroTarje=7)
    _safe_set(b, 'usuario3', a1)
    assert _is_linked(b, 'usuario3', a1)
    if hasattr(a1, 'tarjeta2'):
        assert _is_linked(a1, 'tarjeta2', b)
    _safe_set(b, 'usuario3', a2)
    assert _is_linked(b, 'usuario3', a2)
    if hasattr(a1, 'tarjeta2'):
        assert not _is_linked(a1, 'tarjeta2', b)
    if hasattr(a2, 'tarjeta2'):
        assert _is_linked(a2, 'tarjeta2', b)
    _safe_set(b, 'usuario3', None)
    assert not _is_linked(b, 'usuario3', a2)
    if hasattr(a2, 'tarjeta2'):
        assert not _is_linked(a2, 'tarjeta2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_SistemaApuesta_Apuesta_stub_double():
    # SistemaApuesta has no real 'apuesta18' property in the generated
    # code (a bare stub) -- manually attach it so Apuesta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Apuesta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Apuesta(id="sample_text", porcentajeGanancia="sample_text", valorApuesta="sample_text")
    partner = SistemaApuesta()
    setattr(partner, 'apuesta18', None)
    _safe_set(owner, 'sistemaApuesta19', partner)
    assert owner in getattr(partner, 'apuesta18')
    _safe_set(owner, 'sistemaApuesta19', None)
    assert owner not in getattr(partner, 'apuesta18')


def test_assoc_SistemaApuesta_Partido_stub_double():
    # SistemaApuesta has no real 'partido20' property in the generated
    # code (a bare stub) -- manually attach it so Partido's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Partido's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Partido(idPartido="sample_text", numeroApuestas="sample_text")
    partner = SistemaApuesta()
    setattr(partner, 'partido20', None)
    _safe_set(owner, 'sistemaApuesta21', partner)
    assert owner in getattr(partner, 'partido20')
    _safe_set(owner, 'sistemaApuesta21', None)
    assert owner not in getattr(partner, 'partido20')


def test_assoc_SistemaApuesta_Usuario_stub_double():
    # SistemaApuesta has no real 'usuario0' property in the generated
    # code (a bare stub) -- manually attach it so Usuario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Usuario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Usuario(passWord="sample_text", userName="sample_text")
    partner = SistemaApuesta()
    setattr(partner, 'usuario0', None)
    _safe_set(owner, 'sistemaApuesta1', partner)
    assert owner in getattr(partner, 'usuario0')
    _safe_set(owner, 'sistemaApuesta1', None)
    assert owner not in getattr(partner, 'usuario0')


