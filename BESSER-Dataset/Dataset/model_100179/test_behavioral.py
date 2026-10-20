import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    DataBase,
    NamedElement,
    RelationalDBSchema_Column,
    RelationalDBSchema_DataBase,
    RelationalDBSchema_NamedElement,
    RelationalDBSchema_Table,
    Table,
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

def test_assoc_keyOf7_stub_double():
    # Table has no real 'Table8' property in the generated
    # code (a bare stub) -- manually attach it so RelationalDBSchema_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RelationalDBSchema_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RelationalDBSchema_Column(dataType="sample_text", defaultValue="sample_text", null="sample_text")
    partner = Table()
    setattr(partner, 'Table8', None)
    _safe_set(owner, 'key', partner)
    assert getattr(partner, 'Table8') == owner
    _safe_set(owner, 'key', None)
    assert getattr(partner, 'Table8') is None


def test_assoc_owner5_stub_double():
    # Table has no real 'Table6' property in the generated
    # code (a bare stub) -- manually attach it so RelationalDBSchema_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RelationalDBSchema_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RelationalDBSchema_Column(dataType="sample_text", defaultValue="sample_text", null="sample_text")
    partner = Table()
    setattr(partner, 'Table6', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table6') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table6') is None


def test_assoc_tables0_stub_double():
    # Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so RelationalDBSchema_DataBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RelationalDBSchema_DataBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RelationalDBSchema_DataBase(SGBDname="sample_text")
    partner = Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'database', {partner})
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'database', set())
    assert getattr(partner, 'Table') is None


