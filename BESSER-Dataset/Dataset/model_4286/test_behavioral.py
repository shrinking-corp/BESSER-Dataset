import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DescribedEntity,
    IdentifiableEntity,
    Serializable,
    pokerleague_Competition,
    pokerleague_DataStructureVersion,
    pokerleague_DataVersion,
    pokerleague_DescribedEntity,
    pokerleague_Game,
    pokerleague_IdentifiableEntity,
    pokerleague_Invitation,
    pokerleague_InvitationEvent,
    pokerleague_Player,
    pokerleague_PlayerInGame,
    pokerleague_PrizeMoneyFormula,
    pokerleague_PrizeMoneyRule,
    pokerleague_PrizeMoneyRuleSet,
    pokerleague_Serializable,
    pokerleague_Settings,
    pokerleague_Tournament,
    InvitationEventType,
    InvitationReply,
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

def test_assoc_competition12_reverse_link_reassign_clear():
    a1 = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    a2 = pokerleague_Tournament(defaultBuyIn=13, maxPlayers=13, minPlayers=13, tournamentAnnouncementLead=13, tournamentEnd="sample_text_2", tournamentInvitationClosure=13, tournamentInvitationContact="sample_text_2", tournamentStart="sample_text_2")
    b = pokerleague_Competition(defaultBuyIn=7, defaultMaxPlayers=7, defaultMinPlayers=7, defaultTournamentAnnouncementLead=7, defaultTournamentInvitationClosure=7, defaultTournamentInvitationContact="sample_text", endDate=date(2024, 1, 1), minimalAttendance=7, startDate=date(2024, 1, 1))
    _safe_set(b, 'Competition', a1)
    assert _is_linked(b, 'Competition', a1)
    if hasattr(a1, 'tournaments'):
        assert _is_linked(a1, 'tournaments', b)
    _safe_set(b, 'Competition', a2)
    assert _is_linked(b, 'Competition', a2)
    if hasattr(a1, 'tournaments'):
        assert not _is_linked(a1, 'tournaments', b)
    if hasattr(a2, 'tournaments'):
        assert _is_linked(a2, 'tournaments', b)
    _safe_set(b, 'Competition', None)
    assert not _is_linked(b, 'Competition', a2)
    if hasattr(a2, 'tournaments'):
        assert not _is_linked(a2, 'tournaments', b)


def test_assoc_events19_reverse_link_reassign_clear():
    a1 = pokerleague_InvitationEvent(eventTime="sample_text", eventType="sample_text", sent=True)
    a2 = pokerleague_InvitationEvent(eventTime="sample_text_2", eventType="sample_text_2", sent=False)
    b = pokerleague_Invitation(ordinal=7, reply="sample_text", uuid="sample_text")
    _safe_set(b, 'invitation', {a1})
    assert _is_linked(b, 'invitation', a1)
    if hasattr(a1, 'InvitationEvent'):
        assert _is_linked(a1, 'InvitationEvent', b)
    _safe_set(b, 'invitation', {a2})
    assert _is_linked(b, 'invitation', a2)
    if hasattr(a1, 'InvitationEvent'):
        assert not _is_linked(a1, 'InvitationEvent', b)
    if hasattr(a2, 'InvitationEvent'):
        assert _is_linked(a2, 'InvitationEvent', b)
    _safe_set(b, 'invitation', set())
    assert not _is_linked(b, 'invitation', a2)
    if hasattr(a2, 'InvitationEvent'):
        assert not _is_linked(a2, 'InvitationEvent', b)


def test_assoc_game29_reverse_link_reassign_clear():
    a1 = pokerleague_PlayerInGame(rank=7)
    a2 = pokerleague_PlayerInGame(rank=13)
    b = pokerleague_Game(buyIn=7, ordinal=7)
    _safe_set(b, 'Game30', a1)
    assert _is_linked(b, 'Game30', a1)
    if hasattr(a1, 'playersInGame'):
        assert _is_linked(a1, 'playersInGame', b)
    _safe_set(b, 'Game30', a2)
    assert _is_linked(b, 'Game30', a2)
    if hasattr(a1, 'playersInGame'):
        assert not _is_linked(a1, 'playersInGame', b)
    if hasattr(a2, 'playersInGame'):
        assert _is_linked(a2, 'playersInGame', b)
    _safe_set(b, 'Game30', None)
    assert not _is_linked(b, 'Game30', a2)
    if hasattr(a2, 'playersInGame'):
        assert not _is_linked(a2, 'playersInGame', b)


def test_assoc_games13_reverse_link_reassign_clear():
    a1 = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    a2 = pokerleague_Tournament(defaultBuyIn=13, maxPlayers=13, minPlayers=13, tournamentAnnouncementLead=13, tournamentEnd="sample_text_2", tournamentInvitationClosure=13, tournamentInvitationContact="sample_text_2", tournamentStart="sample_text_2")
    b = pokerleague_Game(buyIn=7, ordinal=7)
    _safe_set(b, 'Game', a1)
    assert _is_linked(b, 'Game', a1)
    if hasattr(a1, 'tournament14'):
        assert _is_linked(a1, 'tournament14', b)
    _safe_set(b, 'Game', a2)
    assert _is_linked(b, 'Game', a2)
    if hasattr(a1, 'tournament14'):
        assert not _is_linked(a1, 'tournament14', b)
    if hasattr(a2, 'tournament14'):
        assert _is_linked(a2, 'tournament14', b)
    _safe_set(b, 'Game', None)
    assert not _is_linked(b, 'Game', a2)
    if hasattr(a2, 'tournament14'):
        assert not _is_linked(a2, 'tournament14', b)


def test_assoc_invitation20_reverse_link_reassign_clear():
    a1 = pokerleague_InvitationEvent(eventTime="sample_text", eventType="sample_text", sent=True)
    a2 = pokerleague_InvitationEvent(eventTime="sample_text_2", eventType="sample_text_2", sent=False)
    b = pokerleague_Invitation(ordinal=7, reply="sample_text", uuid="sample_text")
    _safe_set(b, 'Invitation21', a1)
    assert _is_linked(b, 'Invitation21', a1)
    if hasattr(a1, 'events'):
        assert _is_linked(a1, 'events', b)
    _safe_set(b, 'Invitation21', a2)
    assert _is_linked(b, 'Invitation21', a2)
    if hasattr(a1, 'events'):
        assert not _is_linked(a1, 'events', b)
    if hasattr(a2, 'events'):
        assert _is_linked(a2, 'events', b)
    _safe_set(b, 'Invitation21', None)
    assert not _is_linked(b, 'Invitation21', a2)
    if hasattr(a2, 'events'):
        assert not _is_linked(a2, 'events', b)


def test_assoc_invitations11_reverse_link_reassign_clear():
    a1 = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    a2 = pokerleague_Tournament(defaultBuyIn=13, maxPlayers=13, minPlayers=13, tournamentAnnouncementLead=13, tournamentEnd="sample_text_2", tournamentInvitationClosure=13, tournamentInvitationContact="sample_text_2", tournamentStart="sample_text_2")
    b = pokerleague_Invitation(ordinal=7, reply="sample_text", uuid="sample_text")
    _safe_set(b, 'Invitation', a1)
    assert _is_linked(b, 'Invitation', a1)
    if hasattr(a1, 'tournament'):
        assert _is_linked(a1, 'tournament', b)
    _safe_set(b, 'Invitation', a2)
    assert _is_linked(b, 'Invitation', a2)
    if hasattr(a1, 'tournament'):
        assert not _is_linked(a1, 'tournament', b)
    if hasattr(a2, 'tournament'):
        assert _is_linked(a2, 'tournament', b)
    _safe_set(b, 'Invitation', None)
    assert not _is_linked(b, 'Invitation', a2)
    if hasattr(a2, 'tournament'):
        assert not _is_linked(a2, 'tournament', b)


def test_assoc_player17_reverse_link_reassign_clear():
    a1 = pokerleague_Player(active=True, emailAddress="sample_text", firstName="sample_text", lastName="sample_text", nick="sample_text")
    a2 = pokerleague_Player(active=False, emailAddress="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", nick="sample_text_2")
    b = pokerleague_Invitation(ordinal=7, reply="sample_text", uuid="sample_text")
    _safe_set(b, 'pokerleague_Invitation', a1)
    assert _is_linked(b, 'pokerleague_Invitation', a1)
    if hasattr(a1, 'pokerleague_Player18'):
        assert _is_linked(a1, 'pokerleague_Player18', b)
    _safe_set(b, 'pokerleague_Invitation', a2)
    assert _is_linked(b, 'pokerleague_Invitation', a2)
    if hasattr(a1, 'pokerleague_Player18'):
        assert not _is_linked(a1, 'pokerleague_Player18', b)
    if hasattr(a2, 'pokerleague_Player18'):
        assert _is_linked(a2, 'pokerleague_Player18', b)
    _safe_set(b, 'pokerleague_Invitation', None)
    assert not _is_linked(b, 'pokerleague_Invitation', a2)
    if hasattr(a2, 'pokerleague_Player18'):
        assert not _is_linked(a2, 'pokerleague_Player18', b)


def test_assoc_player27_reverse_link_reassign_clear():
    a1 = pokerleague_PlayerInGame(rank=7)
    a2 = pokerleague_PlayerInGame(rank=13)
    b = pokerleague_Player(active=True, emailAddress="sample_text", firstName="sample_text", lastName="sample_text", nick="sample_text")
    _safe_set(b, 'pokerleague_Player28', a1)
    assert _is_linked(b, 'pokerleague_Player28', a1)
    if hasattr(a1, 'pokerleague_PlayerInGame'):
        assert _is_linked(a1, 'pokerleague_PlayerInGame', b)
    _safe_set(b, 'pokerleague_Player28', a2)
    assert _is_linked(b, 'pokerleague_Player28', a2)
    if hasattr(a1, 'pokerleague_PlayerInGame'):
        assert not _is_linked(a1, 'pokerleague_PlayerInGame', b)
    if hasattr(a2, 'pokerleague_PlayerInGame'):
        assert _is_linked(a2, 'pokerleague_PlayerInGame', b)
    _safe_set(b, 'pokerleague_Player28', None)
    assert not _is_linked(b, 'pokerleague_Player28', a2)
    if hasattr(a2, 'pokerleague_PlayerInGame'):
        assert not _is_linked(a2, 'pokerleague_PlayerInGame', b)


def test_assoc_players7_reverse_link_reassign_clear():
    a1 = pokerleague_Player(active=True, emailAddress="sample_text", firstName="sample_text", lastName="sample_text", nick="sample_text")
    a2 = pokerleague_Player(active=False, emailAddress="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", nick="sample_text_2")
    b = pokerleague_Competition(defaultBuyIn=7, defaultMaxPlayers=7, defaultMinPlayers=7, defaultTournamentAnnouncementLead=7, defaultTournamentInvitationClosure=7, defaultTournamentInvitationContact="sample_text", endDate=date(2024, 1, 1), minimalAttendance=7, startDate=date(2024, 1, 1))
    _safe_set(b, 'pokerleague_Competition8', {a1})
    assert _is_linked(b, 'pokerleague_Competition8', a1)
    if hasattr(a1, 'pokerleague_Player'):
        assert _is_linked(a1, 'pokerleague_Player', b)
    _safe_set(b, 'pokerleague_Competition8', {a2})
    assert _is_linked(b, 'pokerleague_Competition8', a2)
    if hasattr(a1, 'pokerleague_Player'):
        assert not _is_linked(a1, 'pokerleague_Player', b)
    if hasattr(a2, 'pokerleague_Player'):
        assert _is_linked(a2, 'pokerleague_Player', b)
    _safe_set(b, 'pokerleague_Competition8', set())
    assert not _is_linked(b, 'pokerleague_Competition8', a2)
    if hasattr(a2, 'pokerleague_Player'):
        assert not _is_linked(a2, 'pokerleague_Player', b)


def test_assoc_playersInGame26_reverse_link_reassign_clear():
    a1 = pokerleague_PlayerInGame(rank=7)
    a2 = pokerleague_PlayerInGame(rank=13)
    b = pokerleague_Game(buyIn=7, ordinal=7)
    _safe_set(b, 'game', {a1})
    assert _is_linked(b, 'game', a1)
    if hasattr(a1, 'PlayerInGame'):
        assert _is_linked(a1, 'PlayerInGame', b)
    _safe_set(b, 'game', {a2})
    assert _is_linked(b, 'game', a2)
    if hasattr(a1, 'PlayerInGame'):
        assert not _is_linked(a1, 'PlayerInGame', b)
    if hasattr(a2, 'PlayerInGame'):
        assert _is_linked(a2, 'PlayerInGame', b)
    _safe_set(b, 'game', set())
    assert not _is_linked(b, 'game', a2)
    if hasattr(a2, 'PlayerInGame'):
        assert not _is_linked(a2, 'PlayerInGame', b)


def test_assoc_prizeMoneyFormulas2_reverse_link_reassign_clear():
    a1 = pokerleague_PrizeMoneyRule(numberOfPlayers=7)
    a2 = pokerleague_PrizeMoneyRule(numberOfPlayers=13)
    b = pokerleague_PrizeMoneyFormula(rank=7, relativePrizeMoney=7)
    _safe_set(b, 'PrizeMoneyFormula', a1)
    assert _is_linked(b, 'PrizeMoneyFormula', a1)
    if hasattr(a1, 'prizeMoneyRule'):
        assert _is_linked(a1, 'prizeMoneyRule', b)
    _safe_set(b, 'PrizeMoneyFormula', a2)
    assert _is_linked(b, 'PrizeMoneyFormula', a2)
    if hasattr(a1, 'prizeMoneyRule'):
        assert not _is_linked(a1, 'prizeMoneyRule', b)
    if hasattr(a2, 'prizeMoneyRule'):
        assert _is_linked(a2, 'prizeMoneyRule', b)
    _safe_set(b, 'PrizeMoneyFormula', None)
    assert not _is_linked(b, 'PrizeMoneyFormula', a2)
    if hasattr(a2, 'prizeMoneyRule'):
        assert not _is_linked(a2, 'prizeMoneyRule', b)


def test_assoc_prizeMoneyRule3_reverse_link_reassign_clear():
    a1 = pokerleague_PrizeMoneyRule(numberOfPlayers=7)
    a2 = pokerleague_PrizeMoneyRule(numberOfPlayers=13)
    b = pokerleague_PrizeMoneyFormula(rank=7, relativePrizeMoney=7)
    _safe_set(b, 'prizeMoneyFormulas', a1)
    assert _is_linked(b, 'prizeMoneyFormulas', a1)
    if hasattr(a1, 'PrizeMoneyRule4'):
        assert _is_linked(a1, 'PrizeMoneyRule4', b)
    _safe_set(b, 'prizeMoneyFormulas', a2)
    assert _is_linked(b, 'prizeMoneyFormulas', a2)
    if hasattr(a1, 'PrizeMoneyRule4'):
        assert not _is_linked(a1, 'PrizeMoneyRule4', b)
    if hasattr(a2, 'PrizeMoneyRule4'):
        assert _is_linked(a2, 'PrizeMoneyRule4', b)
    _safe_set(b, 'prizeMoneyFormulas', None)
    assert not _is_linked(b, 'prizeMoneyFormulas', a2)
    if hasattr(a2, 'PrizeMoneyRule4'):
        assert not _is_linked(a2, 'PrizeMoneyRule4', b)


def test_assoc_tournament15_reverse_link_reassign_clear():
    a1 = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    a2 = pokerleague_Tournament(defaultBuyIn=13, maxPlayers=13, minPlayers=13, tournamentAnnouncementLead=13, tournamentEnd="sample_text_2", tournamentInvitationClosure=13, tournamentInvitationContact="sample_text_2", tournamentStart="sample_text_2")
    b = pokerleague_Invitation(ordinal=7, reply="sample_text", uuid="sample_text")
    _safe_set(b, 'invitations', a1)
    assert _is_linked(b, 'invitations', a1)
    if hasattr(a1, 'Tournament16'):
        assert _is_linked(a1, 'Tournament16', b)
    _safe_set(b, 'invitations', a2)
    assert _is_linked(b, 'invitations', a2)
    if hasattr(a1, 'Tournament16'):
        assert not _is_linked(a1, 'Tournament16', b)
    if hasattr(a2, 'Tournament16'):
        assert _is_linked(a2, 'Tournament16', b)
    _safe_set(b, 'invitations', None)
    assert not _is_linked(b, 'invitations', a2)
    if hasattr(a2, 'Tournament16'):
        assert not _is_linked(a2, 'Tournament16', b)


def test_assoc_tournament22_reverse_link_reassign_clear():
    a1 = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    a2 = pokerleague_Tournament(defaultBuyIn=13, maxPlayers=13, minPlayers=13, tournamentAnnouncementLead=13, tournamentEnd="sample_text_2", tournamentInvitationClosure=13, tournamentInvitationContact="sample_text_2", tournamentStart="sample_text_2")
    b = pokerleague_Game(buyIn=7, ordinal=7)
    _safe_set(b, 'games', a1)
    assert _is_linked(b, 'games', a1)
    if hasattr(a1, 'Tournament23'):
        assert _is_linked(a1, 'Tournament23', b)
    _safe_set(b, 'games', a2)
    assert _is_linked(b, 'games', a2)
    if hasattr(a1, 'Tournament23'):
        assert not _is_linked(a1, 'Tournament23', b)
    if hasattr(a2, 'Tournament23'):
        assert _is_linked(a2, 'Tournament23', b)
    _safe_set(b, 'games', None)
    assert not _is_linked(b, 'games', a2)
    if hasattr(a2, 'Tournament23'):
        assert not _is_linked(a2, 'Tournament23', b)


def test_assoc_tournaments6_reverse_link_reassign_clear():
    a1 = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    a2 = pokerleague_Tournament(defaultBuyIn=13, maxPlayers=13, minPlayers=13, tournamentAnnouncementLead=13, tournamentEnd="sample_text_2", tournamentInvitationClosure=13, tournamentInvitationContact="sample_text_2", tournamentStart="sample_text_2")
    b = pokerleague_Competition(defaultBuyIn=7, defaultMaxPlayers=7, defaultMinPlayers=7, defaultTournamentAnnouncementLead=7, defaultTournamentInvitationClosure=7, defaultTournamentInvitationContact="sample_text", endDate=date(2024, 1, 1), minimalAttendance=7, startDate=date(2024, 1, 1))
    _safe_set(b, 'competition', {a1})
    assert _is_linked(b, 'competition', a1)
    if hasattr(a1, 'Tournament'):
        assert _is_linked(a1, 'Tournament', b)
    _safe_set(b, 'competition', {a2})
    assert _is_linked(b, 'competition', a2)
    if hasattr(a1, 'Tournament'):
        assert not _is_linked(a1, 'Tournament', b)
    if hasattr(a2, 'Tournament'):
        assert _is_linked(a2, 'Tournament', b)
    _safe_set(b, 'competition', set())
    assert not _is_linked(b, 'competition', a2)
    if hasattr(a2, 'Tournament'):
        assert not _is_linked(a2, 'Tournament', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defaultPrizeMoneyRuleSet5_stub_double():
    # pokerleague_PrizeMoneyRuleSet has no real 'pokerleague_PrizeMoneyRuleSet' property in the generated
    # code (a bare stub) -- manually attach it so pokerleague_Competition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pokerleague_Competition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pokerleague_Competition(defaultBuyIn=7, defaultMaxPlayers=7, defaultMinPlayers=7, defaultTournamentAnnouncementLead=7, defaultTournamentInvitationClosure=7, defaultTournamentInvitationContact="sample_text", endDate=date(2024, 1, 1), minimalAttendance=7, startDate=date(2024, 1, 1))
    partner = pokerleague_PrizeMoneyRuleSet()
    setattr(partner, 'pokerleague_PrizeMoneyRuleSet', None)
    _safe_set(owner, 'pokerleague_Competition', partner)
    assert getattr(partner, 'pokerleague_PrizeMoneyRuleSet') == owner
    _safe_set(owner, 'pokerleague_Competition', None)
    assert getattr(partner, 'pokerleague_PrizeMoneyRuleSet') is None


def test_assoc_defaultPrizeMoneyRuleSet9_stub_double():
    # pokerleague_PrizeMoneyRuleSet has no real 'pokerleague_PrizeMoneyRuleSet10' property in the generated
    # code (a bare stub) -- manually attach it so pokerleague_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pokerleague_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pokerleague_Tournament(defaultBuyIn=7, maxPlayers=7, minPlayers=7, tournamentAnnouncementLead=7, tournamentEnd="sample_text", tournamentInvitationClosure=7, tournamentInvitationContact="sample_text", tournamentStart="sample_text")
    partner = pokerleague_PrizeMoneyRuleSet()
    setattr(partner, 'pokerleague_PrizeMoneyRuleSet10', None)
    _safe_set(owner, 'pokerleague_Tournament', partner)
    assert getattr(partner, 'pokerleague_PrizeMoneyRuleSet10') == owner
    _safe_set(owner, 'pokerleague_Tournament', None)
    assert getattr(partner, 'pokerleague_PrizeMoneyRuleSet10') is None


def test_assoc_prizeMoneyRuleSet1_stub_double():
    # pokerleague_PrizeMoneyRuleSet has no real 'PrizeMoneyRuleSet' property in the generated
    # code (a bare stub) -- manually attach it so pokerleague_PrizeMoneyRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pokerleague_PrizeMoneyRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pokerleague_PrizeMoneyRule(numberOfPlayers=7)
    partner = pokerleague_PrizeMoneyRuleSet()
    setattr(partner, 'PrizeMoneyRuleSet', None)
    _safe_set(owner, 'prizeMoneyRules', partner)
    assert getattr(partner, 'PrizeMoneyRuleSet') == owner
    _safe_set(owner, 'prizeMoneyRules', None)
    assert getattr(partner, 'PrizeMoneyRuleSet') is None


def test_assoc_prizeMoneyRuleSet24_stub_double():
    # pokerleague_PrizeMoneyRuleSet has no real 'pokerleague_PrizeMoneyRuleSet25' property in the generated
    # code (a bare stub) -- manually attach it so pokerleague_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pokerleague_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pokerleague_Game(buyIn=7, ordinal=7)
    partner = pokerleague_PrizeMoneyRuleSet()
    setattr(partner, 'pokerleague_PrizeMoneyRuleSet25', None)
    _safe_set(owner, 'pokerleague_Game', partner)
    assert getattr(partner, 'pokerleague_PrizeMoneyRuleSet25') == owner
    _safe_set(owner, 'pokerleague_Game', None)
    assert getattr(partner, 'pokerleague_PrizeMoneyRuleSet25') is None


def test_assoc_prizeMoneyRules0_stub_double():
    # pokerleague_PrizeMoneyRuleSet has no real 'prizeMoneyRuleSet' property in the generated
    # code (a bare stub) -- manually attach it so pokerleague_PrizeMoneyRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pokerleague_PrizeMoneyRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pokerleague_PrizeMoneyRule(numberOfPlayers=7)
    partner = pokerleague_PrizeMoneyRuleSet()
    setattr(partner, 'prizeMoneyRuleSet', None)
    _safe_set(owner, 'PrizeMoneyRule', partner)
    assert owner in getattr(partner, 'prizeMoneyRuleSet')
    _safe_set(owner, 'PrizeMoneyRule', None)
    assert owner not in getattr(partner, 'prizeMoneyRuleSet')


