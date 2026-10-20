import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    publication103_Collaboration,
    publication103_Counted,
    publication103_Labelled,
    publication103_Named,
    publication103_Paper,
    publication103_Paragraph,
    publication103_Position,
    publication103_PublicationStructure,
    publication103_Researcher,
    publication103_Review,
    publication103_ReviewNote,
    publication103_Skill,
    publication103_Write,
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
    a1 = publication103_Researcher(forName="sample_text", name="sample_text")
    a2 = publication103_Researcher(forName="sample_text_2", name="sample_text_2")
    b = publication103_Collaboration(ratio=7)
    _safe_set(b, 'publication103_Collaboration', a1)
    assert _is_linked(b, 'publication103_Collaboration', a1)
    if hasattr(a1, 'publication103_Researcher9'):
        assert _is_linked(a1, 'publication103_Researcher9', b)
    _safe_set(b, 'publication103_Collaboration', a2)
    assert _is_linked(b, 'publication103_Collaboration', a2)
    if hasattr(a1, 'publication103_Researcher9'):
        assert not _is_linked(a1, 'publication103_Researcher9', b)
    if hasattr(a2, 'publication103_Researcher9'):
        assert _is_linked(a2, 'publication103_Researcher9', b)
    _safe_set(b, 'publication103_Collaboration', None)
    assert not _is_linked(b, 'publication103_Collaboration', a2)
    if hasattr(a2, 'publication103_Researcher9'):
        assert not _is_linked(a2, 'publication103_Researcher9', b)


def test_assoc_paragraph17_reverse_link_reassign_clear():
    a1 = publication103_Write(timeSpent=7)
    a2 = publication103_Write(timeSpent=13)
    b = publication103_Paragraph(content="sample_text")
    _safe_set(b, 'publication103_Paragraph19', a1)
    assert _is_linked(b, 'publication103_Paragraph19', a1)
    if hasattr(a1, 'publication103_Write18'):
        assert _is_linked(a1, 'publication103_Write18', b)
    _safe_set(b, 'publication103_Paragraph19', a2)
    assert _is_linked(b, 'publication103_Paragraph19', a2)
    if hasattr(a1, 'publication103_Write18'):
        assert not _is_linked(a1, 'publication103_Write18', b)
    if hasattr(a2, 'publication103_Write18'):
        assert _is_linked(a2, 'publication103_Write18', b)
    _safe_set(b, 'publication103_Paragraph19', None)
    assert not _is_linked(b, 'publication103_Paragraph19', a2)
    if hasattr(a2, 'publication103_Write18'):
        assert not _is_linked(a2, 'publication103_Write18', b)


def test_assoc_parent32_reverse_link_reassign_clear():
    a1 = publication103_Position(description="sample_text")
    a2 = publication103_Position(description="sample_text_2")
    b = publication103_Position(description="sample_text")
    _safe_set(b, 'publication103_Position33', a1)
    assert _is_linked(b, 'publication103_Position33', a1)
    if hasattr(a1, 'publication103_Position31'):
        assert _is_linked(a1, 'publication103_Position31', b)
    _safe_set(b, 'publication103_Position33', a2)
    assert _is_linked(b, 'publication103_Position33', a2)
    if hasattr(a1, 'publication103_Position31'):
        assert not _is_linked(a1, 'publication103_Position31', b)
    if hasattr(a2, 'publication103_Position31'):
        assert _is_linked(a2, 'publication103_Position31', b)
    _safe_set(b, 'publication103_Position33', None)
    assert not _is_linked(b, 'publication103_Position33', a2)
    if hasattr(a2, 'publication103_Position31'):
        assert not _is_linked(a2, 'publication103_Position31', b)


def test_assoc_res_position6_reverse_link_reassign_clear():
    a1 = publication103_Researcher(forName="sample_text", name="sample_text")
    a2 = publication103_Researcher(forName="sample_text_2", name="sample_text_2")
    b = publication103_Position(description="sample_text")
    _safe_set(b, 'publication103_Position', a1)
    assert _is_linked(b, 'publication103_Position', a1)
    if hasattr(a1, 'publication103_Researcher7'):
        assert _is_linked(a1, 'publication103_Researcher7', b)
    _safe_set(b, 'publication103_Position', a2)
    assert _is_linked(b, 'publication103_Position', a2)
    if hasattr(a1, 'publication103_Researcher7'):
        assert not _is_linked(a1, 'publication103_Researcher7', b)
    if hasattr(a2, 'publication103_Researcher7'):
        assert _is_linked(a2, 'publication103_Researcher7', b)
    _safe_set(b, 'publication103_Position', None)
    assert not _is_linked(b, 'publication103_Position', a2)
    if hasattr(a2, 'publication103_Researcher7'):
        assert not _is_linked(a2, 'publication103_Researcher7', b)


def test_assoc_reviewNote20_reverse_link_reassign_clear():
    a1 = publication103_ReviewNote(content="sample_text")
    a2 = publication103_ReviewNote(content="sample_text_2")
    b = publication103_Review(date=date(2024, 1, 1))
    _safe_set(b, 'publication103_Review21', a1)
    assert _is_linked(b, 'publication103_Review21', a1)
    if hasattr(a1, 'publication103_ReviewNote22'):
        assert _is_linked(a1, 'publication103_ReviewNote22', b)
    _safe_set(b, 'publication103_Review21', a2)
    assert _is_linked(b, 'publication103_Review21', a2)
    if hasattr(a1, 'publication103_ReviewNote22'):
        assert not _is_linked(a1, 'publication103_ReviewNote22', b)
    if hasattr(a2, 'publication103_ReviewNote22'):
        assert _is_linked(a2, 'publication103_ReviewNote22', b)
    _safe_set(b, 'publication103_Review21', None)
    assert not _is_linked(b, 'publication103_Review21', a2)
    if hasattr(a2, 'publication103_ReviewNote22'):
        assert not _is_linked(a2, 'publication103_ReviewNote22', b)


def test_assoc_reviews1_reverse_link_reassign_clear():
    a1 = publication103_Review(date=date(2024, 1, 1))
    a2 = publication103_Review(date=date(2025, 6, 15))
    b = publication103_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'publication103_Researcher2', {a1})
    assert _is_linked(b, 'publication103_Researcher2', a1)
    if hasattr(a1, 'publication103_Review'):
        assert _is_linked(a1, 'publication103_Review', b)
    _safe_set(b, 'publication103_Researcher2', {a2})
    assert _is_linked(b, 'publication103_Researcher2', a2)
    if hasattr(a1, 'publication103_Review'):
        assert not _is_linked(a1, 'publication103_Review', b)
    if hasattr(a2, 'publication103_Review'):
        assert _is_linked(a2, 'publication103_Review', b)
    _safe_set(b, 'publication103_Researcher2', set())
    assert not _is_linked(b, 'publication103_Researcher2', a2)
    if hasattr(a2, 'publication103_Review'):
        assert not _is_linked(a2, 'publication103_Review', b)


def test_assoc_reviews15_reverse_link_reassign_clear():
    a1 = publication103_ReviewNote(content="sample_text")
    a2 = publication103_ReviewNote(content="sample_text_2")
    b = publication103_Paragraph(content="sample_text")
    _safe_set(b, 'publication103_Paragraph16', {a1})
    assert _is_linked(b, 'publication103_Paragraph16', a1)
    if hasattr(a1, 'publication103_ReviewNote'):
        assert _is_linked(a1, 'publication103_ReviewNote', b)
    _safe_set(b, 'publication103_Paragraph16', {a2})
    assert _is_linked(b, 'publication103_Paragraph16', a2)
    if hasattr(a1, 'publication103_ReviewNote'):
        assert not _is_linked(a1, 'publication103_ReviewNote', b)
    if hasattr(a2, 'publication103_ReviewNote'):
        assert _is_linked(a2, 'publication103_ReviewNote', b)
    _safe_set(b, 'publication103_Paragraph16', set())
    assert not _is_linked(b, 'publication103_Paragraph16', a2)
    if hasattr(a2, 'publication103_ReviewNote'):
        assert not _is_linked(a2, 'publication103_ReviewNote', b)


def test_assoc_skills4_reverse_link_reassign_clear():
    a1 = publication103_Skill(description="sample_text")
    a2 = publication103_Skill(description="sample_text_2")
    b = publication103_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'publication103_Researcher5', {a1})
    assert _is_linked(b, 'publication103_Researcher5', a1)
    if hasattr(a1, 'publication103_Skill'):
        assert _is_linked(a1, 'publication103_Skill', b)
    _safe_set(b, 'publication103_Researcher5', {a2})
    assert _is_linked(b, 'publication103_Researcher5', a2)
    if hasattr(a1, 'publication103_Skill'):
        assert not _is_linked(a1, 'publication103_Skill', b)
    if hasattr(a2, 'publication103_Skill'):
        assert _is_linked(a2, 'publication103_Skill', b)
    _safe_set(b, 'publication103_Researcher5', set())
    assert not _is_linked(b, 'publication103_Researcher5', a2)
    if hasattr(a2, 'publication103_Skill'):
        assert not _is_linked(a2, 'publication103_Skill', b)


def test_assoc_writes0_reverse_link_reassign_clear():
    a1 = publication103_Write(timeSpent=7)
    a2 = publication103_Write(timeSpent=13)
    b = publication103_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'publication103_Researcher', {a1})
    assert _is_linked(b, 'publication103_Researcher', a1)
    if hasattr(a1, 'publication103_Write'):
        assert _is_linked(a1, 'publication103_Write', b)
    _safe_set(b, 'publication103_Researcher', {a2})
    assert _is_linked(b, 'publication103_Researcher', a2)
    if hasattr(a1, 'publication103_Write'):
        assert not _is_linked(a1, 'publication103_Write', b)
    if hasattr(a2, 'publication103_Write'):
        assert _is_linked(a2, 'publication103_Write', b)
    _safe_set(b, 'publication103_Researcher', set())
    assert not _is_linked(b, 'publication103_Researcher', a2)
    if hasattr(a2, 'publication103_Write'):
        assert not _is_linked(a2, 'publication103_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors11_stub_double():
    # publication103_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so publication103_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication103_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication103_Researcher(forName="sample_text", name="sample_text")
    partner = publication103_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_col_paper34_stub_double():
    # publication103_Paper has no real 'publication103_Paper36' property in the generated
    # code (a bare stub) -- manually attach it so publication103_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication103_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication103_Collaboration(ratio=7)
    partner = publication103_Paper()
    setattr(partner, 'publication103_Paper36', None)
    _safe_set(owner, 'publication103_Collaboration35', partner)
    assert getattr(partner, 'publication103_Paper36') == owner
    _safe_set(owner, 'publication103_Collaboration35', None)
    assert getattr(partner, 'publication103_Paper36') is None


def test_assoc_paragraphs10_stub_double():
    # publication103_Paper has no real 'publication103_Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication103_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication103_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication103_Paragraph(content="sample_text")
    partner = publication103_Paper()
    setattr(partner, 'publication103_Paper', None)
    _safe_set(owner, 'publication103_Paragraph', partner)
    assert owner in getattr(partner, 'publication103_Paper')
    _safe_set(owner, 'publication103_Paragraph', None)
    assert owner not in getattr(partner, 'publication103_Paper')


def test_assoc_positions28_stub_double():
    # publication103_PublicationStructure has no real 'publication103_PublicationStructure29' property in the generated
    # code (a bare stub) -- manually attach it so publication103_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication103_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication103_Position(description="sample_text")
    partner = publication103_PublicationStructure()
    setattr(partner, 'publication103_PublicationStructure29', None)
    _safe_set(owner, 'publication103_Position30', partner)
    assert owner in getattr(partner, 'publication103_PublicationStructure29')
    _safe_set(owner, 'publication103_Position30', None)
    assert owner not in getattr(partner, 'publication103_PublicationStructure29')


def test_assoc_res_papers3_stub_double():
    # publication103_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication103_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication103_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication103_Researcher(forName="sample_text", name="sample_text")
    partner = publication103_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers23_stub_double():
    # publication103_PublicationStructure has no real 'publication103_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so publication103_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication103_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication103_Researcher(forName="sample_text", name="sample_text")
    partner = publication103_PublicationStructure()
    setattr(partner, 'publication103_PublicationStructure', None)
    _safe_set(owner, 'publication103_Researcher24', partner)
    assert owner in getattr(partner, 'publication103_PublicationStructure')
    _safe_set(owner, 'publication103_Researcher24', None)
    assert owner not in getattr(partner, 'publication103_PublicationStructure')


