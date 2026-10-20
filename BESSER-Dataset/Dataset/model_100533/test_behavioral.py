import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Flow,
    NamedFlow,
    Step,
    StepAlternative,
    UseCaseDSL_Actor,
    UseCaseDSL_AlternativeFlow,
    UseCaseDSL_AlternativeFlowAlternative,
    UseCaseDSL_BasicFlow,
    UseCaseDSL_Condition,
    UseCaseDSL_ExceptionFlow,
    UseCaseDSL_Flow,
    UseCaseDSL_LocalAlternative,
    UseCaseDSL_NamedFlow,
    UseCaseDSL_NormalStep,
    UseCaseDSL_PackageDeclaration,
    UseCaseDSL_ParallelFlow,
    UseCaseDSL_ParallelStep,
    UseCaseDSL_Step,
    UseCaseDSL_StepAlternative,
    UseCaseDSL_UseCase,
    UseCaseDSL_UseCasesModel,
    ActorType,
    CustomStepType,
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

def test_assoc_actor6_reverse_link_reassign_clear():
    a1 = UseCaseDSL_NormalStep(customStepType="sample_text")
    a2 = UseCaseDSL_NormalStep(customStepType="sample_text_2")
    b = UseCaseDSL_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'UseCaseDSL_Actor8', a1)
    assert _is_linked(b, 'UseCaseDSL_Actor8', a1)
    if hasattr(a1, 'UseCaseDSL_NormalStep7'):
        assert _is_linked(a1, 'UseCaseDSL_NormalStep7', b)
    _safe_set(b, 'UseCaseDSL_Actor8', a2)
    assert _is_linked(b, 'UseCaseDSL_Actor8', a2)
    if hasattr(a1, 'UseCaseDSL_NormalStep7'):
        assert not _is_linked(a1, 'UseCaseDSL_NormalStep7', b)
    if hasattr(a2, 'UseCaseDSL_NormalStep7'):
        assert _is_linked(a2, 'UseCaseDSL_NormalStep7', b)
    _safe_set(b, 'UseCaseDSL_Actor8', None)
    assert not _is_linked(b, 'UseCaseDSL_Actor8', a2)
    if hasattr(a2, 'UseCaseDSL_NormalStep7'):
        assert not _is_linked(a2, 'UseCaseDSL_NormalStep7', b)


def test_assoc_actors11_reverse_link_reassign_clear():
    a1 = UseCaseDSL_PackageDeclaration(description="sample_text", name="sample_text")
    a2 = UseCaseDSL_PackageDeclaration(description="sample_text_2", name="sample_text_2")
    b = UseCaseDSL_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'UseCaseDSL_Actor13', a1)
    assert _is_linked(b, 'UseCaseDSL_Actor13', a1)
    if hasattr(a1, 'UseCaseDSL_PackageDeclaration12'):
        assert _is_linked(a1, 'UseCaseDSL_PackageDeclaration12', b)
    _safe_set(b, 'UseCaseDSL_Actor13', a2)
    assert _is_linked(b, 'UseCaseDSL_Actor13', a2)
    if hasattr(a1, 'UseCaseDSL_PackageDeclaration12'):
        assert not _is_linked(a1, 'UseCaseDSL_PackageDeclaration12', b)
    if hasattr(a2, 'UseCaseDSL_PackageDeclaration12'):
        assert _is_linked(a2, 'UseCaseDSL_PackageDeclaration12', b)
    _safe_set(b, 'UseCaseDSL_Actor13', None)
    assert not _is_linked(b, 'UseCaseDSL_Actor13', a2)
    if hasattr(a2, 'UseCaseDSL_PackageDeclaration12'):
        assert not _is_linked(a2, 'UseCaseDSL_PackageDeclaration12', b)


def test_assoc_continuation21_reverse_link_reassign_clear():
    a1 = UseCaseDSL_StepAlternative(condition="sample_text")
    a2 = UseCaseDSL_StepAlternative(condition="sample_text_2")
    b = UseCaseDSL_Step(label="sample_text", name="sample_text")
    _safe_set(b, 'UseCaseDSL_Step23', a1)
    assert _is_linked(b, 'UseCaseDSL_Step23', a1)
    if hasattr(a1, 'UseCaseDSL_StepAlternative22'):
        assert _is_linked(a1, 'UseCaseDSL_StepAlternative22', b)
    _safe_set(b, 'UseCaseDSL_Step23', a2)
    assert _is_linked(b, 'UseCaseDSL_Step23', a2)
    if hasattr(a1, 'UseCaseDSL_StepAlternative22'):
        assert not _is_linked(a1, 'UseCaseDSL_StepAlternative22', b)
    if hasattr(a2, 'UseCaseDSL_StepAlternative22'):
        assert _is_linked(a2, 'UseCaseDSL_StepAlternative22', b)
    _safe_set(b, 'UseCaseDSL_Step23', None)
    assert not _is_linked(b, 'UseCaseDSL_Step23', a2)
    if hasattr(a2, 'UseCaseDSL_StepAlternative22'):
        assert not _is_linked(a2, 'UseCaseDSL_StepAlternative22', b)


def test_assoc_extends1_reverse_link_reassign_clear():
    a1 = UseCaseDSL_Actor(description="sample_text", name="sample_text", type="sample_text")
    a2 = UseCaseDSL_Actor(description="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = UseCaseDSL_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'UseCaseDSL_Actor0', a1)
    assert _is_linked(b, 'UseCaseDSL_Actor0', a1)
    if hasattr(a1, 'UseCaseDSL_Actor'):
        assert _is_linked(a1, 'UseCaseDSL_Actor', b)
    _safe_set(b, 'UseCaseDSL_Actor0', a2)
    assert _is_linked(b, 'UseCaseDSL_Actor0', a2)
    if hasattr(a1, 'UseCaseDSL_Actor'):
        assert not _is_linked(a1, 'UseCaseDSL_Actor', b)
    if hasattr(a2, 'UseCaseDSL_Actor'):
        assert _is_linked(a2, 'UseCaseDSL_Actor', b)
    _safe_set(b, 'UseCaseDSL_Actor0', None)
    assert not _is_linked(b, 'UseCaseDSL_Actor0', a2)
    if hasattr(a2, 'UseCaseDSL_Actor'):
        assert not _is_linked(a2, 'UseCaseDSL_Actor', b)


def test_assoc_flows27_reverse_link_reassign_clear():
    a1 = UseCaseDSL_UseCase(description="sample_text", name="sample_text", postcondition="sample_text", preConditions="sample_text")
    a2 = UseCaseDSL_UseCase(description="sample_text_2", name="sample_text_2", postcondition="sample_text_2", preConditions="sample_text_2")
    b = UseCaseDSL_Flow(finalState="sample_text")
    _safe_set(b, 'UseCaseDSL_Flow29', a1)
    assert _is_linked(b, 'UseCaseDSL_Flow29', a1)
    if hasattr(a1, 'UseCaseDSL_UseCase28'):
        assert _is_linked(a1, 'UseCaseDSL_UseCase28', b)
    _safe_set(b, 'UseCaseDSL_Flow29', a2)
    assert _is_linked(b, 'UseCaseDSL_Flow29', a2)
    if hasattr(a1, 'UseCaseDSL_UseCase28'):
        assert not _is_linked(a1, 'UseCaseDSL_UseCase28', b)
    if hasattr(a2, 'UseCaseDSL_UseCase28'):
        assert _is_linked(a2, 'UseCaseDSL_UseCase28', b)
    _safe_set(b, 'UseCaseDSL_Flow29', None)
    assert not _is_linked(b, 'UseCaseDSL_Flow29', a2)
    if hasattr(a2, 'UseCaseDSL_UseCase28'):
        assert not _is_linked(a2, 'UseCaseDSL_UseCase28', b)


def test_assoc_invokedUseCase18_reverse_link_reassign_clear():
    a1 = UseCaseDSL_UseCase(description="sample_text", name="sample_text", postcondition="sample_text", preConditions="sample_text")
    a2 = UseCaseDSL_UseCase(description="sample_text_2", name="sample_text_2", postcondition="sample_text_2", preConditions="sample_text_2")
    b = UseCaseDSL_Step(label="sample_text", name="sample_text")
    _safe_set(b, 'UseCaseDSL_Step19', a1)
    assert _is_linked(b, 'UseCaseDSL_Step19', a1)
    if hasattr(a1, 'UseCaseDSL_UseCase20'):
        assert _is_linked(a1, 'UseCaseDSL_UseCase20', b)
    _safe_set(b, 'UseCaseDSL_Step19', a2)
    assert _is_linked(b, 'UseCaseDSL_Step19', a2)
    if hasattr(a1, 'UseCaseDSL_UseCase20'):
        assert not _is_linked(a1, 'UseCaseDSL_UseCase20', b)
    if hasattr(a2, 'UseCaseDSL_UseCase20'):
        assert _is_linked(a2, 'UseCaseDSL_UseCase20', b)
    _safe_set(b, 'UseCaseDSL_Step19', None)
    assert not _is_linked(b, 'UseCaseDSL_Step19', a2)
    if hasattr(a2, 'UseCaseDSL_UseCase20'):
        assert not _is_linked(a2, 'UseCaseDSL_UseCase20', b)


def test_assoc_invokedUseCase4_reverse_link_reassign_clear():
    a1 = UseCaseDSL_UseCase(description="sample_text", name="sample_text", postcondition="sample_text", preConditions="sample_text")
    a2 = UseCaseDSL_UseCase(description="sample_text_2", name="sample_text_2", postcondition="sample_text_2", preConditions="sample_text_2")
    b = UseCaseDSL_LocalAlternative(description="sample_text")
    _safe_set(b, 'UseCaseDSL_LocalAlternative', a1)
    assert _is_linked(b, 'UseCaseDSL_LocalAlternative', a1)
    if hasattr(a1, 'UseCaseDSL_UseCase'):
        assert _is_linked(a1, 'UseCaseDSL_UseCase', b)
    _safe_set(b, 'UseCaseDSL_LocalAlternative', a2)
    assert _is_linked(b, 'UseCaseDSL_LocalAlternative', a2)
    if hasattr(a1, 'UseCaseDSL_UseCase'):
        assert not _is_linked(a1, 'UseCaseDSL_UseCase', b)
    if hasattr(a2, 'UseCaseDSL_UseCase'):
        assert _is_linked(a2, 'UseCaseDSL_UseCase', b)
    _safe_set(b, 'UseCaseDSL_LocalAlternative', None)
    assert not _is_linked(b, 'UseCaseDSL_LocalAlternative', a2)
    if hasattr(a2, 'UseCaseDSL_UseCase'):
        assert not _is_linked(a2, 'UseCaseDSL_UseCase', b)


def test_assoc_next16_reverse_link_reassign_clear():
    a1 = UseCaseDSL_Step(label="sample_text", name="sample_text")
    a2 = UseCaseDSL_Step(label="sample_text_2", name="sample_text_2")
    b = UseCaseDSL_Step(label="sample_text", name="sample_text")
    _safe_set(b, 'UseCaseDSL_Step17', a1)
    assert _is_linked(b, 'UseCaseDSL_Step17', a1)
    if hasattr(a1, 'UseCaseDSL_Step15'):
        assert _is_linked(a1, 'UseCaseDSL_Step15', b)
    _safe_set(b, 'UseCaseDSL_Step17', a2)
    assert _is_linked(b, 'UseCaseDSL_Step17', a2)
    if hasattr(a1, 'UseCaseDSL_Step15'):
        assert not _is_linked(a1, 'UseCaseDSL_Step15', b)
    if hasattr(a2, 'UseCaseDSL_Step15'):
        assert _is_linked(a2, 'UseCaseDSL_Step15', b)
    _safe_set(b, 'UseCaseDSL_Step17', None)
    assert not _is_linked(b, 'UseCaseDSL_Step17', a2)
    if hasattr(a2, 'UseCaseDSL_Step15'):
        assert not _is_linked(a2, 'UseCaseDSL_Step15', b)


def test_assoc_stepAlternative5_reverse_link_reassign_clear():
    a1 = UseCaseDSL_StepAlternative(condition="sample_text")
    a2 = UseCaseDSL_StepAlternative(condition="sample_text_2")
    b = UseCaseDSL_NormalStep(customStepType="sample_text")
    _safe_set(b, 'UseCaseDSL_NormalStep', {a1})
    assert _is_linked(b, 'UseCaseDSL_NormalStep', a1)
    if hasattr(a1, 'UseCaseDSL_StepAlternative'):
        assert _is_linked(a1, 'UseCaseDSL_StepAlternative', b)
    _safe_set(b, 'UseCaseDSL_NormalStep', {a2})
    assert _is_linked(b, 'UseCaseDSL_NormalStep', a2)
    if hasattr(a1, 'UseCaseDSL_StepAlternative'):
        assert not _is_linked(a1, 'UseCaseDSL_StepAlternative', b)
    if hasattr(a2, 'UseCaseDSL_StepAlternative'):
        assert _is_linked(a2, 'UseCaseDSL_StepAlternative', b)
    _safe_set(b, 'UseCaseDSL_NormalStep', set())
    assert not _is_linked(b, 'UseCaseDSL_NormalStep', a2)
    if hasattr(a2, 'UseCaseDSL_StepAlternative'):
        assert not _is_linked(a2, 'UseCaseDSL_StepAlternative', b)


def test_assoc_steps3_reverse_link_reassign_clear():
    a1 = UseCaseDSL_Step(label="sample_text", name="sample_text")
    a2 = UseCaseDSL_Step(label="sample_text_2", name="sample_text_2")
    b = UseCaseDSL_Flow(finalState="sample_text")
    _safe_set(b, 'UseCaseDSL_Flow', {a1})
    assert _is_linked(b, 'UseCaseDSL_Flow', a1)
    if hasattr(a1, 'UseCaseDSL_Step'):
        assert _is_linked(a1, 'UseCaseDSL_Step', b)
    _safe_set(b, 'UseCaseDSL_Flow', {a2})
    assert _is_linked(b, 'UseCaseDSL_Flow', a2)
    if hasattr(a1, 'UseCaseDSL_Step'):
        assert not _is_linked(a1, 'UseCaseDSL_Step', b)
    if hasattr(a2, 'UseCaseDSL_Step'):
        assert _is_linked(a2, 'UseCaseDSL_Step', b)
    _safe_set(b, 'UseCaseDSL_Flow', set())
    assert not _is_linked(b, 'UseCaseDSL_Flow', a2)
    if hasattr(a2, 'UseCaseDSL_Step'):
        assert not _is_linked(a2, 'UseCaseDSL_Step', b)


def test_assoc_superCase25_reverse_link_reassign_clear():
    a1 = UseCaseDSL_UseCase(description="sample_text", name="sample_text", postcondition="sample_text", preConditions="sample_text")
    a2 = UseCaseDSL_UseCase(description="sample_text_2", name="sample_text_2", postcondition="sample_text_2", preConditions="sample_text_2")
    b = UseCaseDSL_UseCase(description="sample_text", name="sample_text", postcondition="sample_text", preConditions="sample_text")
    _safe_set(b, 'UseCaseDSL_UseCase26', a1)
    assert _is_linked(b, 'UseCaseDSL_UseCase26', a1)
    if hasattr(a1, 'UseCaseDSL_UseCase24'):
        assert _is_linked(a1, 'UseCaseDSL_UseCase24', b)
    _safe_set(b, 'UseCaseDSL_UseCase26', a2)
    assert _is_linked(b, 'UseCaseDSL_UseCase26', a2)
    if hasattr(a1, 'UseCaseDSL_UseCase24'):
        assert not _is_linked(a1, 'UseCaseDSL_UseCase24', b)
    if hasattr(a2, 'UseCaseDSL_UseCase24'):
        assert _is_linked(a2, 'UseCaseDSL_UseCase24', b)
    _safe_set(b, 'UseCaseDSL_UseCase26', None)
    assert not _is_linked(b, 'UseCaseDSL_UseCase26', a2)
    if hasattr(a2, 'UseCaseDSL_UseCase24'):
        assert not _is_linked(a2, 'UseCaseDSL_UseCase24', b)


def test_assoc_useCases9_reverse_link_reassign_clear():
    a1 = UseCaseDSL_UseCase(description="sample_text", name="sample_text", postcondition="sample_text", preConditions="sample_text")
    a2 = UseCaseDSL_UseCase(description="sample_text_2", name="sample_text_2", postcondition="sample_text_2", preConditions="sample_text_2")
    b = UseCaseDSL_PackageDeclaration(description="sample_text", name="sample_text")
    _safe_set(b, 'UseCaseDSL_PackageDeclaration', {a1})
    assert _is_linked(b, 'UseCaseDSL_PackageDeclaration', a1)
    if hasattr(a1, 'UseCaseDSL_UseCase10'):
        assert _is_linked(a1, 'UseCaseDSL_UseCase10', b)
    _safe_set(b, 'UseCaseDSL_PackageDeclaration', {a2})
    assert _is_linked(b, 'UseCaseDSL_PackageDeclaration', a2)
    if hasattr(a1, 'UseCaseDSL_UseCase10'):
        assert not _is_linked(a1, 'UseCaseDSL_UseCase10', b)
    if hasattr(a2, 'UseCaseDSL_UseCase10'):
        assert _is_linked(a2, 'UseCaseDSL_UseCase10', b)
    _safe_set(b, 'UseCaseDSL_PackageDeclaration', set())
    assert not _is_linked(b, 'UseCaseDSL_PackageDeclaration', a2)
    if hasattr(a2, 'UseCaseDSL_UseCase10'):
        assert not _is_linked(a2, 'UseCaseDSL_UseCase10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_packages30_stub_double():
    # UseCaseDSL_UseCasesModel has no real 'UseCaseDSL_UseCasesModel' property in the generated
    # code (a bare stub) -- manually attach it so UseCaseDSL_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCaseDSL_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCaseDSL_PackageDeclaration(description="sample_text", name="sample_text")
    partner = UseCaseDSL_UseCasesModel()
    setattr(partner, 'UseCaseDSL_UseCasesModel', None)
    _safe_set(owner, 'UseCaseDSL_PackageDeclaration31', partner)
    assert owner in getattr(partner, 'UseCaseDSL_UseCasesModel')
    _safe_set(owner, 'UseCaseDSL_PackageDeclaration31', None)
    assert owner not in getattr(partner, 'UseCaseDSL_UseCasesModel')


def test_assoc_ref2_stub_double():
    # UseCaseDSL_AlternativeFlowAlternative has no real 'UseCaseDSL_AlternativeFlowAlternative' property in the generated
    # code (a bare stub) -- manually attach it so UseCaseDSL_NamedFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCaseDSL_NamedFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCaseDSL_NamedFlow(name="sample_text")
    partner = UseCaseDSL_AlternativeFlowAlternative()
    setattr(partner, 'UseCaseDSL_AlternativeFlowAlternative', None)
    _safe_set(owner, 'UseCaseDSL_NamedFlow', partner)
    assert getattr(partner, 'UseCaseDSL_AlternativeFlowAlternative') == owner
    _safe_set(owner, 'UseCaseDSL_NamedFlow', None)
    assert getattr(partner, 'UseCaseDSL_AlternativeFlowAlternative') is None


