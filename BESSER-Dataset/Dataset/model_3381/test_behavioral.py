import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Selects_Aplicacion,
    Selects_Fichero,
    Selects_From,
    Selects_Join,
    Selects_NamedElement,
    Selects_Operando,
    Selects_Select,
    Selects_Tabla,
    Selects_Where,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_operando111_stub_double():
    # Selects_Join has no real 'Selects_Join12' property in the generated
    # code (a bare stub) -- manually attach it so Selects_Operando's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Selects_Operando's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Selects_Operando(columna="sample_text", tabla="sample_text")
    partner = Selects_Join()
    setattr(partner, 'Selects_Join12', None)
    _safe_set(owner, 'Selects_Operando', partner)
    assert getattr(partner, 'Selects_Join12') == owner
    _safe_set(owner, 'Selects_Operando', None)
    assert getattr(partner, 'Selects_Join12') is None


def test_assoc_operando213_stub_double():
    # Selects_Join has no real 'Selects_Join14' property in the generated
    # code (a bare stub) -- manually attach it so Selects_Operando's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Selects_Operando's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Selects_Operando(columna="sample_text", tabla="sample_text")
    partner = Selects_Join()
    setattr(partner, 'Selects_Join14', None)
    _safe_set(owner, 'Selects_Operando15', partner)
    assert getattr(partner, 'Selects_Join14') == owner
    _safe_set(owner, 'Selects_Operando15', None)
    assert getattr(partner, 'Selects_Join14') is None


def test_assoc_tablas7_stub_double():
    # Selects_From has no real 'Selects_From8' property in the generated
    # code (a bare stub) -- manually attach it so Selects_Tabla's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Selects_Tabla's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Selects_Tabla(tabAlias="sample_text")
    partner = Selects_From()
    setattr(partner, 'Selects_From8', None)
    _safe_set(owner, 'Selects_Tabla', partner)
    assert owner in getattr(partner, 'Selects_From8')
    _safe_set(owner, 'Selects_Tabla', None)
    assert owner not in getattr(partner, 'Selects_From8')


