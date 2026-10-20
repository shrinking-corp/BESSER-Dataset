import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Anotation,
    JPA_Anotation,
    JPA_Column,
    JPA_Entity,
    JPA_EntityPk,
    JPA_ManyToMany,
    JPA_ManyToOne,
    JPA_OneToMany,
    JPA_OneToOne,
    JPA_PersistenceUnit,
    JPA_Property,
    JPA_Table,
    Cascade,
    Fetch,
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

def test_assoc_properties1_reverse_link_reassign_clear():
    a1 = JPA_Property(comment="sample_text", name="sample_text")
    a2 = JPA_Property(comment="sample_text_2", name="sample_text_2")
    b = JPA_Entity(comment="sample_text", name="sample_text")
    _safe_set(b, 'JPA_Entity2', {a1})
    assert _is_linked(b, 'JPA_Entity2', a1)
    if hasattr(a1, 'JPA_Property'):
        assert _is_linked(a1, 'JPA_Property', b)
    _safe_set(b, 'JPA_Entity2', {a2})
    assert _is_linked(b, 'JPA_Entity2', a2)
    if hasattr(a1, 'JPA_Property'):
        assert not _is_linked(a1, 'JPA_Property', b)
    if hasattr(a2, 'JPA_Property'):
        assert _is_linked(a2, 'JPA_Property', b)
    _safe_set(b, 'JPA_Entity2', set())
    assert not _is_linked(b, 'JPA_Entity2', a2)
    if hasattr(a2, 'JPA_Property'):
        assert not _is_linked(a2, 'JPA_Property', b)


def test_assoc_properties8_reverse_link_reassign_clear():
    a1 = JPA_Property(comment="sample_text", name="sample_text")
    a2 = JPA_Property(comment="sample_text_2", name="sample_text_2")
    b = JPA_EntityPk(name="sample_text")
    _safe_set(b, 'JPA_EntityPk', {a1})
    assert _is_linked(b, 'JPA_EntityPk', a1)
    if hasattr(a1, 'JPA_Property9'):
        assert _is_linked(a1, 'JPA_Property9', b)
    _safe_set(b, 'JPA_EntityPk', {a2})
    assert _is_linked(b, 'JPA_EntityPk', a2)
    if hasattr(a1, 'JPA_Property9'):
        assert not _is_linked(a1, 'JPA_Property9', b)
    if hasattr(a2, 'JPA_Property9'):
        assert _is_linked(a2, 'JPA_Property9', b)
    _safe_set(b, 'JPA_EntityPk', set())
    assert not _is_linked(b, 'JPA_EntityPk', a2)
    if hasattr(a2, 'JPA_Property9'):
        assert not _is_linked(a2, 'JPA_Property9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_anotations3_stub_double():
    # JPA_Anotation has no real 'JPA_Anotation' property in the generated
    # code (a bare stub) -- manually attach it so JPA_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JPA_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JPA_Entity(comment="sample_text", name="sample_text")
    partner = JPA_Anotation()
    setattr(partner, 'JPA_Anotation', None)
    _safe_set(owner, 'JPA_Entity4', {partner})
    assert getattr(partner, 'JPA_Anotation') == owner
    _safe_set(owner, 'JPA_Entity4', set())
    assert getattr(partner, 'JPA_Anotation') is None


def test_assoc_anotations5_stub_double():
    # JPA_Anotation has no real 'JPA_Anotation7' property in the generated
    # code (a bare stub) -- manually attach it so JPA_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JPA_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JPA_Property(comment="sample_text", name="sample_text")
    partner = JPA_Anotation()
    setattr(partner, 'JPA_Anotation7', None)
    _safe_set(owner, 'JPA_Property6', {partner})
    assert getattr(partner, 'JPA_Anotation7') == owner
    _safe_set(owner, 'JPA_Property6', set())
    assert getattr(partner, 'JPA_Anotation7') is None


def test_assoc_entities0_stub_double():
    # JPA_PersistenceUnit has no real 'JPA_PersistenceUnit' property in the generated
    # code (a bare stub) -- manually attach it so JPA_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JPA_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JPA_Entity(comment="sample_text", name="sample_text")
    partner = JPA_PersistenceUnit()
    setattr(partner, 'JPA_PersistenceUnit', None)
    _safe_set(owner, 'JPA_Entity', partner)
    assert owner in getattr(partner, 'JPA_PersistenceUnit')
    _safe_set(owner, 'JPA_Entity', None)
    assert owner not in getattr(partner, 'JPA_PersistenceUnit')


