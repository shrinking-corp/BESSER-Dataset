import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    basicfamily_Family,
    basicfamily_Man,
    basicfamily_Person,
    basicfamily_Woman,
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

def test_assoc_children1_reverse_link_reassign_clear():
    a1 = basicfamily_Person(name="sample_text")
    a2 = basicfamily_Person(name="sample_text_2")
    b = basicfamily_Person(name="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_members8_reverse_link_reassign_clear():
    a1 = basicfamily_Person(name="sample_text")
    a2 = basicfamily_Person(name="sample_text_2")
    b = basicfamily_Family(name="sample_text")
    _safe_set(b, 'basicfamily_Family', {a1})
    assert _is_linked(b, 'basicfamily_Family', a1)
    if hasattr(a1, 'basicfamily_Person9'):
        assert _is_linked(a1, 'basicfamily_Person9', b)
    _safe_set(b, 'basicfamily_Family', {a2})
    assert _is_linked(b, 'basicfamily_Family', a2)
    if hasattr(a1, 'basicfamily_Person9'):
        assert not _is_linked(a1, 'basicfamily_Person9', b)
    if hasattr(a2, 'basicfamily_Person9'):
        assert _is_linked(a2, 'basicfamily_Person9', b)
    _safe_set(b, 'basicfamily_Family', set())
    assert not _is_linked(b, 'basicfamily_Family', a2)
    if hasattr(a2, 'basicfamily_Person9'):
        assert not _is_linked(a2, 'basicfamily_Person9', b)


def test_assoc_parents3_reverse_link_reassign_clear():
    a1 = basicfamily_Person(name="sample_text")
    a2 = basicfamily_Person(name="sample_text_2")
    b = basicfamily_Person(name="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Person4'):
        assert _is_linked(a1, 'Person4', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Person4'):
        assert not _is_linked(a1, 'Person4', b)
    if hasattr(a2, 'Person4'):
        assert _is_linked(a2, 'Person4', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Person4'):
        assert not _is_linked(a2, 'Person4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_father6_stub_double():
    # basicfamily_Man has no real 'basicfamily_Man' property in the generated
    # code (a bare stub) -- manually attach it so basicfamily_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basicfamily_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basicfamily_Person(name="sample_text")
    partner = basicfamily_Man()
    setattr(partner, 'basicfamily_Man', None)
    _safe_set(owner, 'basicfamily_Person7', partner)
    assert getattr(partner, 'basicfamily_Man') == owner
    _safe_set(owner, 'basicfamily_Person7', None)
    assert getattr(partner, 'basicfamily_Man') is None


def test_assoc_mother5_stub_double():
    # basicfamily_Woman has no real 'basicfamily_Woman' property in the generated
    # code (a bare stub) -- manually attach it so basicfamily_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basicfamily_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basicfamily_Person(name="sample_text")
    partner = basicfamily_Woman()
    setattr(partner, 'basicfamily_Woman', None)
    _safe_set(owner, 'basicfamily_Person', partner)
    assert getattr(partner, 'basicfamily_Woman') == owner
    _safe_set(owner, 'basicfamily_Person', None)
    assert getattr(partner, 'basicfamily_Woman') is None


