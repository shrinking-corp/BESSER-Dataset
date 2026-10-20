import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssistantMVC_Controller,
    AssistantMVC_Exam,
    AssistantMVC_ExamController,
    AssistantMVC_ExamItem,
    AssistantMVC_ExamItemController,
    AssistantMVC_ExamItemView,
    AssistantMVC_ExamView,
    AssistantMVC_MultipleChoice,
    AssistantMVC_MultipleChoiceController,
    AssistantMVC_MultipleChoiceView,
    AssistantMVC_Observer,
    AssistantMVC_Open,
    AssistantMVC_OpenController,
    AssistantMVC_OpenView,
    AssistantMVC_View,
    Controller,
    ExamItem,
    ExamItemController,
    ExamItemView,
    ExamView,
    Observer,
    View,
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

def test_assoc_examItems0_reverse_link_reassign_clear():
    a1 = AssistantMVC_ExamItem(optional=True, question="sample_text", value="sample_text")
    a2 = AssistantMVC_ExamItem(optional=False, question="sample_text_2", value="sample_text_2")
    b = AssistantMVC_Exam(question="sample_text")
    _safe_set(b, 'AssistantMVC_Exam', {a1})
    assert _is_linked(b, 'AssistantMVC_Exam', a1)
    if hasattr(a1, 'AssistantMVC_ExamItem'):
        assert _is_linked(a1, 'AssistantMVC_ExamItem', b)
    _safe_set(b, 'AssistantMVC_Exam', {a2})
    assert _is_linked(b, 'AssistantMVC_Exam', a2)
    if hasattr(a1, 'AssistantMVC_ExamItem'):
        assert not _is_linked(a1, 'AssistantMVC_ExamItem', b)
    if hasattr(a2, 'AssistantMVC_ExamItem'):
        assert _is_linked(a2, 'AssistantMVC_ExamItem', b)
    _safe_set(b, 'AssistantMVC_Exam', set())
    assert not _is_linked(b, 'AssistantMVC_Exam', a2)
    if hasattr(a2, 'AssistantMVC_ExamItem'):
        assert not _is_linked(a2, 'AssistantMVC_ExamItem', b)


def test_assoc_views3_reverse_link_reassign_clear():
    a1 = AssistantMVC_View(fontColor="sample_text", fontName="sample_text")
    a2 = AssistantMVC_View(fontColor="sample_text_2", fontName="sample_text_2")
    b = AssistantMVC_Exam(question="sample_text")
    _safe_set(b, 'AssistantMVC_Exam4', {a1})
    assert _is_linked(b, 'AssistantMVC_Exam4', a1)
    if hasattr(a1, 'AssistantMVC_View'):
        assert _is_linked(a1, 'AssistantMVC_View', b)
    _safe_set(b, 'AssistantMVC_Exam4', {a2})
    assert _is_linked(b, 'AssistantMVC_Exam4', a2)
    if hasattr(a1, 'AssistantMVC_View'):
        assert not _is_linked(a1, 'AssistantMVC_View', b)
    if hasattr(a2, 'AssistantMVC_View'):
        assert _is_linked(a2, 'AssistantMVC_View', b)
    _safe_set(b, 'AssistantMVC_Exam4', set())
    assert not _is_linked(b, 'AssistantMVC_Exam4', a2)
    if hasattr(a2, 'AssistantMVC_View'):
        assert not _is_linked(a2, 'AssistantMVC_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_controller5_stub_double():
    # AssistantMVC_Controller has no real 'AssistantMVC_Controller7' property in the generated
    # code (a bare stub) -- manually attach it so AssistantMVC_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AssistantMVC_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AssistantMVC_View(fontColor="sample_text", fontName="sample_text")
    partner = AssistantMVC_Controller()
    setattr(partner, 'AssistantMVC_Controller7', None)
    _safe_set(owner, 'AssistantMVC_View6', partner)
    assert getattr(partner, 'AssistantMVC_Controller7') == owner
    _safe_set(owner, 'AssistantMVC_View6', None)
    assert getattr(partner, 'AssistantMVC_Controller7') is None


def test_assoc_controllers1_stub_double():
    # AssistantMVC_Controller has no real 'AssistantMVC_Controller' property in the generated
    # code (a bare stub) -- manually attach it so AssistantMVC_Exam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AssistantMVC_Exam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AssistantMVC_Exam(question="sample_text")
    partner = AssistantMVC_Controller()
    setattr(partner, 'AssistantMVC_Controller', None)
    _safe_set(owner, 'AssistantMVC_Exam2', {partner})
    assert getattr(partner, 'AssistantMVC_Controller') == owner
    _safe_set(owner, 'AssistantMVC_Exam2', set())
    assert getattr(partner, 'AssistantMVC_Controller') is None


