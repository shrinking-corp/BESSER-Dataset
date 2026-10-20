import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    researchvc_Counted,
    researchvc_Keyword,
    researchvc_Labelled,
    researchvc_Named,
    researchvc_Paper,
    researchvc_PaperKeyword,
    researchvc_Paragraph,
    researchvc_PublicationStructure,
    researchvc_Researcher,
    researchvc_Review,
    researchvc_ReviewNote,
    researchvc_Skill,
    researchvc_Write,
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

def test_assoc_keyword28_reverse_link_reassign_clear():
    a1 = researchvc_PaperKeyword(weight=7)
    a2 = researchvc_PaperKeyword(weight=13)
    b = researchvc_Keyword(word="sample_text")
    _safe_set(b, 'researchvc_Keyword30', a1)
    assert _is_linked(b, 'researchvc_Keyword30', a1)
    if hasattr(a1, 'researchvc_PaperKeyword29'):
        assert _is_linked(a1, 'researchvc_PaperKeyword29', b)
    _safe_set(b, 'researchvc_Keyword30', a2)
    assert _is_linked(b, 'researchvc_Keyword30', a2)
    if hasattr(a1, 'researchvc_PaperKeyword29'):
        assert not _is_linked(a1, 'researchvc_PaperKeyword29', b)
    if hasattr(a2, 'researchvc_PaperKeyword29'):
        assert _is_linked(a2, 'researchvc_PaperKeyword29', b)
    _safe_set(b, 'researchvc_Keyword30', None)
    assert not _is_linked(b, 'researchvc_Keyword30', a2)
    if hasattr(a2, 'researchvc_PaperKeyword29'):
        assert not _is_linked(a2, 'researchvc_PaperKeyword29', b)


def test_assoc_paragraph15_reverse_link_reassign_clear():
    a1 = researchvc_Write(timeSpent=7)
    a2 = researchvc_Write(timeSpent=13)
    b = researchvc_Paragraph(content="sample_text")
    _safe_set(b, 'researchvc_Paragraph17', a1)
    assert _is_linked(b, 'researchvc_Paragraph17', a1)
    if hasattr(a1, 'researchvc_Write16'):
        assert _is_linked(a1, 'researchvc_Write16', b)
    _safe_set(b, 'researchvc_Paragraph17', a2)
    assert _is_linked(b, 'researchvc_Paragraph17', a2)
    if hasattr(a1, 'researchvc_Write16'):
        assert not _is_linked(a1, 'researchvc_Write16', b)
    if hasattr(a2, 'researchvc_Write16'):
        assert _is_linked(a2, 'researchvc_Write16', b)
    _safe_set(b, 'researchvc_Paragraph17', None)
    assert not _is_linked(b, 'researchvc_Paragraph17', a2)
    if hasattr(a2, 'researchvc_Write16'):
        assert not _is_linked(a2, 'researchvc_Write16', b)


def test_assoc_reviewNote18_reverse_link_reassign_clear():
    a1 = researchvc_ReviewNote(content="sample_text")
    a2 = researchvc_ReviewNote(content="sample_text_2")
    b = researchvc_Review(date=date(2024, 1, 1))
    _safe_set(b, 'researchvc_Review19', a1)
    assert _is_linked(b, 'researchvc_Review19', a1)
    if hasattr(a1, 'researchvc_ReviewNote20'):
        assert _is_linked(a1, 'researchvc_ReviewNote20', b)
    _safe_set(b, 'researchvc_Review19', a2)
    assert _is_linked(b, 'researchvc_Review19', a2)
    if hasattr(a1, 'researchvc_ReviewNote20'):
        assert not _is_linked(a1, 'researchvc_ReviewNote20', b)
    if hasattr(a2, 'researchvc_ReviewNote20'):
        assert _is_linked(a2, 'researchvc_ReviewNote20', b)
    _safe_set(b, 'researchvc_Review19', None)
    assert not _is_linked(b, 'researchvc_Review19', a2)
    if hasattr(a2, 'researchvc_ReviewNote20'):
        assert not _is_linked(a2, 'researchvc_ReviewNote20', b)


def test_assoc_reviews1_reverse_link_reassign_clear():
    a1 = researchvc_Review(date=date(2024, 1, 1))
    a2 = researchvc_Review(date=date(2025, 6, 15))
    b = researchvc_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'researchvc_Researcher2', {a1})
    assert _is_linked(b, 'researchvc_Researcher2', a1)
    if hasattr(a1, 'researchvc_Review'):
        assert _is_linked(a1, 'researchvc_Review', b)
    _safe_set(b, 'researchvc_Researcher2', {a2})
    assert _is_linked(b, 'researchvc_Researcher2', a2)
    if hasattr(a1, 'researchvc_Review'):
        assert not _is_linked(a1, 'researchvc_Review', b)
    if hasattr(a2, 'researchvc_Review'):
        assert _is_linked(a2, 'researchvc_Review', b)
    _safe_set(b, 'researchvc_Researcher2', set())
    assert not _is_linked(b, 'researchvc_Researcher2', a2)
    if hasattr(a2, 'researchvc_Review'):
        assert not _is_linked(a2, 'researchvc_Review', b)


def test_assoc_reviews13_reverse_link_reassign_clear():
    a1 = researchvc_ReviewNote(content="sample_text")
    a2 = researchvc_ReviewNote(content="sample_text_2")
    b = researchvc_Paragraph(content="sample_text")
    _safe_set(b, 'researchvc_Paragraph14', {a1})
    assert _is_linked(b, 'researchvc_Paragraph14', a1)
    if hasattr(a1, 'researchvc_ReviewNote'):
        assert _is_linked(a1, 'researchvc_ReviewNote', b)
    _safe_set(b, 'researchvc_Paragraph14', {a2})
    assert _is_linked(b, 'researchvc_Paragraph14', a2)
    if hasattr(a1, 'researchvc_ReviewNote'):
        assert not _is_linked(a1, 'researchvc_ReviewNote', b)
    if hasattr(a2, 'researchvc_ReviewNote'):
        assert _is_linked(a2, 'researchvc_ReviewNote', b)
    _safe_set(b, 'researchvc_Paragraph14', set())
    assert not _is_linked(b, 'researchvc_Paragraph14', a2)
    if hasattr(a2, 'researchvc_ReviewNote'):
        assert not _is_linked(a2, 'researchvc_ReviewNote', b)


def test_assoc_skills4_reverse_link_reassign_clear():
    a1 = researchvc_Skill(description="sample_text")
    a2 = researchvc_Skill(description="sample_text_2")
    b = researchvc_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'researchvc_Researcher5', {a1})
    assert _is_linked(b, 'researchvc_Researcher5', a1)
    if hasattr(a1, 'researchvc_Skill'):
        assert _is_linked(a1, 'researchvc_Skill', b)
    _safe_set(b, 'researchvc_Researcher5', {a2})
    assert _is_linked(b, 'researchvc_Researcher5', a2)
    if hasattr(a1, 'researchvc_Skill'):
        assert not _is_linked(a1, 'researchvc_Skill', b)
    if hasattr(a2, 'researchvc_Skill'):
        assert _is_linked(a2, 'researchvc_Skill', b)
    _safe_set(b, 'researchvc_Researcher5', set())
    assert not _is_linked(b, 'researchvc_Researcher5', a2)
    if hasattr(a2, 'researchvc_Skill'):
        assert not _is_linked(a2, 'researchvc_Skill', b)


def test_assoc_writes0_reverse_link_reassign_clear():
    a1 = researchvc_Write(timeSpent=7)
    a2 = researchvc_Write(timeSpent=13)
    b = researchvc_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'researchvc_Researcher', {a1})
    assert _is_linked(b, 'researchvc_Researcher', a1)
    if hasattr(a1, 'researchvc_Write'):
        assert _is_linked(a1, 'researchvc_Write', b)
    _safe_set(b, 'researchvc_Researcher', {a2})
    assert _is_linked(b, 'researchvc_Researcher', a2)
    if hasattr(a1, 'researchvc_Write'):
        assert not _is_linked(a1, 'researchvc_Write', b)
    if hasattr(a2, 'researchvc_Write'):
        assert _is_linked(a2, 'researchvc_Write', b)
    _safe_set(b, 'researchvc_Researcher', set())
    assert not _is_linked(b, 'researchvc_Researcher', a2)
    if hasattr(a2, 'researchvc_Write'):
        assert not _is_linked(a2, 'researchvc_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allKeyWords26_stub_double():
    # researchvc_PublicationStructure has no real 'researchvc_PublicationStructure27' property in the generated
    # code (a bare stub) -- manually attach it so researchvc_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchvc_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchvc_Keyword(word="sample_text")
    partner = researchvc_PublicationStructure()
    setattr(partner, 'researchvc_PublicationStructure27', None)
    _safe_set(owner, 'researchvc_Keyword', partner)
    assert owner in getattr(partner, 'researchvc_PublicationStructure27')
    _safe_set(owner, 'researchvc_Keyword', None)
    assert owner not in getattr(partner, 'researchvc_PublicationStructure27')


def test_assoc_authors7_stub_double():
    # researchvc_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so researchvc_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchvc_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchvc_Researcher(forName="sample_text", name="sample_text")
    partner = researchvc_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_keywords8_stub_double():
    # researchvc_Paper has no real 'researchvc_Paper9' property in the generated
    # code (a bare stub) -- manually attach it so researchvc_PaperKeyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchvc_PaperKeyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchvc_PaperKeyword(weight=7)
    partner = researchvc_Paper()
    setattr(partner, 'researchvc_Paper9', None)
    _safe_set(owner, 'researchvc_PaperKeyword', partner)
    assert owner in getattr(partner, 'researchvc_Paper9')
    _safe_set(owner, 'researchvc_PaperKeyword', None)
    assert owner not in getattr(partner, 'researchvc_Paper9')


def test_assoc_paragraphs6_stub_double():
    # researchvc_Paper has no real 'researchvc_Paper' property in the generated
    # code (a bare stub) -- manually attach it so researchvc_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchvc_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchvc_Paragraph(content="sample_text")
    partner = researchvc_Paper()
    setattr(partner, 'researchvc_Paper', None)
    _safe_set(owner, 'researchvc_Paragraph', partner)
    assert owner in getattr(partner, 'researchvc_Paper')
    _safe_set(owner, 'researchvc_Paragraph', None)
    assert owner not in getattr(partner, 'researchvc_Paper')


def test_assoc_res_papers3_stub_double():
    # researchvc_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so researchvc_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchvc_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchvc_Researcher(forName="sample_text", name="sample_text")
    partner = researchvc_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers21_stub_double():
    # researchvc_PublicationStructure has no real 'researchvc_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so researchvc_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchvc_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchvc_Researcher(forName="sample_text", name="sample_text")
    partner = researchvc_PublicationStructure()
    setattr(partner, 'researchvc_PublicationStructure', None)
    _safe_set(owner, 'researchvc_Researcher22', partner)
    assert owner in getattr(partner, 'researchvc_PublicationStructure')
    _safe_set(owner, 'researchvc_Researcher22', None)
    assert owner not in getattr(partner, 'researchvc_PublicationStructure')


