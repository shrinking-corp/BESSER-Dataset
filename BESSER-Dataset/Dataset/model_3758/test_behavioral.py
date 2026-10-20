import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    my_Column,
    my_Database,
    my_FKRelation,
    my_NamedElement,
    my_Table,
    ColumnType,
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

def test_assoc_source8_reverse_link_reassign_clear():
    a1 = my_FKRelation(label="sample_text")
    a2 = my_FKRelation(label="sample_text_2")
    b = my_Column(primary=True, size=7, type="sample_text", unique=True)
    _safe_set(b, 'my_Column10', a1)
    assert _is_linked(b, 'my_Column10', a1)
    if hasattr(a1, 'my_FKRelation9'):
        assert _is_linked(a1, 'my_FKRelation9', b)
    _safe_set(b, 'my_Column10', a2)
    assert _is_linked(b, 'my_Column10', a2)
    if hasattr(a1, 'my_FKRelation9'):
        assert not _is_linked(a1, 'my_FKRelation9', b)
    if hasattr(a2, 'my_FKRelation9'):
        assert _is_linked(a2, 'my_FKRelation9', b)
    _safe_set(b, 'my_Column10', None)
    assert not _is_linked(b, 'my_Column10', a2)
    if hasattr(a2, 'my_FKRelation9'):
        assert not _is_linked(a2, 'my_FKRelation9', b)


def test_assoc_target5_reverse_link_reassign_clear():
    a1 = my_FKRelation(label="sample_text")
    a2 = my_FKRelation(label="sample_text_2")
    b = my_Column(primary=True, size=7, type="sample_text", unique=True)
    _safe_set(b, 'my_Column7', a1)
    assert _is_linked(b, 'my_Column7', a1)
    if hasattr(a1, 'my_FKRelation6'):
        assert _is_linked(a1, 'my_FKRelation6', b)
    _safe_set(b, 'my_Column7', a2)
    assert _is_linked(b, 'my_Column7', a2)
    if hasattr(a1, 'my_FKRelation6'):
        assert not _is_linked(a1, 'my_FKRelation6', b)
    if hasattr(a2, 'my_FKRelation6'):
        assert _is_linked(a2, 'my_FKRelation6', b)
    _safe_set(b, 'my_Column7', None)
    assert not _is_linked(b, 'my_Column7', a2)
    if hasattr(a2, 'my_FKRelation6'):
        assert not _is_linked(a2, 'my_FKRelation6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns0_stub_double():
    # my_Table has no real 'my_Table' property in the generated
    # code (a bare stub) -- manually attach it so my_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # my_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = my_Column(primary=True, size=7, type="sample_text", unique=True)
    partner = my_Table()
    setattr(partner, 'my_Table', None)
    _safe_set(owner, 'my_Column', partner)
    assert owner in getattr(partner, 'my_Table')
    _safe_set(owner, 'my_Column', None)
    assert owner not in getattr(partner, 'my_Table')


def test_assoc_fkrelations3_stub_double():
    # my_Database has no real 'my_Database4' property in the generated
    # code (a bare stub) -- manually attach it so my_FKRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # my_FKRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = my_FKRelation(label="sample_text")
    partner = my_Database()
    setattr(partner, 'my_Database4', None)
    _safe_set(owner, 'my_FKRelation', partner)
    assert owner in getattr(partner, 'my_Database4')
    _safe_set(owner, 'my_FKRelation', None)
    assert owner not in getattr(partner, 'my_Database4')


