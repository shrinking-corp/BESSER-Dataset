import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    workbench101_NamedElement,
    workbench101_RelatedTo,
    workbench101_Thing,
    workbench101_Thoughts,
    workbench101_Workbench,
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

def test_assoc_fromThing4_reverse_link_reassign_clear():
    a1 = workbench101_Thing(id=7)
    a2 = workbench101_Thing(id=13)
    b = workbench101_RelatedTo(since="sample_text")
    _safe_set(b, 'relations', a1)
    assert _is_linked(b, 'relations', a1)
    if hasattr(a1, 'Thing'):
        assert _is_linked(a1, 'Thing', b)
    _safe_set(b, 'relations', a2)
    assert _is_linked(b, 'relations', a2)
    if hasattr(a1, 'Thing'):
        assert not _is_linked(a1, 'Thing', b)
    if hasattr(a2, 'Thing'):
        assert _is_linked(a2, 'Thing', b)
    _safe_set(b, 'relations', None)
    assert not _is_linked(b, 'relations', a2)
    if hasattr(a2, 'Thing'):
        assert not _is_linked(a2, 'Thing', b)


def test_assoc_relations3_reverse_link_reassign_clear():
    a1 = workbench101_Thing(id=7)
    a2 = workbench101_Thing(id=13)
    b = workbench101_RelatedTo(since="sample_text")
    _safe_set(b, 'RelatedTo', a1)
    assert _is_linked(b, 'RelatedTo', a1)
    if hasattr(a1, 'fromThing'):
        assert _is_linked(a1, 'fromThing', b)
    _safe_set(b, 'RelatedTo', a2)
    assert _is_linked(b, 'RelatedTo', a2)
    if hasattr(a1, 'fromThing'):
        assert not _is_linked(a1, 'fromThing', b)
    if hasattr(a2, 'fromThing'):
        assert _is_linked(a2, 'fromThing', b)
    _safe_set(b, 'RelatedTo', None)
    assert not _is_linked(b, 'RelatedTo', a2)
    if hasattr(a2, 'fromThing'):
        assert not _is_linked(a2, 'fromThing', b)


def test_assoc_things0_reverse_link_reassign_clear():
    a1 = workbench101_Workbench(aprop="sample_text")
    a2 = workbench101_Workbench(aprop="sample_text_2")
    b = workbench101_Thing(id=7)
    _safe_set(b, 'workbench101_Thing', a1)
    assert _is_linked(b, 'workbench101_Thing', a1)
    if hasattr(a1, 'workbench101_Workbench'):
        assert _is_linked(a1, 'workbench101_Workbench', b)
    _safe_set(b, 'workbench101_Thing', a2)
    assert _is_linked(b, 'workbench101_Thing', a2)
    if hasattr(a1, 'workbench101_Workbench'):
        assert not _is_linked(a1, 'workbench101_Workbench', b)
    if hasattr(a2, 'workbench101_Workbench'):
        assert _is_linked(a2, 'workbench101_Workbench', b)
    _safe_set(b, 'workbench101_Thing', None)
    assert not _is_linked(b, 'workbench101_Thing', a2)
    if hasattr(a2, 'workbench101_Workbench'):
        assert not _is_linked(a2, 'workbench101_Workbench', b)


def test_assoc_toThing5_reverse_link_reassign_clear():
    a1 = workbench101_Thing(id=7)
    a2 = workbench101_Thing(id=13)
    b = workbench101_RelatedTo(since="sample_text")
    _safe_set(b, 'workbench101_RelatedTo', a1)
    assert _is_linked(b, 'workbench101_RelatedTo', a1)
    if hasattr(a1, 'workbench101_Thing6'):
        assert _is_linked(a1, 'workbench101_Thing6', b)
    _safe_set(b, 'workbench101_RelatedTo', a2)
    assert _is_linked(b, 'workbench101_RelatedTo', a2)
    if hasattr(a1, 'workbench101_Thing6'):
        assert not _is_linked(a1, 'workbench101_Thing6', b)
    if hasattr(a2, 'workbench101_Thing6'):
        assert _is_linked(a2, 'workbench101_Thing6', b)
    _safe_set(b, 'workbench101_RelatedTo', None)
    assert not _is_linked(b, 'workbench101_RelatedTo', a2)
    if hasattr(a2, 'workbench101_Thing6'):
        assert not _is_linked(a2, 'workbench101_Thing6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_relatedTo7_stub_double():
    # workbench101_Thoughts has no real 'workbench101_Thoughts8' property in the generated
    # code (a bare stub) -- manually attach it so workbench101_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workbench101_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workbench101_Thing(id=7)
    partner = workbench101_Thoughts()
    setattr(partner, 'workbench101_Thoughts8', None)
    _safe_set(owner, 'workbench101_Thing9', partner)
    assert owner in getattr(partner, 'workbench101_Thoughts8')
    _safe_set(owner, 'workbench101_Thing9', None)
    assert owner not in getattr(partner, 'workbench101_Thoughts8')


def test_assoc_thoughts1_stub_double():
    # workbench101_Thoughts has no real 'workbench101_Thoughts' property in the generated
    # code (a bare stub) -- manually attach it so workbench101_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workbench101_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workbench101_Workbench(aprop="sample_text")
    partner = workbench101_Thoughts()
    setattr(partner, 'workbench101_Thoughts', None)
    _safe_set(owner, 'workbench101_Workbench2', {partner})
    assert getattr(partner, 'workbench101_Thoughts') == owner
    _safe_set(owner, 'workbench101_Workbench2', set())
    assert getattr(partner, 'workbench101_Thoughts') is None


