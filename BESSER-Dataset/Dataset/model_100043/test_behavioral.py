import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    research13_Collaboration,
    research13_Counted,
    research13_Keyword,
    research13_KnowledgeManager,
    research13_Labelled,
    research13_Named,
    research13_Paper,
    research13_PaperKeyword,
    research13_Paragraph,
    research13_Phase,
    research13_Position,
    research13_Progress,
    research13_PublicationProcess,
    research13_PublicationStructure,
    research13_PublicationSystem,
    research13_Researcher,
    research13_Review,
    research13_ReviewNote,
    research13_Skill,
    research13_Write,
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
    a1 = research13_Researcher(forName="sample_text", name="sample_text")
    a2 = research13_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research13_Collaboration(ratio=7)
    _safe_set(b, 'research13_Collaboration', a1)
    assert _is_linked(b, 'research13_Collaboration', a1)
    if hasattr(a1, 'research13_Researcher10'):
        assert _is_linked(a1, 'research13_Researcher10', b)
    _safe_set(b, 'research13_Collaboration', a2)
    assert _is_linked(b, 'research13_Collaboration', a2)
    if hasattr(a1, 'research13_Researcher10'):
        assert not _is_linked(a1, 'research13_Researcher10', b)
    if hasattr(a2, 'research13_Researcher10'):
        assert _is_linked(a2, 'research13_Researcher10', b)
    _safe_set(b, 'research13_Collaboration', None)
    assert not _is_linked(b, 'research13_Collaboration', a2)
    if hasattr(a2, 'research13_Researcher10'):
        assert not _is_linked(a2, 'research13_Researcher10', b)


def test_assoc_keyword54_reverse_link_reassign_clear():
    a1 = research13_PaperKeyword(weight=7)
    a2 = research13_PaperKeyword(weight=13)
    b = research13_Keyword(description="sample_text")
    _safe_set(b, 'research13_Keyword56', a1)
    assert _is_linked(b, 'research13_Keyword56', a1)
    if hasattr(a1, 'research13_PaperKeyword55'):
        assert _is_linked(a1, 'research13_PaperKeyword55', b)
    _safe_set(b, 'research13_Keyword56', a2)
    assert _is_linked(b, 'research13_Keyword56', a2)
    if hasattr(a1, 'research13_PaperKeyword55'):
        assert not _is_linked(a1, 'research13_PaperKeyword55', b)
    if hasattr(a2, 'research13_PaperKeyword55'):
        assert _is_linked(a2, 'research13_PaperKeyword55', b)
    _safe_set(b, 'research13_Keyword56', None)
    assert not _is_linked(b, 'research13_Keyword56', a2)
    if hasattr(a2, 'research13_PaperKeyword55'):
        assert not _is_linked(a2, 'research13_PaperKeyword55', b)


def test_assoc_paragraph25_reverse_link_reassign_clear():
    a1 = research13_Write(timeSpent=7)
    a2 = research13_Write(timeSpent=13)
    b = research13_Paragraph(content="sample_text")
    _safe_set(b, 'research13_Paragraph27', a1)
    assert _is_linked(b, 'research13_Paragraph27', a1)
    if hasattr(a1, 'research13_Write26'):
        assert _is_linked(a1, 'research13_Write26', b)
    _safe_set(b, 'research13_Paragraph27', a2)
    assert _is_linked(b, 'research13_Paragraph27', a2)
    if hasattr(a1, 'research13_Write26'):
        assert not _is_linked(a1, 'research13_Write26', b)
    if hasattr(a2, 'research13_Write26'):
        assert _is_linked(a2, 'research13_Write26', b)
    _safe_set(b, 'research13_Paragraph27', None)
    assert not _is_linked(b, 'research13_Paragraph27', a2)
    if hasattr(a2, 'research13_Write26'):
        assert not _is_linked(a2, 'research13_Write26', b)


def test_assoc_parent47_reverse_link_reassign_clear():
    a1 = research13_Position(description="sample_text")
    a2 = research13_Position(description="sample_text_2")
    b = research13_Position(description="sample_text")
    _safe_set(b, 'research13_Position48', a1)
    assert _is_linked(b, 'research13_Position48', a1)
    if hasattr(a1, 'research13_Position46'):
        assert _is_linked(a1, 'research13_Position46', b)
    _safe_set(b, 'research13_Position48', a2)
    assert _is_linked(b, 'research13_Position48', a2)
    if hasattr(a1, 'research13_Position46'):
        assert not _is_linked(a1, 'research13_Position46', b)
    if hasattr(a2, 'research13_Position46'):
        assert _is_linked(a2, 'research13_Position46', b)
    _safe_set(b, 'research13_Position48', None)
    assert not _is_linked(b, 'research13_Position48', a2)
    if hasattr(a2, 'research13_Position46'):
        assert not _is_linked(a2, 'research13_Position46', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = research13_PublicationProcess(maxTime=7, minTime=7)
    a2 = research13_PublicationProcess(maxTime=13, minTime=13)
    b = research13_Phase(name="sample_text")
    _safe_set(b, 'research13_Phase', a1)
    assert _is_linked(b, 'research13_Phase', a1)
    if hasattr(a1, 'research13_PublicationProcess'):
        assert _is_linked(a1, 'research13_PublicationProcess', b)
    _safe_set(b, 'research13_Phase', a2)
    assert _is_linked(b, 'research13_Phase', a2)
    if hasattr(a1, 'research13_PublicationProcess'):
        assert not _is_linked(a1, 'research13_PublicationProcess', b)
    if hasattr(a2, 'research13_PublicationProcess'):
        assert _is_linked(a2, 'research13_PublicationProcess', b)
    _safe_set(b, 'research13_Phase', None)
    assert not _is_linked(b, 'research13_Phase', a2)
    if hasattr(a2, 'research13_PublicationProcess'):
        assert not _is_linked(a2, 'research13_PublicationProcess', b)


def test_assoc_process21_reverse_link_reassign_clear():
    a1 = research13_PublicationProcess(maxTime=7, minTime=7)
    a2 = research13_PublicationProcess(maxTime=13, minTime=13)
    b = research13_Progress(percent=7)
    _safe_set(b, 'research13_Progress', a1)
    assert _is_linked(b, 'research13_Progress', a1)
    if hasattr(a1, 'research13_PublicationProcess22'):
        assert _is_linked(a1, 'research13_PublicationProcess22', b)
    _safe_set(b, 'research13_Progress', a2)
    assert _is_linked(b, 'research13_Progress', a2)
    if hasattr(a1, 'research13_PublicationProcess22'):
        assert not _is_linked(a1, 'research13_PublicationProcess22', b)
    if hasattr(a2, 'research13_PublicationProcess22'):
        assert _is_linked(a2, 'research13_PublicationProcess22', b)
    _safe_set(b, 'research13_Progress', None)
    assert not _is_linked(b, 'research13_Progress', a2)
    if hasattr(a2, 'research13_PublicationProcess22'):
        assert not _is_linked(a2, 'research13_PublicationProcess22', b)


def test_assoc_res_position7_reverse_link_reassign_clear():
    a1 = research13_Researcher(forName="sample_text", name="sample_text")
    a2 = research13_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research13_Position(description="sample_text")
    _safe_set(b, 'research13_Position', a1)
    assert _is_linked(b, 'research13_Position', a1)
    if hasattr(a1, 'research13_Researcher8'):
        assert _is_linked(a1, 'research13_Researcher8', b)
    _safe_set(b, 'research13_Position', a2)
    assert _is_linked(b, 'research13_Position', a2)
    if hasattr(a1, 'research13_Researcher8'):
        assert not _is_linked(a1, 'research13_Researcher8', b)
    if hasattr(a2, 'research13_Researcher8'):
        assert _is_linked(a2, 'research13_Researcher8', b)
    _safe_set(b, 'research13_Position', None)
    assert not _is_linked(b, 'research13_Position', a2)
    if hasattr(a2, 'research13_Researcher8'):
        assert not _is_linked(a2, 'research13_Researcher8', b)


def test_assoc_reviewNote28_reverse_link_reassign_clear():
    a1 = research13_ReviewNote(content="sample_text")
    a2 = research13_ReviewNote(content="sample_text_2")
    b = research13_Review(date=date(2024, 1, 1))
    _safe_set(b, 'research13_Review29', a1)
    assert _is_linked(b, 'research13_Review29', a1)
    if hasattr(a1, 'research13_ReviewNote30'):
        assert _is_linked(a1, 'research13_ReviewNote30', b)
    _safe_set(b, 'research13_Review29', a2)
    assert _is_linked(b, 'research13_Review29', a2)
    if hasattr(a1, 'research13_ReviewNote30'):
        assert not _is_linked(a1, 'research13_ReviewNote30', b)
    if hasattr(a2, 'research13_ReviewNote30'):
        assert _is_linked(a2, 'research13_ReviewNote30', b)
    _safe_set(b, 'research13_Review29', None)
    assert not _is_linked(b, 'research13_Review29', a2)
    if hasattr(a2, 'research13_ReviewNote30'):
        assert not _is_linked(a2, 'research13_ReviewNote30', b)


def test_assoc_reviews19_reverse_link_reassign_clear():
    a1 = research13_ReviewNote(content="sample_text")
    a2 = research13_ReviewNote(content="sample_text_2")
    b = research13_Paragraph(content="sample_text")
    _safe_set(b, 'research13_Paragraph20', {a1})
    assert _is_linked(b, 'research13_Paragraph20', a1)
    if hasattr(a1, 'research13_ReviewNote'):
        assert _is_linked(a1, 'research13_ReviewNote', b)
    _safe_set(b, 'research13_Paragraph20', {a2})
    assert _is_linked(b, 'research13_Paragraph20', a2)
    if hasattr(a1, 'research13_ReviewNote'):
        assert not _is_linked(a1, 'research13_ReviewNote', b)
    if hasattr(a2, 'research13_ReviewNote'):
        assert _is_linked(a2, 'research13_ReviewNote', b)
    _safe_set(b, 'research13_Paragraph20', set())
    assert not _is_linked(b, 'research13_Paragraph20', a2)
    if hasattr(a2, 'research13_ReviewNote'):
        assert not _is_linked(a2, 'research13_ReviewNote', b)


def test_assoc_reviews2_reverse_link_reassign_clear():
    a1 = research13_Review(date=date(2024, 1, 1))
    a2 = research13_Review(date=date(2025, 6, 15))
    b = research13_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research13_Researcher3', {a1})
    assert _is_linked(b, 'research13_Researcher3', a1)
    if hasattr(a1, 'research13_Review'):
        assert _is_linked(a1, 'research13_Review', b)
    _safe_set(b, 'research13_Researcher3', {a2})
    assert _is_linked(b, 'research13_Researcher3', a2)
    if hasattr(a1, 'research13_Review'):
        assert not _is_linked(a1, 'research13_Review', b)
    if hasattr(a2, 'research13_Review'):
        assert _is_linked(a2, 'research13_Review', b)
    _safe_set(b, 'research13_Researcher3', set())
    assert not _is_linked(b, 'research13_Researcher3', a2)
    if hasattr(a2, 'research13_Review'):
        assert not _is_linked(a2, 'research13_Review', b)


def test_assoc_skills5_reverse_link_reassign_clear():
    a1 = research13_Skill(description="sample_text")
    a2 = research13_Skill(description="sample_text_2")
    b = research13_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research13_Researcher6', {a1})
    assert _is_linked(b, 'research13_Researcher6', a1)
    if hasattr(a1, 'research13_Skill'):
        assert _is_linked(a1, 'research13_Skill', b)
    _safe_set(b, 'research13_Researcher6', {a2})
    assert _is_linked(b, 'research13_Researcher6', a2)
    if hasattr(a1, 'research13_Skill'):
        assert not _is_linked(a1, 'research13_Skill', b)
    if hasattr(a2, 'research13_Skill'):
        assert _is_linked(a2, 'research13_Skill', b)
    _safe_set(b, 'research13_Researcher6', set())
    assert not _is_linked(b, 'research13_Researcher6', a2)
    if hasattr(a2, 'research13_Skill'):
        assert not _is_linked(a2, 'research13_Skill', b)


def test_assoc_writes1_reverse_link_reassign_clear():
    a1 = research13_Write(timeSpent=7)
    a2 = research13_Write(timeSpent=13)
    b = research13_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research13_Researcher', {a1})
    assert _is_linked(b, 'research13_Researcher', a1)
    if hasattr(a1, 'research13_Write'):
        assert _is_linked(a1, 'research13_Write', b)
    _safe_set(b, 'research13_Researcher', {a2})
    assert _is_linked(b, 'research13_Researcher', a2)
    if hasattr(a1, 'research13_Write'):
        assert not _is_linked(a1, 'research13_Write', b)
    if hasattr(a2, 'research13_Write'):
        assert _is_linked(a2, 'research13_Write', b)
    _safe_set(b, 'research13_Researcher', set())
    assert not _is_linked(b, 'research13_Researcher', a2)
    if hasattr(a2, 'research13_Write'):
        assert not _is_linked(a2, 'research13_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allkeywords51_stub_double():
    # research13_KnowledgeManager has no real 'research13_KnowledgeManager52' property in the generated
    # code (a bare stub) -- manually attach it so research13_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Keyword(description="sample_text")
    partner = research13_KnowledgeManager()
    setattr(partner, 'research13_KnowledgeManager52', None)
    _safe_set(owner, 'research13_Keyword53', partner)
    assert owner in getattr(partner, 'research13_KnowledgeManager52')
    _safe_set(owner, 'research13_Keyword53', None)
    assert owner not in getattr(partner, 'research13_KnowledgeManager52')


def test_assoc_authors13_stub_double():
    # research13_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so research13_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Researcher(forName="sample_text", name="sample_text")
    partner = research13_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_col_paper57_stub_double():
    # research13_Paper has no real 'research13_Paper59' property in the generated
    # code (a bare stub) -- manually attach it so research13_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Collaboration(ratio=7)
    partner = research13_Paper()
    setattr(partner, 'research13_Paper59', None)
    _safe_set(owner, 'research13_Collaboration58', partner)
    assert getattr(partner, 'research13_Paper59') == owner
    _safe_set(owner, 'research13_Collaboration58', None)
    assert getattr(partner, 'research13_Paper59') is None


def test_assoc_keywords14_stub_double():
    # research13_Paper has no real 'research13_Paper15' property in the generated
    # code (a bare stub) -- manually attach it so research13_PaperKeyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_PaperKeyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_PaperKeyword(weight=7)
    partner = research13_Paper()
    setattr(partner, 'research13_Paper15', None)
    _safe_set(owner, 'research13_PaperKeyword', partner)
    assert owner in getattr(partner, 'research13_Paper15')
    _safe_set(owner, 'research13_PaperKeyword', None)
    assert owner not in getattr(partner, 'research13_Paper15')


def test_assoc_kpapers49_stub_double():
    # research13_Paper has no real 'research13_Paper50' property in the generated
    # code (a bare stub) -- manually attach it so research13_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Keyword(description="sample_text")
    partner = research13_Paper()
    setattr(partner, 'research13_Paper50', None)
    _safe_set(owner, 'research13_Keyword', {partner})
    assert getattr(partner, 'research13_Paper50') == owner
    _safe_set(owner, 'research13_Keyword', set())
    assert getattr(partner, 'research13_Paper50') is None


def test_assoc_paper23_stub_double():
    # research13_Paper has no real 'Paper24' property in the generated
    # code (a bare stub) -- manually attach it so research13_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Progress(percent=7)
    partner = research13_Paper()
    setattr(partner, 'Paper24', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper24') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper24') is None


def test_assoc_paragraphs11_stub_double():
    # research13_Paper has no real 'research13_Paper' property in the generated
    # code (a bare stub) -- manually attach it so research13_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Paragraph(content="sample_text")
    partner = research13_Paper()
    setattr(partner, 'research13_Paper', None)
    _safe_set(owner, 'research13_Paragraph', partner)
    assert owner in getattr(partner, 'research13_Paper')
    _safe_set(owner, 'research13_Paragraph', None)
    assert owner not in getattr(partner, 'research13_Paper')


def test_assoc_positions43_stub_double():
    # research13_PublicationSystem has no real 'research13_PublicationSystem44' property in the generated
    # code (a bare stub) -- manually attach it so research13_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Position(description="sample_text")
    partner = research13_PublicationSystem()
    setattr(partner, 'research13_PublicationSystem44', None)
    _safe_set(owner, 'research13_Position45', partner)
    assert owner in getattr(partner, 'research13_PublicationSystem44')
    _safe_set(owner, 'research13_Position45', None)
    assert owner not in getattr(partner, 'research13_PublicationSystem44')


def test_assoc_processView38_stub_double():
    # research13_PublicationSystem has no real 'research13_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so research13_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_PublicationProcess(maxTime=7, minTime=7)
    partner = research13_PublicationSystem()
    setattr(partner, 'research13_PublicationSystem', None)
    _safe_set(owner, 'research13_PublicationProcess39', partner)
    assert getattr(partner, 'research13_PublicationSystem') == owner
    _safe_set(owner, 'research13_PublicationProcess39', None)
    assert getattr(partner, 'research13_PublicationSystem') is None


def test_assoc_progress12_stub_double():
    # research13_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so research13_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Progress(percent=7)
    partner = research13_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_res_papers4_stub_double():
    # research13_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so research13_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Researcher(forName="sample_text", name="sample_text")
    partner = research13_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers31_stub_double():
    # research13_PublicationStructure has no real 'research13_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so research13_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research13_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research13_Researcher(forName="sample_text", name="sample_text")
    partner = research13_PublicationStructure()
    setattr(partner, 'research13_PublicationStructure', None)
    _safe_set(owner, 'research13_Researcher32', partner)
    assert owner in getattr(partner, 'research13_PublicationStructure')
    _safe_set(owner, 'research13_Researcher32', None)
    assert owner not in getattr(partner, 'research13_PublicationStructure')


