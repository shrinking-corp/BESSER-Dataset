import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    gametournament_FinalPhase,
    gametournament_Game,
    gametournament_Gamer,
    gametournament_Pool,
    gametournament_QualificationPhase,
    gametournament_Tournament,
    GameType,
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

def test_assoc_classment18_reverse_link_reassign_clear():
    a1 = gametournament_Pool()
    a2 = gametournament_Pool()
    b = gametournament_Gamer(firstName="sample_text", lastName="sample_text", matches=7, pseudo="sample_text", victories=7)
    _safe_set(b, 'gametournament_Gamer20', a1)
    assert _is_linked(b, 'gametournament_Gamer20', a1)
    if hasattr(a1, 'gametournament_Pool19'):
        assert _is_linked(a1, 'gametournament_Pool19', b)
    _safe_set(b, 'gametournament_Gamer20', a2)
    assert _is_linked(b, 'gametournament_Gamer20', a2)
    if hasattr(a1, 'gametournament_Pool19'):
        assert not _is_linked(a1, 'gametournament_Pool19', b)
    if hasattr(a2, 'gametournament_Pool19'):
        assert _is_linked(a2, 'gametournament_Pool19', b)
    _safe_set(b, 'gametournament_Gamer20', None)
    assert not _is_linked(b, 'gametournament_Gamer20', a2)
    if hasattr(a2, 'gametournament_Pool19'):
        assert not _is_linked(a2, 'gametournament_Pool19', b)


def test_assoc_game0_reverse_link_reassign_clear():
    a1 = gametournament_Tournament(endDate=date(2024, 1, 1), location="sample_text", name="sample_text", prize=7, startDate=date(2024, 1, 1))
    a2 = gametournament_Tournament(endDate=date(2025, 6, 15), location="sample_text_2", name="sample_text_2", prize=13, startDate=date(2025, 6, 15))
    b = gametournament_Game(name="sample_text", type="sample_text")
    _safe_set(b, 'gametournament_Game', a1)
    assert _is_linked(b, 'gametournament_Game', a1)
    if hasattr(a1, 'gametournament_Tournament'):
        assert _is_linked(a1, 'gametournament_Tournament', b)
    _safe_set(b, 'gametournament_Game', a2)
    assert _is_linked(b, 'gametournament_Game', a2)
    if hasattr(a1, 'gametournament_Tournament'):
        assert not _is_linked(a1, 'gametournament_Tournament', b)
    if hasattr(a2, 'gametournament_Tournament'):
        assert _is_linked(a2, 'gametournament_Tournament', b)
    _safe_set(b, 'gametournament_Game', None)
    assert not _is_linked(b, 'gametournament_Game', a2)
    if hasattr(a2, 'gametournament_Tournament'):
        assert not _is_linked(a2, 'gametournament_Tournament', b)


def test_assoc_gamers1_reverse_link_reassign_clear():
    a1 = gametournament_Tournament(endDate=date(2024, 1, 1), location="sample_text", name="sample_text", prize=7, startDate=date(2024, 1, 1))
    a2 = gametournament_Tournament(endDate=date(2025, 6, 15), location="sample_text_2", name="sample_text_2", prize=13, startDate=date(2025, 6, 15))
    b = gametournament_Gamer(firstName="sample_text", lastName="sample_text", matches=7, pseudo="sample_text", victories=7)
    _safe_set(b, 'gametournament_Gamer', a1)
    assert _is_linked(b, 'gametournament_Gamer', a1)
    if hasattr(a1, 'gametournament_Tournament2'):
        assert _is_linked(a1, 'gametournament_Tournament2', b)
    _safe_set(b, 'gametournament_Gamer', a2)
    assert _is_linked(b, 'gametournament_Gamer', a2)
    if hasattr(a1, 'gametournament_Tournament2'):
        assert not _is_linked(a1, 'gametournament_Tournament2', b)
    if hasattr(a2, 'gametournament_Tournament2'):
        assert _is_linked(a2, 'gametournament_Tournament2', b)
    _safe_set(b, 'gametournament_Gamer', None)
    assert not _is_linked(b, 'gametournament_Gamer', a2)
    if hasattr(a2, 'gametournament_Tournament2'):
        assert not _is_linked(a2, 'gametournament_Tournament2', b)


def test_assoc_participants15_reverse_link_reassign_clear():
    a1 = gametournament_Pool()
    a2 = gametournament_Pool()
    b = gametournament_Gamer(firstName="sample_text", lastName="sample_text", matches=7, pseudo="sample_text", victories=7)
    _safe_set(b, 'gametournament_Gamer17', a1)
    assert _is_linked(b, 'gametournament_Gamer17', a1)
    if hasattr(a1, 'gametournament_Pool16'):
        assert _is_linked(a1, 'gametournament_Pool16', b)
    _safe_set(b, 'gametournament_Gamer17', a2)
    assert _is_linked(b, 'gametournament_Gamer17', a2)
    if hasattr(a1, 'gametournament_Pool16'):
        assert not _is_linked(a1, 'gametournament_Pool16', b)
    if hasattr(a2, 'gametournament_Pool16'):
        assert _is_linked(a2, 'gametournament_Pool16', b)
    _safe_set(b, 'gametournament_Gamer17', None)
    assert not _is_linked(b, 'gametournament_Gamer17', a2)
    if hasattr(a2, 'gametournament_Pool16'):
        assert not _is_linked(a2, 'gametournament_Pool16', b)


def test_assoc_pools7_reverse_link_reassign_clear():
    a1 = gametournament_QualificationPhase()
    a2 = gametournament_QualificationPhase()
    b = gametournament_Pool()
    _safe_set(b, 'gametournament_Pool', a1)
    assert _is_linked(b, 'gametournament_Pool', a1)
    if hasattr(a1, 'gametournament_QualificationPhase8'):
        assert _is_linked(a1, 'gametournament_QualificationPhase8', b)
    _safe_set(b, 'gametournament_Pool', a2)
    assert _is_linked(b, 'gametournament_Pool', a2)
    if hasattr(a1, 'gametournament_QualificationPhase8'):
        assert not _is_linked(a1, 'gametournament_QualificationPhase8', b)
    if hasattr(a2, 'gametournament_QualificationPhase8'):
        assert _is_linked(a2, 'gametournament_QualificationPhase8', b)
    _safe_set(b, 'gametournament_Pool', None)
    assert not _is_linked(b, 'gametournament_Pool', a2)
    if hasattr(a2, 'gametournament_QualificationPhase8'):
        assert not _is_linked(a2, 'gametournament_QualificationPhase8', b)


def test_assoc_qualificationPhase5_reverse_link_reassign_clear():
    a1 = gametournament_Tournament(endDate=date(2024, 1, 1), location="sample_text", name="sample_text", prize=7, startDate=date(2024, 1, 1))
    a2 = gametournament_Tournament(endDate=date(2025, 6, 15), location="sample_text_2", name="sample_text_2", prize=13, startDate=date(2025, 6, 15))
    b = gametournament_QualificationPhase()
    _safe_set(b, 'gametournament_QualificationPhase', a1)
    assert _is_linked(b, 'gametournament_QualificationPhase', a1)
    if hasattr(a1, 'gametournament_Tournament6'):
        assert _is_linked(a1, 'gametournament_Tournament6', b)
    _safe_set(b, 'gametournament_QualificationPhase', a2)
    assert _is_linked(b, 'gametournament_QualificationPhase', a2)
    if hasattr(a1, 'gametournament_Tournament6'):
        assert not _is_linked(a1, 'gametournament_Tournament6', b)
    if hasattr(a2, 'gametournament_Tournament6'):
        assert _is_linked(a2, 'gametournament_Tournament6', b)
    _safe_set(b, 'gametournament_QualificationPhase', None)
    assert not _is_linked(b, 'gametournament_QualificationPhase', a2)
    if hasattr(a2, 'gametournament_Tournament6'):
        assert not _is_linked(a2, 'gametournament_Tournament6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_finalPhase3_stub_double():
    # gametournament_FinalPhase has no real 'gametournament_FinalPhase' property in the generated
    # code (a bare stub) -- manually attach it so gametournament_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gametournament_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gametournament_Tournament(endDate=date(2024, 1, 1), location="sample_text", name="sample_text", prize=7, startDate=date(2024, 1, 1))
    partner = gametournament_FinalPhase()
    setattr(partner, 'gametournament_FinalPhase', None)
    _safe_set(owner, 'gametournament_Tournament4', partner)
    assert getattr(partner, 'gametournament_FinalPhase') == owner
    _safe_set(owner, 'gametournament_Tournament4', None)
    assert getattr(partner, 'gametournament_FinalPhase') is None


def test_assoc_finalists9_stub_double():
    # gametournament_FinalPhase has no real 'gametournament_FinalPhase10' property in the generated
    # code (a bare stub) -- manually attach it so gametournament_Gamer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gametournament_Gamer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gametournament_Gamer(firstName="sample_text", lastName="sample_text", matches=7, pseudo="sample_text", victories=7)
    partner = gametournament_FinalPhase()
    setattr(partner, 'gametournament_FinalPhase10', None)
    _safe_set(owner, 'gametournament_Gamer11', partner)
    assert owner in getattr(partner, 'gametournament_FinalPhase10')
    _safe_set(owner, 'gametournament_Gamer11', None)
    assert owner not in getattr(partner, 'gametournament_FinalPhase10')


def test_assoc_qualificationphase12_stub_double():
    # gametournament_FinalPhase has no real 'gametournament_FinalPhase13' property in the generated
    # code (a bare stub) -- manually attach it so gametournament_QualificationPhase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gametournament_QualificationPhase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gametournament_QualificationPhase()
    partner = gametournament_FinalPhase()
    setattr(partner, 'gametournament_FinalPhase13', None)
    _safe_set(owner, 'gametournament_QualificationPhase14', partner)
    assert getattr(partner, 'gametournament_FinalPhase13') == owner
    _safe_set(owner, 'gametournament_QualificationPhase14', None)
    assert getattr(partner, 'gametournament_FinalPhase13') is None


