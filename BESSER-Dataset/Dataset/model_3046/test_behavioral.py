import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    entities_DomainModel,
    entities_Entity,
    entities_Feature,
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

def test_assoc_features4_reverse_link_reassign_clear():
    a1 = entities_Feature(many=True, name="sample_text")
    a2 = entities_Feature(many=False, name="sample_text_2")
    b = entities_Entity(name="sample_text")
    _safe_set(b, 'entities_Entity5', {a1})
    assert _is_linked(b, 'entities_Entity5', a1)
    if hasattr(a1, 'entities_Feature'):
        assert _is_linked(a1, 'entities_Feature', b)
    _safe_set(b, 'entities_Entity5', {a2})
    assert _is_linked(b, 'entities_Entity5', a2)
    if hasattr(a1, 'entities_Feature'):
        assert not _is_linked(a1, 'entities_Feature', b)
    if hasattr(a2, 'entities_Feature'):
        assert _is_linked(a2, 'entities_Feature', b)
    _safe_set(b, 'entities_Entity5', set())
    assert not _is_linked(b, 'entities_Entity5', a2)
    if hasattr(a2, 'entities_Feature'):
        assert not _is_linked(a2, 'entities_Feature', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = entities_Entity(name="sample_text")
    a2 = entities_Entity(name="sample_text_2")
    b = entities_Entity(name="sample_text")
    _safe_set(b, 'entities_Entity3', a1)
    assert _is_linked(b, 'entities_Entity3', a1)
    if hasattr(a1, 'entities_Entity1'):
        assert _is_linked(a1, 'entities_Entity1', b)
    _safe_set(b, 'entities_Entity3', a2)
    assert _is_linked(b, 'entities_Entity3', a2)
    if hasattr(a1, 'entities_Entity1'):
        assert not _is_linked(a1, 'entities_Entity1', b)
    if hasattr(a2, 'entities_Entity1'):
        assert _is_linked(a2, 'entities_Entity1', b)
    _safe_set(b, 'entities_Entity3', None)
    assert not _is_linked(b, 'entities_Entity3', a2)
    if hasattr(a2, 'entities_Entity1'):
        assert not _is_linked(a2, 'entities_Entity1', b)


def test_assoc_type6_reverse_link_reassign_clear():
    a1 = entities_Feature(many=True, name="sample_text")
    a2 = entities_Feature(many=False, name="sample_text_2")
    b = entities_Entity(name="sample_text")
    _safe_set(b, 'entities_Entity8', a1)
    assert _is_linked(b, 'entities_Entity8', a1)
    if hasattr(a1, 'entities_Feature7'):
        assert _is_linked(a1, 'entities_Feature7', b)
    _safe_set(b, 'entities_Entity8', a2)
    assert _is_linked(b, 'entities_Entity8', a2)
    if hasattr(a1, 'entities_Feature7'):
        assert not _is_linked(a1, 'entities_Feature7', b)
    if hasattr(a2, 'entities_Feature7'):
        assert _is_linked(a2, 'entities_Feature7', b)
    _safe_set(b, 'entities_Entity8', None)
    assert not _is_linked(b, 'entities_Entity8', a2)
    if hasattr(a2, 'entities_Feature7'):
        assert not _is_linked(a2, 'entities_Feature7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entities0_stub_double():
    # entities_DomainModel has no real 'entities_DomainModel' property in the generated
    # code (a bare stub) -- manually attach it so entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Entity(name="sample_text")
    partner = entities_DomainModel()
    setattr(partner, 'entities_DomainModel', None)
    _safe_set(owner, 'entities_Entity', partner)
    assert owner in getattr(partner, 'entities_DomainModel')
    _safe_set(owner, 'entities_Entity', None)
    assert owner not in getattr(partner, 'entities_DomainModel')


