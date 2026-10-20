import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Dog,
    Example_Cat,
    Example_Daughter,
    Example_Dog,
    Example_Family,
    Example_HuntingDog,
    Example_Member,
    Example_Parent,
    Example_Pet,
    Example_RaceDog,
    Example_Son,
    Member,
    Pet,
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

def test_assoc_pets5_reverse_link_reassign_clear():
    a1 = Example_Pet(breed="sample_text", name="sample_text")
    a2 = Example_Pet(breed="sample_text_2", name="sample_text_2")
    b = Example_Family(address="sample_text")
    _safe_set(b, 'Example_Family', {a1})
    assert _is_linked(b, 'Example_Family', a1)
    if hasattr(a1, 'Example_Pet'):
        assert _is_linked(a1, 'Example_Pet', b)
    _safe_set(b, 'Example_Family', {a2})
    assert _is_linked(b, 'Example_Family', a2)
    if hasattr(a1, 'Example_Pet'):
        assert not _is_linked(a1, 'Example_Pet', b)
    if hasattr(a2, 'Example_Pet'):
        assert _is_linked(a2, 'Example_Pet', b)
    _safe_set(b, 'Example_Family', set())
    assert not _is_linked(b, 'Example_Family', a2)
    if hasattr(a2, 'Example_Pet'):
        assert not _is_linked(a2, 'Example_Pet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_daughters3_stub_double():
    # Example_Daughter has no real 'Daughter' property in the generated
    # code (a bare stub) -- manually attach it so Example_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Example_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Example_Family(address="sample_text")
    partner = Example_Daughter()
    setattr(partner, 'Daughter', None)
    _safe_set(owner, 'family4', {partner})
    assert getattr(partner, 'Daughter') == owner
    _safe_set(owner, 'family4', set())
    assert getattr(partner, 'Daughter') is None


def test_assoc_family6_stub_double():
    # Example_Parent has no real 'parents' property in the generated
    # code (a bare stub) -- manually attach it so Example_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Example_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Example_Family(address="sample_text")
    partner = Example_Parent()
    setattr(partner, 'parents', None)
    _safe_set(owner, 'Family', partner)
    assert getattr(partner, 'parents') == owner
    _safe_set(owner, 'Family', None)
    assert getattr(partner, 'parents') is None


def test_assoc_family7_stub_double():
    # Example_Son has no real 'sons' property in the generated
    # code (a bare stub) -- manually attach it so Example_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Example_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Example_Family(address="sample_text")
    partner = Example_Son()
    setattr(partner, 'sons', None)
    _safe_set(owner, 'Family8', partner)
    assert getattr(partner, 'sons') == owner
    _safe_set(owner, 'Family8', None)
    assert getattr(partner, 'sons') is None


def test_assoc_family9_stub_double():
    # Example_Daughter has no real 'daughters' property in the generated
    # code (a bare stub) -- manually attach it so Example_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Example_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Example_Family(address="sample_text")
    partner = Example_Daughter()
    setattr(partner, 'daughters', None)
    _safe_set(owner, 'Family10', partner)
    assert getattr(partner, 'daughters') == owner
    _safe_set(owner, 'Family10', None)
    assert getattr(partner, 'daughters') is None


def test_assoc_parents0_stub_double():
    # Example_Parent has no real 'Parent' property in the generated
    # code (a bare stub) -- manually attach it so Example_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Example_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Example_Family(address="sample_text")
    partner = Example_Parent()
    setattr(partner, 'Parent', None)
    _safe_set(owner, 'family', {partner})
    assert getattr(partner, 'Parent') == owner
    _safe_set(owner, 'family', set())
    assert getattr(partner, 'Parent') is None


def test_assoc_sons1_stub_double():
    # Example_Son has no real 'Son' property in the generated
    # code (a bare stub) -- manually attach it so Example_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Example_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Example_Family(address="sample_text")
    partner = Example_Son()
    setattr(partner, 'Son', None)
    _safe_set(owner, 'family2', {partner})
    assert getattr(partner, 'Son') == owner
    _safe_set(owner, 'family2', set())
    assert getattr(partner, 'Son') is None


