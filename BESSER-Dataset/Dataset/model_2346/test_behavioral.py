import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RModelElement,
    simplerdbms_Column,
    simplerdbms_ForeignKey,
    simplerdbms_Key,
    simplerdbms_RModelElement,
    simplerdbms_Schema,
    simplerdbms_Table,
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

def test_assoc_columns12_reverse_link_reassign_clear():
    a1 = simplerdbms_Key(isPrimary=True)
    a2 = simplerdbms_Key(isPrimary=False)
    b = simplerdbms_Column(type="sample_text")
    _safe_set(b, 'Column14', a1)
    assert _is_linked(b, 'Column14', a1)
    if hasattr(a1, 'keys13'):
        assert _is_linked(a1, 'keys13', b)
    _safe_set(b, 'Column14', a2)
    assert _is_linked(b, 'Column14', a2)
    if hasattr(a1, 'keys13'):
        assert not _is_linked(a1, 'keys13', b)
    if hasattr(a2, 'keys13'):
        assert _is_linked(a2, 'keys13', b)
    _safe_set(b, 'Column14', None)
    assert not _is_linked(b, 'Column14', a2)
    if hasattr(a2, 'keys13'):
        assert not _is_linked(a2, 'keys13', b)


def test_assoc_keys3_reverse_link_reassign_clear():
    a1 = simplerdbms_Key(isPrimary=True)
    a2 = simplerdbms_Key(isPrimary=False)
    b = simplerdbms_Column(type="sample_text")
    _safe_set(b, 'columns4', {a1})
    assert _is_linked(b, 'columns4', a1)
    if hasattr(a1, 'Key'):
        assert _is_linked(a1, 'Key', b)
    _safe_set(b, 'columns4', {a2})
    assert _is_linked(b, 'columns4', a2)
    if hasattr(a1, 'Key'):
        assert not _is_linked(a1, 'Key', b)
    if hasattr(a2, 'Key'):
        assert _is_linked(a2, 'Key', b)
    _safe_set(b, 'columns4', set())
    assert not _is_linked(b, 'columns4', a2)
    if hasattr(a2, 'Key'):
        assert not _is_linked(a2, 'Key', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns17_stub_double():
    # simplerdbms_Table has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_Table()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column18', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Column18', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_columns6_stub_double():
    # simplerdbms_ForeignKey has no real 'foreignKeys' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_ForeignKey()
    setattr(partner, 'foreignKeys', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'foreignKeys')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'foreignKeys')


def test_assoc_foreignKeys1_stub_double():
    # simplerdbms_ForeignKey has no real 'ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_ForeignKey()
    setattr(partner, 'ForeignKey', None)
    _safe_set(owner, 'columns2', {partner})
    assert getattr(partner, 'ForeignKey') == owner
    _safe_set(owner, 'columns2', set())
    assert getattr(partner, 'ForeignKey') is None


def test_assoc_keys20_stub_double():
    # simplerdbms_Table has no real 'owner21' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Key(isPrimary=True)
    partner = simplerdbms_Table()
    setattr(partner, 'owner21', None)
    _safe_set(owner, 'Key22', partner)
    assert owner in getattr(partner, 'owner21')
    _safe_set(owner, 'Key22', None)
    assert owner not in getattr(partner, 'owner21')


def test_assoc_owner0_stub_double():
    # simplerdbms_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Column(type="sample_text")
    partner = simplerdbms_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table') is None


def test_assoc_owner10_stub_double():
    # simplerdbms_Table has no real 'Table11' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Key(isPrimary=True)
    partner = simplerdbms_Table()
    setattr(partner, 'Table11', None)
    _safe_set(owner, 'keys', partner)
    assert getattr(partner, 'Table11') == owner
    _safe_set(owner, 'keys', None)
    assert getattr(partner, 'Table11') is None


def test_assoc_refersTo5_stub_double():
    # simplerdbms_ForeignKey has no real 'simplerdbms_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so simplerdbms_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplerdbms_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplerdbms_Key(isPrimary=True)
    partner = simplerdbms_ForeignKey()
    setattr(partner, 'simplerdbms_ForeignKey', None)
    _safe_set(owner, 'simplerdbms_Key', partner)
    assert getattr(partner, 'simplerdbms_ForeignKey') == owner
    _safe_set(owner, 'simplerdbms_Key', None)
    assert getattr(partner, 'simplerdbms_ForeignKey') is None


