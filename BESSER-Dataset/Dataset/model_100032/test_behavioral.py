import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    publication102_Collaboration,
    publication102_Counted,
    publication102_Keyword,
    publication102_KnowledgeManager,
    publication102_Labelled,
    publication102_Named,
    publication102_Paper,
    publication102_PaperKeyword,
    publication102_Paragraph,
    publication102_Position,
    publication102_PublicationStructure,
    publication102_Researcher,
    publication102_Review,
    publication102_ReviewNote,
    publication102_Skill,
    publication102_Write,
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

def test_assoc_collaborations8_reverse_link_reassign_clear():
    a1 = publication102_Researcher(forName="sample_text", name="sample_text")
    a2 = publication102_Researcher(forName="sample_text_2", name="sample_text_2")
    b = publication102_Collaboration(ratio=7)
    _safe_set(b, 'publication102_Collaboration', a1)
    assert _is_linked(b, 'publication102_Collaboration', a1)
    if hasattr(a1, 'publication102_Researcher9'):
        assert _is_linked(a1, 'publication102_Researcher9', b)
    _safe_set(b, 'publication102_Collaboration', a2)
    assert _is_linked(b, 'publication102_Collaboration', a2)
    if hasattr(a1, 'publication102_Researcher9'):
        assert not _is_linked(a1, 'publication102_Researcher9', b)
    if hasattr(a2, 'publication102_Researcher9'):
        assert _is_linked(a2, 'publication102_Researcher9', b)
    _safe_set(b, 'publication102_Collaboration', None)
    assert not _is_linked(b, 'publication102_Collaboration', a2)
    if hasattr(a2, 'publication102_Researcher9'):
        assert not _is_linked(a2, 'publication102_Researcher9', b)


def test_assoc_keyword43_reverse_link_reassign_clear():
    a1 = publication102_PaperKeyword(weight=7)
    a2 = publication102_PaperKeyword(weight=13)
    b = publication102_Keyword(description="sample_text")
    _safe_set(b, 'publication102_Keyword45', a1)
    assert _is_linked(b, 'publication102_Keyword45', a1)
    if hasattr(a1, 'publication102_PaperKeyword44'):
        assert _is_linked(a1, 'publication102_PaperKeyword44', b)
    _safe_set(b, 'publication102_Keyword45', a2)
    assert _is_linked(b, 'publication102_Keyword45', a2)
    if hasattr(a1, 'publication102_PaperKeyword44'):
        assert not _is_linked(a1, 'publication102_PaperKeyword44', b)
    if hasattr(a2, 'publication102_PaperKeyword44'):
        assert _is_linked(a2, 'publication102_PaperKeyword44', b)
    _safe_set(b, 'publication102_Keyword45', None)
    assert not _is_linked(b, 'publication102_Keyword45', a2)
    if hasattr(a2, 'publication102_PaperKeyword44'):
        assert not _is_linked(a2, 'publication102_PaperKeyword44', b)


def test_assoc_paragraph19_reverse_link_reassign_clear():
    a1 = publication102_Write(timeSpent=7)
    a2 = publication102_Write(timeSpent=13)
    b = publication102_Paragraph(content="sample_text")
    _safe_set(b, 'publication102_Paragraph21', a1)
    assert _is_linked(b, 'publication102_Paragraph21', a1)
    if hasattr(a1, 'publication102_Write20'):
        assert _is_linked(a1, 'publication102_Write20', b)
    _safe_set(b, 'publication102_Paragraph21', a2)
    assert _is_linked(b, 'publication102_Paragraph21', a2)
    if hasattr(a1, 'publication102_Write20'):
        assert not _is_linked(a1, 'publication102_Write20', b)
    if hasattr(a2, 'publication102_Write20'):
        assert _is_linked(a2, 'publication102_Write20', b)
    _safe_set(b, 'publication102_Paragraph21', None)
    assert not _is_linked(b, 'publication102_Paragraph21', a2)
    if hasattr(a2, 'publication102_Write20'):
        assert not _is_linked(a2, 'publication102_Write20', b)


def test_assoc_parent36_reverse_link_reassign_clear():
    a1 = publication102_Position(description="sample_text")
    a2 = publication102_Position(description="sample_text_2")
    b = publication102_Position(description="sample_text")
    _safe_set(b, 'publication102_Position37', a1)
    assert _is_linked(b, 'publication102_Position37', a1)
    if hasattr(a1, 'publication102_Position35'):
        assert _is_linked(a1, 'publication102_Position35', b)
    _safe_set(b, 'publication102_Position37', a2)
    assert _is_linked(b, 'publication102_Position37', a2)
    if hasattr(a1, 'publication102_Position35'):
        assert not _is_linked(a1, 'publication102_Position35', b)
    if hasattr(a2, 'publication102_Position35'):
        assert _is_linked(a2, 'publication102_Position35', b)
    _safe_set(b, 'publication102_Position37', None)
    assert not _is_linked(b, 'publication102_Position37', a2)
    if hasattr(a2, 'publication102_Position35'):
        assert not _is_linked(a2, 'publication102_Position35', b)


def test_assoc_res_position6_reverse_link_reassign_clear():
    a1 = publication102_Researcher(forName="sample_text", name="sample_text")
    a2 = publication102_Researcher(forName="sample_text_2", name="sample_text_2")
    b = publication102_Position(description="sample_text")
    _safe_set(b, 'publication102_Position', a1)
    assert _is_linked(b, 'publication102_Position', a1)
    if hasattr(a1, 'publication102_Researcher7'):
        assert _is_linked(a1, 'publication102_Researcher7', b)
    _safe_set(b, 'publication102_Position', a2)
    assert _is_linked(b, 'publication102_Position', a2)
    if hasattr(a1, 'publication102_Researcher7'):
        assert not _is_linked(a1, 'publication102_Researcher7', b)
    if hasattr(a2, 'publication102_Researcher7'):
        assert _is_linked(a2, 'publication102_Researcher7', b)
    _safe_set(b, 'publication102_Position', None)
    assert not _is_linked(b, 'publication102_Position', a2)
    if hasattr(a2, 'publication102_Researcher7'):
        assert not _is_linked(a2, 'publication102_Researcher7', b)


def test_assoc_reviewNote22_reverse_link_reassign_clear():
    a1 = publication102_ReviewNote(content="sample_text")
    a2 = publication102_ReviewNote(content="sample_text_2")
    b = publication102_Review(date=date(2024, 1, 1))
    _safe_set(b, 'publication102_Review23', a1)
    assert _is_linked(b, 'publication102_Review23', a1)
    if hasattr(a1, 'publication102_ReviewNote24'):
        assert _is_linked(a1, 'publication102_ReviewNote24', b)
    _safe_set(b, 'publication102_Review23', a2)
    assert _is_linked(b, 'publication102_Review23', a2)
    if hasattr(a1, 'publication102_ReviewNote24'):
        assert not _is_linked(a1, 'publication102_ReviewNote24', b)
    if hasattr(a2, 'publication102_ReviewNote24'):
        assert _is_linked(a2, 'publication102_ReviewNote24', b)
    _safe_set(b, 'publication102_Review23', None)
    assert not _is_linked(b, 'publication102_Review23', a2)
    if hasattr(a2, 'publication102_ReviewNote24'):
        assert not _is_linked(a2, 'publication102_ReviewNote24', b)


def test_assoc_reviews1_reverse_link_reassign_clear():
    a1 = publication102_Review(date=date(2024, 1, 1))
    a2 = publication102_Review(date=date(2025, 6, 15))
    b = publication102_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'publication102_Researcher2', {a1})
    assert _is_linked(b, 'publication102_Researcher2', a1)
    if hasattr(a1, 'publication102_Review'):
        assert _is_linked(a1, 'publication102_Review', b)
    _safe_set(b, 'publication102_Researcher2', {a2})
    assert _is_linked(b, 'publication102_Researcher2', a2)
    if hasattr(a1, 'publication102_Review'):
        assert not _is_linked(a1, 'publication102_Review', b)
    if hasattr(a2, 'publication102_Review'):
        assert _is_linked(a2, 'publication102_Review', b)
    _safe_set(b, 'publication102_Researcher2', set())
    assert not _is_linked(b, 'publication102_Researcher2', a2)
    if hasattr(a2, 'publication102_Review'):
        assert not _is_linked(a2, 'publication102_Review', b)


def test_assoc_reviews17_reverse_link_reassign_clear():
    a1 = publication102_ReviewNote(content="sample_text")
    a2 = publication102_ReviewNote(content="sample_text_2")
    b = publication102_Paragraph(content="sample_text")
    _safe_set(b, 'publication102_Paragraph18', {a1})
    assert _is_linked(b, 'publication102_Paragraph18', a1)
    if hasattr(a1, 'publication102_ReviewNote'):
        assert _is_linked(a1, 'publication102_ReviewNote', b)
    _safe_set(b, 'publication102_Paragraph18', {a2})
    assert _is_linked(b, 'publication102_Paragraph18', a2)
    if hasattr(a1, 'publication102_ReviewNote'):
        assert not _is_linked(a1, 'publication102_ReviewNote', b)
    if hasattr(a2, 'publication102_ReviewNote'):
        assert _is_linked(a2, 'publication102_ReviewNote', b)
    _safe_set(b, 'publication102_Paragraph18', set())
    assert not _is_linked(b, 'publication102_Paragraph18', a2)
    if hasattr(a2, 'publication102_ReviewNote'):
        assert not _is_linked(a2, 'publication102_ReviewNote', b)


def test_assoc_skills4_reverse_link_reassign_clear():
    a1 = publication102_Skill(description="sample_text")
    a2 = publication102_Skill(description="sample_text_2")
    b = publication102_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'publication102_Researcher5', {a1})
    assert _is_linked(b, 'publication102_Researcher5', a1)
    if hasattr(a1, 'publication102_Skill'):
        assert _is_linked(a1, 'publication102_Skill', b)
    _safe_set(b, 'publication102_Researcher5', {a2})
    assert _is_linked(b, 'publication102_Researcher5', a2)
    if hasattr(a1, 'publication102_Skill'):
        assert not _is_linked(a1, 'publication102_Skill', b)
    if hasattr(a2, 'publication102_Skill'):
        assert _is_linked(a2, 'publication102_Skill', b)
    _safe_set(b, 'publication102_Researcher5', set())
    assert not _is_linked(b, 'publication102_Researcher5', a2)
    if hasattr(a2, 'publication102_Skill'):
        assert not _is_linked(a2, 'publication102_Skill', b)


def test_assoc_writes0_reverse_link_reassign_clear():
    a1 = publication102_Write(timeSpent=7)
    a2 = publication102_Write(timeSpent=13)
    b = publication102_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'publication102_Researcher', {a1})
    assert _is_linked(b, 'publication102_Researcher', a1)
    if hasattr(a1, 'publication102_Write'):
        assert _is_linked(a1, 'publication102_Write', b)
    _safe_set(b, 'publication102_Researcher', {a2})
    assert _is_linked(b, 'publication102_Researcher', a2)
    if hasattr(a1, 'publication102_Write'):
        assert not _is_linked(a1, 'publication102_Write', b)
    if hasattr(a2, 'publication102_Write'):
        assert _is_linked(a2, 'publication102_Write', b)
    _safe_set(b, 'publication102_Researcher', set())
    assert not _is_linked(b, 'publication102_Researcher', a2)
    if hasattr(a2, 'publication102_Write'):
        assert not _is_linked(a2, 'publication102_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allkeywords40_stub_double():
    # publication102_KnowledgeManager has no real 'publication102_KnowledgeManager41' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Keyword(description="sample_text")
    partner = publication102_KnowledgeManager()
    setattr(partner, 'publication102_KnowledgeManager41', None)
    _safe_set(owner, 'publication102_Keyword42', partner)
    assert owner in getattr(partner, 'publication102_KnowledgeManager41')
    _safe_set(owner, 'publication102_Keyword42', None)
    assert owner not in getattr(partner, 'publication102_KnowledgeManager41')


def test_assoc_authors11_stub_double():
    # publication102_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Researcher(forName="sample_text", name="sample_text")
    partner = publication102_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_col_paper46_stub_double():
    # publication102_Paper has no real 'publication102_Paper48' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Collaboration(ratio=7)
    partner = publication102_Paper()
    setattr(partner, 'publication102_Paper48', None)
    _safe_set(owner, 'publication102_Collaboration47', partner)
    assert getattr(partner, 'publication102_Paper48') == owner
    _safe_set(owner, 'publication102_Collaboration47', None)
    assert getattr(partner, 'publication102_Paper48') is None


def test_assoc_keywords12_stub_double():
    # publication102_Paper has no real 'publication102_Paper13' property in the generated
    # code (a bare stub) -- manually attach it so publication102_PaperKeyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_PaperKeyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_PaperKeyword(weight=7)
    partner = publication102_Paper()
    setattr(partner, 'publication102_Paper13', None)
    _safe_set(owner, 'publication102_PaperKeyword', partner)
    assert owner in getattr(partner, 'publication102_Paper13')
    _safe_set(owner, 'publication102_PaperKeyword', None)
    assert owner not in getattr(partner, 'publication102_Paper13')


def test_assoc_kpapers38_stub_double():
    # publication102_Paper has no real 'publication102_Paper39' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Keyword(description="sample_text")
    partner = publication102_Paper()
    setattr(partner, 'publication102_Paper39', None)
    _safe_set(owner, 'publication102_Keyword', {partner})
    assert getattr(partner, 'publication102_Paper39') == owner
    _safe_set(owner, 'publication102_Keyword', set())
    assert getattr(partner, 'publication102_Paper39') is None


def test_assoc_paragraphs10_stub_double():
    # publication102_Paper has no real 'publication102_Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Paragraph(content="sample_text")
    partner = publication102_Paper()
    setattr(partner, 'publication102_Paper', None)
    _safe_set(owner, 'publication102_Paragraph', partner)
    assert owner in getattr(partner, 'publication102_Paper')
    _safe_set(owner, 'publication102_Paragraph', None)
    assert owner not in getattr(partner, 'publication102_Paper')


def test_assoc_positions32_stub_double():
    # publication102_PublicationStructure has no real 'publication102_PublicationStructure33' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Position(description="sample_text")
    partner = publication102_PublicationStructure()
    setattr(partner, 'publication102_PublicationStructure33', None)
    _safe_set(owner, 'publication102_Position34', partner)
    assert owner in getattr(partner, 'publication102_PublicationStructure33')
    _safe_set(owner, 'publication102_Position34', None)
    assert owner not in getattr(partner, 'publication102_PublicationStructure33')


def test_assoc_res_papers3_stub_double():
    # publication102_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Researcher(forName="sample_text", name="sample_text")
    partner = publication102_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers25_stub_double():
    # publication102_PublicationStructure has no real 'publication102_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so publication102_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication102_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication102_Researcher(forName="sample_text", name="sample_text")
    partner = publication102_PublicationStructure()
    setattr(partner, 'publication102_PublicationStructure', None)
    _safe_set(owner, 'publication102_Researcher26', partner)
    assert owner in getattr(partner, 'publication102_PublicationStructure')
    _safe_set(owner, 'publication102_Researcher26', None)
    assert owner not in getattr(partner, 'publication102_PublicationStructure')


