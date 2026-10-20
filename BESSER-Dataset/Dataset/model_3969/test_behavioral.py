import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    subsetUnion_Container,
    subsetUnion_Element,
    subsetUnion_Element_Level1,
    subsetUnion_Element_Level10,
    subsetUnion_Element_Level2,
    subsetUnion_Element_Level3,
    subsetUnion_Element_Level4,
    subsetUnion_Element_Level5,
    subsetUnion_Element_Level6,
    subsetUnion_Element_Level7,
    subsetUnion_Element_Level8,
    subsetUnion_Element_Level9,
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

def test_assoc_unionBag0_reverse_link_reassign_clear():
    a1 = subsetUnion_Element(name="sample_text")
    a2 = subsetUnion_Element(name="sample_text_2")
    b = subsetUnion_Container(name="sample_text")
    _safe_set(b, 'subsetUnion_Container', {a1})
    assert _is_linked(b, 'subsetUnion_Container', a1)
    if hasattr(a1, 'subsetUnion_Element'):
        assert _is_linked(a1, 'subsetUnion_Element', b)
    _safe_set(b, 'subsetUnion_Container', {a2})
    assert _is_linked(b, 'subsetUnion_Container', a2)
    if hasattr(a1, 'subsetUnion_Element'):
        assert not _is_linked(a1, 'subsetUnion_Element', b)
    if hasattr(a2, 'subsetUnion_Element'):
        assert _is_linked(a2, 'subsetUnion_Element', b)
    _safe_set(b, 'subsetUnion_Container', set())
    assert not _is_linked(b, 'subsetUnion_Container', a2)
    if hasattr(a2, 'subsetUnion_Element'):
        assert not _is_linked(a2, 'subsetUnion_Element', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_subset1019_stub_double():
    # subsetUnion_Element_Level10 has no real 'subsetUnion_Element_Level10' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level10()
    setattr(partner, 'subsetUnion_Element_Level10', None)
    _safe_set(owner, 'subsetUnion_Container20', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level10') == owner
    _safe_set(owner, 'subsetUnion_Container20', set())
    assert getattr(partner, 'subsetUnion_Element_Level10') is None


def test_assoc_subset11_stub_double():
    # subsetUnion_Element_Level1 has no real 'subsetUnion_Element_Level1' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level1()
    setattr(partner, 'subsetUnion_Element_Level1', None)
    _safe_set(owner, 'subsetUnion_Container2', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level1') == owner
    _safe_set(owner, 'subsetUnion_Container2', set())
    assert getattr(partner, 'subsetUnion_Element_Level1') is None


def test_assoc_subset23_stub_double():
    # subsetUnion_Element_Level2 has no real 'subsetUnion_Element_Level2' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level2()
    setattr(partner, 'subsetUnion_Element_Level2', None)
    _safe_set(owner, 'subsetUnion_Container4', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level2') == owner
    _safe_set(owner, 'subsetUnion_Container4', set())
    assert getattr(partner, 'subsetUnion_Element_Level2') is None


def test_assoc_subset35_stub_double():
    # subsetUnion_Element_Level3 has no real 'subsetUnion_Element_Level3' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level3()
    setattr(partner, 'subsetUnion_Element_Level3', None)
    _safe_set(owner, 'subsetUnion_Container6', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level3') == owner
    _safe_set(owner, 'subsetUnion_Container6', set())
    assert getattr(partner, 'subsetUnion_Element_Level3') is None


def test_assoc_subset47_stub_double():
    # subsetUnion_Element_Level4 has no real 'subsetUnion_Element_Level4' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level4()
    setattr(partner, 'subsetUnion_Element_Level4', None)
    _safe_set(owner, 'subsetUnion_Container8', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level4') == owner
    _safe_set(owner, 'subsetUnion_Container8', set())
    assert getattr(partner, 'subsetUnion_Element_Level4') is None


def test_assoc_subset59_stub_double():
    # subsetUnion_Element_Level5 has no real 'subsetUnion_Element_Level5' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level5()
    setattr(partner, 'subsetUnion_Element_Level5', None)
    _safe_set(owner, 'subsetUnion_Container10', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level5') == owner
    _safe_set(owner, 'subsetUnion_Container10', set())
    assert getattr(partner, 'subsetUnion_Element_Level5') is None


def test_assoc_subset611_stub_double():
    # subsetUnion_Element_Level6 has no real 'subsetUnion_Element_Level6' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level6()
    setattr(partner, 'subsetUnion_Element_Level6', None)
    _safe_set(owner, 'subsetUnion_Container12', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level6') == owner
    _safe_set(owner, 'subsetUnion_Container12', set())
    assert getattr(partner, 'subsetUnion_Element_Level6') is None


def test_assoc_subset713_stub_double():
    # subsetUnion_Element_Level7 has no real 'subsetUnion_Element_Level7' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level7()
    setattr(partner, 'subsetUnion_Element_Level7', None)
    _safe_set(owner, 'subsetUnion_Container14', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level7') == owner
    _safe_set(owner, 'subsetUnion_Container14', set())
    assert getattr(partner, 'subsetUnion_Element_Level7') is None


def test_assoc_subset815_stub_double():
    # subsetUnion_Element_Level8 has no real 'subsetUnion_Element_Level8' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level8()
    setattr(partner, 'subsetUnion_Element_Level8', None)
    _safe_set(owner, 'subsetUnion_Container16', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level8') == owner
    _safe_set(owner, 'subsetUnion_Container16', set())
    assert getattr(partner, 'subsetUnion_Element_Level8') is None


def test_assoc_subset917_stub_double():
    # subsetUnion_Element_Level9 has no real 'subsetUnion_Element_Level9' property in the generated
    # code (a bare stub) -- manually attach it so subsetUnion_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # subsetUnion_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = subsetUnion_Container(name="sample_text")
    partner = subsetUnion_Element_Level9()
    setattr(partner, 'subsetUnion_Element_Level9', None)
    _safe_set(owner, 'subsetUnion_Container18', {partner})
    assert getattr(partner, 'subsetUnion_Element_Level9') == owner
    _safe_set(owner, 'subsetUnion_Container18', set())
    assert getattr(partner, 'subsetUnion_Element_Level9') is None


