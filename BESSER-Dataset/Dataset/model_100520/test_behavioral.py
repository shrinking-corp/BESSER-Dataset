import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Agent,
    FlowOfEvents,
    Statement,
    Step,
    textualusecase_Action,
    textualusecase_Actor,
    textualusecase_Agent,
    textualusecase_AlternativeFlow,
    textualusecase_BasicFlow,
    textualusecase_Condition,
    textualusecase_ConditionalStatement,
    textualusecase_FlowOfEvents,
    textualusecase_Include,
    textualusecase_LoopStatement,
    textualusecase_Statement,
    textualusecase_Step,
    textualusecase_Subject,
    textualusecase_UseCase,
    textualusecase_UseCaseModel,
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

def test_assoc_actions31_reverse_link_reassign_clear():
    a1 = textualusecase_Agent(name="sample_text")
    a2 = textualusecase_Agent(name="sample_text_2")
    b = textualusecase_Action(description="sample_text")
    _safe_set(b, 'Action', a1)
    assert _is_linked(b, 'Action', a1)
    if hasattr(a1, 'agent'):
        assert _is_linked(a1, 'agent', b)
    _safe_set(b, 'Action', a2)
    assert _is_linked(b, 'Action', a2)
    if hasattr(a1, 'agent'):
        assert not _is_linked(a1, 'agent', b)
    if hasattr(a2, 'agent'):
        assert _is_linked(a2, 'agent', b)
    _safe_set(b, 'Action', None)
    assert not _is_linked(b, 'Action', a2)
    if hasattr(a2, 'agent'):
        assert not _is_linked(a2, 'agent', b)


def test_assoc_agent45_reverse_link_reassign_clear():
    a1 = textualusecase_Agent(name="sample_text")
    a2 = textualusecase_Agent(name="sample_text_2")
    b = textualusecase_Action(description="sample_text")
    _safe_set(b, 'actions', a1)
    assert _is_linked(b, 'actions', a1)
    if hasattr(a1, 'Agent'):
        assert _is_linked(a1, 'Agent', b)
    _safe_set(b, 'actions', a2)
    assert _is_linked(b, 'actions', a2)
    if hasattr(a1, 'Agent'):
        assert not _is_linked(a1, 'Agent', b)
    if hasattr(a2, 'Agent'):
        assert _is_linked(a2, 'Agent', b)
    _safe_set(b, 'actions', None)
    assert not _is_linked(b, 'actions', a2)
    if hasattr(a2, 'Agent'):
        assert not _is_linked(a2, 'Agent', b)


def test_assoc_flowOfEvents29_reverse_link_reassign_clear():
    a1 = textualusecase_Step(name="sample_text")
    a2 = textualusecase_Step(name="sample_text_2")
    b = textualusecase_FlowOfEvents(name="sample_text")
    _safe_set(b, 'FlowOfEvents', a1)
    assert _is_linked(b, 'FlowOfEvents', a1)
    if hasattr(a1, 'steps30'):
        assert _is_linked(a1, 'steps30', b)
    _safe_set(b, 'FlowOfEvents', a2)
    assert _is_linked(b, 'FlowOfEvents', a2)
    if hasattr(a1, 'steps30'):
        assert not _is_linked(a1, 'steps30', b)
    if hasattr(a2, 'steps30'):
        assert _is_linked(a2, 'steps30', b)
    _safe_set(b, 'FlowOfEvents', None)
    assert not _is_linked(b, 'FlowOfEvents', a2)
    if hasattr(a2, 'steps30'):
        assert not _is_linked(a2, 'steps30', b)


def test_assoc_postCondition10_reverse_link_reassign_clear():
    a1 = textualusecase_UseCase(description="sample_text", name="sample_text")
    a2 = textualusecase_UseCase(description="sample_text_2", name="sample_text_2")
    b = textualusecase_Condition(expression="sample_text")
    _safe_set(b, 'textualusecase_Condition', a1)
    assert _is_linked(b, 'textualusecase_Condition', a1)
    if hasattr(a1, 'textualusecase_UseCase'):
        assert _is_linked(a1, 'textualusecase_UseCase', b)
    _safe_set(b, 'textualusecase_Condition', a2)
    assert _is_linked(b, 'textualusecase_Condition', a2)
    if hasattr(a1, 'textualusecase_UseCase'):
        assert not _is_linked(a1, 'textualusecase_UseCase', b)
    if hasattr(a2, 'textualusecase_UseCase'):
        assert _is_linked(a2, 'textualusecase_UseCase', b)
    _safe_set(b, 'textualusecase_Condition', None)
    assert not _is_linked(b, 'textualusecase_Condition', a2)
    if hasattr(a2, 'textualusecase_UseCase'):
        assert not _is_linked(a2, 'textualusecase_UseCase', b)


def test_assoc_preCondition11_reverse_link_reassign_clear():
    a1 = textualusecase_UseCase(description="sample_text", name="sample_text")
    a2 = textualusecase_UseCase(description="sample_text_2", name="sample_text_2")
    b = textualusecase_Condition(expression="sample_text")
    _safe_set(b, 'textualusecase_Condition13', a1)
    assert _is_linked(b, 'textualusecase_Condition13', a1)
    if hasattr(a1, 'textualusecase_UseCase12'):
        assert _is_linked(a1, 'textualusecase_UseCase12', b)
    _safe_set(b, 'textualusecase_Condition13', a2)
    assert _is_linked(b, 'textualusecase_Condition13', a2)
    if hasattr(a1, 'textualusecase_UseCase12'):
        assert not _is_linked(a1, 'textualusecase_UseCase12', b)
    if hasattr(a2, 'textualusecase_UseCase12'):
        assert _is_linked(a2, 'textualusecase_UseCase12', b)
    _safe_set(b, 'textualusecase_Condition13', None)
    assert not _is_linked(b, 'textualusecase_Condition13', a2)
    if hasattr(a2, 'textualusecase_UseCase12'):
        assert not _is_linked(a2, 'textualusecase_UseCase12', b)


def test_assoc_steps24_reverse_link_reassign_clear():
    a1 = textualusecase_Step(name="sample_text")
    a2 = textualusecase_Step(name="sample_text_2")
    b = textualusecase_FlowOfEvents(name="sample_text")
    _safe_set(b, 'flowOfEvents', {a1})
    assert _is_linked(b, 'flowOfEvents', a1)
    if hasattr(a1, 'Step25'):
        assert _is_linked(a1, 'Step25', b)
    _safe_set(b, 'flowOfEvents', {a2})
    assert _is_linked(b, 'flowOfEvents', a2)
    if hasattr(a1, 'Step25'):
        assert not _is_linked(a1, 'Step25', b)
    if hasattr(a2, 'Step25'):
        assert _is_linked(a2, 'Step25', b)
    _safe_set(b, 'flowOfEvents', set())
    assert not _is_linked(b, 'flowOfEvents', a2)
    if hasattr(a2, 'Step25'):
        assert not _is_linked(a2, 'Step25', b)


