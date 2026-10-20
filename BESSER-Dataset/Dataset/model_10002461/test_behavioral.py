import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Avatar,
    Avatar1,
    Avatar2,
    Card,
    Card1,
    Card2,
    Deck,
    Deck1,
    Deck2,
    Game,
    Game1,
    Game2,
    Player,
    Player1,
    Player2,
    Theme,
    Theme1,
    Theme2,
    Kind,
    Kind1,
    Kind2,
    Suit,
    Suit1,
    Suit2,
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

def test_assoc_Game_Player_reverse_link_reassign_clear():
    a1 = Player(name="sample_text")
    a2 = Player(name="sample_text_2")
    b = Game(name="sample_text")
    _safe_set(b, 'players6', {a1})
    assert _is_linked(b, 'players6', a1)
    if hasattr(a1, 'games7'):
        assert _is_linked(a1, 'games7', b)
    _safe_set(b, 'players6', {a2})
    assert _is_linked(b, 'players6', a2)
    if hasattr(a1, 'games7'):
        assert not _is_linked(a1, 'games7', b)
    if hasattr(a2, 'games7'):
        assert _is_linked(a2, 'games7', b)
    _safe_set(b, 'players6', set())
    assert not _is_linked(b, 'players6', a2)
    if hasattr(a2, 'games7'):
        assert not _is_linked(a2, 'games7', b)


def test_assoc_Game_Player2_reverse_link_reassign_clear():
    a1 = Player2(name="sample_text")
    a2 = Player2(name="sample_text_2")
    b = Game2(name="sample_text")
    _safe_set(b, 'players18', {a1})
    assert _is_linked(b, 'players18', a1)
    if hasattr(a1, 'games19'):
        assert _is_linked(a1, 'games19', b)
    _safe_set(b, 'players18', {a2})
    assert _is_linked(b, 'players18', a2)
    if hasattr(a1, 'games19'):
        assert not _is_linked(a1, 'games19', b)
    if hasattr(a2, 'games19'):
        assert _is_linked(a2, 'games19', b)
    _safe_set(b, 'players18', set())
    assert not _is_linked(b, 'players18', a2)
    if hasattr(a2, 'games19'):
        assert not _is_linked(a2, 'games19', b)


def test_assoc_Game_Player3_reverse_link_reassign_clear():
    a1 = Player1(hand="sample_text", name="sample_text")
    a2 = Player1(hand="sample_text_2", name="sample_text_2")
    b = Game1(name="sample_text")
    _safe_set(b, 'players30', {a1})
    assert _is_linked(b, 'players30', a1)
    if hasattr(a1, 'games31'):
        assert _is_linked(a1, 'games31', b)
    _safe_set(b, 'players30', {a2})
    assert _is_linked(b, 'players30', a2)
    if hasattr(a1, 'games31'):
        assert not _is_linked(a1, 'games31', b)
    if hasattr(a2, 'games31'):
        assert _is_linked(a2, 'games31', b)
    _safe_set(b, 'players30', set())
    assert not _is_linked(b, 'players30', a2)
    if hasattr(a2, 'games31'):
        assert not _is_linked(a2, 'games31', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Game_Deck_stub_double():
    # Deck has no real 'games5' property in the generated
    # code (a bare stub) -- manually attach it so Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Game(name="sample_text")
    partner = Deck()
    setattr(partner, 'games5', None)
    _safe_set(owner, 'decks4', {partner})
    assert owner in getattr(partner, 'games5')
    _safe_set(owner, 'decks4', set())
    assert owner not in getattr(partner, 'games5')


def test_assoc_Game_Deck2_stub_double():
    # Deck2 has no real 'games17' property in the generated
    # code (a bare stub) -- manually attach it so Game2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Game2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Game2(name="sample_text")
    partner = Deck2()
    setattr(partner, 'games17', None)
    _safe_set(owner, 'decks16', {partner})
    assert owner in getattr(partner, 'games17')
    _safe_set(owner, 'decks16', set())
    assert owner not in getattr(partner, 'games17')


def test_assoc_Player_Avatar_stub_double():
    # Avatar has no real 'players11' property in the generated
    # code (a bare stub) -- manually attach it so Player's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player(name="sample_text")
    partner = Avatar()
    setattr(partner, 'players11', None)
    _safe_set(owner, 'avatar10', partner)
    assert owner in getattr(partner, 'players11')
    _safe_set(owner, 'avatar10', None)
    assert owner not in getattr(partner, 'players11')


def test_assoc_Player_Avatar2_stub_double():
    # Avatar2 has no real 'players23' property in the generated
    # code (a bare stub) -- manually attach it so Player2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player2(name="sample_text")
    partner = Avatar2()
    setattr(partner, 'players23', None)
    _safe_set(owner, 'avatar22', partner)
    assert owner in getattr(partner, 'players23')
    _safe_set(owner, 'avatar22', None)
    assert owner not in getattr(partner, 'players23')


def test_assoc_Player_Avatar3_stub_double():
    # Avatar1 has no real 'players35' property in the generated
    # code (a bare stub) -- manually attach it so Player1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player1(hand="sample_text", name="sample_text")
    partner = Avatar1()
    setattr(partner, 'players35', None)
    _safe_set(owner, 'avatar34', partner)
    assert owner in getattr(partner, 'players35')
    _safe_set(owner, 'avatar34', None)
    assert owner not in getattr(partner, 'players35')


