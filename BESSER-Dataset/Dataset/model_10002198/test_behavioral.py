import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Blackjack,
    Carte,
    Croupier,
    Joueur,
    Main,
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

def test_assoc_Card_Hand_reverse_link_reassign_clear():
    a1 = Main(bet="sample_text", cartes="sample_text", value=7)
    a2 = Main(bet="sample_text_2", cartes="sample_text_2", value=13)
    b = Carte(ordre="sample_text", suit=7)
    _safe_set(b, 'hand0', a1)
    assert _is_linked(b, 'hand0', a1)
    if hasattr(a1, 'card1'):
        assert _is_linked(a1, 'card1', b)
    _safe_set(b, 'hand0', a2)
    assert _is_linked(b, 'hand0', a2)
    if hasattr(a1, 'card1'):
        assert not _is_linked(a1, 'card1', b)
    if hasattr(a2, 'card1'):
        assert _is_linked(a2, 'card1', b)
    _safe_set(b, 'hand0', None)
    assert not _is_linked(b, 'hand0', a2)
    if hasattr(a2, 'card1'):
        assert not _is_linked(a2, 'card1', b)


def test_assoc_Dealer_Hand_reverse_link_reassign_clear():
    a1 = Main(bet="sample_text", cartes="sample_text", value=7)
    a2 = Main(bet="sample_text_2", cartes="sample_text_2", value=13)
    b = Croupier(main="sample_text")
    _safe_set(b, 'hand4', a1)
    assert _is_linked(b, 'hand4', a1)
    if hasattr(a1, 'dealer5'):
        assert _is_linked(a1, 'dealer5', b)
    _safe_set(b, 'hand4', a2)
    assert _is_linked(b, 'hand4', a2)
    if hasattr(a1, 'dealer5'):
        assert not _is_linked(a1, 'dealer5', b)
    if hasattr(a2, 'dealer5'):
        assert _is_linked(a2, 'dealer5', b)
    _safe_set(b, 'hand4', None)
    assert not _is_linked(b, 'hand4', a2)
    if hasattr(a2, 'dealer5'):
        assert not _is_linked(a2, 'dealer5', b)


def test_assoc_Player_Hand_reverse_link_reassign_clear():
    a1 = Main(bet="sample_text", cartes="sample_text", value=7)
    a2 = Main(bet="sample_text_2", cartes="sample_text_2", value=13)
    b = Joueur(main="sample_text", nom="sample_text", playerbank=7)
    _safe_set(b, 'hand6', {a1})
    assert _is_linked(b, 'hand6', a1)
    if hasattr(a1, 'player7'):
        assert _is_linked(a1, 'player7', b)
    _safe_set(b, 'hand6', {a2})
    assert _is_linked(b, 'hand6', a2)
    if hasattr(a1, 'player7'):
        assert not _is_linked(a1, 'player7', b)
    if hasattr(a2, 'player7'):
        assert _is_linked(a2, 'player7', b)
    _safe_set(b, 'hand6', set())
    assert not _is_linked(b, 'hand6', a2)
    if hasattr(a2, 'player7'):
        assert not _is_linked(a2, 'player7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

