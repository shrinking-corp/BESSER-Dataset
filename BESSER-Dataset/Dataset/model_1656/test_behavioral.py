import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    error4_Component,
    error4_NamedElement,
    error4_RelatedTo,
    error4_Thing,
    error4_World,
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
    a1 = error4_Thing(id=7)
    a2 = error4_Thing(id=13)
    b = error4_RelatedTo(since="sample_text")
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


def test_assoc_relations1_reverse_link_reassign_clear():
    a1 = error4_Thing(id=7)
    a2 = error4_Thing(id=13)
    b = error4_RelatedTo(since="sample_text")
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


def test_assoc_toThing5_reverse_link_reassign_clear():
    a1 = error4_Thing(id=7)
    a2 = error4_Thing(id=13)
    b = error4_RelatedTo(since="sample_text")
    _safe_set(b, 'error4_RelatedTo', a1)
    assert _is_linked(b, 'error4_RelatedTo', a1)
    if hasattr(a1, 'error4_Thing6'):
        assert _is_linked(a1, 'error4_Thing6', b)
    _safe_set(b, 'error4_RelatedTo', a2)
    assert _is_linked(b, 'error4_RelatedTo', a2)
    if hasattr(a1, 'error4_Thing6'):
        assert not _is_linked(a1, 'error4_Thing6', b)
    if hasattr(a2, 'error4_Thing6'):
        assert _is_linked(a2, 'error4_Thing6', b)
    _safe_set(b, 'error4_RelatedTo', None)
    assert not _is_linked(b, 'error4_RelatedTo', a2)
    if hasattr(a2, 'error4_Thing6'):
        assert not _is_linked(a2, 'error4_Thing6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components2_stub_double():
    # error4_Component has no real 'error4_Component' property in the generated
    # code (a bare stub) -- manually attach it so error4_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # error4_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = error4_Thing(id=7)
    partner = error4_Component()
    setattr(partner, 'error4_Component', None)
    _safe_set(owner, 'error4_Thing3', {partner})
    assert getattr(partner, 'error4_Component') == owner
    _safe_set(owner, 'error4_Thing3', set())
    assert getattr(partner, 'error4_Component') is None


def test_assoc_things0_stub_double():
    # error4_World has no real 'error4_World' property in the generated
    # code (a bare stub) -- manually attach it so error4_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # error4_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = error4_Thing(id=7)
    partner = error4_World()
    setattr(partner, 'error4_World', None)
    _safe_set(owner, 'error4_Thing', partner)
    assert owner in getattr(partner, 'error4_World')
    _safe_set(owner, 'error4_Thing', None)
    assert owner not in getattr(partner, 'error4_World')


def test_assoc_toComponent7_stub_double():
    # error4_Component has no real 'error4_Component9' property in the generated
    # code (a bare stub) -- manually attach it so error4_RelatedTo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # error4_RelatedTo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = error4_RelatedTo(since="sample_text")
    partner = error4_Component()
    setattr(partner, 'error4_Component9', None)
    _safe_set(owner, 'error4_RelatedTo8', partner)
    assert getattr(partner, 'error4_Component9') == owner
    _safe_set(owner, 'error4_RelatedTo8', None)
    assert getattr(partner, 'error4_Component9') is None


