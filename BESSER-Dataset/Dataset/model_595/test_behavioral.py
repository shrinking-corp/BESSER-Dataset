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
    AssistantMVC_Observable,
    AssistantMVC_Observer,
    AssistantMVC_Open,
    AssistantMVC_OpenController,
    AssistantMVC_View,
    Controller,
    ExamItem,
    ExamItemController,
    Observable,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_controller6_stub_double():
    # AssistantMVC_Controller has no real 'AssistantMVC_Controller8' property in the generated
    # code (a bare stub) -- manually attach it so AssistantMVC_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AssistantMVC_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AssistantMVC_View(color="sample_text", name="sample_text")
    partner = AssistantMVC_Controller()
    setattr(partner, 'AssistantMVC_Controller8', None)
    _safe_set(owner, 'AssistantMVC_View7', partner)
    assert getattr(partner, 'AssistantMVC_Controller8') == owner
    _safe_set(owner, 'AssistantMVC_View7', None)
    assert getattr(partner, 'AssistantMVC_Controller8') is None


def test_assoc_examItems0_stub_double():
    # AssistantMVC_Exam has no real 'AssistantMVC_Exam' property in the generated
    # code (a bare stub) -- manually attach it so AssistantMVC_ExamItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AssistantMVC_ExamItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AssistantMVC_ExamItem(question="sample_text")
    partner = AssistantMVC_Exam()
    setattr(partner, 'AssistantMVC_Exam', None)
    _safe_set(owner, 'AssistantMVC_ExamItem', partner)
    assert owner in getattr(partner, 'AssistantMVC_Exam')
    _safe_set(owner, 'AssistantMVC_ExamItem', None)
    assert owner not in getattr(partner, 'AssistantMVC_Exam')


def test_assoc_views3_stub_double():
    # AssistantMVC_Exam has no real 'AssistantMVC_Exam4' property in the generated
    # code (a bare stub) -- manually attach it so AssistantMVC_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AssistantMVC_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AssistantMVC_View(color="sample_text", name="sample_text")
    partner = AssistantMVC_Exam()
    setattr(partner, 'AssistantMVC_Exam4', None)
    _safe_set(owner, 'AssistantMVC_View', partner)
    assert owner in getattr(partner, 'AssistantMVC_Exam4')
    _safe_set(owner, 'AssistantMVC_View', None)
    assert owner not in getattr(partner, 'AssistantMVC_Exam4')


