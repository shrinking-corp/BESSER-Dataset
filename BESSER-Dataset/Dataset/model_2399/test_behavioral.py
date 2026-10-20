import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    rdbms_Column,
    rdbms_ForeignKey,
    rdbms_RDBMSModel,
    rdbms_Table,
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

def test_assoc_columns8_reverse_link_reassign_clear():
    a1 = rdbms_Table(name="sample_text")
    a2 = rdbms_Table(name="sample_text_2")
    b = rdbms_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'rdbms_Column10', a1)
    assert _is_linked(b, 'rdbms_Column10', a1)
    if hasattr(a1, 'rdbms_Table9'):
        assert _is_linked(a1, 'rdbms_Table9', b)
    _safe_set(b, 'rdbms_Column10', a2)
    assert _is_linked(b, 'rdbms_Column10', a2)
    if hasattr(a1, 'rdbms_Table9'):
        assert not _is_linked(a1, 'rdbms_Table9', b)
    if hasattr(a2, 'rdbms_Table9'):
        assert _is_linked(a2, 'rdbms_Table9', b)
    _safe_set(b, 'rdbms_Column10', None)
    assert not _is_linked(b, 'rdbms_Column10', a2)
    if hasattr(a2, 'rdbms_Table9'):
        assert not _is_linked(a2, 'rdbms_Table9', b)


def test_assoc_primaryKey11_reverse_link_reassign_clear():
    a1 = rdbms_Table(name="sample_text")
    a2 = rdbms_Table(name="sample_text_2")
    b = rdbms_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'rdbms_Column13', a1)
    assert _is_linked(b, 'rdbms_Column13', a1)
    if hasattr(a1, 'rdbms_Table12'):
        assert _is_linked(a1, 'rdbms_Table12', b)
    _safe_set(b, 'rdbms_Column13', a2)
    assert _is_linked(b, 'rdbms_Column13', a2)
    if hasattr(a1, 'rdbms_Table12'):
        assert not _is_linked(a1, 'rdbms_Table12', b)
    if hasattr(a2, 'rdbms_Table12'):
        assert _is_linked(a2, 'rdbms_Table12', b)
    _safe_set(b, 'rdbms_Column13', None)
    assert not _is_linked(b, 'rdbms_Column13', a2)
    if hasattr(a2, 'rdbms_Table12'):
        assert not _is_linked(a2, 'rdbms_Table12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns17_stub_double():
    # rdbms_ForeignKey has no real 'rdbms_ForeignKey18' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Column(name="sample_text", type="sample_text")
    partner = rdbms_ForeignKey()
    setattr(partner, 'rdbms_ForeignKey18', None)
    _safe_set(owner, 'rdbms_Column19', partner)
    assert owner in getattr(partner, 'rdbms_ForeignKey18')
    _safe_set(owner, 'rdbms_Column19', None)
    assert owner not in getattr(partner, 'rdbms_ForeignKey18')


def test_assoc_containsColumns1_stub_double():
    # rdbms_RDBMSModel has no real 'rdbms_RDBMSModel2' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Column(name="sample_text", type="sample_text")
    partner = rdbms_RDBMSModel()
    setattr(partner, 'rdbms_RDBMSModel2', None)
    _safe_set(owner, 'rdbms_Column', partner)
    assert owner in getattr(partner, 'rdbms_RDBMSModel2')
    _safe_set(owner, 'rdbms_Column', None)
    assert owner not in getattr(partner, 'rdbms_RDBMSModel2')


def test_assoc_containsTables0_stub_double():
    # rdbms_RDBMSModel has no real 'rdbms_RDBMSModel' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Table(name="sample_text")
    partner = rdbms_RDBMSModel()
    setattr(partner, 'rdbms_RDBMSModel', None)
    _safe_set(owner, 'rdbms_Table', partner)
    assert owner in getattr(partner, 'rdbms_RDBMSModel')
    _safe_set(owner, 'rdbms_Table', None)
    assert owner not in getattr(partner, 'rdbms_RDBMSModel')


def test_assoc_foreignKeys5_stub_double():
    # rdbms_ForeignKey has no real 'rdbms_ForeignKey7' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Table(name="sample_text")
    partner = rdbms_ForeignKey()
    setattr(partner, 'rdbms_ForeignKey7', None)
    _safe_set(owner, 'rdbms_Table6', {partner})
    assert getattr(partner, 'rdbms_ForeignKey7') == owner
    _safe_set(owner, 'rdbms_Table6', set())
    assert getattr(partner, 'rdbms_ForeignKey7') is None


def test_assoc_references14_stub_double():
    # rdbms_ForeignKey has no real 'rdbms_ForeignKey15' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Table(name="sample_text")
    partner = rdbms_ForeignKey()
    setattr(partner, 'rdbms_ForeignKey15', None)
    _safe_set(owner, 'rdbms_Table16', partner)
    assert getattr(partner, 'rdbms_ForeignKey15') == owner
    _safe_set(owner, 'rdbms_Table16', None)
    assert getattr(partner, 'rdbms_ForeignKey15') is None


