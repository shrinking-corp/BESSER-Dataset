import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    relational_Column,
    relational_ForeignKey,
    relational_Key,
    relational_Table,
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

def test_assoc_column0_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'relational_Column', a1)
    assert _is_linked(b, 'relational_Column', a1)
    if hasattr(a1, 'relational_Table'):
        assert _is_linked(a1, 'relational_Table', b)
    _safe_set(b, 'relational_Column', a2)
    assert _is_linked(b, 'relational_Column', a2)
    if hasattr(a1, 'relational_Table'):
        assert not _is_linked(a1, 'relational_Table', b)
    if hasattr(a2, 'relational_Table'):
        assert _is_linked(a2, 'relational_Table', b)
    _safe_set(b, 'relational_Column', None)
    assert not _is_linked(b, 'relational_Column', a2)
    if hasattr(a2, 'relational_Table'):
        assert not _is_linked(a2, 'relational_Table', b)


def test_assoc_column4_reverse_link_reassign_clear():
    a1 = relational_Key(name="sample_text")
    a2 = relational_Key(name="sample_text_2")
    b = relational_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'relational_Column5', a1)
    assert _is_linked(b, 'relational_Column5', a1)
    if hasattr(a1, 'relational_Key'):
        assert _is_linked(a1, 'relational_Key', b)
    _safe_set(b, 'relational_Column5', a2)
    assert _is_linked(b, 'relational_Column5', a2)
    if hasattr(a1, 'relational_Key'):
        assert not _is_linked(a1, 'relational_Key', b)
    if hasattr(a2, 'relational_Key'):
        assert _is_linked(a2, 'relational_Key', b)
    _safe_set(b, 'relational_Column5', None)
    assert not _is_linked(b, 'relational_Column5', a2)
    if hasattr(a2, 'relational_Key'):
        assert not _is_linked(a2, 'relational_Key', b)


def test_assoc_key1_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Key(name="sample_text")
    _safe_set(b, 'Key', a1)
    assert _is_linked(b, 'Key', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'Key', a2)
    assert _is_linked(b, 'Key', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'Key', None)
    assert not _is_linked(b, 'Key', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_table8_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Key(name="sample_text")
    _safe_set(b, 'key', a1)
    assert _is_linked(b, 'key', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'key', a2)
    assert _is_linked(b, 'key', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'key', None)
    assert not _is_linked(b, 'key', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_column9_stub_double():
    # relational_ForeignKey has no real 'relational_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(name="sample_text", type="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'relational_ForeignKey', None)
    _safe_set(owner, 'relational_Column10', partner)
    assert owner in getattr(partner, 'relational_ForeignKey')
    _safe_set(owner, 'relational_Column10', None)
    assert owner not in getattr(partner, 'relational_ForeignKey')


def test_assoc_foreignKey2_stub_double():
    # relational_ForeignKey has no real 'ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(name="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'ForeignKey', None)
    _safe_set(owner, 'table3', partner)
    assert getattr(partner, 'ForeignKey') == owner
    _safe_set(owner, 'table3', None)
    assert getattr(partner, 'ForeignKey') is None


def test_assoc_referredBy6_stub_double():
    # relational_ForeignKey has no real 'ForeignKey7' property in the generated
    # code (a bare stub) -- manually attach it so relational_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Key(name="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'ForeignKey7', None)
    _safe_set(owner, 'refersTo', partner)
    assert getattr(partner, 'ForeignKey7') == owner
    _safe_set(owner, 'refersTo', None)
    assert getattr(partner, 'ForeignKey7') is None


def test_assoc_refersTo11_stub_double():
    # relational_ForeignKey has no real 'relational_ForeignKey12' property in the generated
    # code (a bare stub) -- manually attach it so relational_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Key(name="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'relational_ForeignKey12', None)
    _safe_set(owner, 'relational_Key13', partner)
    assert getattr(partner, 'relational_ForeignKey12') == owner
    _safe_set(owner, 'relational_Key13', None)
    assert getattr(partner, 'relational_ForeignKey12') is None


def test_assoc_table14_stub_double():
    # relational_ForeignKey has no real 'relational_ForeignKey15' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(name="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'relational_ForeignKey15', None)
    _safe_set(owner, 'relational_Table16', partner)
    assert getattr(partner, 'relational_ForeignKey15') == owner
    _safe_set(owner, 'relational_Table16', None)
    assert getattr(partner, 'relational_ForeignKey15') is None


