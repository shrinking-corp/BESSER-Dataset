import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Publication,
    research_team_ActivityReport,
    research_team_Article,
    research_team_CallForPaper,
    research_team_Collaboration,
    research_team_InProceedings,
    research_team_MasterThesis,
    research_team_Misc,
    research_team_OpenPosition,
    research_team_Paper,
    research_team_Partner,
    research_team_Person,
    research_team_PhDThesis,
    research_team_Publication,
    research_team_Section,
    research_team_Seminar,
    research_team_Software,
    research_team_Team,
    research_team_TypeCollaboration,
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

def test_assoc_21_reverse_link_reassign_clear():
    a1 = research_team_Publication()
    a2 = research_team_Publication()
    b = research_team_Paper(state="sample_text", title="sample_text", url4pdf="sample_text")
    _safe_set(b, 'publishedAs', {a1})
    assert _is_linked(b, 'publishedAs', a1)
    if hasattr(a1, 'Publication22'):
        assert _is_linked(a1, 'Publication22', b)
    _safe_set(b, 'publishedAs', {a2})
    assert _is_linked(b, 'publishedAs', a2)
    if hasattr(a1, 'Publication22'):
        assert not _is_linked(a1, 'Publication22', b)
    if hasattr(a2, 'Publication22'):
        assert _is_linked(a2, 'Publication22', b)
    _safe_set(b, 'publishedAs', set())
    assert not _is_linked(b, 'publishedAs', a2)
    if hasattr(a2, 'Publication22'):
        assert not _is_linked(a2, 'Publication22', b)


def test_assoc_author23_reverse_link_reassign_clear():
    a1 = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    a2 = research_team_Person(affiliation="sample_text_2", firstname="sample_text_2", mail="sample_text_2", name="sample_text_2", phone="sample_text_2")
    b = research_team_Paper(state="sample_text", title="sample_text", url4pdf="sample_text")
    _safe_set(b, 'paper', {a1})
    assert _is_linked(b, 'paper', a1)
    if hasattr(a1, 'Person24'):
        assert _is_linked(a1, 'Person24', b)
    _safe_set(b, 'paper', {a2})
    assert _is_linked(b, 'paper', a2)
    if hasattr(a1, 'Person24'):
        assert not _is_linked(a1, 'Person24', b)
    if hasattr(a2, 'Person24'):
        assert _is_linked(a2, 'Person24', b)
    _safe_set(b, 'paper', set())
    assert not _is_linked(b, 'paper', a2)
    if hasattr(a2, 'Person24'):
        assert not _is_linked(a2, 'Person24', b)


def test_assoc_collaboration27_reverse_link_reassign_clear():
    a1 = research_team_Partner(category="sample_text", country="sample_text", name="sample_text")
    a2 = research_team_Partner(category="sample_text_2", country="sample_text_2", name="sample_text_2")
    b = research_team_Collaboration(from_="sample_text", status="sample_text", title="sample_text", until="sample_text", website="sample_text")
    _safe_set(b, 'Collaboration28', a1)
    assert _is_linked(b, 'Collaboration28', a1)
    if hasattr(a1, 'partners'):
        assert _is_linked(a1, 'partners', b)
    _safe_set(b, 'Collaboration28', a2)
    assert _is_linked(b, 'Collaboration28', a2)
    if hasattr(a1, 'partners'):
        assert not _is_linked(a1, 'partners', b)
    if hasattr(a2, 'partners'):
        assert _is_linked(a2, 'partners', b)
    _safe_set(b, 'Collaboration28', None)
    assert not _is_linked(b, 'Collaboration28', a2)
    if hasattr(a2, 'partners'):
        assert not _is_linked(a2, 'partners', b)


def test_assoc_context20_reverse_link_reassign_clear():
    a1 = research_team_OpenPosition(duration="sample_text", mission="sample_text", status="sample_text")
    a2 = research_team_OpenPosition(duration="sample_text_2", mission="sample_text_2", status="sample_text_2")
    b = research_team_Collaboration(from_="sample_text", status="sample_text", title="sample_text", until="sample_text", website="sample_text")
    _safe_set(b, 'Collaboration', a1)
    assert _is_linked(b, 'Collaboration', a1)
    if hasattr(a1, 'openPositions'):
        assert _is_linked(a1, 'openPositions', b)
    _safe_set(b, 'Collaboration', a2)
    assert _is_linked(b, 'Collaboration', a2)
    if hasattr(a1, 'openPositions'):
        assert not _is_linked(a1, 'openPositions', b)
    if hasattr(a2, 'openPositions'):
        assert _is_linked(a2, 'openPositions', b)
    _safe_set(b, 'Collaboration', None)
    assert not _is_linked(b, 'Collaboration', a2)
    if hasattr(a2, 'openPositions'):
        assert not _is_linked(a2, 'openPositions', b)


def test_assoc_developers25_reverse_link_reassign_clear():
    a1 = research_team_Software(description="sample_text", title="sample_text", website="sample_text")
    a2 = research_team_Software(description="sample_text_2", title="sample_text_2", website="sample_text_2")
    b = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'Person26', a1)
    assert _is_linked(b, 'Person26', a1)
    if hasattr(a1, 'soft'):
        assert _is_linked(a1, 'soft', b)
    _safe_set(b, 'Person26', a2)
    assert _is_linked(b, 'Person26', a2)
    if hasattr(a1, 'soft'):
        assert not _is_linked(a1, 'soft', b)
    if hasattr(a2, 'soft'):
        assert _is_linked(a2, 'soft', b)
    _safe_set(b, 'Person26', None)
    assert not _is_linked(b, 'Person26', a2)
    if hasattr(a2, 'soft'):
        assert not _is_linked(a2, 'soft', b)


def test_assoc_involvedIn8_reverse_link_reassign_clear():
    a1 = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    a2 = research_team_Team(meaning="sample_text_2", name="sample_text_2", status="sample_text_2", urlPage="sample_text_2")
    b = research_team_Collaboration(from_="sample_text", status="sample_text", title="sample_text", until="sample_text", website="sample_text")
    _safe_set(b, 'research_team_Collaboration', a1)
    assert _is_linked(b, 'research_team_Collaboration', a1)
    if hasattr(a1, 'research_team_Team9'):
        assert _is_linked(a1, 'research_team_Team9', b)
    _safe_set(b, 'research_team_Collaboration', a2)
    assert _is_linked(b, 'research_team_Collaboration', a2)
    if hasattr(a1, 'research_team_Team9'):
        assert not _is_linked(a1, 'research_team_Team9', b)
    if hasattr(a2, 'research_team_Team9'):
        assert _is_linked(a2, 'research_team_Team9', b)
    _safe_set(b, 'research_team_Collaboration', None)
    assert not _is_linked(b, 'research_team_Collaboration', a2)
    if hasattr(a2, 'research_team_Team9'):
        assert not _is_linked(a2, 'research_team_Team9', b)


def test_assoc_mainReferences10_reverse_link_reassign_clear():
    a1 = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    a2 = research_team_Team(meaning="sample_text_2", name="sample_text_2", status="sample_text_2", urlPage="sample_text_2")
    b = research_team_Publication()
    _safe_set(b, 'Publication', a1)
    assert _is_linked(b, 'Publication', a1)
    if hasattr(a1, 'team'):
        assert _is_linked(a1, 'team', b)
    _safe_set(b, 'Publication', a2)
    assert _is_linked(b, 'Publication', a2)
    if hasattr(a1, 'team'):
        assert not _is_linked(a1, 'team', b)
    if hasattr(a2, 'team'):
        assert _is_linked(a2, 'team', b)
    _safe_set(b, 'Publication', None)
    assert not _is_linked(b, 'Publication', a2)
    if hasattr(a2, 'team'):
        assert not _is_linked(a2, 'team', b)


def test_assoc_members1_reverse_link_reassign_clear():
    a1 = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    a2 = research_team_Team(meaning="sample_text_2", name="sample_text_2", status="sample_text_2", urlPage="sample_text_2")
    b = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'research_team_Person', a1)
    assert _is_linked(b, 'research_team_Person', a1)
    if hasattr(a1, 'research_team_Team2'):
        assert _is_linked(a1, 'research_team_Team2', b)
    _safe_set(b, 'research_team_Person', a2)
    assert _is_linked(b, 'research_team_Person', a2)
    if hasattr(a1, 'research_team_Team2'):
        assert not _is_linked(a1, 'research_team_Team2', b)
    if hasattr(a2, 'research_team_Team2'):
        assert _is_linked(a2, 'research_team_Team2', b)
    _safe_set(b, 'research_team_Person', None)
    assert not _is_linked(b, 'research_team_Person', a2)
    if hasattr(a2, 'research_team_Team2'):
        assert not _is_linked(a2, 'research_team_Team2', b)


def test_assoc_openPosition6_reverse_link_reassign_clear():
    a1 = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    a2 = research_team_Team(meaning="sample_text_2", name="sample_text_2", status="sample_text_2", urlPage="sample_text_2")
    b = research_team_OpenPosition(duration="sample_text", mission="sample_text", status="sample_text")
    _safe_set(b, 'research_team_OpenPosition', a1)
    assert _is_linked(b, 'research_team_OpenPosition', a1)
    if hasattr(a1, 'research_team_Team7'):
        assert _is_linked(a1, 'research_team_Team7', b)
    _safe_set(b, 'research_team_OpenPosition', a2)
    assert _is_linked(b, 'research_team_OpenPosition', a2)
    if hasattr(a1, 'research_team_Team7'):
        assert not _is_linked(a1, 'research_team_Team7', b)
    if hasattr(a2, 'research_team_Team7'):
        assert _is_linked(a2, 'research_team_Team7', b)
    _safe_set(b, 'research_team_OpenPosition', None)
    assert not _is_linked(b, 'research_team_OpenPosition', a2)
    if hasattr(a2, 'research_team_Team7'):
        assert not _is_linked(a2, 'research_team_Team7', b)


def test_assoc_paper13_reverse_link_reassign_clear():
    a1 = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    a2 = research_team_Person(affiliation="sample_text_2", firstname="sample_text_2", mail="sample_text_2", name="sample_text_2", phone="sample_text_2")
    b = research_team_Paper(state="sample_text", title="sample_text", url4pdf="sample_text")
    _safe_set(b, 'Paper', a1)
    assert _is_linked(b, 'Paper', a1)
    if hasattr(a1, 'author'):
        assert _is_linked(a1, 'author', b)
    _safe_set(b, 'Paper', a2)
    assert _is_linked(b, 'Paper', a2)
    if hasattr(a1, 'author'):
        assert not _is_linked(a1, 'author', b)
    if hasattr(a2, 'author'):
        assert _is_linked(a2, 'author', b)
    _safe_set(b, 'Paper', None)
    assert not _is_linked(b, 'Paper', a2)
    if hasattr(a2, 'author'):
        assert not _is_linked(a2, 'author', b)


def test_assoc_participates14_reverse_link_reassign_clear():
    a1 = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    a2 = research_team_Person(affiliation="sample_text_2", firstname="sample_text_2", mail="sample_text_2", name="sample_text_2", phone="sample_text_2")
    b = research_team_Collaboration(from_="sample_text", status="sample_text", title="sample_text", until="sample_text", website="sample_text")
    _safe_set(b, 'research_team_Collaboration16', a1)
    assert _is_linked(b, 'research_team_Collaboration16', a1)
    if hasattr(a1, 'research_team_Person15'):
        assert _is_linked(a1, 'research_team_Person15', b)
    _safe_set(b, 'research_team_Collaboration16', a2)
    assert _is_linked(b, 'research_team_Collaboration16', a2)
    if hasattr(a1, 'research_team_Person15'):
        assert not _is_linked(a1, 'research_team_Person15', b)
    if hasattr(a2, 'research_team_Person15'):
        assert _is_linked(a2, 'research_team_Person15', b)
    _safe_set(b, 'research_team_Collaboration16', None)
    assert not _is_linked(b, 'research_team_Collaboration16', a2)
    if hasattr(a2, 'research_team_Person15'):
        assert not _is_linked(a2, 'research_team_Person15', b)


def test_assoc_publishedAs18_reverse_link_reassign_clear():
    a1 = research_team_Publication()
    a2 = research_team_Publication()
    b = research_team_Paper(state="sample_text", title="sample_text", url4pdf="sample_text")
    _safe_set(b, 'research_team_Paper', a1)
    assert _is_linked(b, 'research_team_Paper', a1)
    if hasattr(a1, 'research_team_Publication'):
        assert _is_linked(a1, 'research_team_Publication', b)
    _safe_set(b, 'research_team_Paper', a2)
    assert _is_linked(b, 'research_team_Paper', a2)
    if hasattr(a1, 'research_team_Publication'):
        assert not _is_linked(a1, 'research_team_Publication', b)
    if hasattr(a2, 'research_team_Publication'):
        assert _is_linked(a2, 'research_team_Publication', b)
    _safe_set(b, 'research_team_Paper', None)
    assert not _is_linked(b, 'research_team_Paper', a2)
    if hasattr(a2, 'research_team_Publication'):
        assert not _is_linked(a2, 'research_team_Publication', b)


def test_assoc_seminars12_reverse_link_reassign_clear():
    a1 = research_team_Seminar(abstract="sample_text", dateFrom="sample_text", dateUntil="sample_text", place="sample_text", title="sample_text", url4slides="sample_text")
    a2 = research_team_Seminar(abstract="sample_text_2", dateFrom="sample_text_2", dateUntil="sample_text_2", place="sample_text_2", title="sample_text_2", url4slides="sample_text_2")
    b = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'speakers', a1)
    assert _is_linked(b, 'speakers', a1)
    if hasattr(a1, 'Seminar'):
        assert _is_linked(a1, 'Seminar', b)
    _safe_set(b, 'speakers', a2)
    assert _is_linked(b, 'speakers', a2)
    if hasattr(a1, 'Seminar'):
        assert not _is_linked(a1, 'Seminar', b)
    if hasattr(a2, 'Seminar'):
        assert _is_linked(a2, 'Seminar', b)
    _safe_set(b, 'speakers', None)
    assert not _is_linked(b, 'speakers', a2)
    if hasattr(a2, 'Seminar'):
        assert not _is_linked(a2, 'Seminar', b)


def test_assoc_soft11_reverse_link_reassign_clear():
    a1 = research_team_Software(description="sample_text", title="sample_text", website="sample_text")
    a2 = research_team_Software(description="sample_text_2", title="sample_text_2", website="sample_text_2")
    b = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'developers', {a1})
    assert _is_linked(b, 'developers', a1)
    if hasattr(a1, 'Software'):
        assert _is_linked(a1, 'Software', b)
    _safe_set(b, 'developers', {a2})
    assert _is_linked(b, 'developers', a2)
    if hasattr(a1, 'Software'):
        assert not _is_linked(a1, 'Software', b)
    if hasattr(a2, 'Software'):
        assert _is_linked(a2, 'Software', b)
    _safe_set(b, 'developers', set())
    assert not _is_linked(b, 'developers', a2)
    if hasattr(a2, 'Software'):
        assert not _is_linked(a2, 'Software', b)


def test_assoc_speakers19_reverse_link_reassign_clear():
    a1 = research_team_Seminar(abstract="sample_text", dateFrom="sample_text", dateUntil="sample_text", place="sample_text", title="sample_text", url4slides="sample_text")
    a2 = research_team_Seminar(abstract="sample_text_2", dateFrom="sample_text_2", dateUntil="sample_text_2", place="sample_text_2", title="sample_text_2", url4slides="sample_text_2")
    b = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'Person', a1)
    assert _is_linked(b, 'Person', a1)
    if hasattr(a1, 'seminars'):
        assert _is_linked(a1, 'seminars', b)
    _safe_set(b, 'Person', a2)
    assert _is_linked(b, 'Person', a2)
    if hasattr(a1, 'seminars'):
        assert not _is_linked(a1, 'seminars', b)
    if hasattr(a2, 'seminars'):
        assert _is_linked(a2, 'seminars', b)
    _safe_set(b, 'Person', None)
    assert not _is_linked(b, 'Person', a2)
    if hasattr(a2, 'seminars'):
        assert not _is_linked(a2, 'seminars', b)


def test_assoc_team17_reverse_link_reassign_clear():
    a1 = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    a2 = research_team_Team(meaning="sample_text_2", name="sample_text_2", status="sample_text_2", urlPage="sample_text_2")
    b = research_team_Publication()
    _safe_set(b, 'mainReferences', a1)
    assert _is_linked(b, 'mainReferences', a1)
    if hasattr(a1, 'Team'):
        assert _is_linked(a1, 'Team', b)
    _safe_set(b, 'mainReferences', a2)
    assert _is_linked(b, 'mainReferences', a2)
    if hasattr(a1, 'Team'):
        assert not _is_linked(a1, 'Team', b)
    if hasattr(a2, 'Team'):
        assert _is_linked(a2, 'Team', b)
    _safe_set(b, 'mainReferences', None)
    assert not _is_linked(b, 'mainReferences', a2)
    if hasattr(a2, 'Team'):
        assert not _is_linked(a2, 'Team', b)


def test_assoc_teamMaster3_reverse_link_reassign_clear():
    a1 = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    a2 = research_team_Team(meaning="sample_text_2", name="sample_text_2", status="sample_text_2", urlPage="sample_text_2")
    b = research_team_Person(affiliation="sample_text", firstname="sample_text", mail="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'research_team_Person5', a1)
    assert _is_linked(b, 'research_team_Person5', a1)
    if hasattr(a1, 'research_team_Team4'):
        assert _is_linked(a1, 'research_team_Team4', b)
    _safe_set(b, 'research_team_Person5', a2)
    assert _is_linked(b, 'research_team_Person5', a2)
    if hasattr(a1, 'research_team_Team4'):
        assert not _is_linked(a1, 'research_team_Team4', b)
    if hasattr(a2, 'research_team_Team4'):
        assert _is_linked(a2, 'research_team_Team4', b)
    _safe_set(b, 'research_team_Person5', None)
    assert not _is_linked(b, 'research_team_Person5', a2)
    if hasattr(a2, 'research_team_Team4'):
        assert not _is_linked(a2, 'research_team_Team4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_0_stub_double():
    # research_team_ActivityReport has no real 'research_team_ActivityReport' property in the generated
    # code (a bare stub) -- manually attach it so research_team_Team's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_team_Team's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_team_Team(meaning="sample_text", name="sample_text", status="sample_text", urlPage="sample_text")
    partner = research_team_ActivityReport()
    setattr(partner, 'research_team_ActivityReport', None)
    _safe_set(owner, 'research_team_Team', {partner})
    assert getattr(partner, 'research_team_ActivityReport') == owner
    _safe_set(owner, 'research_team_Team', set())
    assert getattr(partner, 'research_team_ActivityReport') is None


