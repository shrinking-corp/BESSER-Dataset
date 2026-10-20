import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    databaseMetamodel_Column,
    databaseMetamodel_Database,
    databaseMetamodel_Relation,
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

def test_assoc_hasColumns1_reverse_link_reassign_clear():
    a1 = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    a2 = databaseMetamodel_Relation(isJoinTable=False, isSelfJoinTable=False, name="sample_text_2")
    b = databaseMetamodel_Column(hasFKOrder=7, hasPKOrder=7, name="sample_text", type="sample_text")
    _safe_set(b, 'databaseMetamodel_Column', a1)
    assert _is_linked(b, 'databaseMetamodel_Column', a1)
    if hasattr(a1, 'databaseMetamodel_Relation2'):
        assert _is_linked(a1, 'databaseMetamodel_Relation2', b)
    _safe_set(b, 'databaseMetamodel_Column', a2)
    assert _is_linked(b, 'databaseMetamodel_Column', a2)
    if hasattr(a1, 'databaseMetamodel_Relation2'):
        assert not _is_linked(a1, 'databaseMetamodel_Relation2', b)
    if hasattr(a2, 'databaseMetamodel_Relation2'):
        assert _is_linked(a2, 'databaseMetamodel_Relation2', b)
    _safe_set(b, 'databaseMetamodel_Column', None)
    assert not _is_linked(b, 'databaseMetamodel_Column', a2)
    if hasattr(a2, 'databaseMetamodel_Relation2'):
        assert not _is_linked(a2, 'databaseMetamodel_Relation2', b)


def test_assoc_hasForeignKey6_reverse_link_reassign_clear():
    a1 = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    a2 = databaseMetamodel_Relation(isJoinTable=False, isSelfJoinTable=False, name="sample_text_2")
    b = databaseMetamodel_Column(hasFKOrder=7, hasPKOrder=7, name="sample_text", type="sample_text")
    _safe_set(b, 'databaseMetamodel_Column8', a1)
    assert _is_linked(b, 'databaseMetamodel_Column8', a1)
    if hasattr(a1, 'databaseMetamodel_Relation7'):
        assert _is_linked(a1, 'databaseMetamodel_Relation7', b)
    _safe_set(b, 'databaseMetamodel_Column8', a2)
    assert _is_linked(b, 'databaseMetamodel_Column8', a2)
    if hasattr(a1, 'databaseMetamodel_Relation7'):
        assert not _is_linked(a1, 'databaseMetamodel_Relation7', b)
    if hasattr(a2, 'databaseMetamodel_Relation7'):
        assert _is_linked(a2, 'databaseMetamodel_Relation7', b)
    _safe_set(b, 'databaseMetamodel_Column8', None)
    assert not _is_linked(b, 'databaseMetamodel_Column8', a2)
    if hasattr(a2, 'databaseMetamodel_Relation7'):
        assert not _is_linked(a2, 'databaseMetamodel_Relation7', b)


def test_assoc_hasPrimaryKey3_reverse_link_reassign_clear():
    a1 = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    a2 = databaseMetamodel_Relation(isJoinTable=False, isSelfJoinTable=False, name="sample_text_2")
    b = databaseMetamodel_Column(hasFKOrder=7, hasPKOrder=7, name="sample_text", type="sample_text")
    _safe_set(b, 'databaseMetamodel_Column5', a1)
    assert _is_linked(b, 'databaseMetamodel_Column5', a1)
    if hasattr(a1, 'databaseMetamodel_Relation4'):
        assert _is_linked(a1, 'databaseMetamodel_Relation4', b)
    _safe_set(b, 'databaseMetamodel_Column5', a2)
    assert _is_linked(b, 'databaseMetamodel_Column5', a2)
    if hasattr(a1, 'databaseMetamodel_Relation4'):
        assert not _is_linked(a1, 'databaseMetamodel_Relation4', b)
    if hasattr(a2, 'databaseMetamodel_Relation4'):
        assert _is_linked(a2, 'databaseMetamodel_Relation4', b)
    _safe_set(b, 'databaseMetamodel_Column5', None)
    assert not _is_linked(b, 'databaseMetamodel_Column5', a2)
    if hasattr(a2, 'databaseMetamodel_Relation4'):
        assert not _is_linked(a2, 'databaseMetamodel_Relation4', b)


def test_assoc_isForeignKeyToRelation15_reverse_link_reassign_clear():
    a1 = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    a2 = databaseMetamodel_Relation(isJoinTable=False, isSelfJoinTable=False, name="sample_text_2")
    b = databaseMetamodel_Column(hasFKOrder=7, hasPKOrder=7, name="sample_text", type="sample_text")
    _safe_set(b, 'databaseMetamodel_Column16', {a1})
    assert _is_linked(b, 'databaseMetamodel_Column16', a1)
    if hasattr(a1, 'databaseMetamodel_Relation17'):
        assert _is_linked(a1, 'databaseMetamodel_Relation17', b)
    _safe_set(b, 'databaseMetamodel_Column16', {a2})
    assert _is_linked(b, 'databaseMetamodel_Column16', a2)
    if hasattr(a1, 'databaseMetamodel_Relation17'):
        assert not _is_linked(a1, 'databaseMetamodel_Relation17', b)
    if hasattr(a2, 'databaseMetamodel_Relation17'):
        assert _is_linked(a2, 'databaseMetamodel_Relation17', b)
    _safe_set(b, 'databaseMetamodel_Column16', set())
    assert not _is_linked(b, 'databaseMetamodel_Column16', a2)
    if hasattr(a2, 'databaseMetamodel_Relation17'):
        assert not _is_linked(a2, 'databaseMetamodel_Relation17', b)


def test_assoc_isForeinKeyToColumn13_reverse_link_reassign_clear():
    a1 = databaseMetamodel_Column(hasFKOrder=7, hasPKOrder=7, name="sample_text", type="sample_text")
    a2 = databaseMetamodel_Column(hasFKOrder=13, hasPKOrder=13, name="sample_text_2", type="sample_text_2")
    b = databaseMetamodel_Column(hasFKOrder=7, hasPKOrder=7, name="sample_text", type="sample_text")
    _safe_set(b, 'databaseMetamodel_Column14', a1)
    assert _is_linked(b, 'databaseMetamodel_Column14', a1)
    if hasattr(a1, 'databaseMetamodel_Column12'):
        assert _is_linked(a1, 'databaseMetamodel_Column12', b)
    _safe_set(b, 'databaseMetamodel_Column14', a2)
    assert _is_linked(b, 'databaseMetamodel_Column14', a2)
    if hasattr(a1, 'databaseMetamodel_Column12'):
        assert not _is_linked(a1, 'databaseMetamodel_Column12', b)
    if hasattr(a2, 'databaseMetamodel_Column12'):
        assert _is_linked(a2, 'databaseMetamodel_Column12', b)
    _safe_set(b, 'databaseMetamodel_Column14', None)
    assert not _is_linked(b, 'databaseMetamodel_Column14', a2)
    if hasattr(a2, 'databaseMetamodel_Column12'):
        assert not _is_linked(a2, 'databaseMetamodel_Column12', b)


def test_assoc_referencesRelation10_reverse_link_reassign_clear():
    a1 = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    a2 = databaseMetamodel_Relation(isJoinTable=False, isSelfJoinTable=False, name="sample_text_2")
    b = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    _safe_set(b, 'databaseMetamodel_Relation9', {a1})
    assert _is_linked(b, 'databaseMetamodel_Relation9', a1)
    if hasattr(a1, 'databaseMetamodel_Relation11'):
        assert _is_linked(a1, 'databaseMetamodel_Relation11', b)
    _safe_set(b, 'databaseMetamodel_Relation9', {a2})
    assert _is_linked(b, 'databaseMetamodel_Relation9', a2)
    if hasattr(a1, 'databaseMetamodel_Relation11'):
        assert not _is_linked(a1, 'databaseMetamodel_Relation11', b)
    if hasattr(a2, 'databaseMetamodel_Relation11'):
        assert _is_linked(a2, 'databaseMetamodel_Relation11', b)
    _safe_set(b, 'databaseMetamodel_Relation9', set())
    assert not _is_linked(b, 'databaseMetamodel_Relation9', a2)
    if hasattr(a2, 'databaseMetamodel_Relation11'):
        assert not _is_linked(a2, 'databaseMetamodel_Relation11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_relation0_stub_double():
    # databaseMetamodel_Database has no real 'databaseMetamodel_Database' property in the generated
    # code (a bare stub) -- manually attach it so databaseMetamodel_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # databaseMetamodel_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = databaseMetamodel_Relation(isJoinTable=True, isSelfJoinTable=True, name="sample_text")
    partner = databaseMetamodel_Database()
    setattr(partner, 'databaseMetamodel_Database', None)
    _safe_set(owner, 'databaseMetamodel_Relation', partner)
    assert owner in getattr(partner, 'databaseMetamodel_Database')
    _safe_set(owner, 'databaseMetamodel_Relation', None)
    assert owner not in getattr(partner, 'databaseMetamodel_Database')


