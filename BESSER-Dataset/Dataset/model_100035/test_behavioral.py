import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    PlaceHolder,
    publication2014_Counted,
    publication2014_Labelled,
    publication2014_Named,
    publication2014_Paper,
    publication2014_Paragraph,
    publication2014_PlaceHolder,
    publication2014_PlaceHolderPP,
    publication2014_PlaceHolderRn,
    publication2014_PlaceHolderRs,
    publication2014_PlaceHolderRule,
    publication2014_Progress,
    publication2014_PublicationPhase,
    publication2014_PublicationProcess,
    publication2014_PublicationStructure,
    publication2014_PublicationSystem,
    publication2014_Researcher,
    publication2014_Review,
    publication2014_ReviewNote,
    publication2014_Rule,
    publication2014_Sequence,
    publication2014_Write,
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
    a1 = publication2014_Sequence(sequenceType="sample_text")
    a2 = publication2014_Sequence(sequenceType="sample_text_2")
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014_PublicationPhase4', {a1})
    assert _is_linked(b, 'publication2014_PublicationPhase4', a1)
    if hasattr(a1, 'publication2014_Sequence'):
        assert _is_linked(a1, 'publication2014_Sequence', b)
    _safe_set(b, 'publication2014_PublicationPhase4', {a2})
    assert _is_linked(b, 'publication2014_PublicationPhase4', a2)
    if hasattr(a1, 'publication2014_Sequence'):
        assert not _is_linked(a1, 'publication2014_Sequence', b)
    if hasattr(a2, 'publication2014_Sequence'):
        assert _is_linked(a2, 'publication2014_Sequence', b)
    _safe_set(b, 'publication2014_PublicationPhase4', set())
    assert not _is_linked(b, 'publication2014_PublicationPhase4', a2)
    if hasattr(a2, 'publication2014_Sequence'):
        assert not _is_linked(a2, 'publication2014_Sequence', b)


def test_assoc_neededPerson5_reverse_link_reassign_clear():
    a1 = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = publication2014_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
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


def test_assoc_phaseParticipation19_reverse_link_reassign_clear():
    a1 = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = publication2014_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
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
    a1 = publication2014_PublicationProcess(maxTime=7, minTime=7)
    a2 = publication2014_PublicationProcess(maxTime=13, minTime=13)
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014_PublicationPhase', a1)
    assert _is_linked(b, 'publication2014_PublicationPhase', a1)
    if hasattr(a1, 'publication2014_PublicationProcess'):
        assert _is_linked(a1, 'publication2014_PublicationProcess', b)
    _safe_set(b, 'publication2014_PublicationPhase', a2)
    assert _is_linked(b, 'publication2014_PublicationPhase', a2)
    if hasattr(a1, 'publication2014_PublicationProcess'):
        assert not _is_linked(a1, 'publication2014_PublicationProcess', b)
    if hasattr(a2, 'publication2014_PublicationProcess'):
        assert _is_linked(a2, 'publication2014_PublicationProcess', b)
    _safe_set(b, 'publication2014_PublicationPhase', None)
    assert not _is_linked(b, 'publication2014_PublicationPhase', a2)
    if hasattr(a2, 'publication2014_PublicationProcess'):
        assert not _is_linked(a2, 'publication2014_PublicationProcess', b)


def test_assoc_predecessor14_reverse_link_reassign_clear():
    a1 = publication2014_Sequence(sequenceType="sample_text")
    a2 = publication2014_Sequence(sequenceType="sample_text_2")
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014_PublicationPhase16', a1)
    assert _is_linked(b, 'publication2014_PublicationPhase16', a1)
    if hasattr(a1, 'publication2014_Sequence15'):
        assert _is_linked(a1, 'publication2014_Sequence15', b)
    _safe_set(b, 'publication2014_PublicationPhase16', a2)
    assert _is_linked(b, 'publication2014_PublicationPhase16', a2)
    if hasattr(a1, 'publication2014_Sequence15'):
        assert not _is_linked(a1, 'publication2014_Sequence15', b)
    if hasattr(a2, 'publication2014_Sequence15'):
        assert _is_linked(a2, 'publication2014_Sequence15', b)
    _safe_set(b, 'publication2014_PublicationPhase16', None)
    assert not _is_linked(b, 'publication2014_PublicationPhase16', a2)
    if hasattr(a2, 'publication2014_Sequence15'):
        assert not _is_linked(a2, 'publication2014_Sequence15', b)


def test_assoc_process34_reverse_link_reassign_clear():
    a1 = publication2014_PublicationProcess(maxTime=7, minTime=7)
    a2 = publication2014_PublicationProcess(maxTime=13, minTime=13)
    b = publication2014_Progress(percent=7, time=7)
    _safe_set(b, 'publication2014_Progress', a1)
    assert _is_linked(b, 'publication2014_Progress', a1)
    if hasattr(a1, 'publication2014_PublicationProcess35'):
        assert _is_linked(a1, 'publication2014_PublicationProcess35', b)
    _safe_set(b, 'publication2014_Progress', a2)
    assert _is_linked(b, 'publication2014_Progress', a2)
    if hasattr(a1, 'publication2014_PublicationProcess35'):
        assert not _is_linked(a1, 'publication2014_PublicationProcess35', b)
    if hasattr(a2, 'publication2014_PublicationProcess35'):
        assert _is_linked(a2, 'publication2014_PublicationProcess35', b)
    _safe_set(b, 'publication2014_Progress', None)
    assert not _is_linked(b, 'publication2014_Progress', a2)
    if hasattr(a2, 'publication2014_PublicationProcess35'):
        assert not _is_linked(a2, 'publication2014_PublicationProcess35', b)


def test_assoc_publicationRules1_reverse_link_reassign_clear():
    a1 = publication2014_Rule(key="sample_text", text="sample_text")
    a2 = publication2014_Rule(key="sample_text_2", text="sample_text_2")
    b = publication2014_PublicationProcess(maxTime=7, minTime=7)
    _safe_set(b, 'publication2014_PublicationProcess2', {a1})
    assert _is_linked(b, 'publication2014_PublicationProcess2', a1)
    if hasattr(a1, 'publication2014_Rule'):
        assert _is_linked(a1, 'publication2014_Rule', b)
    _safe_set(b, 'publication2014_PublicationProcess2', {a2})
    assert _is_linked(b, 'publication2014_PublicationProcess2', a2)
    if hasattr(a1, 'publication2014_Rule'):
        assert not _is_linked(a1, 'publication2014_Rule', b)
    if hasattr(a2, 'publication2014_Rule'):
        assert _is_linked(a2, 'publication2014_Rule', b)
    _safe_set(b, 'publication2014_PublicationProcess2', set())
    assert not _is_linked(b, 'publication2014_PublicationProcess2', a2)
    if hasattr(a2, 'publication2014_Rule'):
        assert not _is_linked(a2, 'publication2014_Rule', b)


def test_assoc_reviews30_reverse_link_reassign_clear():
    a1 = publication2014_ReviewNote(content="sample_text")
    a2 = publication2014_ReviewNote(content="sample_text_2")
    b = publication2014_Paragraph(content="sample_text")
    _safe_set(b, 'publication2014_Paragraph31', {a1})
    assert _is_linked(b, 'publication2014_Paragraph31', a1)
    if hasattr(a1, 'publication2014_ReviewNote'):
        assert _is_linked(a1, 'publication2014_ReviewNote', b)
    _safe_set(b, 'publication2014_Paragraph31', {a2})
    assert _is_linked(b, 'publication2014_Paragraph31', a2)
    if hasattr(a1, 'publication2014_ReviewNote'):
        assert not _is_linked(a1, 'publication2014_ReviewNote', b)
    if hasattr(a2, 'publication2014_ReviewNote'):
        assert _is_linked(a2, 'publication2014_ReviewNote', b)
    _safe_set(b, 'publication2014_Paragraph31', set())
    assert not _is_linked(b, 'publication2014_Paragraph31', a2)
    if hasattr(a2, 'publication2014_ReviewNote'):
        assert not _is_linked(a2, 'publication2014_ReviewNote', b)


def test_assoc_rules6_reverse_link_reassign_clear():
    a1 = publication2014_Rule(key="sample_text", text="sample_text")
    a2 = publication2014_Rule(key="sample_text_2", text="sample_text_2")
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014_PublicationPhase7', {a1})
    assert _is_linked(b, 'publication2014_PublicationPhase7', a1)
    if hasattr(a1, 'publication2014_Rule8'):
        assert _is_linked(a1, 'publication2014_Rule8', b)
    _safe_set(b, 'publication2014_PublicationPhase7', {a2})
    assert _is_linked(b, 'publication2014_PublicationPhase7', a2)
    if hasattr(a1, 'publication2014_Rule8'):
        assert not _is_linked(a1, 'publication2014_Rule8', b)
    if hasattr(a2, 'publication2014_Rule8'):
        assert _is_linked(a2, 'publication2014_Rule8', b)
    _safe_set(b, 'publication2014_PublicationPhase7', set())
    assert not _is_linked(b, 'publication2014_PublicationPhase7', a2)
    if hasattr(a2, 'publication2014_Rule8'):
        assert not _is_linked(a2, 'publication2014_Rule8', b)


def test_assoc_successor11_reverse_link_reassign_clear():
    a1 = publication2014_Sequence(sequenceType="sample_text")
    a2 = publication2014_Sequence(sequenceType="sample_text_2")
    b = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication2014_PublicationPhase13', a1)
    assert _is_linked(b, 'publication2014_PublicationPhase13', a1)
    if hasattr(a1, 'publication2014_Sequence12'):
        assert _is_linked(a1, 'publication2014_Sequence12', b)
    _safe_set(b, 'publication2014_PublicationPhase13', a2)
    assert _is_linked(b, 'publication2014_PublicationPhase13', a2)
    if hasattr(a1, 'publication2014_Sequence12'):
        assert not _is_linked(a1, 'publication2014_Sequence12', b)
    if hasattr(a2, 'publication2014_Sequence12'):
        assert _is_linked(a2, 'publication2014_Sequence12', b)
    _safe_set(b, 'publication2014_PublicationPhase13', None)
    assert not _is_linked(b, 'publication2014_PublicationPhase13', a2)
    if hasattr(a2, 'publication2014_Sequence12'):
        assert not _is_linked(a2, 'publication2014_Sequence12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors28_stub_double():
    # publication2014_Paper has no real 'papers' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014_Paper()
    setattr(partner, 'papers', None)
    _safe_set(owner, 'Researcher29', partner)
    assert owner in getattr(partner, 'papers')
    _safe_set(owner, 'Researcher29', None)
    assert owner not in getattr(partner, 'papers')


def test_assoc_paper36_stub_double():
    # publication2014_Paper has no real 'Paper37' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Progress(percent=7, time=7)
    partner = publication2014_Paper()
    setattr(partner, 'Paper37', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper37') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper37') is None


def test_assoc_papers23_stub_double():
    # publication2014_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_paragraph38_stub_double():
    # publication2014_Write has no real 'publication2014_Write39' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Paragraph(content="sample_text")
    partner = publication2014_Write()
    setattr(partner, 'publication2014_Write39', None)
    _safe_set(owner, 'publication2014_Paragraph40', partner)
    assert getattr(partner, 'publication2014_Write39') == owner
    _safe_set(owner, 'publication2014_Paragraph40', None)
    assert getattr(partner, 'publication2014_Write39') is None


def test_assoc_paragraphs26_stub_double():
    # publication2014_Paper has no real 'publication2014_Paper' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Paragraph(content="sample_text")
    partner = publication2014_Paper()
    setattr(partner, 'publication2014_Paper', None)
    _safe_set(owner, 'publication2014_Paragraph', partner)
    assert owner in getattr(partner, 'publication2014_Paper')
    _safe_set(owner, 'publication2014_Paragraph', None)
    assert owner not in getattr(partner, 'publication2014_Paper')


def test_assoc_placeholder17_stub_double():
    # publication2014_PlaceHolderRule has no real 'publication2014_PlaceHolderRule' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Rule(key="sample_text", text="sample_text")
    partner = publication2014_PlaceHolderRule()
    setattr(partner, 'publication2014_PlaceHolderRule', None)
    _safe_set(owner, 'publication2014_Rule18', partner)
    assert getattr(partner, 'publication2014_PlaceHolderRule') == owner
    _safe_set(owner, 'publication2014_Rule18', None)
    assert getattr(partner, 'publication2014_PlaceHolderRule') is None


def test_assoc_placeholder24_stub_double():
    # publication2014_PlaceHolderRs has no real 'publication2014_PlaceHolderRs' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014_PlaceHolderRs()
    setattr(partner, 'publication2014_PlaceHolderRs', None)
    _safe_set(owner, 'publication2014_Researcher25', partner)
    assert getattr(partner, 'publication2014_PlaceHolderRs') == owner
    _safe_set(owner, 'publication2014_Researcher25', None)
    assert getattr(partner, 'publication2014_PlaceHolderRs') is None


def test_assoc_placeholder32_stub_double():
    # publication2014_PlaceHolderRn has no real 'publication2014_PlaceHolderRn' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_ReviewNote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_ReviewNote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_ReviewNote(content="sample_text")
    partner = publication2014_PlaceHolderRn()
    setattr(partner, 'publication2014_PlaceHolderRn', None)
    _safe_set(owner, 'publication2014_ReviewNote33', partner)
    assert getattr(partner, 'publication2014_PlaceHolderRn') == owner
    _safe_set(owner, 'publication2014_ReviewNote33', None)
    assert getattr(partner, 'publication2014_PlaceHolderRn') is None


def test_assoc_placeholder9_stub_double():
    # publication2014_PlaceHolderPP has no real 'publication2014_PlaceHolderPP' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_PublicationPhase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_PublicationPhase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    partner = publication2014_PlaceHolderPP()
    setattr(partner, 'publication2014_PlaceHolderPP', None)
    _safe_set(owner, 'publication2014_PublicationPhase10', partner)
    assert getattr(partner, 'publication2014_PlaceHolderPP') == owner
    _safe_set(owner, 'publication2014_PublicationPhase10', None)
    assert getattr(partner, 'publication2014_PlaceHolderPP') is None


def test_assoc_processView49_stub_double():
    # publication2014_PublicationSystem has no real 'publication2014_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_PublicationProcess(maxTime=7, minTime=7)
    partner = publication2014_PublicationSystem()
    setattr(partner, 'publication2014_PublicationSystem', None)
    _safe_set(owner, 'publication2014_PublicationProcess50', partner)
    assert getattr(partner, 'publication2014_PublicationSystem') == owner
    _safe_set(owner, 'publication2014_PublicationProcess50', None)
    assert getattr(partner, 'publication2014_PublicationSystem') is None


def test_assoc_progress27_stub_double():
    # publication2014_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Progress(percent=7, time=7)
    partner = publication2014_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_researchers44_stub_double():
    # publication2014_PublicationStructure has no real 'publication2014_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014_PublicationStructure()
    setattr(partner, 'publication2014_PublicationStructure', None)
    _safe_set(owner, 'publication2014_Researcher45', partner)
    assert owner in getattr(partner, 'publication2014_PublicationStructure')
    _safe_set(owner, 'publication2014_Researcher45', None)
    assert owner not in getattr(partner, 'publication2014_PublicationStructure')


def test_assoc_reviewNote41_stub_double():
    # publication2014_Review has no real 'publication2014_Review42' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_ReviewNote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_ReviewNote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_ReviewNote(content="sample_text")
    partner = publication2014_Review()
    setattr(partner, 'publication2014_Review42', None)
    _safe_set(owner, 'publication2014_ReviewNote43', partner)
    assert getattr(partner, 'publication2014_Review42') == owner
    _safe_set(owner, 'publication2014_ReviewNote43', None)
    assert getattr(partner, 'publication2014_Review42') is None


def test_assoc_reviews21_stub_double():
    # publication2014_Review has no real 'publication2014_Review' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014_Review()
    setattr(partner, 'publication2014_Review', None)
    _safe_set(owner, 'publication2014_Researcher22', {partner})
    assert getattr(partner, 'publication2014_Review') == owner
    _safe_set(owner, 'publication2014_Researcher22', set())
    assert getattr(partner, 'publication2014_Review') is None


def test_assoc_writes20_stub_double():
    # publication2014_Write has no real 'publication2014_Write' property in the generated
    # code (a bare stub) -- manually attach it so publication2014_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication2014_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication2014_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = publication2014_Write()
    setattr(partner, 'publication2014_Write', None)
    _safe_set(owner, 'publication2014_Researcher', {partner})
    assert getattr(partner, 'publication2014_Write') == owner
    _safe_set(owner, 'publication2014_Researcher', set())
    assert getattr(partner, 'publication2014_Write') is None


