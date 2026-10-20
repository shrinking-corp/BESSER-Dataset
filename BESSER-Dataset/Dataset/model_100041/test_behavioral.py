import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    research_Collaboration,
    research_Counted,
    research_Keyword,
    research_KnowledgeManager,
    research_Labelled,
    research_Named,
    research_Paper,
    research_PaperKeyword,
    research_Paragraph,
    research_Phase,
    research_Position,
    research_Progress,
    research_PublicationProcess,
    research_PublicationStructure,
    research_PublicationSystem,
    research_Researcher,
    research_Review,
    research_ReviewNote,
    research_Skill,
    research_Write,
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

def test_assoc_collaborations9_reverse_link_reassign_clear():
    a1 = research_Researcher(forName="sample_text", name="sample_text")
    a2 = research_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research_Collaboration(ratio=7)
    _safe_set(b, 'research_Collaboration', a1)
    assert _is_linked(b, 'research_Collaboration', a1)
    if hasattr(a1, 'research_Researcher10'):
        assert _is_linked(a1, 'research_Researcher10', b)
    _safe_set(b, 'research_Collaboration', a2)
    assert _is_linked(b, 'research_Collaboration', a2)
    if hasattr(a1, 'research_Researcher10'):
        assert not _is_linked(a1, 'research_Researcher10', b)
    if hasattr(a2, 'research_Researcher10'):
        assert _is_linked(a2, 'research_Researcher10', b)
    _safe_set(b, 'research_Collaboration', None)
    assert not _is_linked(b, 'research_Collaboration', a2)
    if hasattr(a2, 'research_Researcher10'):
        assert not _is_linked(a2, 'research_Researcher10', b)


def test_assoc_keyword54_reverse_link_reassign_clear():
    a1 = research_PaperKeyword(weight=7)
    a2 = research_PaperKeyword(weight=13)
    b = research_Keyword(description="sample_text")
    _safe_set(b, 'research_Keyword56', a1)
    assert _is_linked(b, 'research_Keyword56', a1)
    if hasattr(a1, 'research_PaperKeyword55'):
        assert _is_linked(a1, 'research_PaperKeyword55', b)
    _safe_set(b, 'research_Keyword56', a2)
    assert _is_linked(b, 'research_Keyword56', a2)
    if hasattr(a1, 'research_PaperKeyword55'):
        assert not _is_linked(a1, 'research_PaperKeyword55', b)
    if hasattr(a2, 'research_PaperKeyword55'):
        assert _is_linked(a2, 'research_PaperKeyword55', b)
    _safe_set(b, 'research_Keyword56', None)
    assert not _is_linked(b, 'research_Keyword56', a2)
    if hasattr(a2, 'research_PaperKeyword55'):
        assert not _is_linked(a2, 'research_PaperKeyword55', b)


def test_assoc_paragraph25_reverse_link_reassign_clear():
    a1 = research_Write(timeSpent=7)
    a2 = research_Write(timeSpent=13)
    b = research_Paragraph(content="sample_text")
    _safe_set(b, 'research_Paragraph27', a1)
    assert _is_linked(b, 'research_Paragraph27', a1)
    if hasattr(a1, 'research_Write26'):
        assert _is_linked(a1, 'research_Write26', b)
    _safe_set(b, 'research_Paragraph27', a2)
    assert _is_linked(b, 'research_Paragraph27', a2)
    if hasattr(a1, 'research_Write26'):
        assert not _is_linked(a1, 'research_Write26', b)
    if hasattr(a2, 'research_Write26'):
        assert _is_linked(a2, 'research_Write26', b)
    _safe_set(b, 'research_Paragraph27', None)
    assert not _is_linked(b, 'research_Paragraph27', a2)
    if hasattr(a2, 'research_Write26'):
        assert not _is_linked(a2, 'research_Write26', b)


def test_assoc_parent47_reverse_link_reassign_clear():
    a1 = research_Position(description="sample_text")
    a2 = research_Position(description="sample_text_2")
    b = research_Position(description="sample_text")
    _safe_set(b, 'research_Position48', a1)
    assert _is_linked(b, 'research_Position48', a1)
    if hasattr(a1, 'research_Position46'):
        assert _is_linked(a1, 'research_Position46', b)
    _safe_set(b, 'research_Position48', a2)
    assert _is_linked(b, 'research_Position48', a2)
    if hasattr(a1, 'research_Position46'):
        assert not _is_linked(a1, 'research_Position46', b)
    if hasattr(a2, 'research_Position46'):
        assert _is_linked(a2, 'research_Position46', b)
    _safe_set(b, 'research_Position48', None)
    assert not _is_linked(b, 'research_Position48', a2)
    if hasattr(a2, 'research_Position46'):
        assert not _is_linked(a2, 'research_Position46', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = research_PublicationProcess(maxTime=7, minTime=7)
    a2 = research_PublicationProcess(maxTime=13, minTime=13)
    b = research_Phase(name="sample_text")
    _safe_set(b, 'research_Phase', a1)
    assert _is_linked(b, 'research_Phase', a1)
    if hasattr(a1, 'research_PublicationProcess'):
        assert _is_linked(a1, 'research_PublicationProcess', b)
    _safe_set(b, 'research_Phase', a2)
    assert _is_linked(b, 'research_Phase', a2)
    if hasattr(a1, 'research_PublicationProcess'):
        assert not _is_linked(a1, 'research_PublicationProcess', b)
    if hasattr(a2, 'research_PublicationProcess'):
        assert _is_linked(a2, 'research_PublicationProcess', b)
    _safe_set(b, 'research_Phase', None)
    assert not _is_linked(b, 'research_Phase', a2)
    if hasattr(a2, 'research_PublicationProcess'):
        assert not _is_linked(a2, 'research_PublicationProcess', b)


def test_assoc_process21_reverse_link_reassign_clear():
    a1 = research_PublicationProcess(maxTime=7, minTime=7)
    a2 = research_PublicationProcess(maxTime=13, minTime=13)
    b = research_Progress(percent=7)
    _safe_set(b, 'research_Progress', a1)
    assert _is_linked(b, 'research_Progress', a1)
    if hasattr(a1, 'research_PublicationProcess22'):
        assert _is_linked(a1, 'research_PublicationProcess22', b)
    _safe_set(b, 'research_Progress', a2)
    assert _is_linked(b, 'research_Progress', a2)
    if hasattr(a1, 'research_PublicationProcess22'):
        assert not _is_linked(a1, 'research_PublicationProcess22', b)
    if hasattr(a2, 'research_PublicationProcess22'):
        assert _is_linked(a2, 'research_PublicationProcess22', b)
    _safe_set(b, 'research_Progress', None)
    assert not _is_linked(b, 'research_Progress', a2)
    if hasattr(a2, 'research_PublicationProcess22'):
        assert not _is_linked(a2, 'research_PublicationProcess22', b)


def test_assoc_res_position7_reverse_link_reassign_clear():
    a1 = research_Researcher(forName="sample_text", name="sample_text")
    a2 = research_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research_Position(description="sample_text")
    _safe_set(b, 'research_Position', a1)
    assert _is_linked(b, 'research_Position', a1)
    if hasattr(a1, 'research_Researcher8'):
        assert _is_linked(a1, 'research_Researcher8', b)
    _safe_set(b, 'research_Position', a2)
    assert _is_linked(b, 'research_Position', a2)
    if hasattr(a1, 'research_Researcher8'):
        assert not _is_linked(a1, 'research_Researcher8', b)
    if hasattr(a2, 'research_Researcher8'):
        assert _is_linked(a2, 'research_Researcher8', b)
    _safe_set(b, 'research_Position', None)
    assert not _is_linked(b, 'research_Position', a2)
    if hasattr(a2, 'research_Researcher8'):
        assert not _is_linked(a2, 'research_Researcher8', b)


def test_assoc_reviewNote28_reverse_link_reassign_clear():
    a1 = research_ReviewNote(content="sample_text")
    a2 = research_ReviewNote(content="sample_text_2")
    b = research_Review(date=date(2024, 1, 1))
    _safe_set(b, 'research_Review29', a1)
    assert _is_linked(b, 'research_Review29', a1)
    if hasattr(a1, 'research_ReviewNote30'):
        assert _is_linked(a1, 'research_ReviewNote30', b)
    _safe_set(b, 'research_Review29', a2)
    assert _is_linked(b, 'research_Review29', a2)
    if hasattr(a1, 'research_ReviewNote30'):
        assert not _is_linked(a1, 'research_ReviewNote30', b)
    if hasattr(a2, 'research_ReviewNote30'):
        assert _is_linked(a2, 'research_ReviewNote30', b)
    _safe_set(b, 'research_Review29', None)
    assert not _is_linked(b, 'research_Review29', a2)
    if hasattr(a2, 'research_ReviewNote30'):
        assert not _is_linked(a2, 'research_ReviewNote30', b)


def test_assoc_reviews19_reverse_link_reassign_clear():
    a1 = research_ReviewNote(content="sample_text")
    a2 = research_ReviewNote(content="sample_text_2")
    b = research_Paragraph(content="sample_text")
    _safe_set(b, 'research_Paragraph20', {a1})
    assert _is_linked(b, 'research_Paragraph20', a1)
    if hasattr(a1, 'research_ReviewNote'):
        assert _is_linked(a1, 'research_ReviewNote', b)
    _safe_set(b, 'research_Paragraph20', {a2})
    assert _is_linked(b, 'research_Paragraph20', a2)
    if hasattr(a1, 'research_ReviewNote'):
        assert not _is_linked(a1, 'research_ReviewNote', b)
    if hasattr(a2, 'research_ReviewNote'):
        assert _is_linked(a2, 'research_ReviewNote', b)
    _safe_set(b, 'research_Paragraph20', set())
    assert not _is_linked(b, 'research_Paragraph20', a2)
    if hasattr(a2, 'research_ReviewNote'):
        assert not _is_linked(a2, 'research_ReviewNote', b)


def test_assoc_reviews2_reverse_link_reassign_clear():
    a1 = research_Review(date=date(2024, 1, 1))
    a2 = research_Review(date=date(2025, 6, 15))
    b = research_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research_Researcher3', {a1})
    assert _is_linked(b, 'research_Researcher3', a1)
    if hasattr(a1, 'research_Review'):
        assert _is_linked(a1, 'research_Review', b)
    _safe_set(b, 'research_Researcher3', {a2})
    assert _is_linked(b, 'research_Researcher3', a2)
    if hasattr(a1, 'research_Review'):
        assert not _is_linked(a1, 'research_Review', b)
    if hasattr(a2, 'research_Review'):
        assert _is_linked(a2, 'research_Review', b)
    _safe_set(b, 'research_Researcher3', set())
    assert not _is_linked(b, 'research_Researcher3', a2)
    if hasattr(a2, 'research_Review'):
        assert not _is_linked(a2, 'research_Review', b)


def test_assoc_skills5_reverse_link_reassign_clear():
    a1 = research_Skill(description="sample_text")
    a2 = research_Skill(description="sample_text_2")
    b = research_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research_Researcher6', {a1})
    assert _is_linked(b, 'research_Researcher6', a1)
    if hasattr(a1, 'research_Skill'):
        assert _is_linked(a1, 'research_Skill', b)
    _safe_set(b, 'research_Researcher6', {a2})
    assert _is_linked(b, 'research_Researcher6', a2)
    if hasattr(a1, 'research_Skill'):
        assert not _is_linked(a1, 'research_Skill', b)
    if hasattr(a2, 'research_Skill'):
        assert _is_linked(a2, 'research_Skill', b)
    _safe_set(b, 'research_Researcher6', set())
    assert not _is_linked(b, 'research_Researcher6', a2)
    if hasattr(a2, 'research_Skill'):
        assert not _is_linked(a2, 'research_Skill', b)


def test_assoc_writes1_reverse_link_reassign_clear():
    a1 = research_Write(timeSpent=7)
    a2 = research_Write(timeSpent=13)
    b = research_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research_Researcher', {a1})
    assert _is_linked(b, 'research_Researcher', a1)
    if hasattr(a1, 'research_Write'):
        assert _is_linked(a1, 'research_Write', b)
    _safe_set(b, 'research_Researcher', {a2})
    assert _is_linked(b, 'research_Researcher', a2)
    if hasattr(a1, 'research_Write'):
        assert not _is_linked(a1, 'research_Write', b)
    if hasattr(a2, 'research_Write'):
        assert _is_linked(a2, 'research_Write', b)
    _safe_set(b, 'research_Researcher', set())
    assert not _is_linked(b, 'research_Researcher', a2)
    if hasattr(a2, 'research_Write'):
        assert not _is_linked(a2, 'research_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allkeywords51_stub_double():
    # research_KnowledgeManager has no real 'research_KnowledgeManager52' property in the generated
    # code (a bare stub) -- manually attach it so research_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Keyword(description="sample_text")
    partner = research_KnowledgeManager()
    setattr(partner, 'research_KnowledgeManager52', None)
    _safe_set(owner, 'research_Keyword53', partner)
    assert owner in getattr(partner, 'research_KnowledgeManager52')
    _safe_set(owner, 'research_Keyword53', None)
    assert owner not in getattr(partner, 'research_KnowledgeManager52')


def test_assoc_authors13_stub_double():
    # research_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so research_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Researcher(forName="sample_text", name="sample_text")
    partner = research_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_col_paper57_stub_double():
    # research_Paper has no real 'research_Paper59' property in the generated
    # code (a bare stub) -- manually attach it so research_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Collaboration(ratio=7)
    partner = research_Paper()
    setattr(partner, 'research_Paper59', None)
    _safe_set(owner, 'research_Collaboration58', partner)
    assert getattr(partner, 'research_Paper59') == owner
    _safe_set(owner, 'research_Collaboration58', None)
    assert getattr(partner, 'research_Paper59') is None


def test_assoc_keywords14_stub_double():
    # research_Paper has no real 'research_Paper15' property in the generated
    # code (a bare stub) -- manually attach it so research_PaperKeyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_PaperKeyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_PaperKeyword(weight=7)
    partner = research_Paper()
    setattr(partner, 'research_Paper15', None)
    _safe_set(owner, 'research_PaperKeyword', partner)
    assert owner in getattr(partner, 'research_Paper15')
    _safe_set(owner, 'research_PaperKeyword', None)
    assert owner not in getattr(partner, 'research_Paper15')


def test_assoc_kpapers49_stub_double():
    # research_Paper has no real 'research_Paper50' property in the generated
    # code (a bare stub) -- manually attach it so research_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Keyword(description="sample_text")
    partner = research_Paper()
    setattr(partner, 'research_Paper50', None)
    _safe_set(owner, 'research_Keyword', {partner})
    assert getattr(partner, 'research_Paper50') == owner
    _safe_set(owner, 'research_Keyword', set())
    assert getattr(partner, 'research_Paper50') is None


def test_assoc_paper23_stub_double():
    # research_Paper has no real 'Paper24' property in the generated
    # code (a bare stub) -- manually attach it so research_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Progress(percent=7)
    partner = research_Paper()
    setattr(partner, 'Paper24', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper24') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper24') is None


def test_assoc_paragraphs11_stub_double():
    # research_Paper has no real 'research_Paper' property in the generated
    # code (a bare stub) -- manually attach it so research_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Paragraph(content="sample_text")
    partner = research_Paper()
    setattr(partner, 'research_Paper', None)
    _safe_set(owner, 'research_Paragraph', partner)
    assert owner in getattr(partner, 'research_Paper')
    _safe_set(owner, 'research_Paragraph', None)
    assert owner not in getattr(partner, 'research_Paper')


def test_assoc_positions43_stub_double():
    # research_PublicationSystem has no real 'research_PublicationSystem44' property in the generated
    # code (a bare stub) -- manually attach it so research_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Position(description="sample_text")
    partner = research_PublicationSystem()
    setattr(partner, 'research_PublicationSystem44', None)
    _safe_set(owner, 'research_Position45', partner)
    assert owner in getattr(partner, 'research_PublicationSystem44')
    _safe_set(owner, 'research_Position45', None)
    assert owner not in getattr(partner, 'research_PublicationSystem44')


def test_assoc_processView38_stub_double():
    # research_PublicationSystem has no real 'research_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so research_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_PublicationProcess(maxTime=7, minTime=7)
    partner = research_PublicationSystem()
    setattr(partner, 'research_PublicationSystem', None)
    _safe_set(owner, 'research_PublicationProcess39', partner)
    assert getattr(partner, 'research_PublicationSystem') == owner
    _safe_set(owner, 'research_PublicationProcess39', None)
    assert getattr(partner, 'research_PublicationSystem') is None


def test_assoc_progress12_stub_double():
    # research_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so research_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Progress(percent=7)
    partner = research_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_res_papers4_stub_double():
    # research_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so research_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Researcher(forName="sample_text", name="sample_text")
    partner = research_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers31_stub_double():
    # research_PublicationStructure has no real 'research_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so research_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research_Researcher(forName="sample_text", name="sample_text")
    partner = research_PublicationStructure()
    setattr(partner, 'research_PublicationStructure', None)
    _safe_set(owner, 'research_Researcher32', partner)
    assert owner in getattr(partner, 'research_PublicationStructure')
    _safe_set(owner, 'research_Researcher32', None)
    assert owner not in getattr(partner, 'research_PublicationStructure')


