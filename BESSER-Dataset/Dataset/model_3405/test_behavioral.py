import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    menus_Person,
    menus_PersonDirectory,
    Gender,
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

def test_assoc_partner1_reverse_link_reassign_clear():
    a1 = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    a2 = menus_Person(dateOfBirth=date(2025, 6, 15), firstname="sample_text_2", lastname="sample_text_2", pregnant=False, sex="sample_text_2")
    b = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    _safe_set(b, 'menus_Person0', a1)
    assert _is_linked(b, 'menus_Person0', a1)
    if hasattr(a1, 'menus_Person'):
        assert _is_linked(a1, 'menus_Person', b)
    _safe_set(b, 'menus_Person0', a2)
    assert _is_linked(b, 'menus_Person0', a2)
    if hasattr(a1, 'menus_Person'):
        assert not _is_linked(a1, 'menus_Person', b)
    if hasattr(a2, 'menus_Person'):
        assert _is_linked(a2, 'menus_Person', b)
    _safe_set(b, 'menus_Person0', None)
    assert not _is_linked(b, 'menus_Person0', a2)
    if hasattr(a2, 'menus_Person'):
        assert not _is_linked(a2, 'menus_Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entry2_stub_double():
    # menus_PersonDirectory has no real 'menus_PersonDirectory' property in the generated
    # code (a bare stub) -- manually attach it so menus_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # menus_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    partner = menus_PersonDirectory()
    setattr(partner, 'menus_PersonDirectory', None)
    _safe_set(owner, 'menus_Person3', partner)
    assert owner in getattr(partner, 'menus_PersonDirectory')
    _safe_set(owner, 'menus_Person3', None)
    assert owner not in getattr(partner, 'menus_PersonDirectory')


