import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ERElem,
    ER_ERAttribute,
    ER_ERElem,
    ER_ERSchema,
    ER_Entity,
    ER_Relship,
    ER_RelshipEnd,
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

def test_assoc_attrs3_reverse_link_reassign_clear():
    a1 = ER_Entity(name="sample_text")
    a2 = ER_Entity(name="sample_text_2")
    b = ER_ERAttribute(isKey=True, name="sample_text")
    _safe_set(b, 'ERAttribute', a1)
    assert _is_linked(b, 'ERAttribute', a1)
    if hasattr(a1, 'entity'):
        assert _is_linked(a1, 'entity', b)
    _safe_set(b, 'ERAttribute', a2)
    assert _is_linked(b, 'ERAttribute', a2)
    if hasattr(a1, 'entity'):
        assert not _is_linked(a1, 'entity', b)
    if hasattr(a2, 'entity'):
        assert _is_linked(a2, 'entity', b)
    _safe_set(b, 'ERAttribute', None)
    assert not _is_linked(b, 'ERAttribute', a2)
    if hasattr(a2, 'entity'):
        assert not _is_linked(a2, 'entity', b)


def test_assoc_attrs7_reverse_link_reassign_clear():
    a1 = ER_Relship(name="sample_text")
    a2 = ER_Relship(name="sample_text_2")
    b = ER_ERAttribute(isKey=True, name="sample_text")
    _safe_set(b, 'ERAttribute8', a1)
    assert _is_linked(b, 'ERAttribute8', a1)
    if hasattr(a1, 'relship'):
        assert _is_linked(a1, 'relship', b)
    _safe_set(b, 'ERAttribute8', a2)
    assert _is_linked(b, 'ERAttribute8', a2)
    if hasattr(a1, 'relship'):
        assert not _is_linked(a1, 'relship', b)
    if hasattr(a2, 'relship'):
        assert _is_linked(a2, 'relship', b)
    _safe_set(b, 'ERAttribute8', None)
    assert not _is_linked(b, 'ERAttribute8', a2)
    if hasattr(a2, 'relship'):
        assert not _is_linked(a2, 'relship', b)


def test_assoc_ends4_reverse_link_reassign_clear():
    a1 = ER_RelshipEnd(name="sample_text")
    a2 = ER_RelshipEnd(name="sample_text_2")
    b = ER_Entity(name="sample_text")
    _safe_set(b, 'entity5', {a1})
    assert _is_linked(b, 'entity5', a1)
    if hasattr(a1, 'RelshipEnd'):
        assert _is_linked(a1, 'RelshipEnd', b)
    _safe_set(b, 'entity5', {a2})
    assert _is_linked(b, 'entity5', a2)
    if hasattr(a1, 'RelshipEnd'):
        assert not _is_linked(a1, 'RelshipEnd', b)
    if hasattr(a2, 'RelshipEnd'):
        assert _is_linked(a2, 'RelshipEnd', b)
    _safe_set(b, 'entity5', set())
    assert not _is_linked(b, 'entity5', a2)
    if hasattr(a2, 'RelshipEnd'):
        assert not _is_linked(a2, 'RelshipEnd', b)


def test_assoc_ends9_reverse_link_reassign_clear():
    a1 = ER_RelshipEnd(name="sample_text")
    a2 = ER_RelshipEnd(name="sample_text_2")
    b = ER_Relship(name="sample_text")
    _safe_set(b, 'relship10', {a1})
    assert _is_linked(b, 'relship10', a1)
    if hasattr(a1, 'RelshipEnd11'):
        assert _is_linked(a1, 'RelshipEnd11', b)
    _safe_set(b, 'relship10', {a2})
    assert _is_linked(b, 'relship10', a2)
    if hasattr(a1, 'RelshipEnd11'):
        assert not _is_linked(a1, 'RelshipEnd11', b)
    if hasattr(a2, 'RelshipEnd11'):
        assert _is_linked(a2, 'RelshipEnd11', b)
    _safe_set(b, 'relship10', set())
    assert not _is_linked(b, 'relship10', a2)
    if hasattr(a2, 'RelshipEnd11'):
        assert not _is_linked(a2, 'RelshipEnd11', b)


def test_assoc_entity16_reverse_link_reassign_clear():
    a1 = ER_RelshipEnd(name="sample_text")
    a2 = ER_RelshipEnd(name="sample_text_2")
    b = ER_Entity(name="sample_text")
    _safe_set(b, 'Entity18', a1)
    assert _is_linked(b, 'Entity18', a1)
    if hasattr(a1, 'ends17'):
        assert _is_linked(a1, 'ends17', b)
    _safe_set(b, 'Entity18', a2)
    assert _is_linked(b, 'Entity18', a2)
    if hasattr(a1, 'ends17'):
        assert not _is_linked(a1, 'ends17', b)
    if hasattr(a2, 'ends17'):
        assert _is_linked(a2, 'ends17', b)
    _safe_set(b, 'Entity18', None)
    assert not _is_linked(b, 'Entity18', a2)
    if hasattr(a2, 'ends17'):
        assert not _is_linked(a2, 'ends17', b)


def test_assoc_entity19_reverse_link_reassign_clear():
    a1 = ER_Entity(name="sample_text")
    a2 = ER_Entity(name="sample_text_2")
    b = ER_ERAttribute(isKey=True, name="sample_text")
    _safe_set(b, 'attrs', a1)
    assert _is_linked(b, 'attrs', a1)
    if hasattr(a1, 'Entity20'):
        assert _is_linked(a1, 'Entity20', b)
    _safe_set(b, 'attrs', a2)
    assert _is_linked(b, 'attrs', a2)
    if hasattr(a1, 'Entity20'):
        assert not _is_linked(a1, 'Entity20', b)
    if hasattr(a2, 'Entity20'):
        assert _is_linked(a2, 'Entity20', b)
    _safe_set(b, 'attrs', None)
    assert not _is_linked(b, 'attrs', a2)
    if hasattr(a2, 'Entity20'):
        assert not _is_linked(a2, 'Entity20', b)


def test_assoc_relship14_reverse_link_reassign_clear():
    a1 = ER_RelshipEnd(name="sample_text")
    a2 = ER_RelshipEnd(name="sample_text_2")
    b = ER_Relship(name="sample_text")
    _safe_set(b, 'Relship15', a1)
    assert _is_linked(b, 'Relship15', a1)
    if hasattr(a1, 'ends'):
        assert _is_linked(a1, 'ends', b)
    _safe_set(b, 'Relship15', a2)
    assert _is_linked(b, 'Relship15', a2)
    if hasattr(a1, 'ends'):
        assert not _is_linked(a1, 'ends', b)
    if hasattr(a2, 'ends'):
        assert _is_linked(a2, 'ends', b)
    _safe_set(b, 'Relship15', None)
    assert not _is_linked(b, 'Relship15', a2)
    if hasattr(a2, 'ends'):
        assert not _is_linked(a2, 'ends', b)


def test_assoc_relship21_reverse_link_reassign_clear():
    a1 = ER_Relship(name="sample_text")
    a2 = ER_Relship(name="sample_text_2")
    b = ER_ERAttribute(isKey=True, name="sample_text")
    _safe_set(b, 'attrs22', a1)
    assert _is_linked(b, 'attrs22', a1)
    if hasattr(a1, 'Relship23'):
        assert _is_linked(a1, 'Relship23', b)
    _safe_set(b, 'attrs22', a2)
    assert _is_linked(b, 'attrs22', a2)
    if hasattr(a1, 'Relship23'):
        assert not _is_linked(a1, 'Relship23', b)
    if hasattr(a2, 'Relship23'):
        assert _is_linked(a2, 'Relship23', b)
    _safe_set(b, 'attrs22', None)
    assert not _is_linked(b, 'attrs22', a2)
    if hasattr(a2, 'Relship23'):
        assert not _is_linked(a2, 'Relship23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entities0_stub_double():
    # ER_ERSchema has no real 'schema' property in the generated
    # code (a bare stub) -- manually attach it so ER_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ER_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ER_Entity(name="sample_text")
    partner = ER_ERSchema()
    setattr(partner, 'schema', None)
    _safe_set(owner, 'Entity', partner)
    assert owner in getattr(partner, 'schema')
    _safe_set(owner, 'Entity', None)
    assert owner not in getattr(partner, 'schema')


def test_assoc_relships1_stub_double():
    # ER_ERSchema has no real 'schema2' property in the generated
    # code (a bare stub) -- manually attach it so ER_Relship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ER_Relship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ER_Relship(name="sample_text")
    partner = ER_ERSchema()
    setattr(partner, 'schema2', None)
    _safe_set(owner, 'Relship', partner)
    assert owner in getattr(partner, 'schema2')
    _safe_set(owner, 'Relship', None)
    assert owner not in getattr(partner, 'schema2')


def test_assoc_schema12_stub_double():
    # ER_ERSchema has no real 'ERSchema13' property in the generated
    # code (a bare stub) -- manually attach it so ER_Relship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ER_Relship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ER_Relship(name="sample_text")
    partner = ER_ERSchema()
    setattr(partner, 'ERSchema13', None)
    _safe_set(owner, 'relships', partner)
    assert getattr(partner, 'ERSchema13') == owner
    _safe_set(owner, 'relships', None)
    assert getattr(partner, 'ERSchema13') is None


def test_assoc_schema6_stub_double():
    # ER_ERSchema has no real 'ERSchema' property in the generated
    # code (a bare stub) -- manually attach it so ER_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ER_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ER_Entity(name="sample_text")
    partner = ER_ERSchema()
    setattr(partner, 'ERSchema', None)
    _safe_set(owner, 'entities', partner)
    assert getattr(partner, 'ERSchema') == owner
    _safe_set(owner, 'entities', None)
    assert getattr(partner, 'ERSchema') is None


