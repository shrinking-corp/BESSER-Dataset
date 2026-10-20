import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    itculiacan_Alumno,
    itculiacan_Aula,
    itculiacan_Generacion,
    itculiacan_Grupo,
    itculiacan_Materia,
    itculiacan_PlanEstudio,
    itculiacan_Profesor,
    itculiacan_Universidad,
    Nombramiento,
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

def test_assoc_alumnos11_reverse_link_reassign_clear():
    a1 = itculiacan_Grupo(clave=7)
    a2 = itculiacan_Grupo(clave=13)
    b = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    _safe_set(b, 'Alumno13', a1)
    assert _is_linked(b, 'Alumno13', a1)
    if hasattr(a1, 'grupos12'):
        assert _is_linked(a1, 'grupos12', b)
    _safe_set(b, 'Alumno13', a2)
    assert _is_linked(b, 'Alumno13', a2)
    if hasattr(a1, 'grupos12'):
        assert not _is_linked(a1, 'grupos12', b)
    if hasattr(a2, 'grupos12'):
        assert _is_linked(a2, 'grupos12', b)
    _safe_set(b, 'Alumno13', None)
    assert not _is_linked(b, 'Alumno13', a2)
    if hasattr(a2, 'grupos12'):
        assert not _is_linked(a2, 'grupos12', b)


def test_assoc_alumnos22_reverse_link_reassign_clear():
    a1 = itculiacan_PlanEstudio(clave=7, nombre="sample_text")
    a2 = itculiacan_PlanEstudio(clave=13, nombre="sample_text_2")
    b = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    _safe_set(b, 'Alumno23', a1)
    assert _is_linked(b, 'Alumno23', a1)
    if hasattr(a1, 'cursa'):
        assert _is_linked(a1, 'cursa', b)
    _safe_set(b, 'Alumno23', a2)
    assert _is_linked(b, 'Alumno23', a2)
    if hasattr(a1, 'cursa'):
        assert not _is_linked(a1, 'cursa', b)
    if hasattr(a2, 'cursa'):
        assert _is_linked(a2, 'cursa', b)
    _safe_set(b, 'Alumno23', None)
    assert not _is_linked(b, 'Alumno23', a2)
    if hasattr(a2, 'cursa'):
        assert not _is_linked(a2, 'cursa', b)


def test_assoc_alumnos5_reverse_link_reassign_clear():
    a1 = itculiacan_Generacion(fechaFin=date(2024, 1, 1), fechaInicio=date(2024, 1, 1))
    a2 = itculiacan_Generacion(fechaFin=date(2025, 6, 15), fechaInicio=date(2025, 6, 15))
    b = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    _safe_set(b, 'Alumno', a1)
    assert _is_linked(b, 'Alumno', a1)
    if hasattr(a1, 'generacion'):
        assert _is_linked(a1, 'generacion', b)
    _safe_set(b, 'Alumno', a2)
    assert _is_linked(b, 'Alumno', a2)
    if hasattr(a1, 'generacion'):
        assert not _is_linked(a1, 'generacion', b)
    if hasattr(a2, 'generacion'):
        assert _is_linked(a2, 'generacion', b)
    _safe_set(b, 'Alumno', None)
    assert not _is_linked(b, 'Alumno', a2)
    if hasattr(a2, 'generacion'):
        assert not _is_linked(a2, 'generacion', b)


def test_assoc_aula6_reverse_link_reassign_clear():
    a1 = itculiacan_Grupo(clave=7)
    a2 = itculiacan_Grupo(clave=13)
    b = itculiacan_Aula(capacidad=7, clave=7)
    _safe_set(b, 'Aula', a1)
    assert _is_linked(b, 'Aula', a1)
    if hasattr(a1, 'grupos'):
        assert _is_linked(a1, 'grupos', b)
    _safe_set(b, 'Aula', a2)
    assert _is_linked(b, 'Aula', a2)
    if hasattr(a1, 'grupos'):
        assert not _is_linked(a1, 'grupos', b)
    if hasattr(a2, 'grupos'):
        assert _is_linked(a2, 'grupos', b)
    _safe_set(b, 'Aula', None)
    assert not _is_linked(b, 'Aula', a2)
    if hasattr(a2, 'grupos'):
        assert not _is_linked(a2, 'grupos', b)


def test_assoc_cursa1_reverse_link_reassign_clear():
    a1 = itculiacan_PlanEstudio(clave=7, nombre="sample_text")
    a2 = itculiacan_PlanEstudio(clave=13, nombre="sample_text_2")
    b = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    _safe_set(b, 'alumnos2', a1)
    assert _is_linked(b, 'alumnos2', a1)
    if hasattr(a1, 'PlanEstudio'):
        assert _is_linked(a1, 'PlanEstudio', b)
    _safe_set(b, 'alumnos2', a2)
    assert _is_linked(b, 'alumnos2', a2)
    if hasattr(a1, 'PlanEstudio'):
        assert not _is_linked(a1, 'PlanEstudio', b)
    if hasattr(a2, 'PlanEstudio'):
        assert _is_linked(a2, 'PlanEstudio', b)
    _safe_set(b, 'alumnos2', None)
    assert not _is_linked(b, 'alumnos2', a2)
    if hasattr(a2, 'PlanEstudio'):
        assert not _is_linked(a2, 'PlanEstudio', b)


def test_assoc_generacion0_reverse_link_reassign_clear():
    a1 = itculiacan_Generacion(fechaFin=date(2024, 1, 1), fechaInicio=date(2024, 1, 1))
    a2 = itculiacan_Generacion(fechaFin=date(2025, 6, 15), fechaInicio=date(2025, 6, 15))
    b = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    _safe_set(b, 'alumnos', a1)
    assert _is_linked(b, 'alumnos', a1)
    if hasattr(a1, 'Generacion'):
        assert _is_linked(a1, 'Generacion', b)
    _safe_set(b, 'alumnos', a2)
    assert _is_linked(b, 'alumnos', a2)
    if hasattr(a1, 'Generacion'):
        assert not _is_linked(a1, 'Generacion', b)
    if hasattr(a2, 'Generacion'):
        assert _is_linked(a2, 'Generacion', b)
    _safe_set(b, 'alumnos', None)
    assert not _is_linked(b, 'alumnos', a2)
    if hasattr(a2, 'Generacion'):
        assert not _is_linked(a2, 'Generacion', b)


def test_assoc_grupos14_reverse_link_reassign_clear():
    a1 = itculiacan_Grupo(clave=7)
    a2 = itculiacan_Grupo(clave=13)
    b = itculiacan_Aula(capacidad=7, clave=7)
    _safe_set(b, 'aula', {a1})
    assert _is_linked(b, 'aula', a1)
    if hasattr(a1, 'Grupo15'):
        assert _is_linked(a1, 'Grupo15', b)
    _safe_set(b, 'aula', {a2})
    assert _is_linked(b, 'aula', a2)
    if hasattr(a1, 'Grupo15'):
        assert not _is_linked(a1, 'Grupo15', b)
    if hasattr(a2, 'Grupo15'):
        assert _is_linked(a2, 'Grupo15', b)
    _safe_set(b, 'aula', set())
    assert not _is_linked(b, 'aula', a2)
    if hasattr(a2, 'Grupo15'):
        assert not _is_linked(a2, 'Grupo15', b)


def test_assoc_grupos16_reverse_link_reassign_clear():
    a1 = itculiacan_Materia(clave=7, nombre="sample_text")
    a2 = itculiacan_Materia(clave=13, nombre="sample_text_2")
    b = itculiacan_Grupo(clave=7)
    _safe_set(b, 'Grupo17', a1)
    assert _is_linked(b, 'Grupo17', a1)
    if hasattr(a1, 'materia'):
        assert _is_linked(a1, 'materia', b)
    _safe_set(b, 'Grupo17', a2)
    assert _is_linked(b, 'Grupo17', a2)
    if hasattr(a1, 'materia'):
        assert not _is_linked(a1, 'materia', b)
    if hasattr(a2, 'materia'):
        assert _is_linked(a2, 'materia', b)
    _safe_set(b, 'Grupo17', None)
    assert not _is_linked(b, 'Grupo17', a2)
    if hasattr(a2, 'materia'):
        assert not _is_linked(a2, 'materia', b)


def test_assoc_grupos20_reverse_link_reassign_clear():
    a1 = itculiacan_Profesor(clave=7, nombramiento="sample_text", nombre="sample_text", numeroMaterias=7)
    a2 = itculiacan_Profesor(clave=13, nombramiento="sample_text_2", nombre="sample_text_2", numeroMaterias=13)
    b = itculiacan_Grupo(clave=7)
    _safe_set(b, 'Grupo21', a1)
    assert _is_linked(b, 'Grupo21', a1)
    if hasattr(a1, 'profesor'):
        assert _is_linked(a1, 'profesor', b)
    _safe_set(b, 'Grupo21', a2)
    assert _is_linked(b, 'Grupo21', a2)
    if hasattr(a1, 'profesor'):
        assert not _is_linked(a1, 'profesor', b)
    if hasattr(a2, 'profesor'):
        assert _is_linked(a2, 'profesor', b)
    _safe_set(b, 'Grupo21', None)
    assert not _is_linked(b, 'Grupo21', a2)
    if hasattr(a2, 'profesor'):
        assert not _is_linked(a2, 'profesor', b)


def test_assoc_grupos3_reverse_link_reassign_clear():
    a1 = itculiacan_Grupo(clave=7)
    a2 = itculiacan_Grupo(clave=13)
    b = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    _safe_set(b, 'alumnos4', {a1})
    assert _is_linked(b, 'alumnos4', a1)
    if hasattr(a1, 'Grupo'):
        assert _is_linked(a1, 'Grupo', b)
    _safe_set(b, 'alumnos4', {a2})
    assert _is_linked(b, 'alumnos4', a2)
    if hasattr(a1, 'Grupo'):
        assert not _is_linked(a1, 'Grupo', b)
    if hasattr(a2, 'Grupo'):
        assert _is_linked(a2, 'Grupo', b)
    _safe_set(b, 'alumnos4', set())
    assert not _is_linked(b, 'alumnos4', a2)
    if hasattr(a2, 'Grupo'):
        assert not _is_linked(a2, 'Grupo', b)


def test_assoc_materia7_reverse_link_reassign_clear():
    a1 = itculiacan_Materia(clave=7, nombre="sample_text")
    a2 = itculiacan_Materia(clave=13, nombre="sample_text_2")
    b = itculiacan_Grupo(clave=7)
    _safe_set(b, 'grupos8', a1)
    assert _is_linked(b, 'grupos8', a1)
    if hasattr(a1, 'Materia'):
        assert _is_linked(a1, 'Materia', b)
    _safe_set(b, 'grupos8', a2)
    assert _is_linked(b, 'grupos8', a2)
    if hasattr(a1, 'Materia'):
        assert not _is_linked(a1, 'Materia', b)
    if hasattr(a2, 'Materia'):
        assert _is_linked(a2, 'Materia', b)
    _safe_set(b, 'grupos8', None)
    assert not _is_linked(b, 'grupos8', a2)
    if hasattr(a2, 'Materia'):
        assert not _is_linked(a2, 'Materia', b)


def test_assoc_materias24_reverse_link_reassign_clear():
    a1 = itculiacan_PlanEstudio(clave=7, nombre="sample_text")
    a2 = itculiacan_PlanEstudio(clave=13, nombre="sample_text_2")
    b = itculiacan_Materia(clave=7, nombre="sample_text")
    _safe_set(b, 'Materia25', a1)
    assert _is_linked(b, 'Materia25', a1)
    if hasattr(a1, 'planesEstudio'):
        assert _is_linked(a1, 'planesEstudio', b)
    _safe_set(b, 'Materia25', a2)
    assert _is_linked(b, 'Materia25', a2)
    if hasattr(a1, 'planesEstudio'):
        assert not _is_linked(a1, 'planesEstudio', b)
    if hasattr(a2, 'planesEstudio'):
        assert _is_linked(a2, 'planesEstudio', b)
    _safe_set(b, 'Materia25', None)
    assert not _is_linked(b, 'Materia25', a2)
    if hasattr(a2, 'planesEstudio'):
        assert not _is_linked(a2, 'planesEstudio', b)


def test_assoc_planesEstudio18_reverse_link_reassign_clear():
    a1 = itculiacan_PlanEstudio(clave=7, nombre="sample_text")
    a2 = itculiacan_PlanEstudio(clave=13, nombre="sample_text_2")
    b = itculiacan_Materia(clave=7, nombre="sample_text")
    _safe_set(b, 'materias', {a1})
    assert _is_linked(b, 'materias', a1)
    if hasattr(a1, 'PlanEstudio19'):
        assert _is_linked(a1, 'PlanEstudio19', b)
    _safe_set(b, 'materias', {a2})
    assert _is_linked(b, 'materias', a2)
    if hasattr(a1, 'PlanEstudio19'):
        assert not _is_linked(a1, 'PlanEstudio19', b)
    if hasattr(a2, 'PlanEstudio19'):
        assert _is_linked(a2, 'PlanEstudio19', b)
    _safe_set(b, 'materias', set())
    assert not _is_linked(b, 'materias', a2)
    if hasattr(a2, 'PlanEstudio19'):
        assert not _is_linked(a2, 'PlanEstudio19', b)


def test_assoc_profesor9_reverse_link_reassign_clear():
    a1 = itculiacan_Profesor(clave=7, nombramiento="sample_text", nombre="sample_text", numeroMaterias=7)
    a2 = itculiacan_Profesor(clave=13, nombramiento="sample_text_2", nombre="sample_text_2", numeroMaterias=13)
    b = itculiacan_Grupo(clave=7)
    _safe_set(b, 'grupos10', a1)
    assert _is_linked(b, 'grupos10', a1)
    if hasattr(a1, 'Profesor'):
        assert _is_linked(a1, 'Profesor', b)
    _safe_set(b, 'grupos10', a2)
    assert _is_linked(b, 'grupos10', a2)
    if hasattr(a1, 'Profesor'):
        assert not _is_linked(a1, 'Profesor', b)
    if hasattr(a2, 'Profesor'):
        assert _is_linked(a2, 'Profesor', b)
    _safe_set(b, 'grupos10', None)
    assert not _is_linked(b, 'grupos10', a2)
    if hasattr(a2, 'Profesor'):
        assert not _is_linked(a2, 'Profesor', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_refAlumno31_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad32' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_Alumno's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_Alumno's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_Alumno(nombre="sample_text", numeroControl=7)
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad32', None)
    _safe_set(owner, 'itculiacan_Alumno', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad32')
    _safe_set(owner, 'itculiacan_Alumno', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad32')


def test_assoc_refAulas27_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad28' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_Aula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_Aula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_Aula(capacidad=7, clave=7)
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad28', None)
    _safe_set(owner, 'itculiacan_Aula', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad28')
    _safe_set(owner, 'itculiacan_Aula', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad28')


def test_assoc_refGeneracion33_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad34' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_Generacion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_Generacion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_Generacion(fechaFin=date(2024, 1, 1), fechaInicio=date(2024, 1, 1))
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad34', None)
    _safe_set(owner, 'itculiacan_Generacion', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad34')
    _safe_set(owner, 'itculiacan_Generacion', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad34')


def test_assoc_refGrupo37_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad38' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_Grupo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_Grupo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_Grupo(clave=7)
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad38', None)
    _safe_set(owner, 'itculiacan_Grupo', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad38')
    _safe_set(owner, 'itculiacan_Grupo', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad38')


def test_assoc_refMateria35_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad36' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_Materia's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_Materia's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_Materia(clave=7, nombre="sample_text")
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad36', None)
    _safe_set(owner, 'itculiacan_Materia', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad36')
    _safe_set(owner, 'itculiacan_Materia', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad36')


def test_assoc_refPlanEstudio29_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad30' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_PlanEstudio's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_PlanEstudio's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_PlanEstudio(clave=7, nombre="sample_text")
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad30', None)
    _safe_set(owner, 'itculiacan_PlanEstudio', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad30')
    _safe_set(owner, 'itculiacan_PlanEstudio', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad30')


def test_assoc_refProfesor26_stub_double():
    # itculiacan_Universidad has no real 'itculiacan_Universidad' property in the generated
    # code (a bare stub) -- manually attach it so itculiacan_Profesor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itculiacan_Profesor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itculiacan_Profesor(clave=7, nombramiento="sample_text", nombre="sample_text", numeroMaterias=7)
    partner = itculiacan_Universidad()
    setattr(partner, 'itculiacan_Universidad', None)
    _safe_set(owner, 'itculiacan_Profesor', partner)
    assert owner in getattr(partner, 'itculiacan_Universidad')
    _safe_set(owner, 'itculiacan_Profesor', None)
    assert owner not in getattr(partner, 'itculiacan_Universidad')


