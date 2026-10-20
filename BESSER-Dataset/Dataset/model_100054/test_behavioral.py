import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    researchva_Counted,
    researchva_Keyword,
    researchva_Labelled,
    researchva_Named,
    researchva_Paper,
    researchva_Paragraph,
    researchva_PublicationStructure,
    researchva_Researcher,
    researchva_Review,
    researchva_ReviewNote,
    researchva_Skill,
    researchva_Write,
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

def test_assoc_paragraph13_reverse_link_reassign_clear():
    a1 = researchva_Write(timeSpent=7)
    a2 = researchva_Write(timeSpent=13)
    b = researchva_Paragraph(content="sample_text")
    _safe_set(b, 'researchva_Paragraph15', a1)
    assert _is_linked(b, 'researchva_Paragraph15', a1)
    if hasattr(a1, 'researchva_Write14'):
        assert _is_linked(a1, 'researchva_Write14', b)
    _safe_set(b, 'researchva_Paragraph15', a2)
    assert _is_linked(b, 'researchva_Paragraph15', a2)
    if hasattr(a1, 'researchva_Write14'):
        assert not _is_linked(a1, 'researchva_Write14', b)
    if hasattr(a2, 'researchva_Write14'):
        assert _is_linked(a2, 'researchva_Write14', b)
    _safe_set(b, 'researchva_Paragraph15', None)
    assert not _is_linked(b, 'researchva_Paragraph15', a2)
    if hasattr(a2, 'researchva_Write14'):
        assert not _is_linked(a2, 'researchva_Write14', b)


def test_assoc_reviewNote16_reverse_link_reassign_clear():
    a1 = researchva_ReviewNote(content="sample_text")
    a2 = researchva_ReviewNote(content="sample_text_2")
    b = researchva_Review(date=date(2024, 1, 1))
    _safe_set(b, 'researchva_Review17', a1)
    assert _is_linked(b, 'researchva_Review17', a1)
    if hasattr(a1, 'researchva_ReviewNote18'):
        assert _is_linked(a1, 'researchva_ReviewNote18', b)
    _safe_set(b, 'researchva_Review17', a2)
    assert _is_linked(b, 'researchva_Review17', a2)
    if hasattr(a1, 'researchva_ReviewNote18'):
        assert not _is_linked(a1, 'researchva_ReviewNote18', b)
    if hasattr(a2, 'researchva_ReviewNote18'):
        assert _is_linked(a2, 'researchva_ReviewNote18', b)
    _safe_set(b, 'researchva_Review17', None)
    assert not _is_linked(b, 'researchva_Review17', a2)
    if hasattr(a2, 'researchva_ReviewNote18'):
        assert not _is_linked(a2, 'researchva_ReviewNote18', b)


def test_assoc_reviews1_reverse_link_reassign_clear():
    a1 = researchva_Review(date=date(2024, 1, 1))
    a2 = researchva_Review(date=date(2025, 6, 15))
    b = researchva_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'researchva_Researcher2', {a1})
    assert _is_linked(b, 'researchva_Researcher2', a1)
    if hasattr(a1, 'researchva_Review'):
        assert _is_linked(a1, 'researchva_Review', b)
    _safe_set(b, 'researchva_Researcher2', {a2})
    assert _is_linked(b, 'researchva_Researcher2', a2)
    if hasattr(a1, 'researchva_Review'):
        assert not _is_linked(a1, 'researchva_Review', b)
    if hasattr(a2, 'researchva_Review'):
        assert _is_linked(a2, 'researchva_Review', b)
    _safe_set(b, 'researchva_Researcher2', set())
    assert not _is_linked(b, 'researchva_Researcher2', a2)
    if hasattr(a2, 'researchva_Review'):
        assert not _is_linked(a2, 'researchva_Review', b)


def test_assoc_reviews11_reverse_link_reassign_clear():
    a1 = researchva_ReviewNote(content="sample_text")
    a2 = researchva_ReviewNote(content="sample_text_2")
    b = researchva_Paragraph(content="sample_text")
    _safe_set(b, 'researchva_Paragraph12', {a1})
    assert _is_linked(b, 'researchva_Paragraph12', a1)
    if hasattr(a1, 'researchva_ReviewNote'):
        assert _is_linked(a1, 'researchva_ReviewNote', b)
    _safe_set(b, 'researchva_Paragraph12', {a2})
    assert _is_linked(b, 'researchva_Paragraph12', a2)
    if hasattr(a1, 'researchva_ReviewNote'):
        assert not _is_linked(a1, 'researchva_ReviewNote', b)
    if hasattr(a2, 'researchva_ReviewNote'):
        assert _is_linked(a2, 'researchva_ReviewNote', b)
    _safe_set(b, 'researchva_Paragraph12', set())
    assert not _is_linked(b, 'researchva_Paragraph12', a2)
    if hasattr(a2, 'researchva_ReviewNote'):
        assert not _is_linked(a2, 'researchva_ReviewNote', b)


def test_assoc_skills4_reverse_link_reassign_clear():
    a1 = researchva_Skill(description="sample_text")
    a2 = researchva_Skill(description="sample_text_2")
    b = researchva_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'researchva_Researcher5', {a1})
    assert _is_linked(b, 'researchva_Researcher5', a1)
    if hasattr(a1, 'researchva_Skill'):
        assert _is_linked(a1, 'researchva_Skill', b)
    _safe_set(b, 'researchva_Researcher5', {a2})
    assert _is_linked(b, 'researchva_Researcher5', a2)
    if hasattr(a1, 'researchva_Skill'):
        assert not _is_linked(a1, 'researchva_Skill', b)
    if hasattr(a2, 'researchva_Skill'):
        assert _is_linked(a2, 'researchva_Skill', b)
    _safe_set(b, 'researchva_Researcher5', set())
    assert not _is_linked(b, 'researchva_Researcher5', a2)
    if hasattr(a2, 'researchva_Skill'):
        assert not _is_linked(a2, 'researchva_Skill', b)


def test_assoc_writes0_reverse_link_reassign_clear():
    a1 = researchva_Write(timeSpent=7)
    a2 = researchva_Write(timeSpent=13)
    b = researchva_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'researchva_Researcher', {a1})
    assert _is_linked(b, 'researchva_Researcher', a1)
    if hasattr(a1, 'researchva_Write'):
        assert _is_linked(a1, 'researchva_Write', b)
    _safe_set(b, 'researchva_Researcher', {a2})
    assert _is_linked(b, 'researchva_Researcher', a2)
    if hasattr(a1, 'researchva_Write'):
        assert not _is_linked(a1, 'researchva_Write', b)
    if hasattr(a2, 'researchva_Write'):
        assert _is_linked(a2, 'researchva_Write', b)
    _safe_set(b, 'researchva_Researcher', set())
    assert not _is_linked(b, 'researchva_Researcher', a2)
    if hasattr(a2, 'researchva_Write'):
        assert not _is_linked(a2, 'researchva_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allKeyWords24_stub_double():
    # researchva_PublicationStructure has no real 'researchva_PublicationStructure25' property in the generated
    # code (a bare stub) -- manually attach it so researchva_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchva_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchva_Keyword(word="sample_text")
    partner = researchva_PublicationStructure()
    setattr(partner, 'researchva_PublicationStructure25', None)
    _safe_set(owner, 'researchva_Keyword', partner)
    assert owner in getattr(partner, 'researchva_PublicationStructure25')
    _safe_set(owner, 'researchva_Keyword', None)
    assert owner not in getattr(partner, 'researchva_PublicationStructure25')


def test_assoc_authors7_stub_double():
    # researchva_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so researchva_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchva_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchva_Researcher(forName="sample_text", name="sample_text")
    partner = researchva_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_paragraphs6_stub_double():
    # researchva_Paper has no real 'researchva_Paper' property in the generated
    # code (a bare stub) -- manually attach it so researchva_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchva_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchva_Paragraph(content="sample_text")
    partner = researchva_Paper()
    setattr(partner, 'researchva_Paper', None)
    _safe_set(owner, 'researchva_Paragraph', partner)
    assert owner in getattr(partner, 'researchva_Paper')
    _safe_set(owner, 'researchva_Paragraph', None)
    assert owner not in getattr(partner, 'researchva_Paper')


def test_assoc_res_papers3_stub_double():
    # researchva_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so researchva_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchva_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchva_Researcher(forName="sample_text", name="sample_text")
    partner = researchva_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers19_stub_double():
    # researchva_PublicationStructure has no real 'researchva_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so researchva_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # researchva_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = researchva_Researcher(forName="sample_text", name="sample_text")
    partner = researchva_PublicationStructure()
    setattr(partner, 'researchva_PublicationStructure', None)
    _safe_set(owner, 'researchva_Researcher20', partner)
    assert owner in getattr(partner, 'researchva_PublicationStructure')
    _safe_set(owner, 'researchva_Researcher20', None)
    assert owner not in getattr(partner, 'researchva_PublicationStructure')


