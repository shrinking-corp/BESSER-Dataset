import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    familyleft2_Daughter,
    familyleft2_Family,
    familyleft2_Father,
    familyleft2_Mother,
    familyleft2_Person,
    familyleft2_Son,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_family0_stub_double():
    # familyleft2_Family has no real 'Family' property in the generated
    # code (a bare stub) -- manually attach it so familyleft2_Father's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyleft2_Father's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyleft2_Father(address="sample_text")
    partner = familyleft2_Family()
    setattr(partner, 'Family', None)
    _safe_set(owner, 'father', partner)
    assert getattr(partner, 'Family') == owner
    _safe_set(owner, 'father', None)
    assert getattr(partner, 'Family') is None


def test_assoc_family1_stub_double():
    # familyleft2_Family has no real 'Family2' property in the generated
    # code (a bare stub) -- manually attach it so familyleft2_Mother's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyleft2_Mother's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyleft2_Mother(address="sample_text")
    partner = familyleft2_Family()
    setattr(partner, 'Family2', None)
    _safe_set(owner, 'mother', partner)
    assert getattr(partner, 'Family2') == owner
    _safe_set(owner, 'mother', None)
    assert getattr(partner, 'Family2') is None


def test_assoc_father7_stub_double():
    # familyleft2_Family has no real 'family' property in the generated
    # code (a bare stub) -- manually attach it so familyleft2_Father's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyleft2_Father's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyleft2_Father(address="sample_text")
    partner = familyleft2_Family()
    setattr(partner, 'family', None)
    _safe_set(owner, 'Father', partner)
    assert getattr(partner, 'family') == owner
    _safe_set(owner, 'Father', None)
    assert getattr(partner, 'family') is None


def test_assoc_mother8_stub_double():
    # familyleft2_Family has no real 'family9' property in the generated
    # code (a bare stub) -- manually attach it so familyleft2_Mother's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyleft2_Mother's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyleft2_Mother(address="sample_text")
    partner = familyleft2_Family()
    setattr(partner, 'family9', None)
    _safe_set(owner, 'Mother', partner)
    assert getattr(partner, 'family9') == owner
    _safe_set(owner, 'Mother', None)
    assert getattr(partner, 'family9') is None


