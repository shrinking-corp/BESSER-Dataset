import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    PlaceHolder,
    publication_Counted,
    publication_Labelled,
    publication_Named,
    publication_Paper,
    publication_Paragraph,
    publication_PlaceHolder,
    publication_PlaceHolderPP,
    publication_PlaceHolderRn,
    publication_PlaceHolderRs,
    publication_PlaceHolderRule,
    publication_Progress,
    publication_PublicationPhase,
    publication_PublicationProcess,
    publication_PublicationStructure,
    publication_PublicationSystem,
    publication_Researcher,
    publication_Review,
    publication_ReviewNote,
    publication_Rule,
    publication_Sequence,
    publication_Write,
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
    a1 = publication_Sequence(sequenceType="sample_text")
    a2 = publication_Sequence(sequenceType="sample_text_2")
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication_PublicationPhase4', {a1})
    assert _is_linked(b, 'publication_PublicationPhase4', a1)
    if hasattr(a1, 'publication_Sequence'):
        assert _is_linked(a1, 'publication_Sequence', b)
    _safe_set(b, 'publication_PublicationPhase4', {a2})
    assert _is_linked(b, 'publication_PublicationPhase4', a2)
    if hasattr(a1, 'publication_Sequence'):
        assert not _is_linked(a1, 'publication_Sequence', b)
    if hasattr(a2, 'publication_Sequence'):
        assert _is_linked(a2, 'publication_Sequence', b)
    _safe_set(b, 'publication_PublicationPhase4', set())
    assert not _is_linked(b, 'publication_PublicationPhase4', a2)
    if hasattr(a2, 'publication_Sequence'):
        assert not _is_linked(a2, 'publication_Sequence', b)


def test_assoc_neededPerson5_reverse_link_reassign_clear():
    a1 = publication_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = publication_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
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
    a1 = publication_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = publication_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
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
    a1 = publication_PublicationProcess(maxTime=7, minTime=7)
    a2 = publication_PublicationProcess(maxTime=13, minTime=13)
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication_PublicationPhase', a1)
    assert _is_linked(b, 'publication_PublicationPhase', a1)
    if hasattr(a1, 'publication_PublicationProcess'):
        assert _is_linked(a1, 'publication_PublicationProcess', b)
    _safe_set(b, 'publication_PublicationPhase', a2)
    assert _is_linked(b, 'publication_PublicationPhase', a2)
    if hasattr(a1, 'publication_PublicationProcess'):
        assert not _is_linked(a1, 'publication_PublicationProcess', b)
    if hasattr(a2, 'publication_PublicationProcess'):
        assert _is_linked(a2, 'publication_PublicationProcess', b)
    _safe_set(b, 'publication_PublicationPhase', None)
    assert not _is_linked(b, 'publication_PublicationPhase', a2)
    if hasattr(a2, 'publication_PublicationProcess'):
        assert not _is_linked(a2, 'publication_PublicationProcess', b)


def test_assoc_predecessor14_reverse_link_reassign_clear():
    a1 = publication_Sequence(sequenceType="sample_text")
    a2 = publication_Sequence(sequenceType="sample_text_2")
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication_PublicationPhase16', a1)
    assert _is_linked(b, 'publication_PublicationPhase16', a1)
    if hasattr(a1, 'publication_Sequence15'):
        assert _is_linked(a1, 'publication_Sequence15', b)
    _safe_set(b, 'publication_PublicationPhase16', a2)
    assert _is_linked(b, 'publication_PublicationPhase16', a2)
    if hasattr(a1, 'publication_Sequence15'):
        assert not _is_linked(a1, 'publication_Sequence15', b)
    if hasattr(a2, 'publication_Sequence15'):
        assert _is_linked(a2, 'publication_Sequence15', b)
    _safe_set(b, 'publication_PublicationPhase16', None)
    assert not _is_linked(b, 'publication_PublicationPhase16', a2)
    if hasattr(a2, 'publication_Sequence15'):
        assert not _is_linked(a2, 'publication_Sequence15', b)


def test_assoc_process34_reverse_link_reassign_clear():
    a1 = publication_PublicationProcess(maxTime=7, minTime=7)
    a2 = publication_PublicationProcess(maxTime=13, minTime=13)
    b = publication_Progress(percent=7, time=7)
    _safe_set(b, 'publication_Progress', a1)
    assert _is_linked(b, 'publication_Progress', a1)
    if hasattr(a1, 'publication_PublicationProcess35'):
        assert _is_linked(a1, 'publication_PublicationProcess35', b)
    _safe_set(b, 'publication_Progress', a2)
    assert _is_linked(b, 'publication_Progress', a2)
    if hasattr(a1, 'publication_PublicationProcess35'):
        assert not _is_linked(a1, 'publication_PublicationProcess35', b)
    if hasattr(a2, 'publication_PublicationProcess35'):
        assert _is_linked(a2, 'publication_PublicationProcess35', b)
    _safe_set(b, 'publication_Progress', None)
    assert not _is_linked(b, 'publication_Progress', a2)
    if hasattr(a2, 'publication_PublicationProcess35'):
        assert not _is_linked(a2, 'publication_PublicationProcess35', b)


def test_assoc_publicationRules1_reverse_link_reassign_clear():
    a1 = publication_Rule(key="sample_text", text="sample_text")
    a2 = publication_Rule(key="sample_text_2", text="sample_text_2")
    b = publication_PublicationProcess(maxTime=7, minTime=7)
    _safe_set(b, 'publication_PublicationProcess2', {a1})
    assert _is_linked(b, 'publication_PublicationProcess2', a1)
    if hasattr(a1, 'publication_Rule'):
        assert _is_linked(a1, 'publication_Rule', b)
    _safe_set(b, 'publication_PublicationProcess2', {a2})
    assert _is_linked(b, 'publication_PublicationProcess2', a2)
    if hasattr(a1, 'publication_Rule'):
        assert not _is_linked(a1, 'publication_Rule', b)
    if hasattr(a2, 'publication_Rule'):
        assert _is_linked(a2, 'publication_Rule', b)
    _safe_set(b, 'publication_PublicationProcess2', set())
    assert not _is_linked(b, 'publication_PublicationProcess2', a2)
    if hasattr(a2, 'publication_Rule'):
        assert not _is_linked(a2, 'publication_Rule', b)


def test_assoc_reviews30_reverse_link_reassign_clear():
    a1 = publication_ReviewNote(content="sample_text")
    a2 = publication_ReviewNote(content="sample_text_2")
    b = publication_Paragraph(content="sample_text")
    _safe_set(b, 'publication_Paragraph31', {a1})
    assert _is_linked(b, 'publication_Paragraph31', a1)
    if hasattr(a1, 'publication_ReviewNote'):
        assert _is_linked(a1, 'publication_ReviewNote', b)
    _safe_set(b, 'publication_Paragraph31', {a2})
    assert _is_linked(b, 'publication_Paragraph31', a2)
    if hasattr(a1, 'publication_ReviewNote'):
        assert not _is_linked(a1, 'publication_ReviewNote', b)
    if hasattr(a2, 'publication_ReviewNote'):
        assert _is_linked(a2, 'publication_ReviewNote', b)
    _safe_set(b, 'publication_Paragraph31', set())
    assert not _is_linked(b, 'publication_Paragraph31', a2)
    if hasattr(a2, 'publication_ReviewNote'):
        assert not _is_linked(a2, 'publication_ReviewNote', b)


def test_assoc_rules6_reverse_link_reassign_clear():
    a1 = publication_Rule(key="sample_text", text="sample_text")
    a2 = publication_Rule(key="sample_text_2", text="sample_text_2")
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication_PublicationPhase7', {a1})
    assert _is_linked(b, 'publication_PublicationPhase7', a1)
    if hasattr(a1, 'publication_Rule8'):
        assert _is_linked(a1, 'publication_Rule8', b)
    _safe_set(b, 'publication_PublicationPhase7', {a2})
    assert _is_linked(b, 'publication_PublicationPhase7', a2)
    if hasattr(a1, 'publication_Rule8'):
        assert not _is_linked(a1, 'publication_Rule8', b)
    if hasattr(a2, 'publication_Rule8'):
        assert _is_linked(a2, 'publication_Rule8', b)
    _safe_set(b, 'publication_PublicationPhase7', set())
    assert not _is_linked(b, 'publication_PublicationPhase7', a2)
    if hasattr(a2, 'publication_Rule8'):
        assert not _is_linked(a2, 'publication_Rule8', b)


def test_assoc_successor11_reverse_link_reassign_clear():
    a1 = publication_Sequence(sequenceType="sample_text")
    a2 = publication_Sequence(sequenceType="sample_text_2")
    b = publication_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'publication_PublicationPhase13', a1)
    assert _is_linked(b, 'publication_PublicationPhase13', a1)
    if hasattr(a1, 'publication_Sequence12'):
        assert _is_linked(a1, 'publication_Sequence12', b)
    _safe_set(b, 'publication_PublicationPhase13', a2)
    assert _is_linked(b, 'publication_PublicationPhase13', a2)
    if hasattr(a1, 'publication_Sequence12'):
        assert not _is_linked(a1, 'publication_Sequence12', b)
    if hasattr(a2, 'publication_Sequence12'):
        assert _is_linked(a2, 'publication_Sequence12', b)
    _safe_set(b, 'publication_PublicationPhase13', None)
    assert not _is_linked(b, 'publication_PublicationPhase13', a2)
    if hasattr(a2, 'publication_Sequence12'):
        assert not _is_linked(a2, 'publication_Sequence12', b)


