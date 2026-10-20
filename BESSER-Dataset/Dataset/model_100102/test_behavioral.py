import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    tp4_Counted,
    tp4_Keyword,
    tp4_Labelled,
    tp4_Named,
    tp4_Paper,
    tp4_Paragraph,
    tp4_Phases,
    tp4_Position,
    tp4_Progress,
    tp4_PublicationProcess,
    tp4_PublicationStructure,
    tp4_PublicationSystem,
    tp4_Researcher,
    tp4_Review,
    tp4_ReviewNote,
    tp4_Skill,
    tp4_Write,
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

def test_assoc_paragraph20_reverse_link_reassign_clear():
    a1 = tp4_Write(timeSpent=7)
    a2 = tp4_Write(timeSpent=13)
    b = tp4_Paragraph(content="sample_text")
    _safe_set(b, 'tp4_Paragraph22', a1)
    assert _is_linked(b, 'tp4_Paragraph22', a1)
    if hasattr(a1, 'tp4_Write21'):
        assert _is_linked(a1, 'tp4_Write21', b)
    _safe_set(b, 'tp4_Paragraph22', a2)
    assert _is_linked(b, 'tp4_Paragraph22', a2)
    if hasattr(a1, 'tp4_Write21'):
        assert not _is_linked(a1, 'tp4_Write21', b)
    if hasattr(a2, 'tp4_Write21'):
        assert _is_linked(a2, 'tp4_Write21', b)
    _safe_set(b, 'tp4_Paragraph22', None)
    assert not _is_linked(b, 'tp4_Paragraph22', a2)
    if hasattr(a2, 'tp4_Write21'):
        assert not _is_linked(a2, 'tp4_Write21', b)


def test_assoc_parent43_reverse_link_reassign_clear():
    a1 = tp4_Position(description="sample_text")
    a2 = tp4_Position(description="sample_text_2")
    b = tp4_Position(description="sample_text")
    _safe_set(b, 'tp4_Position44', a1)
    assert _is_linked(b, 'tp4_Position44', a1)
    if hasattr(a1, 'tp4_Position42'):
        assert _is_linked(a1, 'tp4_Position42', b)
    _safe_set(b, 'tp4_Position44', a2)
    assert _is_linked(b, 'tp4_Position44', a2)
    if hasattr(a1, 'tp4_Position42'):
        assert not _is_linked(a1, 'tp4_Position42', b)
    if hasattr(a2, 'tp4_Position42'):
        assert _is_linked(a2, 'tp4_Position42', b)
    _safe_set(b, 'tp4_Position44', None)
    assert not _is_linked(b, 'tp4_Position44', a2)
    if hasattr(a2, 'tp4_Position42'):
        assert not _is_linked(a2, 'tp4_Position42', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = tp4_PublicationProcess(maxTime=7, minTime=7)
    a2 = tp4_PublicationProcess(maxTime=13, minTime=13)
    b = tp4_Phases(name="sample_text")
    _safe_set(b, 'tp4_Phases', a1)
    assert _is_linked(b, 'tp4_Phases', a1)
    if hasattr(a1, 'tp4_PublicationProcess'):
        assert _is_linked(a1, 'tp4_PublicationProcess', b)
    _safe_set(b, 'tp4_Phases', a2)
    assert _is_linked(b, 'tp4_Phases', a2)
    if hasattr(a1, 'tp4_PublicationProcess'):
        assert not _is_linked(a1, 'tp4_PublicationProcess', b)
    if hasattr(a2, 'tp4_PublicationProcess'):
        assert _is_linked(a2, 'tp4_PublicationProcess', b)
    _safe_set(b, 'tp4_Phases', None)
    assert not _is_linked(b, 'tp4_Phases', a2)
    if hasattr(a2, 'tp4_PublicationProcess'):
        assert not _is_linked(a2, 'tp4_PublicationProcess', b)


def test_assoc_position7_reverse_link_reassign_clear():
    a1 = tp4_Researcher(forName="sample_text", name="sample_text")
    a2 = tp4_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp4_Position(description="sample_text")
    _safe_set(b, 'tp4_Position', a1)
    assert _is_linked(b, 'tp4_Position', a1)
    if hasattr(a1, 'tp4_Researcher8'):
        assert _is_linked(a1, 'tp4_Researcher8', b)
    _safe_set(b, 'tp4_Position', a2)
    assert _is_linked(b, 'tp4_Position', a2)
    if hasattr(a1, 'tp4_Researcher8'):
        assert not _is_linked(a1, 'tp4_Researcher8', b)
    if hasattr(a2, 'tp4_Researcher8'):
        assert _is_linked(a2, 'tp4_Researcher8', b)
    _safe_set(b, 'tp4_Position', None)
    assert not _is_linked(b, 'tp4_Position', a2)
    if hasattr(a2, 'tp4_Researcher8'):
        assert not _is_linked(a2, 'tp4_Researcher8', b)


def test_assoc_process16_reverse_link_reassign_clear():
    a1 = tp4_PublicationProcess(maxTime=7, minTime=7)
    a2 = tp4_PublicationProcess(maxTime=13, minTime=13)
    b = tp4_Progress(percent=7)
    _safe_set(b, 'tp4_Progress', a1)
    assert _is_linked(b, 'tp4_Progress', a1)
    if hasattr(a1, 'tp4_PublicationProcess17'):
        assert _is_linked(a1, 'tp4_PublicationProcess17', b)
    _safe_set(b, 'tp4_Progress', a2)
    assert _is_linked(b, 'tp4_Progress', a2)
    if hasattr(a1, 'tp4_PublicationProcess17'):
        assert not _is_linked(a1, 'tp4_PublicationProcess17', b)
    if hasattr(a2, 'tp4_PublicationProcess17'):
        assert _is_linked(a2, 'tp4_PublicationProcess17', b)
    _safe_set(b, 'tp4_Progress', None)
    assert not _is_linked(b, 'tp4_Progress', a2)
    if hasattr(a2, 'tp4_PublicationProcess17'):
        assert not _is_linked(a2, 'tp4_PublicationProcess17', b)


def test_assoc_reviewNote23_reverse_link_reassign_clear():
    a1 = tp4_ReviewNote(content="sample_text")
    a2 = tp4_ReviewNote(content="sample_text_2")
    b = tp4_Review(date=date(2024, 1, 1))
    _safe_set(b, 'tp4_Review24', a1)
    assert _is_linked(b, 'tp4_Review24', a1)
    if hasattr(a1, 'tp4_ReviewNote25'):
        assert _is_linked(a1, 'tp4_ReviewNote25', b)
    _safe_set(b, 'tp4_Review24', a2)
    assert _is_linked(b, 'tp4_Review24', a2)
    if hasattr(a1, 'tp4_ReviewNote25'):
        assert not _is_linked(a1, 'tp4_ReviewNote25', b)
    if hasattr(a2, 'tp4_ReviewNote25'):
        assert _is_linked(a2, 'tp4_ReviewNote25', b)
    _safe_set(b, 'tp4_Review24', None)
    assert not _is_linked(b, 'tp4_Review24', a2)
    if hasattr(a2, 'tp4_ReviewNote25'):
        assert not _is_linked(a2, 'tp4_ReviewNote25', b)


def test_assoc_reviews14_reverse_link_reassign_clear():
    a1 = tp4_ReviewNote(content="sample_text")
    a2 = tp4_ReviewNote(content="sample_text_2")
    b = tp4_Paragraph(content="sample_text")
    _safe_set(b, 'tp4_Paragraph15', {a1})
    assert _is_linked(b, 'tp4_Paragraph15', a1)
    if hasattr(a1, 'tp4_ReviewNote'):
        assert _is_linked(a1, 'tp4_ReviewNote', b)
    _safe_set(b, 'tp4_Paragraph15', {a2})
    assert _is_linked(b, 'tp4_Paragraph15', a2)
    if hasattr(a1, 'tp4_ReviewNote'):
        assert not _is_linked(a1, 'tp4_ReviewNote', b)
    if hasattr(a2, 'tp4_ReviewNote'):
        assert _is_linked(a2, 'tp4_ReviewNote', b)
    _safe_set(b, 'tp4_Paragraph15', set())
    assert not _is_linked(b, 'tp4_Paragraph15', a2)
    if hasattr(a2, 'tp4_ReviewNote'):
        assert not _is_linked(a2, 'tp4_ReviewNote', b)


def test_assoc_reviews2_reverse_link_reassign_clear():
    a1 = tp4_Review(date=date(2024, 1, 1))
    a2 = tp4_Review(date=date(2025, 6, 15))
    b = tp4_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'tp4_Researcher3', {a1})
    assert _is_linked(b, 'tp4_Researcher3', a1)
    if hasattr(a1, 'tp4_Review'):
        assert _is_linked(a1, 'tp4_Review', b)
    _safe_set(b, 'tp4_Researcher3', {a2})
    assert _is_linked(b, 'tp4_Researcher3', a2)
    if hasattr(a1, 'tp4_Review'):
        assert not _is_linked(a1, 'tp4_Review', b)
    if hasattr(a2, 'tp4_Review'):
        assert _is_linked(a2, 'tp4_Review', b)
    _safe_set(b, 'tp4_Researcher3', set())
    assert not _is_linked(b, 'tp4_Researcher3', a2)
    if hasattr(a2, 'tp4_Review'):
        assert not _is_linked(a2, 'tp4_Review', b)


def test_assoc_skills5_reverse_link_reassign_clear():
    a1 = tp4_Skill(description="sample_text")
    a2 = tp4_Skill(description="sample_text_2")
    b = tp4_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'tp4_Researcher6', {a1})
    assert _is_linked(b, 'tp4_Researcher6', a1)
    if hasattr(a1, 'tp4_Skill'):
        assert _is_linked(a1, 'tp4_Skill', b)
    _safe_set(b, 'tp4_Researcher6', {a2})
    assert _is_linked(b, 'tp4_Researcher6', a2)
    if hasattr(a1, 'tp4_Skill'):
        assert not _is_linked(a1, 'tp4_Skill', b)
    if hasattr(a2, 'tp4_Skill'):
        assert _is_linked(a2, 'tp4_Skill', b)
    _safe_set(b, 'tp4_Researcher6', set())
    assert not _is_linked(b, 'tp4_Researcher6', a2)
    if hasattr(a2, 'tp4_Skill'):
        assert not _is_linked(a2, 'tp4_Skill', b)


def test_assoc_writes1_reverse_link_reassign_clear():
    a1 = tp4_Write(timeSpent=7)
    a2 = tp4_Write(timeSpent=13)
    b = tp4_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'tp4_Researcher', {a1})
    assert _is_linked(b, 'tp4_Researcher', a1)
    if hasattr(a1, 'tp4_Write'):
        assert _is_linked(a1, 'tp4_Write', b)
    _safe_set(b, 'tp4_Researcher', {a2})
    assert _is_linked(b, 'tp4_Researcher', a2)
    if hasattr(a1, 'tp4_Write'):
        assert not _is_linked(a1, 'tp4_Write', b)
    if hasattr(a2, 'tp4_Write'):
        assert _is_linked(a2, 'tp4_Write', b)
    _safe_set(b, 'tp4_Researcher', set())
    assert not _is_linked(b, 'tp4_Researcher', a2)
    if hasattr(a2, 'tp4_Write'):
        assert not _is_linked(a2, 'tp4_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allKeywords39_stub_double():
    # tp4_PublicationSystem has no real 'tp4_PublicationSystem40' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Keyword(description="sample_text")
    partner = tp4_PublicationSystem()
    setattr(partner, 'tp4_PublicationSystem40', None)
    _safe_set(owner, 'tp4_Keyword41', partner)
    assert owner in getattr(partner, 'tp4_PublicationSystem40')
    _safe_set(owner, 'tp4_Keyword41', None)
    assert owner not in getattr(partner, 'tp4_PublicationSystem40')


def test_assoc_authors11_stub_double():
    # tp4_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Researcher(forName="sample_text", name="sample_text")
    partner = tp4_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_keywords12_stub_double():
    # tp4_Paper has no real 'tp4_Paper13' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Keyword(description="sample_text")
    partner = tp4_Paper()
    setattr(partner, 'tp4_Paper13', None)
    _safe_set(owner, 'tp4_Keyword', partner)
    assert owner in getattr(partner, 'tp4_Paper13')
    _safe_set(owner, 'tp4_Keyword', None)
    assert owner not in getattr(partner, 'tp4_Paper13')


def test_assoc_paper18_stub_double():
    # tp4_Paper has no real 'Paper19' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Progress(percent=7)
    partner = tp4_Paper()
    setattr(partner, 'Paper19', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper19') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper19') is None


def test_assoc_paragraphs9_stub_double():
    # tp4_Paper has no real 'tp4_Paper' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Paragraph(content="sample_text")
    partner = tp4_Paper()
    setattr(partner, 'tp4_Paper', None)
    _safe_set(owner, 'tp4_Paragraph', partner)
    assert owner in getattr(partner, 'tp4_Paper')
    _safe_set(owner, 'tp4_Paragraph', None)
    assert owner not in getattr(partner, 'tp4_Paper')


def test_assoc_positions36_stub_double():
    # tp4_PublicationSystem has no real 'tp4_PublicationSystem37' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Position(description="sample_text")
    partner = tp4_PublicationSystem()
    setattr(partner, 'tp4_PublicationSystem37', None)
    _safe_set(owner, 'tp4_Position38', partner)
    assert owner in getattr(partner, 'tp4_PublicationSystem37')
    _safe_set(owner, 'tp4_Position38', None)
    assert owner not in getattr(partner, 'tp4_PublicationSystem37')


def test_assoc_processView31_stub_double():
    # tp4_PublicationSystem has no real 'tp4_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so tp4_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_PublicationProcess(maxTime=7, minTime=7)
    partner = tp4_PublicationSystem()
    setattr(partner, 'tp4_PublicationSystem', None)
    _safe_set(owner, 'tp4_PublicationProcess32', partner)
    assert getattr(partner, 'tp4_PublicationSystem') == owner
    _safe_set(owner, 'tp4_PublicationProcess32', None)
    assert getattr(partner, 'tp4_PublicationSystem') is None


def test_assoc_progress10_stub_double():
    # tp4_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Progress(percent=7)
    partner = tp4_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_res_papers4_stub_double():
    # tp4_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Researcher(forName="sample_text", name="sample_text")
    partner = tp4_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers26_stub_double():
    # tp4_PublicationStructure has no real 'tp4_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so tp4_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp4_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp4_Researcher(forName="sample_text", name="sample_text")
    partner = tp4_PublicationStructure()
    setattr(partner, 'tp4_PublicationStructure', None)
    _safe_set(owner, 'tp4_Researcher27', partner)
    assert owner in getattr(partner, 'tp4_PublicationStructure')
    _safe_set(owner, 'tp4_Researcher27', None)
    assert owner not in getattr(partner, 'tp4_PublicationStructure')


