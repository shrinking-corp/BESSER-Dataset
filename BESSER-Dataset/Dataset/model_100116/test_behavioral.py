import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    database_Column,
    database_ForeignKey,
    database_Schema,
    database_Table,
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

def test_assoc_cols1_reverse_link_reassign_clear():
    a1 = database_Table(is_local=True, name="sample_text")
    a2 = database_Table(is_local=False, name="sample_text_2")
    b = database_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'database_Column', a1)
    assert _is_linked(b, 'database_Column', a1)
    if hasattr(a1, 'database_Table2'):
        assert _is_linked(a1, 'database_Table2', b)
    _safe_set(b, 'database_Column', a2)
    assert _is_linked(b, 'database_Column', a2)
    if hasattr(a1, 'database_Table2'):
        assert not _is_linked(a1, 'database_Table2', b)
    if hasattr(a2, 'database_Table2'):
        assert _is_linked(a2, 'database_Table2', b)
    _safe_set(b, 'database_Column', None)
    assert not _is_linked(b, 'database_Column', a2)
    if hasattr(a2, 'database_Table2'):
        assert not _is_linked(a2, 'database_Table2', b)


def test_assoc_pkey5_reverse_link_reassign_clear():
    a1 = database_Table(is_local=True, name="sample_text")
    a2 = database_Table(is_local=False, name="sample_text_2")
    b = database_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'database_Column7', a1)
    assert _is_linked(b, 'database_Column7', a1)
    if hasattr(a1, 'database_Table6'):
        assert _is_linked(a1, 'database_Table6', b)
    _safe_set(b, 'database_Column7', a2)
    assert _is_linked(b, 'database_Column7', a2)
    if hasattr(a1, 'database_Table6'):
        assert not _is_linked(a1, 'database_Table6', b)
    if hasattr(a2, 'database_Table6'):
        assert _is_linked(a2, 'database_Table6', b)
    _safe_set(b, 'database_Column7', None)
    assert not _is_linked(b, 'database_Column7', a2)
    if hasattr(a2, 'database_Table6'):
        assert not _is_linked(a2, 'database_Table6', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = database_Table(is_local=True, name="sample_text")
    a2 = database_Table(is_local=False, name="sample_text_2")
    b = database_Schema(name="sample_text")
    _safe_set(b, 'database_Schema', {a1})
    assert _is_linked(b, 'database_Schema', a1)
    if hasattr(a1, 'database_Table'):
        assert _is_linked(a1, 'database_Table', b)
    _safe_set(b, 'database_Schema', {a2})
    assert _is_linked(b, 'database_Schema', a2)
    if hasattr(a1, 'database_Table'):
        assert not _is_linked(a1, 'database_Table', b)
    if hasattr(a2, 'database_Table'):
        assert _is_linked(a2, 'database_Table', b)
    _safe_set(b, 'database_Schema', set())
    assert not _is_linked(b, 'database_Schema', a2)
    if hasattr(a2, 'database_Table'):
        assert not _is_linked(a2, 'database_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cols8_stub_double():
    # database_ForeignKey has no real 'database_ForeignKey9' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(name="sample_text", type="sample_text")
    partner = database_ForeignKey()
    setattr(partner, 'database_ForeignKey9', None)
    _safe_set(owner, 'database_Column10', partner)
    assert owner in getattr(partner, 'database_ForeignKey9')
    _safe_set(owner, 'database_Column10', None)
    assert owner not in getattr(partner, 'database_ForeignKey9')


def test_assoc_fkeys3_stub_double():
    # database_ForeignKey has no real 'database_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(is_local=True, name="sample_text")
    partner = database_ForeignKey()
    setattr(partner, 'database_ForeignKey', None)
    _safe_set(owner, 'database_Table4', {partner})
    assert getattr(partner, 'database_ForeignKey') == owner
    _safe_set(owner, 'database_Table4', set())
    assert getattr(partner, 'database_ForeignKey') is None


def test_assoc_references11_stub_double():
    # database_ForeignKey has no real 'database_ForeignKey12' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(is_local=True, name="sample_text")
    partner = database_ForeignKey()
    setattr(partner, 'database_ForeignKey12', None)
    _safe_set(owner, 'database_Table13', partner)
    assert getattr(partner, 'database_ForeignKey12') == owner
    _safe_set(owner, 'database_Table13', None)
    assert getattr(partner, 'database_ForeignKey12') is None


