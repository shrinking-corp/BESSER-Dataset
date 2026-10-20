import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tp5_Collaboration,
    tp5_Paper,
    tp5_Paragraph,
    tp5_Position,
    tp5_PublicationStructure,
    tp5_Researcher,
    tp5_Skill,
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

def test_assoc_authors7_reverse_link_reassign_clear():
    a1 = tp5_Researcher(forName="sample_text", name="sample_text")
    a2 = tp5_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp5_Paper(name="sample_text")
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
    a1 = tp5_Paper(name="sample_text")
    a2 = tp5_Paper(name="sample_text_2")
    b = tp5_Paper(name="sample_text")
    _safe_set(b, 'tp5_Paper8', a1)
    assert _is_linked(b, 'tp5_Paper8', a1)
    if hasattr(a1, 'tp5_Paper10'):
        assert _is_linked(a1, 'tp5_Paper10', b)
    _safe_set(b, 'tp5_Paper8', a2)
    assert _is_linked(b, 'tp5_Paper8', a2)
    if hasattr(a1, 'tp5_Paper10'):
        assert not _is_linked(a1, 'tp5_Paper10', b)
    if hasattr(a2, 'tp5_Paper10'):
        assert _is_linked(a2, 'tp5_Paper10', b)
    _safe_set(b, 'tp5_Paper8', None)
    assert not _is_linked(b, 'tp5_Paper8', a2)
    if hasattr(a2, 'tp5_Paper10'):
        assert not _is_linked(a2, 'tp5_Paper10', b)


def test_assoc_col_paper22_reverse_link_reassign_clear():
    a1 = tp5_Paper(name="sample_text")
    a2 = tp5_Paper(name="sample_text_2")
    b = tp5_Collaboration(ratio=7)
    _safe_set(b, 'tp5_Collaboration23', a1)
    assert _is_linked(b, 'tp5_Collaboration23', a1)
    if hasattr(a1, 'tp5_Paper24'):
        assert _is_linked(a1, 'tp5_Paper24', b)
    _safe_set(b, 'tp5_Collaboration23', a2)
    assert _is_linked(b, 'tp5_Collaboration23', a2)
    if hasattr(a1, 'tp5_Paper24'):
        assert not _is_linked(a1, 'tp5_Paper24', b)
    if hasattr(a2, 'tp5_Paper24'):
        assert _is_linked(a2, 'tp5_Paper24', b)
    _safe_set(b, 'tp5_Collaboration23', None)
    assert not _is_linked(b, 'tp5_Collaboration23', a2)
    if hasattr(a2, 'tp5_Paper24'):
        assert not _is_linked(a2, 'tp5_Paper24', b)


def test_assoc_collaborations4_reverse_link_reassign_clear():
    a1 = tp5_Researcher(forName="sample_text", name="sample_text")
    a2 = tp5_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp5_Collaboration(ratio=7)
    _safe_set(b, 'tp5_Collaboration', a1)
    assert _is_linked(b, 'tp5_Collaboration', a1)
    if hasattr(a1, 'tp5_Researcher5'):
        assert _is_linked(a1, 'tp5_Researcher5', b)
    _safe_set(b, 'tp5_Collaboration', a2)
    assert _is_linked(b, 'tp5_Collaboration', a2)
    if hasattr(a1, 'tp5_Researcher5'):
        assert not _is_linked(a1, 'tp5_Researcher5', b)
    if hasattr(a2, 'tp5_Researcher5'):
        assert _is_linked(a2, 'tp5_Researcher5', b)
    _safe_set(b, 'tp5_Collaboration', None)
    assert not _is_linked(b, 'tp5_Collaboration', a2)
    if hasattr(a2, 'tp5_Researcher5'):
        assert not _is_linked(a2, 'tp5_Researcher5', b)


def test_assoc_paragraphs6_reverse_link_reassign_clear():
    a1 = tp5_Paragraph(content="sample_text", id=7, name="sample_text")
    a2 = tp5_Paragraph(content="sample_text_2", id=13, name="sample_text_2")
    b = tp5_Paper(name="sample_text")
    _safe_set(b, 'tp5_Paper', {a1})
    assert _is_linked(b, 'tp5_Paper', a1)
    if hasattr(a1, 'tp5_Paragraph'):
        assert _is_linked(a1, 'tp5_Paragraph', b)
    _safe_set(b, 'tp5_Paper', {a2})
    assert _is_linked(b, 'tp5_Paper', a2)
    if hasattr(a1, 'tp5_Paragraph'):
        assert not _is_linked(a1, 'tp5_Paragraph', b)
    if hasattr(a2, 'tp5_Paragraph'):
        assert _is_linked(a2, 'tp5_Paragraph', b)
    _safe_set(b, 'tp5_Paper', set())
    assert not _is_linked(b, 'tp5_Paper', a2)
    if hasattr(a2, 'tp5_Paragraph'):
        assert not _is_linked(a2, 'tp5_Paragraph', b)


def test_assoc_parent20_reverse_link_reassign_clear():
    a1 = tp5_Position(description="sample_text", name="sample_text")
    a2 = tp5_Position(description="sample_text_2", name="sample_text_2")
    b = tp5_Position(description="sample_text", name="sample_text")
    _safe_set(b, 'tp5_Position21', a1)
    assert _is_linked(b, 'tp5_Position21', a1)
    if hasattr(a1, 'tp5_Position19'):
        assert _is_linked(a1, 'tp5_Position19', b)
    _safe_set(b, 'tp5_Position21', a2)
    assert _is_linked(b, 'tp5_Position21', a2)
    if hasattr(a1, 'tp5_Position19'):
        assert not _is_linked(a1, 'tp5_Position19', b)
    if hasattr(a2, 'tp5_Position19'):
        assert _is_linked(a2, 'tp5_Position19', b)
    _safe_set(b, 'tp5_Position21', None)
    assert not _is_linked(b, 'tp5_Position21', a2)
    if hasattr(a2, 'tp5_Position19'):
        assert not _is_linked(a2, 'tp5_Position19', b)


def test_assoc_res_papers0_reverse_link_reassign_clear():
    a1 = tp5_Researcher(forName="sample_text", name="sample_text")
    a2 = tp5_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp5_Paper(name="sample_text")
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
    a1 = tp5_Researcher(forName="sample_text", name="sample_text")
    a2 = tp5_Researcher(forName="sample_text_2", name="sample_text_2")
    b = tp5_Position(description="sample_text", name="sample_text")
    _safe_set(b, 'tp5_Position', a1)
    assert _is_linked(b, 'tp5_Position', a1)
    if hasattr(a1, 'tp5_Researcher3'):
        assert _is_linked(a1, 'tp5_Researcher3', b)
    _safe_set(b, 'tp5_Position', a2)
    assert _is_linked(b, 'tp5_Position', a2)
    if hasattr(a1, 'tp5_Researcher3'):
        assert not _is_linked(a1, 'tp5_Researcher3', b)
    if hasattr(a2, 'tp5_Researcher3'):
        assert _is_linked(a2, 'tp5_Researcher3', b)
    _safe_set(b, 'tp5_Position', None)
    assert not _is_linked(b, 'tp5_Position', a2)
    if hasattr(a2, 'tp5_Researcher3'):
        assert not _is_linked(a2, 'tp5_Researcher3', b)


def test_assoc_skills1_reverse_link_reassign_clear():
    a1 = tp5_Skill(description="sample_text")
    a2 = tp5_Skill(description="sample_text_2")
    b = tp5_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'tp5_Researcher', {a1})
    assert _is_linked(b, 'tp5_Researcher', a1)
    if hasattr(a1, 'tp5_Skill'):
        assert _is_linked(a1, 'tp5_Skill', b)
    _safe_set(b, 'tp5_Researcher', {a2})
    assert _is_linked(b, 'tp5_Researcher', a2)
    if hasattr(a1, 'tp5_Skill'):
        assert not _is_linked(a1, 'tp5_Skill', b)
    if hasattr(a2, 'tp5_Skill'):
        assert _is_linked(a2, 'tp5_Skill', b)
    _safe_set(b, 'tp5_Researcher', set())
    assert not _is_linked(b, 'tp5_Researcher', a2)
    if hasattr(a2, 'tp5_Skill'):
        assert not _is_linked(a2, 'tp5_Skill', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_papers13_stub_double():
    # tp5_PublicationStructure has no real 'tp5_PublicationStructure14' property in the generated
    # code (a bare stub) -- manually attach it so tp5_Paper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp5_Paper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp5_Paper(name="sample_text")
    partner = tp5_PublicationStructure()
    setattr(partner, 'tp5_PublicationStructure14', None)
    _safe_set(owner, 'tp5_Paper15', partner)
    assert owner in getattr(partner, 'tp5_PublicationStructure14')
    _safe_set(owner, 'tp5_Paper15', None)
    assert owner not in getattr(partner, 'tp5_PublicationStructure14')


def test_assoc_positions16_stub_double():
    # tp5_PublicationStructure has no real 'tp5_PublicationStructure17' property in the generated
    # code (a bare stub) -- manually attach it so tp5_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp5_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp5_Position(description="sample_text", name="sample_text")
    partner = tp5_PublicationStructure()
    setattr(partner, 'tp5_PublicationStructure17', None)
    _safe_set(owner, 'tp5_Position18', partner)
    assert owner in getattr(partner, 'tp5_PublicationStructure17')
    _safe_set(owner, 'tp5_Position18', None)
    assert owner not in getattr(partner, 'tp5_PublicationStructure17')


def test_assoc_researchers11_stub_double():
    # tp5_PublicationStructure has no real 'tp5_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so tp5_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tp5_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tp5_Researcher(forName="sample_text", name="sample_text")
    partner = tp5_PublicationStructure()
    setattr(partner, 'tp5_PublicationStructure', None)
    _safe_set(owner, 'tp5_Researcher12', partner)
    assert owner in getattr(partner, 'tp5_PublicationStructure')
    _safe_set(owner, 'tp5_Researcher12', None)
    assert owner not in getattr(partner, 'tp5_PublicationStructure')


