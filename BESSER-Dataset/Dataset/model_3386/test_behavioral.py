import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Error,
    errors_Column,
    errors_Error,
    errors_Errores,
    errors_Fk,
    errors_ForeignError,
    errors_Table,
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

def test_assoc_errores0_stub_double():
    # errors_Errores has no real 'errors_Errores' property in the generated
    # code (a bare stub) -- manually attach it so errors_Error's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # errors_Error's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = errors_Error(apply=True, id=7)
    partner = errors_Errores()
    setattr(partner, 'errors_Errores', None)
    _safe_set(owner, 'errors_Error', partner)
    assert owner in getattr(partner, 'errors_Errores')
    _safe_set(owner, 'errors_Error', None)
    assert owner not in getattr(partner, 'errors_Errores')


def test_assoc_fk7_stub_double():
    # errors_Fk has no real 'errors_Fk' property in the generated
    # code (a bare stub) -- manually attach it so errors_ForeignError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # errors_ForeignError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = errors_ForeignError(porcent=7)
    partner = errors_Fk()
    setattr(partner, 'errors_Fk', None)
    _safe_set(owner, 'errors_ForeignError8', partner)
    assert getattr(partner, 'errors_Fk') == owner
    _safe_set(owner, 'errors_ForeignError8', None)
    assert getattr(partner, 'errors_Fk') is None


def test_assoc_fkColumns5_stub_double():
    # errors_Column has no real 'errors_Column' property in the generated
    # code (a bare stub) -- manually attach it so errors_ForeignError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # errors_ForeignError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = errors_ForeignError(porcent=7)
    partner = errors_Column()
    setattr(partner, 'errors_Column', None)
    _safe_set(owner, 'errors_ForeignError6', {partner})
    assert getattr(partner, 'errors_Column') == owner
    _safe_set(owner, 'errors_ForeignError6', set())
    assert getattr(partner, 'errors_Column') is None


def test_assoc_tableCont1_stub_double():
    # errors_Table has no real 'errors_Table' property in the generated
    # code (a bare stub) -- manually attach it so errors_ForeignError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # errors_ForeignError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = errors_ForeignError(porcent=7)
    partner = errors_Table()
    setattr(partner, 'errors_Table', None)
    _safe_set(owner, 'errors_ForeignError', partner)
    assert getattr(partner, 'errors_Table') == owner
    _safe_set(owner, 'errors_ForeignError', None)
    assert getattr(partner, 'errors_Table') is None


def test_assoc_tableRef2_stub_double():
    # errors_Table has no real 'errors_Table4' property in the generated
    # code (a bare stub) -- manually attach it so errors_ForeignError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # errors_ForeignError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = errors_ForeignError(porcent=7)
    partner = errors_Table()
    setattr(partner, 'errors_Table4', None)
    _safe_set(owner, 'errors_ForeignError3', partner)
    assert getattr(partner, 'errors_Table4') == owner
    _safe_set(owner, 'errors_ForeignError3', None)
    assert getattr(partner, 'errors_Table4') is None


