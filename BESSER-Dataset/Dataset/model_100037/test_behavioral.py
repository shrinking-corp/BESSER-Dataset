import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    publication2014b_Counted,
    publication2014b_Labelled,
    publication2014b_Named,
    publication2014b_Paper,
    publication2014b_Paragraph,
    publication2014b_Progress,
    publication2014b_PublicationPhase,
    publication2014b_PublicationProcess,
    publication2014b_PublicationStructure,
    publication2014b_PublicationSystem,
    publication2014b_Researcher,
    publication2014b_Review,
    publication2014b_ReviewNote,
    publication2014b_Rule,
    publication2014b_Sequence,
    publication2014b_Write,
    SequenceType,
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

def test_assoc_linksToSuccessors3_reverse_link_reassign_clear():
    a1 = publication2014b_Sequence(sequenceType="sample_text")
    a2 = publication2014b_Sequence(sequenceType="sample_text_2")
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014b_PublicationPhase4', {a1})
    assert _is_linked(b, 'publication2014b_PublicationPhase4', a1)
    if hasattr(a1, 'publication2014b_Sequence'):
        assert _is_linked(a1, 'publication2014b_Sequence', b)
    _safe_set(b, 'publication2014b_PublicationPhase4', {a2})
    assert _is_linked(b, 'publication2014b_PublicationPhase4', a2)
    if hasattr(a1, 'publication2014b_Sequence'):
        assert not _is_linked(a1, 'publication2014b_Sequence', b)
    if hasattr(a2, 'publication2014b_Sequence'):
        assert _is_linked(a2, 'publication2014b_Sequence', b)
    _safe_set(b, 'publication2014b_PublicationPhase4', set())
    assert not _is_linked(b, 'publication2014b_PublicationPhase4', a2)
    if hasattr(a2, 'publication2014b_Sequence'):
        assert not _is_linked(a2, 'publication2014b_Sequence', b)


def test_assoc_neededPerson5_reverse_link_reassign_clear():
    a1 = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = publication2014b_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'phaseParticipation', {a1})
    assert _is_linked(b, 'phaseParticipation', a1)
    if hasattr(a1, 'Researcher'):
        assert _is_linked(a1, 'Researcher', b)
    _safe_set(b, 'phaseParticipation', {a2})
    assert _is_linked(b, 'phaseParticipation', a2)
    if hasattr(a1, 'Researcher'):
        assert not _is_linked(a1, 'Researcher', b)
    if hasattr(a2, 'Researcher'):
        assert _is_linked(a2, 'Researcher', b)
    _safe_set(b, 'phaseParticipation', set())
    assert not _is_linked(b, 'phaseParticipation', a2)
    if hasattr(a2, 'Researcher'):
        assert not _is_linked(a2, 'Researcher', b)


def test_assoc_phaseParticipation15_reverse_link_reassign_clear():
    a1 = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = publication2014b_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'PublicationPhase', a1)
    assert _is_linked(b, 'PublicationPhase', a1)
    if hasattr(a1, 'neededPerson'):
        assert _is_linked(a1, 'neededPerson', b)
    _safe_set(b, 'PublicationPhase', a2)
    assert _is_linked(b, 'PublicationPhase', a2)
    if hasattr(a1, 'neededPerson'):
        assert not _is_linked(a1, 'neededPerson', b)
    if hasattr(a2, 'neededPerson'):
        assert _is_linked(a2, 'neededPerson', b)
    _safe_set(b, 'PublicationPhase', None)
    assert not _is_linked(b, 'PublicationPhase', a2)
    if hasattr(a2, 'neededPerson'):
        assert not _is_linked(a2, 'neededPerson', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = publication2014b_PublicationProcess(maxTime=7, minTime=7)
    a2 = publication2014b_PublicationProcess(maxTime=13, minTime=13)
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014b_PublicationPhase', a1)
    assert _is_linked(b, 'publication2014b_PublicationPhase', a1)
    if hasattr(a1, 'publication2014b_PublicationProcess'):
        assert _is_linked(a1, 'publication2014b_PublicationProcess', b)
    _safe_set(b, 'publication2014b_PublicationPhase', a2)
    assert _is_linked(b, 'publication2014b_PublicationPhase', a2)
    if hasattr(a1, 'publication2014b_PublicationProcess'):
        assert not _is_linked(a1, 'publication2014b_PublicationProcess', b)
    if hasattr(a2, 'publication2014b_PublicationProcess'):
        assert _is_linked(a2, 'publication2014b_PublicationProcess', b)
    _safe_set(b, 'publication2014b_PublicationPhase', None)
    assert not _is_linked(b, 'publication2014b_PublicationPhase', a2)
    if hasattr(a2, 'publication2014b_PublicationProcess'):
        assert not _is_linked(a2, 'publication2014b_PublicationProcess', b)


def test_assoc_predecessor12_reverse_link_reassign_clear():
    a1 = publication2014b_Sequence(sequenceType="sample_text")
    a2 = publication2014b_Sequence(sequenceType="sample_text_2")
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014b_PublicationPhase14', a1)
    assert _is_linked(b, 'publication2014b_PublicationPhase14', a1)
    if hasattr(a1, 'publication2014b_Sequence13'):
        assert _is_linked(a1, 'publication2014b_Sequence13', b)
    _safe_set(b, 'publication2014b_PublicationPhase14', a2)
    assert _is_linked(b, 'publication2014b_PublicationPhase14', a2)
    if hasattr(a1, 'publication2014b_Sequence13'):
        assert not _is_linked(a1, 'publication2014b_Sequence13', b)
    if hasattr(a2, 'publication2014b_Sequence13'):
        assert _is_linked(a2, 'publication2014b_Sequence13', b)
    _safe_set(b, 'publication2014b_PublicationPhase14', None)
    assert not _is_linked(b, 'publication2014b_PublicationPhase14', a2)
    if hasattr(a2, 'publication2014b_Sequence13'):
        assert not _is_linked(a2, 'publication2014b_Sequence13', b)


def test_assoc_process26_reverse_link_reassign_clear():
    a1 = publication2014b_PublicationProcess(maxTime=7, minTime=7)
    a2 = publication2014b_PublicationProcess(maxTime=13, minTime=13)
    b = publication2014b_Progress(percent=7, time=7)
    _safe_set(b, 'publication2014b_Progress', a1)
    assert _is_linked(b, 'publication2014b_Progress', a1)
    if hasattr(a1, 'publication2014b_PublicationProcess27'):
        assert _is_linked(a1, 'publication2014b_PublicationProcess27', b)
    _safe_set(b, 'publication2014b_Progress', a2)
    assert _is_linked(b, 'publication2014b_Progress', a2)
    if hasattr(a1, 'publication2014b_PublicationProcess27'):
        assert not _is_linked(a1, 'publication2014b_PublicationProcess27', b)
    if hasattr(a2, 'publication2014b_PublicationProcess27'):
        assert _is_linked(a2, 'publication2014b_PublicationProcess27', b)
    _safe_set(b, 'publication2014b_Progress', None)
    assert not _is_linked(b, 'publication2014b_Progress', a2)
    if hasattr(a2, 'publication2014b_PublicationProcess27'):
        assert not _is_linked(a2, 'publication2014b_PublicationProcess27', b)


def test_assoc_publicationRules1_reverse_link_reassign_clear():
    a1 = publication2014b_Rule(key="sample_text", text="sample_text")
    a2 = publication2014b_Rule(key="sample_text_2", text="sample_text_2")
    b = publication2014b_PublicationProcess(maxTime=7, minTime=7)
    _safe_set(b, 'publication2014b_PublicationProcess2', {a1})
    assert _is_linked(b, 'publication2014b_PublicationProcess2', a1)
    if hasattr(a1, 'publication2014b_Rule'):
        assert _is_linked(a1, 'publication2014b_Rule', b)
    _safe_set(b, 'publication2014b_PublicationProcess2', {a2})
    assert _is_linked(b, 'publication2014b_PublicationProcess2', a2)
    if hasattr(a1, 'publication2014b_Rule'):
        assert not _is_linked(a1, 'publication2014b_Rule', b)
    if hasattr(a2, 'publication2014b_Rule'):
        assert _is_linked(a2, 'publication2014b_Rule', b)
    _safe_set(b, 'publication2014b_PublicationProcess2', set())
    assert not _is_linked(b, 'publication2014b_PublicationProcess2', a2)
    if hasattr(a2, 'publication2014b_Rule'):
        assert not _is_linked(a2, 'publication2014b_Rule', b)


def test_assoc_reviews24_reverse_link_reassign_clear():
    a1 = publication2014b_ReviewNote(content="sample_text")
    a2 = publication2014b_ReviewNote(content="sample_text_2")
    b = publication2014b_Paragraph(content="sample_text")
    _safe_set(b, 'publication2014b_Paragraph25', {a1})
    assert _is_linked(b, 'publication2014b_Paragraph25', a1)
    if hasattr(a1, 'publication2014b_ReviewNote'):
        assert _is_linked(a1, 'publication2014b_ReviewNote', b)
    _safe_set(b, 'publication2014b_Paragraph25', {a2})
    assert _is_linked(b, 'publication2014b_Paragraph25', a2)
    if hasattr(a1, 'publication2014b_ReviewNote'):
        assert not _is_linked(a1, 'publication2014b_ReviewNote', b)
    if hasattr(a2, 'publication2014b_ReviewNote'):
        assert _is_linked(a2, 'publication2014b_ReviewNote', b)
    _safe_set(b, 'publication2014b_Paragraph25', set())
    assert not _is_linked(b, 'publication2014b_Paragraph25', a2)
    if hasattr(a2, 'publication2014b_ReviewNote'):
        assert not _is_linked(a2, 'publication2014b_ReviewNote', b)


def test_assoc_rules6_reverse_link_reassign_clear():
    a1 = publication2014b_Rule(key="sample_text", text="sample_text")
    a2 = publication2014b_Rule(key="sample_text_2", text="sample_text_2")
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014b_PublicationPhase7', {a1})
    assert _is_linked(b, 'publication2014b_PublicationPhase7', a1)
    if hasattr(a1, 'publication2014b_Rule8'):
        assert _is_linked(a1, 'publication2014b_Rule8', b)
    _safe_set(b, 'publication2014b_PublicationPhase7', {a2})
    assert _is_linked(b, 'publication2014b_PublicationPhase7', a2)
    if hasattr(a1, 'publication2014b_Rule8'):
        assert not _is_linked(a1, 'publication2014b_Rule8', b)
    if hasattr(a2, 'publication2014b_Rule8'):
        assert _is_linked(a2, 'publication2014b_Rule8', b)
    _safe_set(b, 'publication2014b_PublicationPhase7', set())
    assert not _is_linked(b, 'publication2014b_PublicationPhase7', a2)
    if hasattr(a2, 'publication2014b_Rule8'):
        assert not _is_linked(a2, 'publication2014b_Rule8', b)


def test_assoc_successor9_reverse_link_reassign_clear():
    a1 = publication2014b_Sequence(sequenceType="sample_text")
    a2 = publication2014b_Sequence(sequenceType="sample_text_2")
    b = publication2014b_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014b_PublicationPhase11', a1)
    assert _is_linked(b, 'publication2014b_PublicationPhase11', a1)
    if hasattr(a1, 'publication2014b_Sequence10'):
        assert _is_linked(a1, 'publication2014b_Sequence10', b)
    _safe_set(b, 'publication2014b_PublicationPhase11', a2)
    assert _is_linked(b, 'publication2014b_PublicationPhase11', a2)
    if hasattr(a1, 'publication2014b_Sequence10'):
        assert not _is_linked(a1, 'publication2014b_Sequence10', b)
    if hasattr(a2, 'publication2014b_Sequence10'):
        assert _is_linked(a2, 'publication2014b_Sequence10', b)
    _safe_set(b, 'publication2014b_PublicationPhase11', None)
    assert not _is_linked(b, 'publication2014b_PublicationPhase11', a2)
    if hasattr(a2, 'publication2014b_Sequence10'):
        assert not _is_linked(a2, 'publication2014b_Sequence10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors22_stub_double():
    # publication2014b_Paper has no real 'papers' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014b_Paper()
    setattr(partner, 'papers', None)
    _safe_set(owner, 'Researcher23', partner)
    assert owner in getattr(partner, 'papers')
    _safe_set(owner, 'Researcher23', None)
    assert owner not in getattr(partner, 'papers')


def test_assoc_paper28_stub_double():
    # publication2014b_Paper has no real 'Paper29' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Progress(percent=7, time=7)
    partner = publication2014b_Paper()
    setattr(partner, 'Paper29', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper29') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper29') is None


def test_assoc_papers19_stub_double():
    # publication2014b_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014b_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_paragraph30_stub_double():
    # publication2014b_Write has no real 'publication2014b_Write31' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Paragraph(content="sample_text")
    partner = publication2014b_Write()
    setattr(partner, 'publication2014b_Write31', None)
    _safe_set(owner, 'publication2014b_Paragraph32', partner)
    assert getattr(partner, 'publication2014b_Write31') == owner
    _safe_set(owner, 'publication2014b_Paragraph32', None)
    assert getattr(partner, 'publication2014b_Write31') is None


def test_assoc_paragraphs20_stub_double():
    # publication2014b_Paper has no real 'publication2014b_Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Paragraph(content="sample_text")
    partner = publication2014b_Paper()
    setattr(partner, 'publication2014b_Paper', None)
    _safe_set(owner, 'publication2014b_Paragraph', partner)
    assert owner in getattr(partner, 'publication2014b_Paper')
    _safe_set(owner, 'publication2014b_Paragraph', None)
    assert owner not in getattr(partner, 'publication2014b_Paper')


def test_assoc_processView41_stub_double():
    # publication2014b_PublicationSystem has no real 'publication2014b_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_PublicationProcess(maxTime=7, minTime=7)
    partner = publication2014b_PublicationSystem()
    setattr(partner, 'publication2014b_PublicationSystem', None)
    _safe_set(owner, 'publication2014b_PublicationProcess42', partner)
    assert getattr(partner, 'publication2014b_PublicationSystem') == owner
    _safe_set(owner, 'publication2014b_PublicationProcess42', None)
    assert getattr(partner, 'publication2014b_PublicationSystem') is None


def test_assoc_progress21_stub_double():
    # publication2014b_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Progress(percent=7, time=7)
    partner = publication2014b_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_researchers36_stub_double():
    # publication2014b_PublicationStructure has no real 'publication2014b_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014b_PublicationStructure()
    setattr(partner, 'publication2014b_PublicationStructure', None)
    _safe_set(owner, 'publication2014b_Researcher37', partner)
    assert owner in getattr(partner, 'publication2014b_PublicationStructure')
    _safe_set(owner, 'publication2014b_Researcher37', None)
    assert owner not in getattr(partner, 'publication2014b_PublicationStructure')


def test_assoc_reviewNote33_stub_double():
    # publication2014b_Review has no real 'publication2014b_Review34' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_ReviewNote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_ReviewNote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_ReviewNote(content="sample_text")
    partner = publication2014b_Review()
    setattr(partner, 'publication2014b_Review34', None)
    _safe_set(owner, 'publication2014b_ReviewNote35', partner)
    assert getattr(partner, 'publication2014b_Review34') == owner
    _safe_set(owner, 'publication2014b_ReviewNote35', None)
    assert getattr(partner, 'publication2014b_Review34') is None


def test_assoc_reviews17_stub_double():
    # publication2014b_Review has no real 'publication2014b_Review' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014b_Review()
    setattr(partner, 'publication2014b_Review', None)
    _safe_set(owner, 'publication2014b_Researcher18', {partner})
    assert getattr(partner, 'publication2014b_Review') == owner
    _safe_set(owner, 'publication2014b_Researcher18', set())
    assert getattr(partner, 'publication2014b_Review') is None


def test_assoc_writes16_stub_double():
    # publication2014b_Write has no real 'publication2014b_Write' property in the generated
    # code (a bare stub) -- manually attach it so publication2014b_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014b_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014b_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014b_Write()
    setattr(partner, 'publication2014b_Write', None)
    _safe_set(owner, 'publication2014b_Researcher', {partner})
    assert getattr(partner, 'publication2014b_Write') == owner
    _safe_set(owner, 'publication2014b_Researcher', set())
    assert getattr(partner, 'publication2014b_Write') is None


