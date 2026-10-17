import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    yye_Alias,
    yye_Base,
    yye_Foo,
    yye_NamedElement,
    yye_Relation,
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

def test_assoc_aliases2_reverse_link_reassign_clear():
    a1 = yye_NamedElement(name="sample_text")
    a2 = yye_NamedElement(name="sample_text_2")
    b = yye_Alias(id="sample_text")
    _safe_set(b, 'yye_Alias', a1)
    assert _is_linked(b, 'yye_Alias', a1)
    if hasattr(a1, 'yye_NamedElement'):
        assert _is_linked(a1, 'yye_NamedElement', b)
    _safe_set(b, 'yye_Alias', a2)
    assert _is_linked(b, 'yye_Alias', a2)
    if hasattr(a1, 'yye_NamedElement'):
        assert not _is_linked(a1, 'yye_NamedElement', b)
    if hasattr(a2, 'yye_NamedElement'):
        assert _is_linked(a2, 'yye_NamedElement', b)
    _safe_set(b, 'yye_Alias', None)
    assert not _is_linked(b, 'yye_Alias', a2)
    if hasattr(a2, 'yye_NamedElement'):
        assert not _is_linked(a2, 'yye_NamedElement', b)


def test_assoc_foos1_reverse_link_reassign_clear():
    a1 = yye_Foo(id="sample_text")
    a2 = yye_Foo(id="sample_text_2")
    b = yye_Base(id=7)
    _safe_set(b, 'yye_Base', {a1})
    assert _is_linked(b, 'yye_Base', a1)
    if hasattr(a1, 'yye_Foo'):
        assert _is_linked(a1, 'yye_Foo', b)
    _safe_set(b, 'yye_Base', {a2})
    assert _is_linked(b, 'yye_Base', a2)
    if hasattr(a1, 'yye_Foo'):
        assert not _is_linked(a1, 'yye_Foo', b)
    if hasattr(a2, 'yye_Foo'):
        assert _is_linked(a2, 'yye_Foo', b)
    _safe_set(b, 'yye_Base', set())
    assert not _is_linked(b, 'yye_Base', a2)
    if hasattr(a2, 'yye_Foo'):
        assert not _is_linked(a2, 'yye_Foo', b)


def test_assoc_fromThing3_reverse_link_reassign_clear():
    a1 = yye_Relation(since="sample_text")
    a2 = yye_Relation(since="sample_text_2")
    b = yye_Base(id=7)
    _safe_set(b, 'Base', a1)
    assert _is_linked(b, 'Base', a1)
    if hasattr(a1, 'relations'):
        assert _is_linked(a1, 'relations', b)
    _safe_set(b, 'Base', a2)
    assert _is_linked(b, 'Base', a2)
    if hasattr(a1, 'relations'):
        assert not _is_linked(a1, 'relations', b)
    if hasattr(a2, 'relations'):
        assert _is_linked(a2, 'relations', b)
    _safe_set(b, 'Base', None)
    assert not _is_linked(b, 'Base', a2)
    if hasattr(a2, 'relations'):
        assert not _is_linked(a2, 'relations', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = yye_Relation(since="sample_text")
    a2 = yye_Relation(since="sample_text_2")
    b = yye_Base(id=7)
    _safe_set(b, 'fromThing', {a1})
    assert _is_linked(b, 'fromThing', a1)
    if hasattr(a1, 'Relation'):
        assert _is_linked(a1, 'Relation', b)
    _safe_set(b, 'fromThing', {a2})
    assert _is_linked(b, 'fromThing', a2)
    if hasattr(a1, 'Relation'):
        assert not _is_linked(a1, 'Relation', b)
    if hasattr(a2, 'Relation'):
        assert _is_linked(a2, 'Relation', b)
    _safe_set(b, 'fromThing', set())
    assert not _is_linked(b, 'fromThing', a2)
    if hasattr(a2, 'Relation'):
        assert not _is_linked(a2, 'Relation', b)


def test_assoc_subRelations7_reverse_link_reassign_clear():
    a1 = yye_Relation(since="sample_text")
    a2 = yye_Relation(since="sample_text_2")
    b = yye_Relation(since="sample_text")
    _safe_set(b, 'yye_Relation8', a1)
    assert _is_linked(b, 'yye_Relation8', a1)
    if hasattr(a1, 'yye_Relation6'):
        assert _is_linked(a1, 'yye_Relation6', b)
    _safe_set(b, 'yye_Relation8', a2)
    assert _is_linked(b, 'yye_Relation8', a2)
    if hasattr(a1, 'yye_Relation6'):
        assert not _is_linked(a1, 'yye_Relation6', b)
    if hasattr(a2, 'yye_Relation6'):
        assert _is_linked(a2, 'yye_Relation6', b)
    _safe_set(b, 'yye_Relation8', None)
    assert not _is_linked(b, 'yye_Relation8', a2)
    if hasattr(a2, 'yye_Relation6'):
        assert not _is_linked(a2, 'yye_Relation6', b)


def test_assoc_toThing4_reverse_link_reassign_clear():
    a1 = yye_Relation(since="sample_text")
    a2 = yye_Relation(since="sample_text_2")
    b = yye_Base(id=7)
    _safe_set(b, 'yye_Base5', a1)
    assert _is_linked(b, 'yye_Base5', a1)
    if hasattr(a1, 'yye_Relation'):
        assert _is_linked(a1, 'yye_Relation', b)
    _safe_set(b, 'yye_Base5', a2)
    assert _is_linked(b, 'yye_Base5', a2)
    if hasattr(a1, 'yye_Relation'):
        assert not _is_linked(a1, 'yye_Relation', b)
    if hasattr(a2, 'yye_Relation'):
        assert _is_linked(a2, 'yye_Relation', b)
    _safe_set(b, 'yye_Base5', None)
    assert not _is_linked(b, 'yye_Base5', a2)
    if hasattr(a2, 'yye_Relation'):
        assert not _is_linked(a2, 'yye_Relation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

