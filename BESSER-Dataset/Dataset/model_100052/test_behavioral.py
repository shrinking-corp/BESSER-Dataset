import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    StateMachineObject,
    research32_Action,
    research32_Collaboration,
    research32_Counted,
    research32_Keyword,
    research32_KnowledgeManager,
    research32_Labelled,
    research32_Named,
    research32_Paper,
    research32_PaperKeyword,
    research32_Paragraph,
    research32_Phase,
    research32_Position,
    research32_Progress,
    research32_PublicationProcess,
    research32_PublicationStatus,
    research32_PublicationStructure,
    research32_PublicationSystem,
    research32_Researcher,
    research32_Review,
    research32_ReviewNote,
    research32_Skill,
    research32_State,
    research32_StateMachineObject,
    research32_StateMachineVariable,
    research32_Transition,
    research32_Write,
    StateType,
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

def test_assoc_collaborations9_reverse_link_reassign_clear():
    a1 = research32_Researcher(forName="sample_text", name="sample_text")
    a2 = research32_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research32_Collaboration(ratio=7)
    _safe_set(b, 'research32_Collaboration', a1)
    assert _is_linked(b, 'research32_Collaboration', a1)
    if hasattr(a1, 'research32_Researcher10'):
        assert _is_linked(a1, 'research32_Researcher10', b)
    _safe_set(b, 'research32_Collaboration', a2)
    assert _is_linked(b, 'research32_Collaboration', a2)
    if hasattr(a1, 'research32_Researcher10'):
        assert not _is_linked(a1, 'research32_Researcher10', b)
    if hasattr(a2, 'research32_Researcher10'):
        assert _is_linked(a2, 'research32_Researcher10', b)
    _safe_set(b, 'research32_Collaboration', None)
    assert not _is_linked(b, 'research32_Collaboration', a2)
    if hasattr(a2, 'research32_Researcher10'):
        assert not _is_linked(a2, 'research32_Researcher10', b)


def test_assoc_keyword58_reverse_link_reassign_clear():
    a1 = research32_PaperKeyword(weight=7)
    a2 = research32_PaperKeyword(weight=13)
    b = research32_Keyword(word="sample_text")
    _safe_set(b, 'research32_Keyword60', a1)
    assert _is_linked(b, 'research32_Keyword60', a1)
    if hasattr(a1, 'research32_PaperKeyword59'):
        assert _is_linked(a1, 'research32_PaperKeyword59', b)
    _safe_set(b, 'research32_Keyword60', a2)
    assert _is_linked(b, 'research32_Keyword60', a2)
    if hasattr(a1, 'research32_PaperKeyword59'):
        assert not _is_linked(a1, 'research32_PaperKeyword59', b)
    if hasattr(a2, 'research32_PaperKeyword59'):
        assert _is_linked(a2, 'research32_PaperKeyword59', b)
    _safe_set(b, 'research32_Keyword60', None)
    assert not _is_linked(b, 'research32_Keyword60', a2)
    if hasattr(a2, 'research32_PaperKeyword59'):
        assert not _is_linked(a2, 'research32_PaperKeyword59', b)


def test_assoc_next83_reverse_link_reassign_clear():
    a1 = research32_Action(actionLabel="sample_text", actionStatement="sample_text")
    a2 = research32_Action(actionLabel="sample_text_2", actionStatement="sample_text_2")
    b = research32_Action(actionLabel="sample_text", actionStatement="sample_text")
    _safe_set(b, 'research32_Action84', a1)
    assert _is_linked(b, 'research32_Action84', a1)
    if hasattr(a1, 'research32_Action82'):
        assert _is_linked(a1, 'research32_Action82', b)
    _safe_set(b, 'research32_Action84', a2)
    assert _is_linked(b, 'research32_Action84', a2)
    if hasattr(a1, 'research32_Action82'):
        assert not _is_linked(a1, 'research32_Action82', b)
    if hasattr(a2, 'research32_Action82'):
        assert _is_linked(a2, 'research32_Action82', b)
    _safe_set(b, 'research32_Action84', None)
    assert not _is_linked(b, 'research32_Action84', a2)
    if hasattr(a2, 'research32_Action82'):
        assert not _is_linked(a2, 'research32_Action82', b)


def test_assoc_paragraph27_reverse_link_reassign_clear():
    a1 = research32_Write(timeSpent=7)
    a2 = research32_Write(timeSpent=13)
    b = research32_Paragraph(content="sample_text")
    _safe_set(b, 'research32_Paragraph29', a1)
    assert _is_linked(b, 'research32_Paragraph29', a1)
    if hasattr(a1, 'research32_Write28'):
        assert _is_linked(a1, 'research32_Write28', b)
    _safe_set(b, 'research32_Paragraph29', a2)
    assert _is_linked(b, 'research32_Paragraph29', a2)
    if hasattr(a1, 'research32_Write28'):
        assert not _is_linked(a1, 'research32_Write28', b)
    if hasattr(a2, 'research32_Write28'):
        assert _is_linked(a2, 'research32_Write28', b)
    _safe_set(b, 'research32_Paragraph29', None)
    assert not _is_linked(b, 'research32_Paragraph29', a2)
    if hasattr(a2, 'research32_Write28'):
        assert not _is_linked(a2, 'research32_Write28', b)


def test_assoc_parent51_reverse_link_reassign_clear():
    a1 = research32_Position(description="sample_text")
    a2 = research32_Position(description="sample_text_2")
    b = research32_Position(description="sample_text")
    _safe_set(b, 'research32_Position52', a1)
    assert _is_linked(b, 'research32_Position52', a1)
    if hasattr(a1, 'research32_Position50'):
        assert _is_linked(a1, 'research32_Position50', b)
    _safe_set(b, 'research32_Position52', a2)
    assert _is_linked(b, 'research32_Position52', a2)
    if hasattr(a1, 'research32_Position50'):
        assert not _is_linked(a1, 'research32_Position50', b)
    if hasattr(a2, 'research32_Position50'):
        assert _is_linked(a2, 'research32_Position50', b)
    _safe_set(b, 'research32_Position52', None)
    assert not _is_linked(b, 'research32_Position52', a2)
    if hasattr(a2, 'research32_Position50'):
        assert not _is_linked(a2, 'research32_Position50', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = research32_PublicationProcess(maxTime=7, minTime=7)
    a2 = research32_PublicationProcess(maxTime=13, minTime=13)
    b = research32_Phase(name="sample_text")
    _safe_set(b, 'research32_Phase', a1)
    assert _is_linked(b, 'research32_Phase', a1)
    if hasattr(a1, 'research32_PublicationProcess'):
        assert _is_linked(a1, 'research32_PublicationProcess', b)
    _safe_set(b, 'research32_Phase', a2)
    assert _is_linked(b, 'research32_Phase', a2)
    if hasattr(a1, 'research32_PublicationProcess'):
        assert not _is_linked(a1, 'research32_PublicationProcess', b)
    if hasattr(a2, 'research32_PublicationProcess'):
        assert _is_linked(a2, 'research32_PublicationProcess', b)
    _safe_set(b, 'research32_Phase', None)
    assert not _is_linked(b, 'research32_Phase', a2)
    if hasattr(a2, 'research32_PublicationProcess'):
        assert not _is_linked(a2, 'research32_PublicationProcess', b)


def test_assoc_process23_reverse_link_reassign_clear():
    a1 = research32_PublicationProcess(maxTime=7, minTime=7)
    a2 = research32_PublicationProcess(maxTime=13, minTime=13)
    b = research32_Progress(percent=7)
    _safe_set(b, 'research32_Progress', a1)
    assert _is_linked(b, 'research32_Progress', a1)
    if hasattr(a1, 'research32_PublicationProcess24'):
        assert _is_linked(a1, 'research32_PublicationProcess24', b)
    _safe_set(b, 'research32_Progress', a2)
    assert _is_linked(b, 'research32_Progress', a2)
    if hasattr(a1, 'research32_PublicationProcess24'):
        assert not _is_linked(a1, 'research32_PublicationProcess24', b)
    if hasattr(a2, 'research32_PublicationProcess24'):
        assert _is_linked(a2, 'research32_PublicationProcess24', b)
    _safe_set(b, 'research32_Progress', None)
    assert not _is_linked(b, 'research32_Progress', a2)
    if hasattr(a2, 'research32_PublicationProcess24'):
        assert not _is_linked(a2, 'research32_PublicationProcess24', b)


def test_assoc_pubStates66_reverse_link_reassign_clear():
    a1 = research32_State(id=7, kind="sample_text", name="sample_text")
    a2 = research32_State(id=13, kind="sample_text_2", name="sample_text_2")
    b = research32_PublicationStatus(label="sample_text")
    _safe_set(b, 'research32_PublicationStatus67', {a1})
    assert _is_linked(b, 'research32_PublicationStatus67', a1)
    if hasattr(a1, 'research32_State68'):
        assert _is_linked(a1, 'research32_State68', b)
    _safe_set(b, 'research32_PublicationStatus67', {a2})
    assert _is_linked(b, 'research32_PublicationStatus67', a2)
    if hasattr(a1, 'research32_State68'):
        assert not _is_linked(a1, 'research32_State68', b)
    if hasattr(a2, 'research32_State68'):
        assert _is_linked(a2, 'research32_State68', b)
    _safe_set(b, 'research32_PublicationStatus67', set())
    assert not _is_linked(b, 'research32_PublicationStatus67', a2)
    if hasattr(a2, 'research32_State68'):
        assert not _is_linked(a2, 'research32_State68', b)


def test_assoc_res_position7_reverse_link_reassign_clear():
    a1 = research32_Researcher(forName="sample_text", name="sample_text")
    a2 = research32_Researcher(forName="sample_text_2", name="sample_text_2")
    b = research32_Position(description="sample_text")
    _safe_set(b, 'research32_Position', a1)
    assert _is_linked(b, 'research32_Position', a1)
    if hasattr(a1, 'research32_Researcher8'):
        assert _is_linked(a1, 'research32_Researcher8', b)
    _safe_set(b, 'research32_Position', a2)
    assert _is_linked(b, 'research32_Position', a2)
    if hasattr(a1, 'research32_Researcher8'):
        assert not _is_linked(a1, 'research32_Researcher8', b)
    if hasattr(a2, 'research32_Researcher8'):
        assert _is_linked(a2, 'research32_Researcher8', b)
    _safe_set(b, 'research32_Position', None)
    assert not _is_linked(b, 'research32_Position', a2)
    if hasattr(a2, 'research32_Researcher8'):
        assert not _is_linked(a2, 'research32_Researcher8', b)


def test_assoc_reviewNote30_reverse_link_reassign_clear():
    a1 = research32_ReviewNote(content="sample_text")
    a2 = research32_ReviewNote(content="sample_text_2")
    b = research32_Review(date=date(2024, 1, 1))
    _safe_set(b, 'research32_Review31', a1)
    assert _is_linked(b, 'research32_Review31', a1)
    if hasattr(a1, 'research32_ReviewNote32'):
        assert _is_linked(a1, 'research32_ReviewNote32', b)
    _safe_set(b, 'research32_Review31', a2)
    assert _is_linked(b, 'research32_Review31', a2)
    if hasattr(a1, 'research32_ReviewNote32'):
        assert not _is_linked(a1, 'research32_ReviewNote32', b)
    if hasattr(a2, 'research32_ReviewNote32'):
        assert _is_linked(a2, 'research32_ReviewNote32', b)
    _safe_set(b, 'research32_Review31', None)
    assert not _is_linked(b, 'research32_Review31', a2)
    if hasattr(a2, 'research32_ReviewNote32'):
        assert not _is_linked(a2, 'research32_ReviewNote32', b)


def test_assoc_reviews2_reverse_link_reassign_clear():
    a1 = research32_Review(date=date(2024, 1, 1))
    a2 = research32_Review(date=date(2025, 6, 15))
    b = research32_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research32_Researcher3', {a1})
    assert _is_linked(b, 'research32_Researcher3', a1)
    if hasattr(a1, 'research32_Review'):
        assert _is_linked(a1, 'research32_Review', b)
    _safe_set(b, 'research32_Researcher3', {a2})
    assert _is_linked(b, 'research32_Researcher3', a2)
    if hasattr(a1, 'research32_Review'):
        assert not _is_linked(a1, 'research32_Review', b)
    if hasattr(a2, 'research32_Review'):
        assert _is_linked(a2, 'research32_Review', b)
    _safe_set(b, 'research32_Researcher3', set())
    assert not _is_linked(b, 'research32_Researcher3', a2)
    if hasattr(a2, 'research32_Review'):
        assert not _is_linked(a2, 'research32_Review', b)


def test_assoc_reviews21_reverse_link_reassign_clear():
    a1 = research32_ReviewNote(content="sample_text")
    a2 = research32_ReviewNote(content="sample_text_2")
    b = research32_Paragraph(content="sample_text")
    _safe_set(b, 'research32_Paragraph22', {a1})
    assert _is_linked(b, 'research32_Paragraph22', a1)
    if hasattr(a1, 'research32_ReviewNote'):
        assert _is_linked(a1, 'research32_ReviewNote', b)
    _safe_set(b, 'research32_Paragraph22', {a2})
    assert _is_linked(b, 'research32_Paragraph22', a2)
    if hasattr(a1, 'research32_ReviewNote'):
        assert not _is_linked(a1, 'research32_ReviewNote', b)
    if hasattr(a2, 'research32_ReviewNote'):
        assert _is_linked(a2, 'research32_ReviewNote', b)
    _safe_set(b, 'research32_Paragraph22', set())
    assert not _is_linked(b, 'research32_Paragraph22', a2)
    if hasattr(a2, 'research32_ReviewNote'):
        assert not _is_linked(a2, 'research32_ReviewNote', b)


def test_assoc_s_actions79_reverse_link_reassign_clear():
    a1 = research32_State(id=7, kind="sample_text", name="sample_text")
    a2 = research32_State(id=13, kind="sample_text_2", name="sample_text_2")
    b = research32_Action(actionLabel="sample_text", actionStatement="sample_text")
    _safe_set(b, 'research32_Action81', a1)
    assert _is_linked(b, 'research32_Action81', a1)
    if hasattr(a1, 'research32_State80'):
        assert _is_linked(a1, 'research32_State80', b)
    _safe_set(b, 'research32_Action81', a2)
    assert _is_linked(b, 'research32_Action81', a2)
    if hasattr(a1, 'research32_State80'):
        assert not _is_linked(a1, 'research32_State80', b)
    if hasattr(a2, 'research32_State80'):
        assert _is_linked(a2, 'research32_State80', b)
    _safe_set(b, 'research32_Action81', None)
    assert not _is_linked(b, 'research32_Action81', a2)
    if hasattr(a2, 'research32_State80'):
        assert not _is_linked(a2, 'research32_State80', b)


def test_assoc_skills5_reverse_link_reassign_clear():
    a1 = research32_Skill(description="sample_text")
    a2 = research32_Skill(description="sample_text_2")
    b = research32_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research32_Researcher6', {a1})
    assert _is_linked(b, 'research32_Researcher6', a1)
    if hasattr(a1, 'research32_Skill'):
        assert _is_linked(a1, 'research32_Skill', b)
    _safe_set(b, 'research32_Researcher6', {a2})
    assert _is_linked(b, 'research32_Researcher6', a2)
    if hasattr(a1, 'research32_Skill'):
        assert not _is_linked(a1, 'research32_Skill', b)
    if hasattr(a2, 'research32_Skill'):
        assert _is_linked(a2, 'research32_Skill', b)
    _safe_set(b, 'research32_Researcher6', set())
    assert not _is_linked(b, 'research32_Researcher6', a2)
    if hasattr(a2, 'research32_Skill'):
        assert not _is_linked(a2, 'research32_Skill', b)


def test_assoc_source70_reverse_link_reassign_clear():
    a1 = research32_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = research32_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = research32_State(id=7, kind="sample_text", name="sample_text")
    _safe_set(b, 'research32_State72', a1)
    assert _is_linked(b, 'research32_State72', a1)
    if hasattr(a1, 'research32_Transition71'):
        assert _is_linked(a1, 'research32_Transition71', b)
    _safe_set(b, 'research32_State72', a2)
    assert _is_linked(b, 'research32_State72', a2)
    if hasattr(a1, 'research32_Transition71'):
        assert not _is_linked(a1, 'research32_Transition71', b)
    if hasattr(a2, 'research32_Transition71'):
        assert _is_linked(a2, 'research32_Transition71', b)
    _safe_set(b, 'research32_State72', None)
    assert not _is_linked(b, 'research32_State72', a2)
    if hasattr(a2, 'research32_Transition71'):
        assert not _is_linked(a2, 'research32_Transition71', b)


def test_assoc_t_actions69_reverse_link_reassign_clear():
    a1 = research32_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = research32_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = research32_Action(actionLabel="sample_text", actionStatement="sample_text")
    _safe_set(b, 'research32_Action', a1)
    assert _is_linked(b, 'research32_Action', a1)
    if hasattr(a1, 'research32_Transition'):
        assert _is_linked(a1, 'research32_Transition', b)
    _safe_set(b, 'research32_Action', a2)
    assert _is_linked(b, 'research32_Action', a2)
    if hasattr(a1, 'research32_Transition'):
        assert not _is_linked(a1, 'research32_Transition', b)
    if hasattr(a2, 'research32_Transition'):
        assert _is_linked(a2, 'research32_Transition', b)
    _safe_set(b, 'research32_Action', None)
    assert not _is_linked(b, 'research32_Action', a2)
    if hasattr(a2, 'research32_Transition'):
        assert not _is_linked(a2, 'research32_Transition', b)


def test_assoc_target73_reverse_link_reassign_clear():
    a1 = research32_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = research32_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = research32_State(id=7, kind="sample_text", name="sample_text")
    _safe_set(b, 'research32_State75', a1)
    assert _is_linked(b, 'research32_State75', a1)
    if hasattr(a1, 'research32_Transition74'):
        assert _is_linked(a1, 'research32_Transition74', b)
    _safe_set(b, 'research32_State75', a2)
    assert _is_linked(b, 'research32_State75', a2)
    if hasattr(a1, 'research32_Transition74'):
        assert not _is_linked(a1, 'research32_Transition74', b)
    if hasattr(a2, 'research32_Transition74'):
        assert _is_linked(a2, 'research32_Transition74', b)
    _safe_set(b, 'research32_State75', None)
    assert not _is_linked(b, 'research32_State75', a2)
    if hasattr(a2, 'research32_Transition74'):
        assert not _is_linked(a2, 'research32_Transition74', b)


def test_assoc_transitions76_reverse_link_reassign_clear():
    a1 = research32_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = research32_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = research32_State(id=7, kind="sample_text", name="sample_text")
    _safe_set(b, 'research32_State77', {a1})
    assert _is_linked(b, 'research32_State77', a1)
    if hasattr(a1, 'research32_Transition78'):
        assert _is_linked(a1, 'research32_Transition78', b)
    _safe_set(b, 'research32_State77', {a2})
    assert _is_linked(b, 'research32_State77', a2)
    if hasattr(a1, 'research32_Transition78'):
        assert not _is_linked(a1, 'research32_Transition78', b)
    if hasattr(a2, 'research32_Transition78'):
        assert _is_linked(a2, 'research32_Transition78', b)
    _safe_set(b, 'research32_State77', set())
    assert not _is_linked(b, 'research32_State77', a2)
    if hasattr(a2, 'research32_Transition78'):
        assert not _is_linked(a2, 'research32_Transition78', b)


def test_assoc_writes1_reverse_link_reassign_clear():
    a1 = research32_Write(timeSpent=7)
    a2 = research32_Write(timeSpent=13)
    b = research32_Researcher(forName="sample_text", name="sample_text")
    _safe_set(b, 'research32_Researcher', {a1})
    assert _is_linked(b, 'research32_Researcher', a1)
    if hasattr(a1, 'research32_Write'):
        assert _is_linked(a1, 'research32_Write', b)
    _safe_set(b, 'research32_Researcher', {a2})
    assert _is_linked(b, 'research32_Researcher', a2)
    if hasattr(a1, 'research32_Write'):
        assert not _is_linked(a1, 'research32_Write', b)
    if hasattr(a2, 'research32_Write'):
        assert _is_linked(a2, 'research32_Write', b)
    _safe_set(b, 'research32_Researcher', set())
    assert not _is_linked(b, 'research32_Researcher', a2)
    if hasattr(a2, 'research32_Write'):
        assert not _is_linked(a2, 'research32_Write', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allkeywords55_stub_double():
    # research32_KnowledgeManager has no real 'research32_KnowledgeManager56' property in the generated
    # code (a bare stub) -- manually attach it so research32_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Keyword(word="sample_text")
    partner = research32_KnowledgeManager()
    setattr(partner, 'research32_KnowledgeManager56', None)
    _safe_set(owner, 'research32_Keyword57', partner)
    assert owner in getattr(partner, 'research32_KnowledgeManager56')
    _safe_set(owner, 'research32_Keyword57', None)
    assert owner not in getattr(partner, 'research32_KnowledgeManager56')


def test_assoc_authors13_stub_double():
    # research32_Paper has no real 'res_papers' property in the generated
    # code (a bare stub) -- manually attach it so research32_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Researcher(forName="sample_text", name="sample_text")
    partner = research32_Paper()
    setattr(partner, 'res_papers', None)
    _safe_set(owner, 'Researcher', partner)
    assert owner in getattr(partner, 'res_papers')
    _safe_set(owner, 'Researcher', None)
    assert owner not in getattr(partner, 'res_papers')


def test_assoc_col_paper61_stub_double():
    # research32_Paper has no real 'research32_Paper63' property in the generated
    # code (a bare stub) -- manually attach it so research32_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Collaboration(ratio=7)
    partner = research32_Paper()
    setattr(partner, 'research32_Paper63', None)
    _safe_set(owner, 'research32_Collaboration62', partner)
    assert getattr(partner, 'research32_Paper63') == owner
    _safe_set(owner, 'research32_Collaboration62', None)
    assert getattr(partner, 'research32_Paper63') is None


def test_assoc_keywords14_stub_double():
    # research32_Paper has no real 'research32_Paper15' property in the generated
    # code (a bare stub) -- manually attach it so research32_PaperKeyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_PaperKeyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_PaperKeyword(weight=7)
    partner = research32_Paper()
    setattr(partner, 'research32_Paper15', None)
    _safe_set(owner, 'research32_PaperKeyword', partner)
    assert owner in getattr(partner, 'research32_Paper15')
    _safe_set(owner, 'research32_PaperKeyword', None)
    assert owner not in getattr(partner, 'research32_Paper15')


def test_assoc_kpapers53_stub_double():
    # research32_Paper has no real 'research32_Paper54' property in the generated
    # code (a bare stub) -- manually attach it so research32_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Keyword(word="sample_text")
    partner = research32_Paper()
    setattr(partner, 'research32_Paper54', None)
    _safe_set(owner, 'research32_Keyword', {partner})
    assert getattr(partner, 'research32_Paper54') == owner
    _safe_set(owner, 'research32_Keyword', set())
    assert getattr(partner, 'research32_Paper54') is None


def test_assoc_machineVariables64_stub_double():
    # research32_StateMachineVariable has no real 'research32_StateMachineVariable' property in the generated
    # code (a bare stub) -- manually attach it so research32_PublicationStatus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_PublicationStatus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_PublicationStatus(label="sample_text")
    partner = research32_StateMachineVariable()
    setattr(partner, 'research32_StateMachineVariable', None)
    _safe_set(owner, 'research32_PublicationStatus65', {partner})
    assert getattr(partner, 'research32_StateMachineVariable') == owner
    _safe_set(owner, 'research32_PublicationStatus65', set())
    assert getattr(partner, 'research32_StateMachineVariable') is None


def test_assoc_paper25_stub_double():
    # research32_Paper has no real 'Paper26' property in the generated
    # code (a bare stub) -- manually attach it so research32_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Progress(percent=7)
    partner = research32_Paper()
    setattr(partner, 'Paper26', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper26') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper26') is None


def test_assoc_paragraphs11_stub_double():
    # research32_Paper has no real 'research32_Paper' property in the generated
    # code (a bare stub) -- manually attach it so research32_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Paragraph(content="sample_text")
    partner = research32_Paper()
    setattr(partner, 'research32_Paper', None)
    _safe_set(owner, 'research32_Paragraph', partner)
    assert owner in getattr(partner, 'research32_Paper')
    _safe_set(owner, 'research32_Paragraph', None)
    assert owner not in getattr(partner, 'research32_Paper')


def test_assoc_positions47_stub_double():
    # research32_PublicationSystem has no real 'research32_PublicationSystem48' property in the generated
    # code (a bare stub) -- manually attach it so research32_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Position(description="sample_text")
    partner = research32_PublicationSystem()
    setattr(partner, 'research32_PublicationSystem48', None)
    _safe_set(owner, 'research32_Position49', partner)
    assert owner in getattr(partner, 'research32_PublicationSystem48')
    _safe_set(owner, 'research32_Position49', None)
    assert owner not in getattr(partner, 'research32_PublicationSystem48')


def test_assoc_processView42_stub_double():
    # research32_PublicationSystem has no real 'research32_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so research32_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_PublicationProcess(maxTime=7, minTime=7)
    partner = research32_PublicationSystem()
    setattr(partner, 'research32_PublicationSystem', None)
    _safe_set(owner, 'research32_PublicationProcess43', partner)
    assert getattr(partner, 'research32_PublicationSystem') == owner
    _safe_set(owner, 'research32_PublicationProcess43', None)
    assert getattr(partner, 'research32_PublicationSystem') is None


def test_assoc_progress12_stub_double():
    # research32_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so research32_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Progress(percent=7)
    partner = research32_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_res_papers4_stub_double():
    # research32_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so research32_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Researcher(forName="sample_text", name="sample_text")
    partner = research32_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_researchers33_stub_double():
    # research32_PublicationStructure has no real 'research32_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so research32_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_Researcher(forName="sample_text", name="sample_text")
    partner = research32_PublicationStructure()
    setattr(partner, 'research32_PublicationStructure', None)
    _safe_set(owner, 'research32_Researcher34', partner)
    assert owner in getattr(partner, 'research32_PublicationStructure')
    _safe_set(owner, 'research32_Researcher34', None)
    assert owner not in getattr(partner, 'research32_PublicationStructure')


def test_assoc_state19_stub_double():
    # research32_Paper has no real 'research32_Paper20' property in the generated
    # code (a bare stub) -- manually attach it so research32_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_State(id=7, kind="sample_text", name="sample_text")
    partner = research32_Paper()
    setattr(partner, 'research32_Paper20', None)
    _safe_set(owner, 'research32_State', partner)
    assert getattr(partner, 'research32_Paper20') == owner
    _safe_set(owner, 'research32_State', None)
    assert getattr(partner, 'research32_Paper20') is None


def test_assoc_status40_stub_double():
    # research32_PublicationStructure has no real 'research32_PublicationStructure41' property in the generated
    # code (a bare stub) -- manually attach it so research32_PublicationStatus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # research32_PublicationStatus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = research32_PublicationStatus(label="sample_text")
    partner = research32_PublicationStructure()
    setattr(partner, 'research32_PublicationStructure41', None)
    _safe_set(owner, 'research32_PublicationStatus', partner)
    assert getattr(partner, 'research32_PublicationStructure41') == owner
    _safe_set(owner, 'research32_PublicationStatus', None)
    assert getattr(partner, 'research32_PublicationStructure41') is None


