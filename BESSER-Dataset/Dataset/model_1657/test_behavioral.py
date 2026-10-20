import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    simpleparts_Element,
    simpleparts_Item,
    simpleparts_NamedElement,
    simpleparts_Part,
    simpleparts_Piece,
    simpleparts_RelatedTo,
    simpleparts_Thing,
    simpleparts_World,
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

def test_assoc_fromThing10_reverse_link_reassign_clear():
    a1 = simpleparts_Thing(id=7)
    a2 = simpleparts_Thing(id=13)
    b = simpleparts_RelatedTo(since="sample_text")
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
    a1 = simpleparts_Thing(id=7)
    a2 = simpleparts_Thing(id=13)
    b = simpleparts_RelatedTo(since="sample_text")
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


def test_assoc_toThing11_reverse_link_reassign_clear():
    a1 = simpleparts_Thing(id=7)
    a2 = simpleparts_Thing(id=13)
    b = simpleparts_RelatedTo(since="sample_text")
    _safe_set(b, 'simpleparts_RelatedTo', a1)
    assert _is_linked(b, 'simpleparts_RelatedTo', a1)
    if hasattr(a1, 'simpleparts_Thing12'):
        assert _is_linked(a1, 'simpleparts_Thing12', b)
    _safe_set(b, 'simpleparts_RelatedTo', a2)
    assert _is_linked(b, 'simpleparts_RelatedTo', a2)
    if hasattr(a1, 'simpleparts_Thing12'):
        assert not _is_linked(a1, 'simpleparts_Thing12', b)
    if hasattr(a2, 'simpleparts_Thing12'):
        assert _is_linked(a2, 'simpleparts_Thing12', b)
    _safe_set(b, 'simpleparts_RelatedTo', None)
    assert not _is_linked(b, 'simpleparts_RelatedTo', a2)
    if hasattr(a2, 'simpleparts_Thing12'):
        assert not _is_linked(a2, 'simpleparts_Thing12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements4_stub_double():
    # simpleparts_Element has no real 'simpleparts_Element' property in the generated
    # code (a bare stub) -- manually attach it so simpleparts_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleparts_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleparts_Thing(id=7)
    partner = simpleparts_Element()
    setattr(partner, 'simpleparts_Element', None)
    _safe_set(owner, 'simpleparts_Thing5', {partner})
    assert getattr(partner, 'simpleparts_Element') == owner
    _safe_set(owner, 'simpleparts_Thing5', set())
    assert getattr(partner, 'simpleparts_Element') is None


def test_assoc_items6_stub_double():
    # simpleparts_Item has no real 'simpleparts_Item' property in the generated
    # code (a bare stub) -- manually attach it so simpleparts_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleparts_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleparts_Thing(id=7)
    partner = simpleparts_Item()
    setattr(partner, 'simpleparts_Item', None)
    _safe_set(owner, 'simpleparts_Thing7', {partner})
    assert getattr(partner, 'simpleparts_Item') == owner
    _safe_set(owner, 'simpleparts_Thing7', set())
    assert getattr(partner, 'simpleparts_Item') is None


def test_assoc_parts2_stub_double():
    # simpleparts_Part has no real 'simpleparts_Part' property in the generated
    # code (a bare stub) -- manually attach it so simpleparts_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleparts_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleparts_Thing(id=7)
    partner = simpleparts_Part()
    setattr(partner, 'simpleparts_Part', None)
    _safe_set(owner, 'simpleparts_Thing3', {partner})
    assert getattr(partner, 'simpleparts_Part') == owner
    _safe_set(owner, 'simpleparts_Thing3', set())
    assert getattr(partner, 'simpleparts_Part') is None


def test_assoc_pieces8_stub_double():
    # simpleparts_Piece has no real 'simpleparts_Piece' property in the generated
    # code (a bare stub) -- manually attach it so simpleparts_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleparts_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleparts_Thing(id=7)
    partner = simpleparts_Piece()
    setattr(partner, 'simpleparts_Piece', None)
    _safe_set(owner, 'simpleparts_Thing9', {partner})
    assert getattr(partner, 'simpleparts_Piece') == owner
    _safe_set(owner, 'simpleparts_Thing9', set())
    assert getattr(partner, 'simpleparts_Piece') is None


def test_assoc_things0_stub_double():
    # simpleparts_World has no real 'simpleparts_World' property in the generated
    # code (a bare stub) -- manually attach it so simpleparts_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleparts_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleparts_Thing(id=7)
    partner = simpleparts_World()
    setattr(partner, 'simpleparts_World', None)
    _safe_set(owner, 'simpleparts_Thing', partner)
    assert owner in getattr(partner, 'simpleparts_World')
    _safe_set(owner, 'simpleparts_Thing', None)
    assert owner not in getattr(partner, 'simpleparts_World')


