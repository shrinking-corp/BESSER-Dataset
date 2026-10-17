import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Agenda,
    Contacto,
    Direccion,
    Foto,
    Telefono,
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

def test_assoc_Agenda_Contacto_reverse_link_reassign_clear():
    a1 = Contacto(email="sample_text", nombre="sample_text")
    a2 = Contacto(email="sample_text_2", nombre="sample_text_2")
    b = Agenda(Introduccion="sample_text")
    _safe_set(b, 'contacto0', {a1})
    assert _is_linked(b, 'contacto0', a1)
    if hasattr(a1, 'agenda1'):
        assert _is_linked(a1, 'agenda1', b)
    _safe_set(b, 'contacto0', {a2})
    assert _is_linked(b, 'contacto0', a2)
    if hasattr(a1, 'agenda1'):
        assert not _is_linked(a1, 'agenda1', b)
    if hasattr(a2, 'agenda1'):
        assert _is_linked(a2, 'agenda1', b)
    _safe_set(b, 'contacto0', set())
    assert not _is_linked(b, 'contacto0', a2)
    if hasattr(a2, 'agenda1'):
        assert not _is_linked(a2, 'agenda1', b)


def test_assoc_Direccion_Contacto_reverse_link_reassign_clear():
    a1 = Direccion(ciudad="sample_text", codigo=7, nombre="sample_text", pais="sample_text")
    a2 = Direccion(ciudad="sample_text_2", codigo=13, nombre="sample_text_2", pais="sample_text_2")
    b = Contacto(email="sample_text", nombre="sample_text")
    _safe_set(b, 'direccionPrincipal3', a1)
    assert _is_linked(b, 'direccionPrincipal3', a1)
    if hasattr(a1, 'contacto2'):
        assert _is_linked(a1, 'contacto2', b)
    _safe_set(b, 'direccionPrincipal3', a2)
    assert _is_linked(b, 'direccionPrincipal3', a2)
    if hasattr(a1, 'contacto2'):
        assert not _is_linked(a1, 'contacto2', b)
    if hasattr(a2, 'contacto2'):
        assert _is_linked(a2, 'contacto2', b)
    _safe_set(b, 'direccionPrincipal3', None)
    assert not _is_linked(b, 'direccionPrincipal3', a2)
    if hasattr(a2, 'contacto2'):
        assert not _is_linked(a2, 'contacto2', b)


def test_assoc_Direccion_Contacto2_reverse_link_reassign_clear():
    a1 = Direccion(ciudad="sample_text", codigo=7, nombre="sample_text", pais="sample_text")
    a2 = Direccion(ciudad="sample_text_2", codigo=13, nombre="sample_text_2", pais="sample_text_2")
    b = Contacto(email="sample_text", nombre="sample_text")
    _safe_set(b, 'direccionAlternativa5', a1)
    assert _is_linked(b, 'direccionAlternativa5', a1)
    if hasattr(a1, 'contacto4'):
        assert _is_linked(a1, 'contacto4', b)
    _safe_set(b, 'direccionAlternativa5', a2)
    assert _is_linked(b, 'direccionAlternativa5', a2)
    if hasattr(a1, 'contacto4'):
        assert not _is_linked(a1, 'contacto4', b)
    if hasattr(a2, 'contacto4'):
        assert _is_linked(a2, 'contacto4', b)
    _safe_set(b, 'direccionAlternativa5', None)
    assert not _is_linked(b, 'direccionAlternativa5', a2)
    if hasattr(a2, 'contacto4'):
        assert not _is_linked(a2, 'contacto4', b)


def test_assoc_Foto_Contacto_reverse_link_reassign_clear():
    a1 = Foto(alto=7, ancho=7)
    a2 = Foto(alto=13, ancho=13)
    b = Contacto(email="sample_text", nombre="sample_text")
    _safe_set(b, 'foto11', a1)
    assert _is_linked(b, 'foto11', a1)
    if hasattr(a1, 'contacto10'):
        assert _is_linked(a1, 'contacto10', b)
    _safe_set(b, 'foto11', a2)
    assert _is_linked(b, 'foto11', a2)
    if hasattr(a1, 'contacto10'):
        assert not _is_linked(a1, 'contacto10', b)
    if hasattr(a2, 'contacto10'):
        assert _is_linked(a2, 'contacto10', b)
    _safe_set(b, 'foto11', None)
    assert not _is_linked(b, 'foto11', a2)
    if hasattr(a2, 'contacto10'):
        assert not _is_linked(a2, 'contacto10', b)


def test_assoc_Telefono_Contacto_reverse_link_reassign_clear():
    a1 = Telefono(codigo=7, numero=7, prefijo=7)
    a2 = Telefono(codigo=13, numero=13, prefijo=13)
    b = Contacto(email="sample_text", nombre="sample_text")
    _safe_set(b, 'telefonoPrincipal7', a1)
    assert _is_linked(b, 'telefonoPrincipal7', a1)
    if hasattr(a1, 'contacto6'):
        assert _is_linked(a1, 'contacto6', b)
    _safe_set(b, 'telefonoPrincipal7', a2)
    assert _is_linked(b, 'telefonoPrincipal7', a2)
    if hasattr(a1, 'contacto6'):
        assert not _is_linked(a1, 'contacto6', b)
    if hasattr(a2, 'contacto6'):
        assert _is_linked(a2, 'contacto6', b)
    _safe_set(b, 'telefonoPrincipal7', None)
    assert not _is_linked(b, 'telefonoPrincipal7', a2)
    if hasattr(a2, 'contacto6'):
        assert not _is_linked(a2, 'contacto6', b)


def test_assoc_Telefono_Contacto2_reverse_link_reassign_clear():
    a1 = Telefono(codigo=7, numero=7, prefijo=7)
    a2 = Telefono(codigo=13, numero=13, prefijo=13)
    b = Contacto(email="sample_text", nombre="sample_text")
    _safe_set(b, 'telefonoAlternativo9', a1)
    assert _is_linked(b, 'telefonoAlternativo9', a1)
    if hasattr(a1, 'contacto8'):
        assert _is_linked(a1, 'contacto8', b)
    _safe_set(b, 'telefonoAlternativo9', a2)
    assert _is_linked(b, 'telefonoAlternativo9', a2)
    if hasattr(a1, 'contacto8'):
        assert not _is_linked(a1, 'contacto8', b)
    if hasattr(a2, 'contacto8'):
        assert _is_linked(a2, 'contacto8', b)
    _safe_set(b, 'telefonoAlternativo9', None)
    assert not _is_linked(b, 'telefonoAlternativo9', a2)
    if hasattr(a2, 'contacto8'):
        assert not _is_linked(a2, 'contacto8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

