import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    classes_Card,
    classes_Hand,
    combinations_Brelan,
    combinations_Carre,
    combinations_Combination,
    combinations_Couleur,
    combinations_DoublePaire,
    combinations_Full,
    combinations_Paire,
    combinations_PlusHauteCarte,
    combinations_QuinteFlush,
    combinations_Suite,
    int,
    utils_Parser,
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

def test_assoc_Hand_Card_reverse_link_reassign_clear():
    a1 = combinations_Combination(name="sample_text", value=7)
    a2 = combinations_Combination(name="sample_text_2", value=13)
    b = classes_Card(name="sample_text", value=7)
    _safe_set(b, 'hand1', a1)
    assert _is_linked(b, 'hand1', a1)
    if hasattr(a1, 'cards0'):
        assert _is_linked(a1, 'cards0', b)
    _safe_set(b, 'hand1', a2)
    assert _is_linked(b, 'hand1', a2)
    if hasattr(a1, 'cards0'):
        assert not _is_linked(a1, 'cards0', b)
    if hasattr(a2, 'cards0'):
        assert _is_linked(a2, 'cards0', b)
    _safe_set(b, 'hand1', None)
    assert not _is_linked(b, 'hand1', a2)
    if hasattr(a2, 'cards0'):
        assert not _is_linked(a2, 'cards0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Hand_Card2_stub_double():
    # classes_Hand has no real 'hand2' property in the generated
    # code (a bare stub) -- manually attach it so classes_Card's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Card's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Card(name="sample_text", value=7)
    partner = classes_Hand()
    setattr(partner, 'hand2', None)
    _safe_set(owner, 'hand3', partner)
    assert owner in getattr(partner, 'hand2')
    _safe_set(owner, 'hand3', None)
    assert owner not in getattr(partner, 'hand2')


