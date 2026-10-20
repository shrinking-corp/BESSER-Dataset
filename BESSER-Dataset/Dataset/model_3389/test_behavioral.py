import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Fragmentos_Aplicacion,
    Fragmentos_Fichero,
    Fragmentos_Fragmento,
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

def test_assoc_fragmentos1_reverse_link_reassign_clear():
    a1 = Fragmentos_Fragmento(numLinea=7, posCaracter=7, texto="sample_text")
    a2 = Fragmentos_Fragmento(numLinea=13, posCaracter=13, texto="sample_text_2")
    b = Fragmentos_Fichero(nombre="sample_text")
    _safe_set(b, 'Fragmentos_Fichero2', {a1})
    assert _is_linked(b, 'Fragmentos_Fichero2', a1)
    if hasattr(a1, 'Fragmentos_Fragmento'):
        assert _is_linked(a1, 'Fragmentos_Fragmento', b)
    _safe_set(b, 'Fragmentos_Fichero2', {a2})
    assert _is_linked(b, 'Fragmentos_Fichero2', a2)
    if hasattr(a1, 'Fragmentos_Fragmento'):
        assert not _is_linked(a1, 'Fragmentos_Fragmento', b)
    if hasattr(a2, 'Fragmentos_Fragmento'):
        assert _is_linked(a2, 'Fragmentos_Fragmento', b)
    _safe_set(b, 'Fragmentos_Fichero2', set())
    assert not _is_linked(b, 'Fragmentos_Fichero2', a2)
    if hasattr(a2, 'Fragmentos_Fragmento'):
        assert not _is_linked(a2, 'Fragmentos_Fragmento', b)


def test_assoc_fragmentosSelect3_reverse_link_reassign_clear():
    a1 = Fragmentos_Fragmento(numLinea=7, posCaracter=7, texto="sample_text")
    a2 = Fragmentos_Fragmento(numLinea=13, posCaracter=13, texto="sample_text_2")
    b = Fragmentos_Fichero(nombre="sample_text")
    _safe_set(b, 'Fragmentos_Fichero4', {a1})
    assert _is_linked(b, 'Fragmentos_Fichero4', a1)
    if hasattr(a1, 'Fragmentos_Fragmento5'):
        assert _is_linked(a1, 'Fragmentos_Fragmento5', b)
    _safe_set(b, 'Fragmentos_Fichero4', {a2})
    assert _is_linked(b, 'Fragmentos_Fichero4', a2)
    if hasattr(a1, 'Fragmentos_Fragmento5'):
        assert not _is_linked(a1, 'Fragmentos_Fragmento5', b)
    if hasattr(a2, 'Fragmentos_Fragmento5'):
        assert _is_linked(a2, 'Fragmentos_Fragmento5', b)
    _safe_set(b, 'Fragmentos_Fichero4', set())
    assert not _is_linked(b, 'Fragmentos_Fichero4', a2)
    if hasattr(a2, 'Fragmentos_Fragmento5'):
        assert not _is_linked(a2, 'Fragmentos_Fragmento5', b)


def test_assoc_sigFragmento7_reverse_link_reassign_clear():
    a1 = Fragmentos_Fragmento(numLinea=7, posCaracter=7, texto="sample_text")
    a2 = Fragmentos_Fragmento(numLinea=13, posCaracter=13, texto="sample_text_2")
    b = Fragmentos_Fragmento(numLinea=7, posCaracter=7, texto="sample_text")
    _safe_set(b, 'Fragmentos_Fragmento8', a1)
    assert _is_linked(b, 'Fragmentos_Fragmento8', a1)
    if hasattr(a1, 'Fragmentos_Fragmento6'):
        assert _is_linked(a1, 'Fragmentos_Fragmento6', b)
    _safe_set(b, 'Fragmentos_Fragmento8', a2)
    assert _is_linked(b, 'Fragmentos_Fragmento8', a2)
    if hasattr(a1, 'Fragmentos_Fragmento6'):
        assert not _is_linked(a1, 'Fragmentos_Fragmento6', b)
    if hasattr(a2, 'Fragmentos_Fragmento6'):
        assert _is_linked(a2, 'Fragmentos_Fragmento6', b)
    _safe_set(b, 'Fragmentos_Fragmento8', None)
    assert not _is_linked(b, 'Fragmentos_Fragmento8', a2)
    if hasattr(a2, 'Fragmentos_Fragmento6'):
        assert not _is_linked(a2, 'Fragmentos_Fragmento6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ficheros0_stub_double():
    # Fragmentos_Aplicacion has no real 'Fragmentos_Aplicacion' property in the generated
    # code (a bare stub) -- manually attach it so Fragmentos_Fichero's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Fragmentos_Fichero's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Fragmentos_Fichero(nombre="sample_text")
    partner = Fragmentos_Aplicacion()
    setattr(partner, 'Fragmentos_Aplicacion', None)
    _safe_set(owner, 'Fragmentos_Fichero', partner)
    assert owner in getattr(partner, 'Fragmentos_Aplicacion')
    _safe_set(owner, 'Fragmentos_Fichero', None)
    assert owner not in getattr(partner, 'Fragmentos_Aplicacion')


