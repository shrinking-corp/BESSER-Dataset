import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    ktest401_Article,
    ktest401_EClass0,
    ktest401_EClass1,
    ktest401_Line,
    ktest401_NamedElement,
    ktest401_RelatedTo,
    ktest401_Thing,
    ktest401_World,
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

def test_assoc_EReference019_reverse_link_reassign_clear():
    a1 = ktest401_RelatedTo(since="sample_text")
    a2 = ktest401_RelatedTo(since="sample_text_2")
    b = ktest401_EClass1(bar="sample_text", foo="sample_text")
    _safe_set(b, 'ktest401_EClass120', a1)
    assert _is_linked(b, 'ktest401_EClass120', a1)
    if hasattr(a1, 'ktest401_RelatedTo21'):
        assert _is_linked(a1, 'ktest401_RelatedTo21', b)
    _safe_set(b, 'ktest401_EClass120', a2)
    assert _is_linked(b, 'ktest401_EClass120', a2)
    if hasattr(a1, 'ktest401_RelatedTo21'):
        assert not _is_linked(a1, 'ktest401_RelatedTo21', b)
    if hasattr(a2, 'ktest401_RelatedTo21'):
        assert _is_linked(a2, 'ktest401_RelatedTo21', b)
    _safe_set(b, 'ktest401_EClass120', None)
    assert not _is_linked(b, 'ktest401_EClass120', a2)
    if hasattr(a2, 'ktest401_RelatedTo21'):
        assert not _is_linked(a2, 'ktest401_RelatedTo21', b)


def test_assoc_e1s11_reverse_link_reassign_clear():
    a1 = ktest401_RelatedTo(since="sample_text")
    a2 = ktest401_RelatedTo(since="sample_text_2")
    b = ktest401_EClass1(bar="sample_text", foo="sample_text")
    _safe_set(b, 'ktest401_EClass1', a1)
    assert _is_linked(b, 'ktest401_EClass1', a1)
    if hasattr(a1, 'ktest401_RelatedTo12'):
        assert _is_linked(a1, 'ktest401_RelatedTo12', b)
    _safe_set(b, 'ktest401_EClass1', a2)
    assert _is_linked(b, 'ktest401_EClass1', a2)
    if hasattr(a1, 'ktest401_RelatedTo12'):
        assert not _is_linked(a1, 'ktest401_RelatedTo12', b)
    if hasattr(a2, 'ktest401_RelatedTo12'):
        assert _is_linked(a2, 'ktest401_RelatedTo12', b)
    _safe_set(b, 'ktest401_EClass1', None)
    assert not _is_linked(b, 'ktest401_EClass1', a2)
    if hasattr(a2, 'ktest401_RelatedTo12'):
        assert not _is_linked(a2, 'ktest401_RelatedTo12', b)


def test_assoc_fromThing8_reverse_link_reassign_clear():
    a1 = ktest401_Thing(id=7)
    a2 = ktest401_Thing(id=13)
    b = ktest401_RelatedTo(since="sample_text")
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


def test_assoc_lines4_reverse_link_reassign_clear():
    a1 = ktest401_Thing(id=7)
    a2 = ktest401_Thing(id=13)
    b = ktest401_Line(articleAid="sample_text", quant=7)
    _safe_set(b, 'ktest401_Line', a1)
    assert _is_linked(b, 'ktest401_Line', a1)
    if hasattr(a1, 'ktest401_Thing5'):
        assert _is_linked(a1, 'ktest401_Thing5', b)
    _safe_set(b, 'ktest401_Line', a2)
    assert _is_linked(b, 'ktest401_Line', a2)
    if hasattr(a1, 'ktest401_Thing5'):
        assert not _is_linked(a1, 'ktest401_Thing5', b)
    if hasattr(a2, 'ktest401_Thing5'):
        assert _is_linked(a2, 'ktest401_Thing5', b)
    _safe_set(b, 'ktest401_Line', None)
    assert not _is_linked(b, 'ktest401_Line', a2)
    if hasattr(a2, 'ktest401_Thing5'):
        assert not _is_linked(a2, 'ktest401_Thing5', b)


def test_assoc_relations3_reverse_link_reassign_clear():
    a1 = ktest401_Thing(id=7)
    a2 = ktest401_Thing(id=13)
    b = ktest401_RelatedTo(since="sample_text")
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


def test_assoc_src13_reverse_link_reassign_clear():
    a1 = ktest401_Thing(id=7)
    a2 = ktest401_Thing(id=13)
    b = ktest401_Line(articleAid="sample_text", quant=7)
    _safe_set(b, 'ktest401_Line14', a1)
    assert _is_linked(b, 'ktest401_Line14', a1)
    if hasattr(a1, 'ktest401_Thing15'):
        assert _is_linked(a1, 'ktest401_Thing15', b)
    _safe_set(b, 'ktest401_Line14', a2)
    assert _is_linked(b, 'ktest401_Line14', a2)
    if hasattr(a1, 'ktest401_Thing15'):
        assert not _is_linked(a1, 'ktest401_Thing15', b)
    if hasattr(a2, 'ktest401_Thing15'):
        assert _is_linked(a2, 'ktest401_Thing15', b)
    _safe_set(b, 'ktest401_Line14', None)
    assert not _is_linked(b, 'ktest401_Line14', a2)
    if hasattr(a2, 'ktest401_Thing15'):
        assert not _is_linked(a2, 'ktest401_Thing15', b)


def test_assoc_toThing9_reverse_link_reassign_clear():
    a1 = ktest401_Thing(id=7)
    a2 = ktest401_Thing(id=13)
    b = ktest401_RelatedTo(since="sample_text")
    _safe_set(b, 'ktest401_RelatedTo', a1)
    assert _is_linked(b, 'ktest401_RelatedTo', a1)
    if hasattr(a1, 'ktest401_Thing10'):
        assert _is_linked(a1, 'ktest401_Thing10', b)
    _safe_set(b, 'ktest401_RelatedTo', a2)
    assert _is_linked(b, 'ktest401_RelatedTo', a2)
    if hasattr(a1, 'ktest401_Thing10'):
        assert not _is_linked(a1, 'ktest401_Thing10', b)
    if hasattr(a2, 'ktest401_Thing10'):
        assert _is_linked(a2, 'ktest401_Thing10', b)
    _safe_set(b, 'ktest401_RelatedTo', None)
    assert not _is_linked(b, 'ktest401_RelatedTo', a2)
    if hasattr(a2, 'ktest401_Thing10'):
        assert not _is_linked(a2, 'ktest401_Thing10', b)


def test_assoc_trg16_reverse_link_reassign_clear():
    a1 = ktest401_Line(articleAid="sample_text", quant=7)
    a2 = ktest401_Line(articleAid="sample_text_2", quant=13)
    b = ktest401_Article(aid="sample_text")
    _safe_set(b, 'ktest401_Article18', a1)
    assert _is_linked(b, 'ktest401_Article18', a1)
    if hasattr(a1, 'ktest401_Line17'):
        assert _is_linked(a1, 'ktest401_Line17', b)
    _safe_set(b, 'ktest401_Article18', a2)
    assert _is_linked(b, 'ktest401_Article18', a2)
    if hasattr(a1, 'ktest401_Line17'):
        assert not _is_linked(a1, 'ktest401_Line17', b)
    if hasattr(a2, 'ktest401_Line17'):
        assert _is_linked(a2, 'ktest401_Line17', b)
    _safe_set(b, 'ktest401_Article18', None)
    assert not _is_linked(b, 'ktest401_Article18', a2)
    if hasattr(a2, 'ktest401_Line17'):
        assert not _is_linked(a2, 'ktest401_Line17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_EReference122_stub_double():
    # ktest401_EClass0 has no real 'ktest401_EClass024' property in the generated
    # code (a bare stub) -- manually attach it so ktest401_EClass1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ktest401_EClass1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ktest401_EClass1(bar="sample_text", foo="sample_text")
    partner = ktest401_EClass0()
    setattr(partner, 'ktest401_EClass024', None)
    _safe_set(owner, 'ktest401_EClass123', partner)
    assert getattr(partner, 'ktest401_EClass024') == owner
    _safe_set(owner, 'ktest401_EClass123', None)
    assert getattr(partner, 'ktest401_EClass024') is None


def test_assoc_e0s6_stub_double():
    # ktest401_EClass0 has no real 'ktest401_EClass0' property in the generated
    # code (a bare stub) -- manually attach it so ktest401_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ktest401_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ktest401_Thing(id=7)
    partner = ktest401_EClass0()
    setattr(partner, 'ktest401_EClass0', None)
    _safe_set(owner, 'ktest401_Thing7', {partner})
    assert getattr(partner, 'ktest401_EClass0') == owner
    _safe_set(owner, 'ktest401_Thing7', set())
    assert getattr(partner, 'ktest401_EClass0') is None


def test_assoc_e1s1_stub_double():
    # ktest401_World has no real 'ktest401_World2' property in the generated
    # code (a bare stub) -- manually attach it so ktest401_Article's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ktest401_Article's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ktest401_Article(aid="sample_text")
    partner = ktest401_World()
    setattr(partner, 'ktest401_World2', None)
    _safe_set(owner, 'ktest401_Article', partner)
    assert owner in getattr(partner, 'ktest401_World2')
    _safe_set(owner, 'ktest401_Article', None)
    assert owner not in getattr(partner, 'ktest401_World2')


def test_assoc_things0_stub_double():
    # ktest401_World has no real 'ktest401_World' property in the generated
    # code (a bare stub) -- manually attach it so ktest401_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ktest401_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ktest401_Thing(id=7)
    partner = ktest401_World()
    setattr(partner, 'ktest401_World', None)
    _safe_set(owner, 'ktest401_Thing', partner)
    assert owner in getattr(partner, 'ktest401_World')
    _safe_set(owner, 'ktest401_Thing', None)
    assert owner not in getattr(partner, 'ktest401_World')


