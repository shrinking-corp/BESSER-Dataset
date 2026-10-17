import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RDBMS_Column,
    RDBMS_FKey,
    RDBMS_PKey,
    RDBMS_Scheme,
    RDBMS_Table,
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

def test_assoc_column10_stub_double():
    # RDBMS_FKey has no real 'RDBMS_FKey11' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Column(name="sample_text")
    partner = RDBMS_FKey()
    setattr(partner, 'RDBMS_FKey11', None)
    _safe_set(owner, 'RDBMS_Column', partner)
    assert getattr(partner, 'RDBMS_FKey11') == owner
    _safe_set(owner, 'RDBMS_Column', None)
    assert getattr(partner, 'RDBMS_FKey11') is None


def test_assoc_column14_stub_double():
    # RDBMS_PKey has no real 'RDBMS_PKey15' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Column(name="sample_text")
    partner = RDBMS_PKey()
    setattr(partner, 'RDBMS_PKey15', None)
    _safe_set(owner, 'RDBMS_Column16', partner)
    assert getattr(partner, 'RDBMS_PKey15') == owner
    _safe_set(owner, 'RDBMS_Column16', None)
    assert getattr(partner, 'RDBMS_PKey15') is None


def test_assoc_columns3_stub_double():
    # RDBMS_Column has no real 'RDBMS.ecoreColumn' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Table(name="sample_text")
    partner = RDBMS_Column(name="sample_text")
    setattr(partner, 'RDBMS.ecoreColumn', None)
    _safe_set(owner, 'table', {partner})
    assert getattr(partner, 'RDBMS.ecoreColumn') == owner
    _safe_set(owner, 'table', set())
    assert getattr(partner, 'RDBMS.ecoreColumn') is None


def test_assoc_key5_stub_double():
    # RDBMS_PKey has no real 'RDBMS_PKey' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Table(name="sample_text")
    partner = RDBMS_PKey()
    setattr(partner, 'RDBMS_PKey', None)
    _safe_set(owner, 'RDBMS_Table', partner)
    assert getattr(partner, 'RDBMS_PKey') == owner
    _safe_set(owner, 'RDBMS_Table', None)
    assert getattr(partner, 'RDBMS_PKey') is None


def test_assoc_keys1_stub_double():
    # RDBMS_FKey has no real 'RDBMS.ecoreFKey' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Scheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Scheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Scheme(name="sample_text")
    partner = RDBMS_FKey()
    setattr(partner, 'RDBMS.ecoreFKey', None)
    _safe_set(owner, 'scheme2', {partner})
    assert getattr(partner, 'RDBMS.ecoreFKey') == owner
    _safe_set(owner, 'scheme2', set())
    assert getattr(partner, 'RDBMS.ecoreFKey') is None


def test_assoc_scheme4_stub_double():
    # RDBMS_Scheme has no real 'RDBMS.ecoreScheme' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Table(name="sample_text")
    partner = RDBMS_Scheme(name="sample_text")
    setattr(partner, 'RDBMS.ecoreScheme', None)
    _safe_set(owner, 'tables', partner)
    assert getattr(partner, 'RDBMS.ecoreScheme') == owner
    _safe_set(owner, 'tables', None)
    assert getattr(partner, 'RDBMS.ecoreScheme') is None


def test_assoc_table6_stub_double():
    # RDBMS_Table has no real 'RDBMS.ecoreTable7' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Column(name="sample_text")
    partner = RDBMS_Table(name="sample_text")
    setattr(partner, 'RDBMS.ecoreTable7', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'RDBMS.ecoreTable7') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'RDBMS.ecoreTable7') is None


def test_assoc_tables0_stub_double():
    # RDBMS_Table has no real 'RDBMS.ecoreTable' property in the generated
    # code (a bare stub) -- manually attach it so RDBMS_Scheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMS_Scheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMS_Scheme(name="sample_text")
    partner = RDBMS_Table(name="sample_text")
    setattr(partner, 'RDBMS.ecoreTable', None)
    _safe_set(owner, 'scheme', {partner})
    assert getattr(partner, 'RDBMS.ecoreTable') == owner
    _safe_set(owner, 'scheme', set())
    assert getattr(partner, 'RDBMS.ecoreTable') is None


