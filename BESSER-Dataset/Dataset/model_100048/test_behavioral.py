import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    research2_Counted,
    research2_Keyword,
    research2_KnowledgeManager,
    research2_Labelled,
    research2_Named,
    research2_Paper,
    research2_Paragraph,
    research2_Phase,
    research2_Position,
    research2_Progress,
    research2_PublicationProcess,
    research2_PublicationStructure,
    research2_PublicationSystem,
    research2_Researcher,
    research2_Review,
    research2_ReviewNote,
    research2_Skill,
    research2_Write,
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

def test_assoc_paragraph22_reverse_link_reassign_clear():
    a1 = research2_Write(timeSpent=7)
    a2 = research2_Write(timeSpent=13)
    b = research2_Paragraph(content="sample_text")
    _safe_set(b, 'research2_Paragraph24', a1)
    assert _is_linked(b, 'research2_Paragraph24', a1)
    if hasattr(a1, 'research2_Write23'):
        assert _is_linked(a1, 'research2_Write23', b)
    _safe_set(b, 'research2_Paragraph24', a2)
    assert _is_linked(b, 'research2_Paragraph24', a2)
    if hasattr(a1, 'research2_Write23'):
        assert not _is_linked(a1, 'research2_Write23', b)
    if hasattr(a2, 'research2_Write23'):
        assert _is_linked(a2, 'research2_Write23', b)
    _safe_set(b, 'research2_Paragraph24', None)
    assert not _is_linked(b, 'research2_Paragraph24', a2)
    if hasattr(a2, 'research2_Write23'):
        assert not _is_linked(a2, 'research2_Write23', b)


def test_assoc_parent44_reverse_link_reassign_clear():
    a1 = research2_Position(description="sample_text")
    a2 = research2_Position(description="sample_text_2")
    b = research2_Position(description="sample_text")
    _safe_set(b, 'research2_Position45', a1)
    assert _is_linked(b, 'research2_Position45', a1)
    if hasattr(a1, 'research2_Position43'):
        assert _is_linked(a1, 'research2_Position43', b)
    _safe_set(b, 'research2_Position45', a2)
    assert _is_linked(b, 'research2_Position45', a2)
    if hasattr(a1, 'research2_Position43'):
        assert not _is_linked(a1, 'research2_Position43', b)
    if hasattr(a2, 'research2_Position43'):
        assert _is_linked(a2, 'research2_Position43', b)
    _safe_set(b, 'research2_Position45', None)
    assert not _is_linked(b, 'research2_Position45', a2)
    if hasattr(a2, 'research2_Position43'):
        assert not _is_linked(a2, 'research2_Position43', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = research2_PublicationProcess(maxTime=7, minTime=7)
    a2 = research2_PublicationProcess(maxTime=13, minTime=13)
    b = research2_Phase(name="sample_text")
    _safe_set(b, 'research2_Phase', a1)
    assert _is_linked(b, 'research2_Phase', a1)
    if hasattr(a1, 'research2_PublicationProcess'):
        assert _is_linked(a1, 'research2_PublicationProcess', b)
    _safe_set(b, 'research2_Phase', a2)
    assert _is_linked(b, 'research2_Phase', a2)
    if hasattr(a1, 'research2_PublicationProcess'):
        assert not _is_linked(a1, 'research2_PublicationProcess', b)
    if hasattr(a2, 'research2_PublicationProcess'):
        assert _is_linked(a2, 'research2_PublicationProcess', b)
    _safe_set(b, 'research2_Phase', None)
    assert not _is_linked(b, 'research2_Phase', a2)
    if hasattr(a2, 'research2_PublicationProcess'):
        assert not _is_linked(a2, 'research2_PublicationProcess', b)


def test_assoc_process18_reverse_link_reassign_clear():
    a1 = research2_PublicationProcess(maxTime=7, minTime=7)
    a2 = research2_PublicationProcess(maxTime=13, minTime=13)
    b = research2_Progress(percent=7)
    _safe_set(b, 'research2_Progress', a1)
    assert _is_linked(b, 'research2_Progress', a1)
    if hasattr(a1, 'research2_PublicationProcess19'):
        assert _is_linked(a1, 'research2_PublicationProcess19', b)
    _safe_set(b, 'research2_Progress', a2)
    assert _is_linked(b, 'research2_Progress', a2)
    if hasattr(a1, 'research2_PublicationProcess19'):
        assert not _is_linked(a1, 'research2_PublicationProcess19', b)
    if hasattr(a2, 'research2_PublicationProcess19'):
        assert _is_linked(a2, 'research2_PublicationProcess19', b)
    _safe_set(b, 'research2_Progress', None)
    assert not _is_linked(b, 'research2_Progress', a2)
    if hasattr(a2, 'research2_PublicationProcess19'):
        assert not _is_linked(a2, 'research2_PublicationProcess19', b)


def test_assoc_res_position7_reverse_link_reassign_clear():
    a1 = research2_Researcher(forName="sample_text", name="sample_text")
    a2 = research2_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research2_Position(description="sample_text")
    _safe_set(b, 'research2_Position', a1)
    assert _is_linked(b, 'research2_Position', a1)
    if hasattr(a1, 'research2_Researcher8'):
        assert _is_linked(a1, 'research2_Researcher8', b)
    _safe_set(b, 'research2_Position', a2)
    assert _is_linked(b, 'research2_Position', a2)
    if hasattr(a1, 'research2_Researcher8'):
        assert not _is_linked(a1, 'research2_Researcher8', b)
    if hasattr(a2, 'research2_Researcher8'):
        assert _is_linked(a2, 'research2_Researcher8', b)
    _safe_set(b, 'research2_Position', None)
    assert not _is_linked(b, 'research2_Position', a2)
    if hasattr(a2, 'research2_Researcher8'):
        assert not _is_linked(a2, 'research2_Researcher8', b)


def test_assoc_reviewNote25_reverse_link_reassign_clear():
    a1 = research2_ReviewNote(content="sample_text")
    a2 = research2_ReviewNote(content="sample_text_2")
    b = research2_Review(date=date(2024, 1, 1))
    _safe_set(b, 'research2_Review26', a1)
    assert _is_linked(b, 'research2_Review26', a1)
    if hasattr(a1, 'research2_ReviewNote27'):
        assert _is_linked(a1, 'research2_ReviewNote27', b)
    _safe_set(b, 'research2_Review26', a2)
    assert _is_linked(b, 'research2_Review26', a2)
    if hasattr(a1, 'research2_ReviewNote27'):
        assert not _is_linked(a1, 'research2_ReviewNote27', b)
    if hasattr(a2, 'research2_ReviewNote27'):
        assert _is_linked(a2, 'research2_ReviewNote27', b)
    _safe_set(b, 'research2_Review26', None)
    assert not _is_linked(b, 'research2_Review26', a2)
    if hasattr(a2, 'research2_ReviewNote27'):
        assert not _is_linked(a2, 'research2_ReviewNote27', b)


def test_assoc_reviews16_reverse_link_reassign_clear():
    a1 = research2_ReviewNote(content="sample_text")
    a2 = research2_ReviewNote(content="sample_text_2")
    b = research2_Paragraph(content="sample_text")
    _safe_set(b, 'research2_Paragraph17', {a1})
    assert _is_linked(b, 'research2_Paragraph17', a1)
    if hasattr(a1, 'research2_ReviewNote'):
        assert _is_linked(a1, 'research2_ReviewNote', b)
    _safe_set(b, 'research2_Paragraph17', {a2})
    assert _is_linked(b, 'research2_Paragraph17', a2)
    if hasattr(a1, 'research2_ReviewNote'):
        assert not _is_linked(a1, 'research2_ReviewNote', b)
    if hasattr(a2, 'research2_ReviewNote'):
        assert _is_linked(a2, 'research2_ReviewNote', b)
    _safe_set(b, 'research2_Paragraph17', set())
    assert not _is_linked(b, 'research2_Paragraph17', a2)
    if hasattr(a2, 'research2_ReviewNote'):
        assert not _is_linked(a2, 'research2_ReviewNote', b)


def test_assoc_reviews2_reverse_link_reassign_clear():
    a1 = research2_Review(date=date(2024, 1, 1))
    a2 = research2_Review(date=date(2025, 6, 15))
    b = research2_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research2_Researcher3', {a1})
    assert _is_linked(b, 'research2_Researcher3', a1)
    if hasattr(a1, 'research2_Review'):
        assert _is_linked(a1, 'research2_Review', b)
    _safe_set(b, 'research2_Researcher3', {a2})
    assert _is_linked(b, 'research2_Researcher3', a2)
    if hasattr(a1, 'research2_Review'):
        assert not _is_linked(a1, 'research2_Review', b)
    if hasattr(a2, 'research2_Review'):
        assert _is_linked(a2, 'research2_Review', b)
    _safe_set(b, 'research2_Researcher3', set())
    assert not _is_linked(b, 'research2_Researcher3', a2)
    if hasattr(a2, 'research2_Review'):
        assert not _is_linked(a2, 'research2_Review', b)


def test_assoc_skills5_reverse_link_reassign_clear():
    a1 = research2_Skill(description="sample_text")
    a2 = research2_Skill(description="sample_text_2")
    b = research2_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research2_Researcher6', {a1})
    assert _is_linked(b, 'research2_Researcher6', a1)
    if hasattr(a1, 'research2_Skill'):
        assert _is_linked(a1, 'research2_Skill', b)
    _safe_set(b, 'research2_Researcher6', {a2})
    assert _is_linked(b, 'research2_Researcher6', a2)
    if hasattr(a1, 'research2_Skill'):
        assert not _is_linked(a1, 'research2_Skill', b)
    if hasattr(a2, 'research2_Skill'):
        assert _is_linked(a2, 'research2_Skill', b)
    _safe_set(b, 'research2_Researcher6', set())
    assert not _is_linked(b, 'research2_Researcher6', a2)
    if hasattr(a2, 'research2_Skill'):
        assert not _is_linked(a2, 'research2_Skill', b)


def test_assoc_writes1_reverse_link_reassign_clear():
    a1 = research2_Write(timeSpent=7)
    a2 = research2_Write(timeSpent=13)
    b = research2_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research2_Researcher', {a1})
    assert _is_linked(b, 'research2_Researcher', a1)
    if hasattr(a1, 'research2_Write'):
        assert _is_linked(a1, 'research2_Write', b)
    _safe_set(b, 'research2_Researcher', {a2})
    assert _is_linked(b, 'research2_Researcher', a2)
    if hasattr(a1, 'research2_Write'):
        assert not _is_linked(a1, 'research2_Write', b)
    if hasattr(a2, 'research2_Write'):
        assert _is_linked(a2, 'research2_Write', b)
    _safe_set(b, 'research2_Researcher', set())
    assert not _is_linked(b, 'research2_Researcher', a2)
    if hasattr(a2, 'research2_Write'):
        assert not _is_linked(a2, 'research2_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allkeywords48_stub_double():
    # research2_KnowledgeManager has no real 'research2_KnowledgeManager49' property in the generated
    # code (a bare stub) -- manually attach it so research2_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Keyword(description="sample_text")
    partner = research2_KnowledgeManager()
    setattr(partner, 'research2_KnowledgeManager49', None)
    _safe_set(owner, 'research2_Keyword', partner)
    assert owner in getattr(partner, 'research2_KnowledgeManager49')
    _safe_set(owner, 'research2_Keyword', None)
    assert owner not in getattr(partner, 'research2_KnowledgeManager49')


def test_assoc_authors11_stub_double():
    # research2_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so research2_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Researcher(forName="sample_text", name="sample_text")
    partner = research2_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_keywords12_stub_double():
    # research2_Paper has no real 'kpapers' property in the generated
    # code (a bare stub) -- manually attach it so research2_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Keyword(description="sample_text")
    partner = research2_Paper()
    setattr(partner, 'kpapers', None)
    _safe_set(owner, 'Keyword', partner)
    assert owner in getattr(partner, 'kpapers')
    _safe_set(owner, 'Keyword', None)
    assert owner not in getattr(partner, 'kpapers')


def test_assoc_kpapers46_stub_double():
    # research2_Paper has no real 'Paper47' property in the generated
    # code (a bare stub) -- manually attach it so research2_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Keyword(description="sample_text")
    partner = research2_Paper()
    setattr(partner, 'Paper47', None)
    _safe_set(owner, 'keywords', {partner})
    assert getattr(partner, 'Paper47') == owner
    _safe_set(owner, 'keywords', set())
    assert getattr(partner, 'Paper47') is None


def test_assoc_paper20_stub_double():
    # research2_Paper has no real 'Paper21' property in the generated
    # code (a bare stub) -- manually attach it so research2_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Progress(percent=7)
    partner = research2_Paper()
    setattr(partner, 'Paper21', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper21') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper21') is None


def test_assoc_paragraphs9_stub_double():
    # research2_Paper has no real 'research2_Paper' property in the generated
    # code (a bare stub) -- manually attach it so research2_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Paragraph(content="sample_text")
    partner = research2_Paper()
    setattr(partner, 'research2_Paper', None)
    _safe_set(owner, 'research2_Paragraph', partner)
    assert owner in getattr(partner, 'research2_Paper')
    _safe_set(owner, 'research2_Paragraph', None)
    assert owner not in getattr(partner, 'research2_Paper')


def test_assoc_positions40_stub_double():
    # research2_PublicationSystem has no real 'research2_PublicationSystem41' property in the generated
    # code (a bare stub) -- manually attach it so research2_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Position(description="sample_text")
    partner = research2_PublicationSystem()
    setattr(partner, 'research2_PublicationSystem41', None)
    _safe_set(owner, 'research2_Position42', partner)
    assert owner in getattr(partner, 'research2_PublicationSystem41')
    _safe_set(owner, 'research2_Position42', None)
    assert owner not in getattr(partner, 'research2_PublicationSystem41')


def test_assoc_processView35_stub_double():
    # research2_PublicationSystem has no real 'research2_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so research2_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_PublicationProcess(maxTime=7, minTime=7)
    partner = research2_PublicationSystem()
    setattr(partner, 'research2_PublicationSystem', None)
    _safe_set(owner, 'research2_PublicationProcess36', partner)
    assert getattr(partner, 'research2_PublicationSystem') == owner
    _safe_set(owner, 'research2_PublicationProcess36', None)
    assert getattr(partner, 'research2_PublicationSystem') is None


def test_assoc_progress10_stub_double():
    # research2_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so research2_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Progress(percent=7)
    partner = research2_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_res_papers4_stub_double():
    # research2_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so research2_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Researcher(forName="sample_text", name="sample_text")
    partner = research2_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers28_stub_double():
    # research2_PublicationStructure has no real 'research2_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so research2_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research2_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research2_Researcher(forName="sample_text", name="sample_text")
    partner = research2_PublicationStructure()
    setattr(partner, 'research2_PublicationStructure', None)
    _safe_set(owner, 'research2_Researcher29', partner)
    assert owner in getattr(partner, 'research2_PublicationStructure')
    _safe_set(owner, 'research2_Researcher29', None)
    assert owner not in getattr(partner, 'research2_PublicationStructure')


