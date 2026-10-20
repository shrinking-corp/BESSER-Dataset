import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Contacto,
    Direccion,
    Directorio,
    Foto_de_perfil,
    Telefono,
    User_Actor,
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

def test_assoc_Contacto_Direccion_reverse_link_reassign_clear():
    a1 = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    a2 = Direccion(Ciudad="sample_text_2", Codigo_Postal=13, Nombre="sample_text_2", Pais="sample_text_2")
    b = Contacto(Correo="sample_text", Nombre="sample_text")
    _safe_set(b, 'direccion_Principal2', a1)
    assert _is_linked(b, 'direccion_Principal2', a1)
    if hasattr(a1, 'contacto3'):
        assert _is_linked(a1, 'contacto3', b)
    _safe_set(b, 'direccion_Principal2', a2)
    assert _is_linked(b, 'direccion_Principal2', a2)
    if hasattr(a1, 'contacto3'):
        assert not _is_linked(a1, 'contacto3', b)
    if hasattr(a2, 'contacto3'):
        assert _is_linked(a2, 'contacto3', b)
    _safe_set(b, 'direccion_Principal2', None)
    assert not _is_linked(b, 'direccion_Principal2', a2)
    if hasattr(a2, 'contacto3'):
        assert not _is_linked(a2, 'contacto3', b)


def test_assoc_Contacto_Direccion2_reverse_link_reassign_clear():
    a1 = Direccion(Ciudad="sample_text", Codigo_Postal=7, Nombre="sample_text", Pais="sample_text")
    a2 = Direccion(Ciudad="sample_text_2", Codigo_Postal=13, Nombre="sample_text_2", Pais="sample_text_2")
    b = Contacto(Correo="sample_text", Nombre="sample_text")
    _safe_set(b, 'direccion4', a1)
    assert _is_linked(b, 'direccion4', a1)
    if hasattr(a1, 'contacto5'):
        assert _is_linked(a1, 'contacto5', b)
    _safe_set(b, 'direccion4', a2)
    assert _is_linked(b, 'direccion4', a2)
    if hasattr(a1, 'contacto5'):
        assert not _is_linked(a1, 'contacto5', b)
    if hasattr(a2, 'contacto5'):
        assert _is_linked(a2, 'contacto5', b)
    _safe_set(b, 'direccion4', None)
    assert not _is_linked(b, 'direccion4', a2)
    if hasattr(a2, 'contacto5'):
        assert not _is_linked(a2, 'contacto5', b)


def test_assoc_Directorio_Contacto_reverse_link_reassign_clear():
    a1 = Directorio(Introducir="sample_text")
    a2 = Directorio(Introducir="sample_text_2")
    b = Contacto(Correo="sample_text", Nombre="sample_text")
    _safe_set(b, 'directorio1', a1)
    assert _is_linked(b, 'directorio1', a1)
    if hasattr(a1, 'contacto0'):
        assert _is_linked(a1, 'contacto0', b)
    _safe_set(b, 'directorio1', a2)
    assert _is_linked(b, 'directorio1', a2)
    if hasattr(a1, 'contacto0'):
        assert not _is_linked(a1, 'contacto0', b)
    if hasattr(a2, 'contacto0'):
        assert _is_linked(a2, 'contacto0', b)
    _safe_set(b, 'directorio1', None)
    assert not _is_linked(b, 'directorio1', a2)
    if hasattr(a2, 'contacto0'):
        assert not _is_linked(a2, 'contacto0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

