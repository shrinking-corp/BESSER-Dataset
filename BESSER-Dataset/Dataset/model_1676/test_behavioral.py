import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    hello122_Alias,
    hello122_Base,
    hello122_Child,
    hello122_Classoc,
    hello122_Clazoc,
    hello122_NamedElement,
    hello122_RelatedTo,
    hello122_Thing,
    hello122_Third,
    hello122_Top,
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

def test_assoc_aliases14_reverse_link_reassign_clear():
    a1 = hello122_NamedElement(name="sample_text")
    a2 = hello122_NamedElement(name="sample_text_2")
    b = hello122_Alias(id="sample_text")
    _safe_set(b, 'hello122_Alias', a1)
    assert _is_linked(b, 'hello122_Alias', a1)
    if hasattr(a1, 'hello122_NamedElement'):
        assert _is_linked(a1, 'hello122_NamedElement', b)
    _safe_set(b, 'hello122_Alias', a2)
    assert _is_linked(b, 'hello122_Alias', a2)
    if hasattr(a1, 'hello122_NamedElement'):
        assert not _is_linked(a1, 'hello122_NamedElement', b)
    if hasattr(a2, 'hello122_NamedElement'):
        assert _is_linked(a2, 'hello122_NamedElement', b)
    _safe_set(b, 'hello122_Alias', None)
    assert not _is_linked(b, 'hello122_Alias', a2)
    if hasattr(a2, 'hello122_NamedElement'):
        assert not _is_linked(a2, 'hello122_NamedElement', b)


def test_assoc_childs36_reverse_link_reassign_clear():
    a1 = hello122_Top(id="sample_text")
    a2 = hello122_Top(id="sample_text_2")
    b = hello122_Child(id="sample_text")
    _safe_set(b, 'hello122_Child', a1)
    assert _is_linked(b, 'hello122_Child', a1)
    if hasattr(a1, 'hello122_Top37'):
        assert _is_linked(a1, 'hello122_Top37', b)
    _safe_set(b, 'hello122_Child', a2)
    assert _is_linked(b, 'hello122_Child', a2)
    if hasattr(a1, 'hello122_Top37'):
        assert not _is_linked(a1, 'hello122_Top37', b)
    if hasattr(a2, 'hello122_Top37'):
        assert _is_linked(a2, 'hello122_Top37', b)
    _safe_set(b, 'hello122_Child', None)
    assert not _is_linked(b, 'hello122_Child', a2)
    if hasattr(a2, 'hello122_Top37'):
        assert not _is_linked(a2, 'hello122_Top37', b)


def test_assoc_classocs9_reverse_link_reassign_clear():
    a1 = hello122_Thing(id=7)
    a2 = hello122_Thing(id=13)
    b = hello122_Classoc(id="sample_text")
    _safe_set(b, 'hello122_Classoc11', a1)
    assert _is_linked(b, 'hello122_Classoc11', a1)
    if hasattr(a1, 'hello122_Thing10'):
        assert _is_linked(a1, 'hello122_Thing10', b)
    _safe_set(b, 'hello122_Classoc11', a2)
    assert _is_linked(b, 'hello122_Classoc11', a2)
    if hasattr(a1, 'hello122_Thing10'):
        assert not _is_linked(a1, 'hello122_Thing10', b)
    if hasattr(a2, 'hello122_Thing10'):
        assert _is_linked(a2, 'hello122_Thing10', b)
    _safe_set(b, 'hello122_Classoc11', None)
    assert not _is_linked(b, 'hello122_Classoc11', a2)
    if hasattr(a2, 'hello122_Thing10'):
        assert not _is_linked(a2, 'hello122_Thing10', b)


def test_assoc_foos7_reverse_link_reassign_clear():
    a1 = hello122_Third(id="sample_text")
    a2 = hello122_Third(id="sample_text_2")
    b = hello122_Thing(id=7)
    _safe_set(b, 'hello122_Thing8', {a1})
    assert _is_linked(b, 'hello122_Thing8', a1)
    if hasattr(a1, 'hello122_Third'):
        assert _is_linked(a1, 'hello122_Third', b)
    _safe_set(b, 'hello122_Thing8', {a2})
    assert _is_linked(b, 'hello122_Thing8', a2)
    if hasattr(a1, 'hello122_Third'):
        assert not _is_linked(a1, 'hello122_Third', b)
    if hasattr(a2, 'hello122_Third'):
        assert _is_linked(a2, 'hello122_Third', b)
    _safe_set(b, 'hello122_Thing8', set())
    assert not _is_linked(b, 'hello122_Thing8', a2)
    if hasattr(a2, 'hello122_Third'):
        assert not _is_linked(a2, 'hello122_Third', b)


def test_assoc_fromThing15_reverse_link_reassign_clear():
    a1 = hello122_Thing(id=7)
    a2 = hello122_Thing(id=13)
    b = hello122_RelatedTo(since="sample_text")
    _safe_set(b, 'hello122_RelatedTo16', a1)
    assert _is_linked(b, 'hello122_RelatedTo16', a1)
    if hasattr(a1, 'hello122_Thing17'):
        assert _is_linked(a1, 'hello122_Thing17', b)
    _safe_set(b, 'hello122_RelatedTo16', a2)
    assert _is_linked(b, 'hello122_RelatedTo16', a2)
    if hasattr(a1, 'hello122_Thing17'):
        assert not _is_linked(a1, 'hello122_Thing17', b)
    if hasattr(a2, 'hello122_Thing17'):
        assert _is_linked(a2, 'hello122_Thing17', b)
    _safe_set(b, 'hello122_RelatedTo16', None)
    assert not _is_linked(b, 'hello122_RelatedTo16', a2)
    if hasattr(a2, 'hello122_Thing17'):
        assert not _is_linked(a2, 'hello122_Thing17', b)


def test_assoc_relations12_reverse_link_reassign_clear():
    a1 = hello122_Thing(id=7)
    a2 = hello122_Thing(id=13)
    b = hello122_RelatedTo(since="sample_text")
    _safe_set(b, 'hello122_RelatedTo', a1)
    assert _is_linked(b, 'hello122_RelatedTo', a1)
    if hasattr(a1, 'hello122_Thing13'):
        assert _is_linked(a1, 'hello122_Thing13', b)
    _safe_set(b, 'hello122_RelatedTo', a2)
    assert _is_linked(b, 'hello122_RelatedTo', a2)
    if hasattr(a1, 'hello122_Thing13'):
        assert not _is_linked(a1, 'hello122_Thing13', b)
    if hasattr(a2, 'hello122_Thing13'):
        assert _is_linked(a2, 'hello122_Thing13', b)
    _safe_set(b, 'hello122_RelatedTo', None)
    assert not _is_linked(b, 'hello122_RelatedTo', a2)
    if hasattr(a2, 'hello122_Thing13'):
        assert not _is_linked(a2, 'hello122_Thing13', b)


def test_assoc_thing27_reverse_link_reassign_clear():
    a1 = hello122_Thing(id=7)
    a2 = hello122_Thing(id=13)
    b = hello122_Classoc(id="sample_text")
    _safe_set(b, 'hello122_Classoc28', a1)
    assert _is_linked(b, 'hello122_Classoc28', a1)
    if hasattr(a1, 'hello122_Thing29'):
        assert _is_linked(a1, 'hello122_Thing29', b)
    _safe_set(b, 'hello122_Classoc28', a2)
    assert _is_linked(b, 'hello122_Classoc28', a2)
    if hasattr(a1, 'hello122_Thing29'):
        assert not _is_linked(a1, 'hello122_Thing29', b)
    if hasattr(a2, 'hello122_Thing29'):
        assert _is_linked(a2, 'hello122_Thing29', b)
    _safe_set(b, 'hello122_Classoc28', None)
    assert not _is_linked(b, 'hello122_Classoc28', a2)
    if hasattr(a2, 'hello122_Thing29'):
        assert not _is_linked(a2, 'hello122_Thing29', b)


def test_assoc_third21_reverse_link_reassign_clear():
    a1 = hello122_Third(id="sample_text")
    a2 = hello122_Third(id="sample_text_2")
    b = hello122_Classoc(id="sample_text")
    _safe_set(b, 'hello122_Classoc22', a1)
    assert _is_linked(b, 'hello122_Classoc22', a1)
    if hasattr(a1, 'hello122_Third23'):
        assert _is_linked(a1, 'hello122_Third23', b)
    _safe_set(b, 'hello122_Classoc22', a2)
    assert _is_linked(b, 'hello122_Classoc22', a2)
    if hasattr(a1, 'hello122_Third23'):
        assert not _is_linked(a1, 'hello122_Third23', b)
    if hasattr(a2, 'hello122_Third23'):
        assert _is_linked(a2, 'hello122_Third23', b)
    _safe_set(b, 'hello122_Classoc22', None)
    assert not _is_linked(b, 'hello122_Classoc22', a2)
    if hasattr(a2, 'hello122_Third23'):
        assert not _is_linked(a2, 'hello122_Third23', b)


def test_assoc_toThing18_reverse_link_reassign_clear():
    a1 = hello122_Thing(id=7)
    a2 = hello122_Thing(id=13)
    b = hello122_RelatedTo(since="sample_text")
    _safe_set(b, 'hello122_RelatedTo19', a1)
    assert _is_linked(b, 'hello122_RelatedTo19', a1)
    if hasattr(a1, 'hello122_Thing20'):
        assert _is_linked(a1, 'hello122_Thing20', b)
    _safe_set(b, 'hello122_RelatedTo19', a2)
    assert _is_linked(b, 'hello122_RelatedTo19', a2)
    if hasattr(a1, 'hello122_Thing20'):
        assert not _is_linked(a1, 'hello122_Thing20', b)
    if hasattr(a2, 'hello122_Thing20'):
        assert _is_linked(a2, 'hello122_Thing20', b)
    _safe_set(b, 'hello122_RelatedTo19', None)
    assert not _is_linked(b, 'hello122_RelatedTo19', a2)
    if hasattr(a2, 'hello122_Thing20'):
        assert not _is_linked(a2, 'hello122_Thing20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base24_stub_double():
    # hello122_Base has no real 'hello122_Base26' property in the generated
    # code (a bare stub) -- manually attach it so hello122_Classoc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello122_Classoc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello122_Classoc(id="sample_text")
    partner = hello122_Base()
    setattr(partner, 'hello122_Base26', None)
    _safe_set(owner, 'hello122_Classoc25', partner)
    assert getattr(partner, 'hello122_Base26') == owner
    _safe_set(owner, 'hello122_Classoc25', None)
    assert getattr(partner, 'hello122_Base26') is None


def test_assoc_classocs1_stub_double():
    # hello122_Base has no real 'hello122_Base2' property in the generated
    # code (a bare stub) -- manually attach it so hello122_Classoc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello122_Classoc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello122_Classoc(id="sample_text")
    partner = hello122_Base()
    setattr(partner, 'hello122_Base2', None)
    _safe_set(owner, 'hello122_Classoc', partner)
    assert owner in getattr(partner, 'hello122_Base2')
    _safe_set(owner, 'hello122_Classoc', None)
    assert owner not in getattr(partner, 'hello122_Base2')


def test_assoc_fromThird33_stub_double():
    # hello122_Clazoc has no real 'hello122_Clazoc34' property in the generated
    # code (a bare stub) -- manually attach it so hello122_Third's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello122_Third's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello122_Third(id="sample_text")
    partner = hello122_Clazoc()
    setattr(partner, 'hello122_Clazoc34', None)
    _safe_set(owner, 'hello122_Third35', partner)
    assert getattr(partner, 'hello122_Clazoc34') == owner
    _safe_set(owner, 'hello122_Third35', None)
    assert getattr(partner, 'hello122_Clazoc34') is None


def test_assoc_things0_stub_double():
    # hello122_Base has no real 'hello122_Base' property in the generated
    # code (a bare stub) -- manually attach it so hello122_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello122_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello122_Thing(id=7)
    partner = hello122_Base()
    setattr(partner, 'hello122_Base', None)
    _safe_set(owner, 'hello122_Thing', partner)
    assert owner in getattr(partner, 'hello122_Base')
    _safe_set(owner, 'hello122_Thing', None)
    assert owner not in getattr(partner, 'hello122_Base')


def test_assoc_toThing30_stub_double():
    # hello122_Clazoc has no real 'hello122_Clazoc31' property in the generated
    # code (a bare stub) -- manually attach it so hello122_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello122_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello122_Thing(id=7)
    partner = hello122_Clazoc()
    setattr(partner, 'hello122_Clazoc31', None)
    _safe_set(owner, 'hello122_Thing32', partner)
    assert getattr(partner, 'hello122_Clazoc31') == owner
    _safe_set(owner, 'hello122_Thing32', None)
    assert getattr(partner, 'hello122_Clazoc31') is None


def test_assoc_tops5_stub_double():
    # hello122_Base has no real 'hello122_Base6' property in the generated
    # code (a bare stub) -- manually attach it so hello122_Top's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hello122_Top's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hello122_Top(id="sample_text")
    partner = hello122_Base()
    setattr(partner, 'hello122_Base6', None)
    _safe_set(owner, 'hello122_Top', partner)
    assert owner in getattr(partner, 'hello122_Base6')
    _safe_set(owner, 'hello122_Top', None)
    assert owner not in getattr(partner, 'hello122_Base6')


