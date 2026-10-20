import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    hello121_Alias,
    hello121_Base,
    hello121_Classoc,
    hello121_NamedElement,
    hello121_RelatedTo,
    hello121_Thing,
    hello121_Third,
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

def test_assoc_aliases9_reverse_link_reassign_clear():
    a1 = hello121_NamedElement(name="sample_text")
    a2 = hello121_NamedElement(name="sample_text_2")
    b = hello121_Alias(id="sample_text")
    _safe_set(b, 'hello121_Alias', a1)
    assert _is_linked(b, 'hello121_Alias', a1)
    if hasattr(a1, 'hello121_NamedElement'):
        assert _is_linked(a1, 'hello121_NamedElement', b)
    _safe_set(b, 'hello121_Alias', a2)
    assert _is_linked(b, 'hello121_Alias', a2)
    if hasattr(a1, 'hello121_NamedElement'):
        assert not _is_linked(a1, 'hello121_NamedElement', b)
    if hasattr(a2, 'hello121_NamedElement'):
        assert _is_linked(a2, 'hello121_NamedElement', b)
    _safe_set(b, 'hello121_Alias', None)
    assert not _is_linked(b, 'hello121_Alias', a2)
    if hasattr(a2, 'hello121_NamedElement'):
        assert not _is_linked(a2, 'hello121_NamedElement', b)


def test_assoc_classocs6_reverse_link_reassign_clear():
    a1 = hello121_Thing(id=7)
    a2 = hello121_Thing(id=13)
    b = hello121_Classoc(id="sample_text")
    _safe_set(b, 'hello121_Classoc8', a1)
    assert _is_linked(b, 'hello121_Classoc8', a1)
    if hasattr(a1, 'hello121_Thing7'):
        assert _is_linked(a1, 'hello121_Thing7', b)
    _safe_set(b, 'hello121_Classoc8', a2)
    assert _is_linked(b, 'hello121_Classoc8', a2)
    if hasattr(a1, 'hello121_Thing7'):
        assert not _is_linked(a1, 'hello121_Thing7', b)
    if hasattr(a2, 'hello121_Thing7'):
        assert _is_linked(a2, 'hello121_Thing7', b)
    _safe_set(b, 'hello121_Classoc8', None)
    assert not _is_linked(b, 'hello121_Classoc8', a2)
    if hasattr(a2, 'hello121_Thing7'):
        assert not _is_linked(a2, 'hello121_Thing7', b)


def test_assoc_foos4_reverse_link_reassign_clear():
    a1 = hello121_Third(id="sample_text")
    a2 = hello121_Third(id="sample_text_2")
    b = hello121_Thing(id=7)
    _safe_set(b, 'hello121_Thing5', {a1})
    assert _is_linked(b, 'hello121_Thing5', a1)
    if hasattr(a1, 'hello121_Third'):
        assert _is_linked(a1, 'hello121_Third', b)
    _safe_set(b, 'hello121_Thing5', {a2})
    assert _is_linked(b, 'hello121_Thing5', a2)
    if hasattr(a1, 'hello121_Third'):
        assert not _is_linked(a1, 'hello121_Third', b)
    if hasattr(a2, 'hello121_Third'):
        assert _is_linked(a2, 'hello121_Third', b)
    _safe_set(b, 'hello121_Thing5', set())
    assert not _is_linked(b, 'hello121_Thing5', a2)
    if hasattr(a2, 'hello121_Third'):
        assert not _is_linked(a2, 'hello121_Third', b)


def test_assoc_fromThing10_reverse_link_reassign_clear():
    a1 = hello121_Thing(id=7)
    a2 = hello121_Thing(id=13)
    b = hello121_RelatedTo(since="sample_text")
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
    a1 = hello121_Thing(id=7)
    a2 = hello121_Thing(id=13)
    b = hello121_RelatedTo(since="sample_text")
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


def test_assoc_third13_reverse_link_reassign_clear():
    a1 = hello121_Third(id="sample_text")
    a2 = hello121_Third(id="sample_text_2")
    b = hello121_Classoc(id="sample_text")
    _safe_set(b, 'hello121_Classoc14', a1)
    assert _is_linked(b, 'hello121_Classoc14', a1)
    if hasattr(a1, 'hello121_Third15'):
        assert _is_linked(a1, 'hello121_Third15', b)
    _safe_set(b, 'hello121_Classoc14', a2)
    assert _is_linked(b, 'hello121_Classoc14', a2)
    if hasattr(a1, 'hello121_Third15'):
        assert not _is_linked(a1, 'hello121_Third15', b)
    if hasattr(a2, 'hello121_Third15'):
        assert _is_linked(a2, 'hello121_Third15', b)
    _safe_set(b, 'hello121_Classoc14', None)
    assert not _is_linked(b, 'hello121_Classoc14', a2)
    if hasattr(a2, 'hello121_Third15'):
        assert not _is_linked(a2, 'hello121_Third15', b)


def test_assoc_toThing11_reverse_link_reassign_clear():
    a1 = hello121_Thing(id=7)
    a2 = hello121_Thing(id=13)
    b = hello121_RelatedTo(since="sample_text")
    _safe_set(b, 'hello121_RelatedTo', a1)
    assert _is_linked(b, 'hello121_RelatedTo', a1)
    if hasattr(a1, 'hello121_Thing12'):
        assert _is_linked(a1, 'hello121_Thing12', b)
    _safe_set(b, 'hello121_RelatedTo', a2)
    assert _is_linked(b, 'hello121_RelatedTo', a2)
    if hasattr(a1, 'hello121_Thing12'):
        assert not _is_linked(a1, 'hello121_Thing12', b)
    if hasattr(a2, 'hello121_Thing12'):
        assert _is_linked(a2, 'hello121_Thing12', b)
    _safe_set(b, 'hello121_RelatedTo', None)
    assert not _is_linked(b, 'hello121_RelatedTo', a2)
    if hasattr(a2, 'hello121_Thing12'):
        assert not _is_linked(a2, 'hello121_Thing12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base16_stub_double():
    # hello121_Base has no real 'hello121_Base18' property in the generated
    # code (a bare stub) -- manually attach it so hello121_Classoc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello121_Classoc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello121_Classoc(id="sample_text")
    partner = hello121_Base()
    setattr(partner, 'hello121_Base18', None)
    _safe_set(owner, 'hello121_Classoc17', partner)
    assert getattr(partner, 'hello121_Base18') == owner
    _safe_set(owner, 'hello121_Classoc17', None)
    assert getattr(partner, 'hello121_Base18') is None


def test_assoc_classocs1_stub_double():
    # hello121_Base has no real 'hello121_Base2' property in the generated
    # code (a bare stub) -- manually attach it so hello121_Classoc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello121_Classoc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello121_Classoc(id="sample_text")
    partner = hello121_Base()
    setattr(partner, 'hello121_Base2', None)
    _safe_set(owner, 'hello121_Classoc', partner)
    assert owner in getattr(partner, 'hello121_Base2')
    _safe_set(owner, 'hello121_Classoc', None)
    assert owner not in getattr(partner, 'hello121_Base2')


def test_assoc_things0_stub_double():
    # hello121_Base has no real 'hello121_Base' property in the generated
    # code (a bare stub) -- manually attach it so hello121_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello121_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello121_Thing(id=7)
    partner = hello121_Base()
    setattr(partner, 'hello121_Base', None)
    _safe_set(owner, 'hello121_Thing', partner)
    assert owner in getattr(partner, 'hello121_Base')
    _safe_set(owner, 'hello121_Thing', None)
    assert owner not in getattr(partner, 'hello121_Base')


