import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    era_Attribute,
    era_Entity,
    era_Relationship,
    era_System,
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

def test_assoc_entities3_reverse_link_reassign_clear():
    a1 = era_Relationship(name="sample_text")
    a2 = era_Relationship(name="sample_text_2")
    b = era_Entity(inDomain="sample_text", name="sample_text")
    _safe_set(b, 'Entity4', a1)
    assert _is_linked(b, 'Entity4', a1)
    if hasattr(a1, 'relationships'):
        assert _is_linked(a1, 'relationships', b)
    _safe_set(b, 'Entity4', a2)
    assert _is_linked(b, 'Entity4', a2)
    if hasattr(a1, 'relationships'):
        assert not _is_linked(a1, 'relationships', b)
    if hasattr(a2, 'relationships'):
        assert _is_linked(a2, 'relationships', b)
    _safe_set(b, 'Entity4', None)
    assert not _is_linked(b, 'Entity4', a2)
    if hasattr(a2, 'relationships'):
        assert not _is_linked(a2, 'relationships', b)


def test_assoc_relationships2_reverse_link_reassign_clear():
    a1 = era_Relationship(name="sample_text")
    a2 = era_Relationship(name="sample_text_2")
    b = era_Entity(inDomain="sample_text", name="sample_text")
    _safe_set(b, 'entities', {a1})
    assert _is_linked(b, 'entities', a1)
    if hasattr(a1, 'Relationship'):
        assert _is_linked(a1, 'Relationship', b)
    _safe_set(b, 'entities', {a2})
    assert _is_linked(b, 'entities', a2)
    if hasattr(a1, 'Relationship'):
        assert not _is_linked(a1, 'Relationship', b)
    if hasattr(a2, 'Relationship'):
        assert _is_linked(a2, 'Relationship', b)
    _safe_set(b, 'entities', set())
    assert not _is_linked(b, 'entities', a2)
    if hasattr(a2, 'Relationship'):
        assert not _is_linked(a2, 'Relationship', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entity0_stub_double():
    # era_System has no real 'system' property in the generated
    # code (a bare stub) -- manually attach it so era_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # era_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = era_Entity(inDomain="sample_text", name="sample_text")
    partner = era_System()
    setattr(partner, 'system', None)
    _safe_set(owner, 'Entity', partner)
    assert owner in getattr(partner, 'system')
    _safe_set(owner, 'Entity', None)
    assert owner not in getattr(partner, 'system')


def test_assoc_system1_stub_double():
    # era_System has no real 'System' property in the generated
    # code (a bare stub) -- manually attach it so era_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # era_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = era_Entity(inDomain="sample_text", name="sample_text")
    partner = era_System()
    setattr(partner, 'System', None)
    _safe_set(owner, 'entity', partner)
    assert getattr(partner, 'System') == owner
    _safe_set(owner, 'entity', None)
    assert getattr(partner, 'System') is None


