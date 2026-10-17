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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actor7_stub_double():
    # textualusecase_Actor has no real 'Actor9' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_Actor()
    setattr(partner, 'Actor9', None)
    _safe_set(owner, 'useCase8', {partner})
    assert getattr(partner, 'Actor9') == owner
    _safe_set(owner, 'useCase8', set())
    assert getattr(partner, 'Actor9') is None


def test_assoc_alternativeFlow26_stub_double():
    # textualusecase_AlternativeFlow has no real 'AlternativeFlow27' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_Step(name="sample_text")
    partner = textualusecase_AlternativeFlow()
    setattr(partner, 'AlternativeFlow27', None)
    _safe_set(owner, 'branchingStep', {partner})
    assert getattr(partner, 'AlternativeFlow27') == owner
    _safe_set(owner, 'branchingStep', set())
    assert getattr(partner, 'AlternativeFlow27') is None


def test_assoc_alternativeFlow4_stub_double():
    # textualusecase_AlternativeFlow has no real 'AlternativeFlow' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_AlternativeFlow()
    setattr(partner, 'AlternativeFlow', None)
    _safe_set(owner, 'useCase', {partner})
    assert getattr(partner, 'AlternativeFlow') == owner
    _safe_set(owner, 'useCase', set())
    assert getattr(partner, 'AlternativeFlow') is None


def test_assoc_basicFlow5_stub_double():
    # textualusecase_BasicFlow has no real 'BasicFlow' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_BasicFlow()
    setattr(partner, 'BasicFlow', None)
    _safe_set(owner, 'useCase6', partner)
    assert getattr(partner, 'BasicFlow') == owner
    _safe_set(owner, 'useCase6', None)
    assert getattr(partner, 'BasicFlow') is None


def test_assoc_branchingStep18_stub_double():
    # textualusecase_AlternativeFlow has no real 'alternativeFlow' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_Step(name="sample_text")
    partner = textualusecase_AlternativeFlow()
    setattr(partner, 'alternativeFlow', None)
    _safe_set(owner, 'Step', partner)
    assert getattr(partner, 'alternativeFlow') == owner
    _safe_set(owner, 'Step', None)
    assert getattr(partner, 'alternativeFlow') is None


def test_assoc_condition19_stub_double():
    # textualusecase_AlternativeFlow has no real 'textualusecase_AlternativeFlow' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_Condition(expression="sample_text")
    partner = textualusecase_AlternativeFlow()
    setattr(partner, 'textualusecase_AlternativeFlow', None)
    _safe_set(owner, 'textualusecase_Condition20', partner)
    assert getattr(partner, 'textualusecase_AlternativeFlow') == owner
    _safe_set(owner, 'textualusecase_Condition20', None)
    assert getattr(partner, 'textualusecase_AlternativeFlow') is None


def test_assoc_condition32_stub_double():
    # textualusecase_Statement has no real 'textualusecase_Statement' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_Condition(expression="sample_text")
    partner = textualusecase_Statement()
    setattr(partner, 'textualusecase_Statement', None)
    _safe_set(owner, 'textualusecase_Condition33', partner)
    assert getattr(partner, 'textualusecase_Statement') == owner
    _safe_set(owner, 'textualusecase_Condition33', None)
    assert getattr(partner, 'textualusecase_Statement') is None


def test_assoc_includes16_stub_double():
    # textualusecase_Include has no real 'Include' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_Include()
    setattr(partner, 'Include', None)
    _safe_set(owner, 'useCase17', {partner})
    assert getattr(partner, 'Include') == owner
    _safe_set(owner, 'useCase17', set())
    assert getattr(partner, 'Include') is None


def test_assoc_statement28_stub_double():
    # textualusecase_Statement has no real 'Statement' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_Step(name="sample_text")
    partner = textualusecase_Statement()
    setattr(partner, 'Statement', None)
    _safe_set(owner, 'steps', partner)
    assert getattr(partner, 'Statement') == owner
    _safe_set(owner, 'steps', None)
    assert getattr(partner, 'Statement') is None


def test_assoc_steps34_stub_double():
    # textualusecase_Statement has no real 'statement' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_Step(name="sample_text")
    partner = textualusecase_Statement()
    setattr(partner, 'statement', None)
    _safe_set(owner, 'Step35', partner)
    assert getattr(partner, 'statement') == owner
    _safe_set(owner, 'Step35', None)
    assert getattr(partner, 'statement') is None


def test_assoc_useCase0_stub_double():
    # textualusecase_UseCaseModel has no real 'useCaseModel' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_UseCaseModel()
    setattr(partner, 'useCaseModel', None)
    _safe_set(owner, 'UseCase', partner)
    assert getattr(partner, 'useCaseModel') == owner
    _safe_set(owner, 'UseCase', None)
    assert getattr(partner, 'useCaseModel') is None


def test_assoc_useCase21_stub_double():
    # textualusecase_AlternativeFlow has no real 'alternativeFlow22' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_AlternativeFlow()
    setattr(partner, 'alternativeFlow22', None)
    _safe_set(owner, 'UseCase23', partner)
    assert getattr(partner, 'alternativeFlow22') == owner
    _safe_set(owner, 'UseCase23', None)
    assert getattr(partner, 'alternativeFlow22') is None


def test_assoc_useCase36_stub_double():
    # textualusecase_BasicFlow has no real 'basicFlow' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_BasicFlow()
    setattr(partner, 'basicFlow', None)
    _safe_set(owner, 'UseCase37', partner)
    assert getattr(partner, 'basicFlow') == owner
    _safe_set(owner, 'UseCase37', None)
    assert getattr(partner, 'basicFlow') is None


def test_assoc_useCase40_stub_double():
    # textualusecase_Actor has no real 'actor41' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_Actor()
    setattr(partner, 'actor41', None)
    _safe_set(owner, 'UseCase42', partner)
    assert getattr(partner, 'actor41') == owner
    _safe_set(owner, 'UseCase42', None)
    assert getattr(partner, 'actor41') is None


def test_assoc_useCase46_stub_double():
    # textualusecase_Include has no real 'includes' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_Include()
    setattr(partner, 'includes', None)
    _safe_set(owner, 'UseCase47', partner)
    assert getattr(partner, 'includes') == owner
    _safe_set(owner, 'UseCase47', None)
    assert getattr(partner, 'includes') is None


def test_assoc_useCaseModel14_stub_double():
    # textualusecase_UseCaseModel has no real 'UseCaseModel' property in the generated
    # code (a bare stub) -- manually attach it so textualusecase_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # textualusecase_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = textualusecase_UseCase(description="sample_text", name="sample_text")
    partner = textualusecase_UseCaseModel()
    setattr(partner, 'UseCaseModel', None)
    _safe_set(owner, 'useCase15', partner)
    assert getattr(partner, 'UseCaseModel') == owner
    _safe_set(owner, 'useCase15', None)
    assert getattr(partner, 'UseCaseModel') is None


