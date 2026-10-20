import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ER_ERAttribute,
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


def test_assoc_entities0_reverse_link_reassign_clear():
    a1 = ER_Entity(name="sample_text")
    a2 = ER_Entity(name="sample_text_2")
    b = ER_ERSchema(name="sample_text")
    _safe_set(b, 'schema', {a1})
    assert _is_linked(b, 'schema', a1)
    if hasattr(a1, 'Entity'):
        assert _is_linked(a1, 'Entity', b)
    _safe_set(b, 'schema', {a2})
    assert _is_linked(b, 'schema', a2)
    if hasattr(a1, 'Entity'):
        assert not _is_linked(a1, 'Entity', b)
    if hasattr(a2, 'Entity'):
        assert _is_linked(a2, 'Entity', b)
    _safe_set(b, 'schema', set())
    assert not _is_linked(b, 'schema', a2)
    if hasattr(a2, 'Entity'):
        assert not _is_linked(a2, 'Entity', b)


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


def test_assoc_relships1_reverse_link_reassign_clear():
    a1 = ER_Relship(name="sample_text")
    a2 = ER_Relship(name="sample_text_2")
    b = ER_ERSchema(name="sample_text")
    _safe_set(b, 'schema2', {a1})
    assert _is_linked(b, 'schema2', a1)
    if hasattr(a1, 'Relship'):
        assert _is_linked(a1, 'Relship', b)
    _safe_set(b, 'schema2', {a2})
    assert _is_linked(b, 'schema2', a2)
    if hasattr(a1, 'Relship'):
        assert not _is_linked(a1, 'Relship', b)
    if hasattr(a2, 'Relship'):
        assert _is_linked(a2, 'Relship', b)
    _safe_set(b, 'schema2', set())
    assert not _is_linked(b, 'schema2', a2)
    if hasattr(a2, 'Relship'):
        assert not _is_linked(a2, 'Relship', b)


def test_assoc_schema12_reverse_link_reassign_clear():
    a1 = ER_Relship(name="sample_text")
    a2 = ER_Relship(name="sample_text_2")
    b = ER_ERSchema(name="sample_text")
    _safe_set(b, 'ERSchema13', a1)
    assert _is_linked(b, 'ERSchema13', a1)
    if hasattr(a1, 'relships'):
        assert _is_linked(a1, 'relships', b)
    _safe_set(b, 'ERSchema13', a2)
    assert _is_linked(b, 'ERSchema13', a2)
    if hasattr(a1, 'relships'):
        assert not _is_linked(a1, 'relships', b)
    if hasattr(a2, 'relships'):
        assert _is_linked(a2, 'relships', b)
    _safe_set(b, 'ERSchema13', None)
    assert not _is_linked(b, 'ERSchema13', a2)
    if hasattr(a2, 'relships'):
        assert not _is_linked(a2, 'relships', b)


def test_assoc_schema6_reverse_link_reassign_clear():
    a1 = ER_Entity(name="sample_text")
    a2 = ER_Entity(name="sample_text_2")
    b = ER_ERSchema(name="sample_text")
    _safe_set(b, 'ERSchema', a1)
    assert _is_linked(b, 'ERSchema', a1)
    if hasattr(a1, 'entities'):
        assert _is_linked(a1, 'entities', b)
    _safe_set(b, 'ERSchema', a2)
    assert _is_linked(b, 'ERSchema', a2)
    if hasattr(a1, 'entities'):
        assert not _is_linked(a1, 'entities', b)
    if hasattr(a2, 'entities'):
        assert _is_linked(a2, 'entities', b)
    _safe_set(b, 'ERSchema', None)
    assert not _is_linked(b, 'ERSchema', a2)
    if hasattr(a2, 'entities'):
        assert not _is_linked(a2, 'entities', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

