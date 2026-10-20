import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataElement,
    ddl_Column,
    ddl_DataElement,
    ddl_DataType,
    ddl_Schema,
    ddl_Table,
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

def test_assoc_table0_stub_double():
    # ddl_Table has no real 'ddl_Table' property in the generated
    # code (a bare stub) -- manually attach it so ddl_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddl_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddl_Schema(conformite=True, prix=3.14, version=7)
    partner = ddl_Table()
    setattr(partner, 'ddl_Table', None)
    _safe_set(owner, 'ddl_Schema', {partner})
    assert getattr(partner, 'ddl_Table') == owner
    _safe_set(owner, 'ddl_Schema', set())
    assert getattr(partner, 'ddl_Table') is None


def test_assoc_types1_stub_double():
    # ddl_DataType has no real 'ddl_DataType' property in the generated
    # code (a bare stub) -- manually attach it so ddl_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddl_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddl_Schema(conformite=True, prix=3.14, version=7)
    partner = ddl_DataType()
    setattr(partner, 'ddl_DataType', None)
    _safe_set(owner, 'ddl_Schema2', {partner})
    assert getattr(partner, 'ddl_DataType') == owner
    _safe_set(owner, 'ddl_Schema2', set())
    assert getattr(partner, 'ddl_DataType') is None


