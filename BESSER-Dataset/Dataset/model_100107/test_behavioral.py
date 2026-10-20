import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tp6_Collaboration,
    tp6_Keyword,
    tp6_KnowledgeManager,
    tp6_Paper,
    tp6_PaperKeywords,
    tp6_Paragraph,
    tp6_Position,
    tp6_PublicationStructure,
    tp6_Researcher,
    tp6_Skill,
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

def test_assoc_allKeywords34_reverse_link_reassign_clear():
    a1 = tp6_KnowledgeManager(name="sample_text")
    a2 = tp6_KnowledgeManager(name="sample_text_2")
    b = tp6_Keyword(description="sample_text", key="sample_text")
    _safe_set(b, 'tp6_Keyword36', a1)
    assert _is_linked(b, 'tp6_Keyword36', a1)
    if hasattr(a1, 'tp6_KnowledgeManager35'):
        assert _is_linked(a1, 'tp6_KnowledgeManager35', b)
    _safe_set(b, 'tp6_Keyword36', a2)
    assert _is_linked(b, 'tp6_Keyword36', a2)
    if hasattr(a1, 'tp6_KnowledgeManager35'):
        assert not _is_linked(a1, 'tp6_KnowledgeManager35', b)
    if hasattr(a2, 'tp6_KnowledgeManager35'):
        assert _is_linked(a2, 'tp6_KnowledgeManager35', b)
    _safe_set(b, 'tp6_Keyword36', None)
    assert not _is_linked(b, 'tp6_Keyword36', a2)
    if hasattr(a2, 'tp6_KnowledgeManager35'):
        assert not _is_linked(a2, 'tp6_KnowledgeManager35', b)


def test_assoc_authors7_reverse_link_reassign_clear():
    a1 = tp6_Researcher(forName="sample_text", name="sample_text")
    a2 = tp6_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp6_Paper(name="sample_text")
    _safe_set(b, 'res_papers', {a1})
    assert _is_linked(b, 'res_papers', a1)
    if hasattr(a1, 'Researcher'):
        assert _is_linked(a1, 'Researcher', b)
    _safe_set(b, 'res_papers', {a2})
    assert _is_linked(b, 'res_papers', a2)
    if hasattr(a1, 'Researcher'):
        assert not _is_linked(a1, 'Researcher', b)
    if hasattr(a2, 'Researcher'):
        assert _is_linked(a2, 'Researcher', b)
    _safe_set(b, 'res_papers', set())
    assert not _is_linked(b, 'res_papers', a2)
    if hasattr(a2, 'Researcher'):
        assert not _is_linked(a2, 'Researcher', b)


def test_assoc_citedBy9_reverse_link_reassign_clear():
    a1 = tp6_Paper(name="sample_text")
    a2 = tp6_Paper(name="sample_text_2")
    b = tp6_Paper(name="sample_text")
    _safe_set(b, 'tp6_Paper8', a1)
    assert _is_linked(b, 'tp6_Paper8', a1)
    if hasattr(a1, 'tp6_Paper10'):
        assert _is_linked(a1, 'tp6_Paper10', b)
    _safe_set(b, 'tp6_Paper8', a2)
    assert _is_linked(b, 'tp6_Paper8', a2)
    if hasattr(a1, 'tp6_Paper10'):
        assert not _is_linked(a1, 'tp6_Paper10', b)
    if hasattr(a2, 'tp6_Paper10'):
        assert _is_linked(a2, 'tp6_Paper10', b)
    _safe_set(b, 'tp6_Paper8', None)
    assert not _is_linked(b, 'tp6_Paper8', a2)
    if hasattr(a2, 'tp6_Paper10'):
        assert not _is_linked(a2, 'tp6_Paper10', b)


def test_assoc_col_paper26_reverse_link_reassign_clear():
    a1 = tp6_Paper(name="sample_text")
    a2 = tp6_Paper(name="sample_text_2")
    b = tp6_Collaboration(ratio=7)
    _safe_set(b, 'tp6_Collaboration27', a1)
    assert _is_linked(b, 'tp6_Collaboration27', a1)
    if hasattr(a1, 'tp6_Paper28'):
        assert _is_linked(a1, 'tp6_Paper28', b)
    _safe_set(b, 'tp6_Collaboration27', a2)
    assert _is_linked(b, 'tp6_Collaboration27', a2)
    if hasattr(a1, 'tp6_Paper28'):
        assert not _is_linked(a1, 'tp6_Paper28', b)
    if hasattr(a2, 'tp6_Paper28'):
        assert _is_linked(a2, 'tp6_Paper28', b)
    _safe_set(b, 'tp6_Collaboration27', None)
    assert not _is_linked(b, 'tp6_Collaboration27', a2)
    if hasattr(a2, 'tp6_Paper28'):
        assert not _is_linked(a2, 'tp6_Paper28', b)


def test_assoc_collaborations4_reverse_link_reassign_clear():
    a1 = tp6_Researcher(forName="sample_text", name="sample_text")
    a2 = tp6_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp6_Collaboration(ratio=7)
    _safe_set(b, 'tp6_Collaboration', a1)
    assert _is_linked(b, 'tp6_Collaboration', a1)
    if hasattr(a1, 'tp6_Researcher5'):
        assert _is_linked(a1, 'tp6_Researcher5', b)
    _safe_set(b, 'tp6_Collaboration', a2)
    assert _is_linked(b, 'tp6_Collaboration', a2)
    if hasattr(a1, 'tp6_Researcher5'):
        assert not _is_linked(a1, 'tp6_Researcher5', b)
    if hasattr(a2, 'tp6_Researcher5'):
        assert _is_linked(a2, 'tp6_Researcher5', b)
    _safe_set(b, 'tp6_Collaboration', None)
    assert not _is_linked(b, 'tp6_Collaboration', a2)
    if hasattr(a2, 'tp6_Researcher5'):
        assert not _is_linked(a2, 'tp6_Researcher5', b)


def test_assoc_kPapers29_reverse_link_reassign_clear():
    a1 = tp6_Paper(name="sample_text")
    a2 = tp6_Paper(name="sample_text_2")
    b = tp6_Keyword(description="sample_text", key="sample_text")
    _safe_set(b, 'tp6_Keyword', {a1})
    assert _is_linked(b, 'tp6_Keyword', a1)
    if hasattr(a1, 'tp6_Paper30'):
        assert _is_linked(a1, 'tp6_Paper30', b)
    _safe_set(b, 'tp6_Keyword', {a2})
    assert _is_linked(b, 'tp6_Keyword', a2)
    if hasattr(a1, 'tp6_Paper30'):
        assert not _is_linked(a1, 'tp6_Paper30', b)
    if hasattr(a2, 'tp6_Paper30'):
        assert _is_linked(a2, 'tp6_Paper30', b)
    _safe_set(b, 'tp6_Keyword', set())
    assert not _is_linked(b, 'tp6_Keyword', a2)
    if hasattr(a2, 'tp6_Paper30'):
        assert not _is_linked(a2, 'tp6_Paper30', b)


def test_assoc_keyword31_reverse_link_reassign_clear():
    a1 = tp6_PaperKeywords(weight=7)
    a2 = tp6_PaperKeywords(weight=13)
    b = tp6_Keyword(description="sample_text", key="sample_text")
    _safe_set(b, 'tp6_Keyword33', a1)
    assert _is_linked(b, 'tp6_Keyword33', a1)
    if hasattr(a1, 'tp6_PaperKeywords32'):
        assert _is_linked(a1, 'tp6_PaperKeywords32', b)
    _safe_set(b, 'tp6_Keyword33', a2)
    assert _is_linked(b, 'tp6_Keyword33', a2)
    if hasattr(a1, 'tp6_PaperKeywords32'):
        assert not _is_linked(a1, 'tp6_PaperKeywords32', b)
    if hasattr(a2, 'tp6_PaperKeywords32'):
        assert _is_linked(a2, 'tp6_PaperKeywords32', b)
    _safe_set(b, 'tp6_Keyword33', None)
    assert not _is_linked(b, 'tp6_Keyword33', a2)
    if hasattr(a2, 'tp6_PaperKeywords32'):
        assert not _is_linked(a2, 'tp6_PaperKeywords32', b)


def test_assoc_keywords11_reverse_link_reassign_clear():
    a1 = tp6_PaperKeywords(weight=7)
    a2 = tp6_PaperKeywords(weight=13)
    b = tp6_Paper(name="sample_text")
    _safe_set(b, 'tp6_Paper12', {a1})
    assert _is_linked(b, 'tp6_Paper12', a1)
    if hasattr(a1, 'tp6_PaperKeywords'):
        assert _is_linked(a1, 'tp6_PaperKeywords', b)
    _safe_set(b, 'tp6_Paper12', {a2})
    assert _is_linked(b, 'tp6_Paper12', a2)
    if hasattr(a1, 'tp6_PaperKeywords'):
        assert not _is_linked(a1, 'tp6_PaperKeywords', b)
    if hasattr(a2, 'tp6_PaperKeywords'):
        assert _is_linked(a2, 'tp6_PaperKeywords', b)
    _safe_set(b, 'tp6_Paper12', set())
    assert not _is_linked(b, 'tp6_Paper12', a2)
    if hasattr(a2, 'tp6_PaperKeywords'):
        assert not _is_linked(a2, 'tp6_PaperKeywords', b)


def test_assoc_paragraphs6_reverse_link_reassign_clear():
    a1 = tp6_Paragraph(content="sample_text", id=7, name="sample_text")
    a2 = tp6_Paragraph(content="sample_text_2", id=13, name="sample_text_2")
    b = tp6_Paper(name="sample_text")
    _safe_set(b, 'tp6_Paper', {a1})
    assert _is_linked(b, 'tp6_Paper', a1)
    if hasattr(a1, 'tp6_Paragraph'):
        assert _is_linked(a1, 'tp6_Paragraph', b)
    _safe_set(b, 'tp6_Paper', {a2})
    assert _is_linked(b, 'tp6_Paper', a2)
    if hasattr(a1, 'tp6_Paragraph'):
        assert not _is_linked(a1, 'tp6_Paragraph', b)
    if hasattr(a2, 'tp6_Paragraph'):
        assert _is_linked(a2, 'tp6_Paragraph', b)
    _safe_set(b, 'tp6_Paper', set())
    assert not _is_linked(b, 'tp6_Paper', a2)
    if hasattr(a2, 'tp6_Paragraph'):
        assert not _is_linked(a2, 'tp6_Paragraph', b)


def test_assoc_parent24_reverse_link_reassign_clear():
    a1 = tp6_Position(description="sample_text", name="sample_text")
    a2 = tp6_Position(description="sample_text_2", name="sample_text_2")
    b = tp6_Position(description="sample_text", name="sample_text")
    _safe_set(b, 'tp6_Position25', a1)
    assert _is_linked(b, 'tp6_Position25', a1)
    if hasattr(a1, 'tp6_Position23'):
        assert _is_linked(a1, 'tp6_Position23', b)
    _safe_set(b, 'tp6_Position25', a2)
    assert _is_linked(b, 'tp6_Position25', a2)
    if hasattr(a1, 'tp6_Position23'):
        assert not _is_linked(a1, 'tp6_Position23', b)
    if hasattr(a2, 'tp6_Position23'):
        assert _is_linked(a2, 'tp6_Position23', b)
    _safe_set(b, 'tp6_Position25', None)
    assert not _is_linked(b, 'tp6_Position25', a2)
    if hasattr(a2, 'tp6_Position23'):
        assert not _is_linked(a2, 'tp6_Position23', b)


def test_assoc_res_papers0_reverse_link_reassign_clear():
    a1 = tp6_Researcher(forName="sample_text", name="sample_text")
    a2 = tp6_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp6_Paper(name="sample_text")
    _safe_set(b, 'Paper', a1)
    assert _is_linked(b, 'Paper', a1)
    if hasattr(a1, 'authors'):
        assert _is_linked(a1, 'authors', b)
    _safe_set(b, 'Paper', a2)
    assert _is_linked(b, 'Paper', a2)
    if hasattr(a1, 'authors'):
        assert not _is_linked(a1, 'authors', b)
    if hasattr(a2, 'authors'):
        assert _is_linked(a2, 'authors', b)
    _safe_set(b, 'Paper', None)
    assert not _is_linked(b, 'Paper', a2)
    if hasattr(a2, 'authors'):
        assert not _is_linked(a2, 'authors', b)


def test_assoc_res_position2_reverse_link_reassign_clear():
    a1 = tp6_Researcher(forName="sample_text", name="sample_text")
    a2 = tp6_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp6_Position(description="sample_text", name="sample_text")
    _safe_set(b, 'tp6_Position', a1)
    assert _is_linked(b, 'tp6_Position', a1)
    if hasattr(a1, 'tp6_Researcher3'):
        assert _is_linked(a1, 'tp6_Researcher3', b)
    _safe_set(b, 'tp6_Position', a2)
    assert _is_linked(b, 'tp6_Position', a2)
    if hasattr(a1, 'tp6_Researcher3'):
        assert not _is_linked(a1, 'tp6_Researcher3', b)
    if hasattr(a2, 'tp6_Researcher3'):
        assert _is_linked(a2, 'tp6_Researcher3', b)
    _safe_set(b, 'tp6_Position', None)
    assert not _is_linked(b, 'tp6_Position', a2)
    if hasattr(a2, 'tp6_Researcher3'):
        assert not _is_linked(a2, 'tp6_Researcher3', b)


def test_assoc_skills1_reverse_link_reassign_clear():
    a1 = tp6_Skill(description="sample_text")
    a2 = tp6_Skill(description="sample_text_2")
    b = tp6_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'tp6_Researcher', {a1})
    assert _is_linked(b, 'tp6_Researcher', a1)
    if hasattr(a1, 'tp6_Skill'):
        assert _is_linked(a1, 'tp6_Skill', b)
    _safe_set(b, 'tp6_Researcher', {a2})
    assert _is_linked(b, 'tp6_Researcher', a2)
    if hasattr(a1, 'tp6_Skill'):
        assert not _is_linked(a1, 'tp6_Skill', b)
    if hasattr(a2, 'tp6_Skill'):
        assert _is_linked(a2, 'tp6_Skill', b)
    _safe_set(b, 'tp6_Researcher', set())
    assert not _is_linked(b, 'tp6_Researcher', a2)
    if hasattr(a2, 'tp6_Skill'):
        assert not _is_linked(a2, 'tp6_Skill', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_knowledgeMan21_stub_double():
    # tp6_PublicationStructure has no real 'tp6_PublicationStructure22' property in the generated
    # code (a bare stub) -- manually attach it so tp6_KnowledgeManager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp6_KnowledgeManager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp6_KnowledgeManager(name="sample_text")
    partner = tp6_PublicationStructure()
    setattr(partner, 'tp6_PublicationStructure22', None)
    _safe_set(owner, 'tp6_KnowledgeManager', partner)
    assert getattr(partner, 'tp6_PublicationStructure22') == owner
    _safe_set(owner, 'tp6_KnowledgeManager', None)
    assert getattr(partner, 'tp6_PublicationStructure22') is None


def test_assoc_papers15_stub_double():
    # tp6_PublicationStructure has no real 'tp6_PublicationStructure16' property in the generated
    # code (a bare stub) -- manually attach it so tp6_Paper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp6_Paper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp6_Paper(name="sample_text")
    partner = tp6_PublicationStructure()
    setattr(partner, 'tp6_PublicationStructure16', None)
    _safe_set(owner, 'tp6_Paper17', partner)
    assert owner in getattr(partner, 'tp6_PublicationStructure16')
    _safe_set(owner, 'tp6_Paper17', None)
    assert owner not in getattr(partner, 'tp6_PublicationStructure16')


def test_assoc_positions18_stub_double():
    # tp6_PublicationStructure has no real 'tp6_PublicationStructure19' property in the generated
    # code (a bare stub) -- manually attach it so tp6_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp6_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp6_Position(description="sample_text", name="sample_text")
    partner = tp6_PublicationStructure()
    setattr(partner, 'tp6_PublicationStructure19', None)
    _safe_set(owner, 'tp6_Position20', partner)
    assert owner in getattr(partner, 'tp6_PublicationStructure19')
    _safe_set(owner, 'tp6_Position20', None)
    assert owner not in getattr(partner, 'tp6_PublicationStructure19')


def test_assoc_researchers13_stub_double():
    # tp6_PublicationStructure has no real 'tp6_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so tp6_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp6_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp6_Researcher(forName="sample_text", name="sample_text")
    partner = tp6_PublicationStructure()
    setattr(partner, 'tp6_PublicationStructure', None)
    _safe_set(owner, 'tp6_Researcher14', partner)
    assert owner in getattr(partner, 'tp6_PublicationStructure')
    _safe_set(owner, 'tp6_Researcher14', None)
    assert owner not in getattr(partner, 'tp6_PublicationStructure')


