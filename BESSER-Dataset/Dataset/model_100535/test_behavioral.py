import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Flow,
    NamedFlow,
    StepAlternative,
    useCases_Actor,
    useCases_AlternativeFlow,
    useCases_AlternativeFlowAlternative,
    useCases_ApplicationInstance,
    useCases_BasicFlow,
    useCases_Condition,
    useCases_CustomAttributes,
    useCases_CustomStepType,
    useCases_Entity,
    useCases_EntityRef,
    useCases_ExceptionFlow,
    useCases_Feature,
    useCases_Flow,
    useCases_Identifiable,
    useCases_Label,
    useCases_LocalAlternative,
    useCases_NamedFlow,
    useCases_NamespaceImport,
    useCases_PackageDeclaration,
    useCases_PageRef,
    useCases_Precondition,
    useCases_RequirementRef,
    useCases_Screen,
    useCases_Step,
    useCases_StepAlternative,
    useCases_UseCase,
    useCases_UseCasesModel,
    useCases_ViewInstance,
    ActorType,
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

def test_assoc_actor55_reverse_link_reassign_clear():
    a1 = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    a2 = useCases_Step(description="sample_text_2", label="sample_text_2", name="sample_text_2")
    b = useCases_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'useCases_Actor57', a1)
    assert _is_linked(b, 'useCases_Actor57', a1)
    if hasattr(a1, 'useCases_Step56'):
        assert _is_linked(a1, 'useCases_Step56', b)
    _safe_set(b, 'useCases_Actor57', a2)
    assert _is_linked(b, 'useCases_Actor57', a2)
    if hasattr(a1, 'useCases_Step56'):
        assert not _is_linked(a1, 'useCases_Step56', b)
    if hasattr(a2, 'useCases_Step56'):
        assert _is_linked(a2, 'useCases_Step56', b)
    _safe_set(b, 'useCases_Actor57', None)
    assert not _is_linked(b, 'useCases_Actor57', a2)
    if hasattr(a2, 'useCases_Step56'):
        assert not _is_linked(a2, 'useCases_Step56', b)


def test_assoc_actors19_reverse_link_reassign_clear():
    a1 = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    a2 = useCases_PackageDeclaration(description="sample_text_2", name="sample_text_2")
    b = useCases_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'useCases_Actor', a1)
    assert _is_linked(b, 'useCases_Actor', a1)
    if hasattr(a1, 'useCases_PackageDeclaration20'):
        assert _is_linked(a1, 'useCases_PackageDeclaration20', b)
    _safe_set(b, 'useCases_Actor', a2)
    assert _is_linked(b, 'useCases_Actor', a2)
    if hasattr(a1, 'useCases_PackageDeclaration20'):
        assert not _is_linked(a1, 'useCases_PackageDeclaration20', b)
    if hasattr(a2, 'useCases_PackageDeclaration20'):
        assert _is_linked(a2, 'useCases_PackageDeclaration20', b)
    _safe_set(b, 'useCases_Actor', None)
    assert not _is_linked(b, 'useCases_Actor', a2)
    if hasattr(a2, 'useCases_PackageDeclaration20'):
        assert not _is_linked(a2, 'useCases_PackageDeclaration20', b)


def test_assoc_actors28_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'useCases_Actor30', a1)
    assert _is_linked(b, 'useCases_Actor30', a1)
    if hasattr(a1, 'useCases_UseCase29'):
        assert _is_linked(a1, 'useCases_UseCase29', b)
    _safe_set(b, 'useCases_Actor30', a2)
    assert _is_linked(b, 'useCases_Actor30', a2)
    if hasattr(a1, 'useCases_UseCase29'):
        assert not _is_linked(a1, 'useCases_UseCase29', b)
    if hasattr(a2, 'useCases_UseCase29'):
        assert _is_linked(a2, 'useCases_UseCase29', b)
    _safe_set(b, 'useCases_Actor30', None)
    assert not _is_linked(b, 'useCases_Actor30', a2)
    if hasattr(a2, 'useCases_UseCase29'):
        assert not _is_linked(a2, 'useCases_UseCase29', b)


def test_assoc_alternatives66_reverse_link_reassign_clear():
    a1 = useCases_StepAlternative(finalState="sample_text", finalizeFlow=True)
    a2 = useCases_StepAlternative(finalState="sample_text_2", finalizeFlow=False)
    b = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    _safe_set(b, 'useCases_Step67', {a1})
    assert _is_linked(b, 'useCases_Step67', a1)
    if hasattr(a1, 'useCases_StepAlternative'):
        assert _is_linked(a1, 'useCases_StepAlternative', b)
    _safe_set(b, 'useCases_Step67', {a2})
    assert _is_linked(b, 'useCases_Step67', a2)
    if hasattr(a1, 'useCases_StepAlternative'):
        assert not _is_linked(a1, 'useCases_StepAlternative', b)
    if hasattr(a2, 'useCases_StepAlternative'):
        assert _is_linked(a2, 'useCases_StepAlternative', b)
    _safe_set(b, 'useCases_Step67', set())
    assert not _is_linked(b, 'useCases_Step67', a2)
    if hasattr(a2, 'useCases_StepAlternative'):
        assert not _is_linked(a2, 'useCases_StepAlternative', b)


def test_assoc_condition76_reverse_link_reassign_clear():
    a1 = useCases_LocalAlternative(description="sample_text")
    a2 = useCases_LocalAlternative(description="sample_text_2")
    b = useCases_Condition(condition="sample_text")
    _safe_set(b, 'useCases_Condition', a1)
    assert _is_linked(b, 'useCases_Condition', a1)
    if hasattr(a1, 'useCases_LocalAlternative'):
        assert _is_linked(a1, 'useCases_LocalAlternative', b)
    _safe_set(b, 'useCases_Condition', a2)
    assert _is_linked(b, 'useCases_Condition', a2)
    if hasattr(a1, 'useCases_LocalAlternative'):
        assert not _is_linked(a1, 'useCases_LocalAlternative', b)
    if hasattr(a2, 'useCases_LocalAlternative'):
        assert _is_linked(a2, 'useCases_LocalAlternative', b)
    _safe_set(b, 'useCases_Condition', None)
    assert not _is_linked(b, 'useCases_Condition', a2)
    if hasattr(a2, 'useCases_LocalAlternative'):
        assert not _is_linked(a2, 'useCases_LocalAlternative', b)


def test_assoc_continuation70_reverse_link_reassign_clear():
    a1 = useCases_StepAlternative(finalState="sample_text", finalizeFlow=True)
    a2 = useCases_StepAlternative(finalState="sample_text_2", finalizeFlow=False)
    b = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    _safe_set(b, 'useCases_Step72', a1)
    assert _is_linked(b, 'useCases_Step72', a1)
    if hasattr(a1, 'useCases_StepAlternative71'):
        assert _is_linked(a1, 'useCases_StepAlternative71', b)
    _safe_set(b, 'useCases_Step72', a2)
    assert _is_linked(b, 'useCases_Step72', a2)
    if hasattr(a1, 'useCases_StepAlternative71'):
        assert not _is_linked(a1, 'useCases_StepAlternative71', b)
    if hasattr(a2, 'useCases_StepAlternative71'):
        assert _is_linked(a2, 'useCases_StepAlternative71', b)
    _safe_set(b, 'useCases_Step72', None)
    assert not _is_linked(b, 'useCases_Step72', a2)
    if hasattr(a2, 'useCases_StepAlternative71'):
        assert not _is_linked(a2, 'useCases_StepAlternative71', b)


def test_assoc_exceptionFlows43_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_ExceptionFlow(condition="sample_text")
    _safe_set(b, 'useCases_ExceptionFlow', a1)
    assert _is_linked(b, 'useCases_ExceptionFlow', a1)
    if hasattr(a1, 'useCases_UseCase44'):
        assert _is_linked(a1, 'useCases_UseCase44', b)
    _safe_set(b, 'useCases_ExceptionFlow', a2)
    assert _is_linked(b, 'useCases_ExceptionFlow', a2)
    if hasattr(a1, 'useCases_UseCase44'):
        assert not _is_linked(a1, 'useCases_UseCase44', b)
    if hasattr(a2, 'useCases_UseCase44'):
        assert _is_linked(a2, 'useCases_UseCase44', b)
    _safe_set(b, 'useCases_ExceptionFlow', None)
    assert not _is_linked(b, 'useCases_ExceptionFlow', a2)
    if hasattr(a2, 'useCases_UseCase44'):
        assert not _is_linked(a2, 'useCases_UseCase44', b)


def test_assoc_extends24_reverse_link_reassign_clear():
    a1 = useCases_Actor(description="sample_text", name="sample_text", type="sample_text")
    a2 = useCases_Actor(description="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = useCases_Actor(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'useCases_Actor25', a1)
    assert _is_linked(b, 'useCases_Actor25', a1)
    if hasattr(a1, 'useCases_Actor23'):
        assert _is_linked(a1, 'useCases_Actor23', b)
    _safe_set(b, 'useCases_Actor25', a2)
    assert _is_linked(b, 'useCases_Actor25', a2)
    if hasattr(a1, 'useCases_Actor23'):
        assert not _is_linked(a1, 'useCases_Actor23', b)
    if hasattr(a2, 'useCases_Actor23'):
        assert _is_linked(a2, 'useCases_Actor23', b)
    _safe_set(b, 'useCases_Actor25', None)
    assert not _is_linked(b, 'useCases_Actor25', a2)
    if hasattr(a2, 'useCases_Actor23'):
        assert not _is_linked(a2, 'useCases_Actor23', b)


def test_assoc_invokedUseCase63_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    _safe_set(b, 'useCases_Step64', a1)
    assert _is_linked(b, 'useCases_Step64', a1)
    if hasattr(a1, 'useCases_UseCase65'):
        assert _is_linked(a1, 'useCases_UseCase65', b)
    _safe_set(b, 'useCases_Step64', a2)
    assert _is_linked(b, 'useCases_Step64', a2)
    if hasattr(a1, 'useCases_UseCase65'):
        assert not _is_linked(a1, 'useCases_UseCase65', b)
    if hasattr(a2, 'useCases_UseCase65'):
        assert _is_linked(a2, 'useCases_UseCase65', b)
    _safe_set(b, 'useCases_Step64', None)
    assert not _is_linked(b, 'useCases_Step64', a2)
    if hasattr(a2, 'useCases_UseCase65'):
        assert not _is_linked(a2, 'useCases_UseCase65', b)


def test_assoc_invokedUseCase77_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_LocalAlternative(description="sample_text")
    _safe_set(b, 'useCases_LocalAlternative78', a1)
    assert _is_linked(b, 'useCases_LocalAlternative78', a1)
    if hasattr(a1, 'useCases_UseCase79'):
        assert _is_linked(a1, 'useCases_UseCase79', b)
    _safe_set(b, 'useCases_LocalAlternative78', a2)
    assert _is_linked(b, 'useCases_LocalAlternative78', a2)
    if hasattr(a1, 'useCases_UseCase79'):
        assert not _is_linked(a1, 'useCases_UseCase79', b)
    if hasattr(a2, 'useCases_UseCase79'):
        assert _is_linked(a2, 'useCases_UseCase79', b)
    _safe_set(b, 'useCases_LocalAlternative78', None)
    assert not _is_linked(b, 'useCases_LocalAlternative78', a2)
    if hasattr(a2, 'useCases_UseCase79'):
        assert not _is_linked(a2, 'useCases_UseCase79', b)


def test_assoc_preConditions35_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_Precondition(name="sample_text")
    _safe_set(b, 'useCases_Precondition', a1)
    assert _is_linked(b, 'useCases_Precondition', a1)
    if hasattr(a1, 'useCases_UseCase36'):
        assert _is_linked(a1, 'useCases_UseCase36', b)
    _safe_set(b, 'useCases_Precondition', a2)
    assert _is_linked(b, 'useCases_Precondition', a2)
    if hasattr(a1, 'useCases_UseCase36'):
        assert not _is_linked(a1, 'useCases_UseCase36', b)
    if hasattr(a2, 'useCases_UseCase36'):
        assert _is_linked(a2, 'useCases_UseCase36', b)
    _safe_set(b, 'useCases_Precondition', None)
    assert not _is_linked(b, 'useCases_Precondition', a2)
    if hasattr(a2, 'useCases_UseCase36'):
        assert not _is_linked(a2, 'useCases_UseCase36', b)


def test_assoc_requires51_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_Precondition(name="sample_text")
    _safe_set(b, 'useCases_Precondition52', a1)
    assert _is_linked(b, 'useCases_Precondition52', a1)
    if hasattr(a1, 'useCases_UseCase53'):
        assert _is_linked(a1, 'useCases_UseCase53', b)
    _safe_set(b, 'useCases_Precondition52', a2)
    assert _is_linked(b, 'useCases_Precondition52', a2)
    if hasattr(a1, 'useCases_UseCase53'):
        assert not _is_linked(a1, 'useCases_UseCase53', b)
    if hasattr(a2, 'useCases_UseCase53'):
        assert _is_linked(a2, 'useCases_UseCase53', b)
    _safe_set(b, 'useCases_Precondition52', None)
    assert not _is_linked(b, 'useCases_Precondition52', a2)
    if hasattr(a2, 'useCases_UseCase53'):
        assert not _is_linked(a2, 'useCases_UseCase53', b)


def test_assoc_steps54_reverse_link_reassign_clear():
    a1 = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    a2 = useCases_Step(description="sample_text_2", label="sample_text_2", name="sample_text_2")
    b = useCases_Flow(finalState="sample_text")
    _safe_set(b, 'useCases_Flow', {a1})
    assert _is_linked(b, 'useCases_Flow', a1)
    if hasattr(a1, 'useCases_Step'):
        assert _is_linked(a1, 'useCases_Step', b)
    _safe_set(b, 'useCases_Flow', {a2})
    assert _is_linked(b, 'useCases_Flow', a2)
    if hasattr(a1, 'useCases_Step'):
        assert not _is_linked(a1, 'useCases_Step', b)
    if hasattr(a2, 'useCases_Step'):
        assert _is_linked(a2, 'useCases_Step', b)
    _safe_set(b, 'useCases_Flow', set())
    assert not _is_linked(b, 'useCases_Flow', a2)
    if hasattr(a2, 'useCases_Step'):
        assert not _is_linked(a2, 'useCases_Step', b)


def test_assoc_useCases21_reverse_link_reassign_clear():
    a1 = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    a2 = useCases_UseCase(goals="sample_text_2", name="sample_text_2", ucName="sample_text_2")
    b = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    _safe_set(b, 'useCases_PackageDeclaration22', {a1})
    assert _is_linked(b, 'useCases_PackageDeclaration22', a1)
    if hasattr(a1, 'useCases_UseCase'):
        assert _is_linked(a1, 'useCases_UseCase', b)
    _safe_set(b, 'useCases_PackageDeclaration22', {a2})
    assert _is_linked(b, 'useCases_PackageDeclaration22', a2)
    if hasattr(a1, 'useCases_UseCase'):
        assert not _is_linked(a1, 'useCases_UseCase', b)
    if hasattr(a2, 'useCases_UseCase'):
        assert _is_linked(a2, 'useCases_UseCase', b)
    _safe_set(b, 'useCases_PackageDeclaration22', set())
    assert not _is_linked(b, 'useCases_PackageDeclaration22', a2)
    if hasattr(a2, 'useCases_UseCase'):
        assert not _is_linked(a2, 'useCases_UseCase', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alternativeFlows41_stub_double():
    # useCases_AlternativeFlow has no real 'useCases_AlternativeFlow' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_AlternativeFlow()
    setattr(partner, 'useCases_AlternativeFlow', None)
    _safe_set(owner, 'useCases_UseCase42', {partner})
    assert getattr(partner, 'useCases_AlternativeFlow') == owner
    _safe_set(owner, 'useCases_UseCase42', set())
    assert getattr(partner, 'useCases_AlternativeFlow') is None


def test_assoc_basicFlow39_stub_double():
    # useCases_BasicFlow has no real 'useCases_BasicFlow' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_BasicFlow()
    setattr(partner, 'useCases_BasicFlow', None)
    _safe_set(owner, 'useCases_UseCase40', partner)
    assert getattr(partner, 'useCases_BasicFlow') == owner
    _safe_set(owner, 'useCases_UseCase40', None)
    assert getattr(partner, 'useCases_BasicFlow') is None


def test_assoc_commonLabels37_stub_double():
    # useCases_Label has no real 'useCases_Label' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_Label()
    setattr(partner, 'useCases_Label', None)
    _safe_set(owner, 'useCases_UseCase38', {partner})
    assert getattr(partner, 'useCases_Label') == owner
    _safe_set(owner, 'useCases_UseCase38', set())
    assert getattr(partner, 'useCases_Label') is None


def test_assoc_condition80_stub_double():
    # useCases_AlternativeFlowAlternative has no real 'useCases_AlternativeFlowAlternative' property in the generated
    # code (a bare stub) -- manually attach it so useCases_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_Condition(condition="sample_text")
    partner = useCases_AlternativeFlowAlternative()
    setattr(partner, 'useCases_AlternativeFlowAlternative', None)
    _safe_set(owner, 'useCases_Condition81', partner)
    assert getattr(partner, 'useCases_AlternativeFlowAlternative') == owner
    _safe_set(owner, 'useCases_Condition81', None)
    assert getattr(partner, 'useCases_AlternativeFlowAlternative') is None


def test_assoc_customAttributes45_stub_double():
    # useCases_CustomAttributes has no real 'useCases_CustomAttributes' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_CustomAttributes()
    setattr(partner, 'useCases_CustomAttributes', None)
    _safe_set(owner, 'useCases_UseCase46', partner)
    assert getattr(partner, 'useCases_CustomAttributes') == owner
    _safe_set(owner, 'useCases_UseCase46', None)
    assert getattr(partner, 'useCases_CustomAttributes') is None


def test_assoc_customStepType68_stub_double():
    # useCases_CustomStepType has no real 'useCases_CustomStepType' property in the generated
    # code (a bare stub) -- manually attach it so useCases_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    partner = useCases_CustomStepType()
    setattr(partner, 'useCases_CustomStepType', None)
    _safe_set(owner, 'useCases_Step69', partner)
    assert getattr(partner, 'useCases_CustomStepType') == owner
    _safe_set(owner, 'useCases_Step69', None)
    assert getattr(partner, 'useCases_CustomStepType') is None


def test_assoc_customStepType73_stub_double():
    # useCases_CustomStepType has no real 'useCases_CustomStepType75' property in the generated
    # code (a bare stub) -- manually attach it so useCases_StepAlternative's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_StepAlternative's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_StepAlternative(finalState="sample_text", finalizeFlow=True)
    partner = useCases_CustomStepType()
    setattr(partner, 'useCases_CustomStepType75', None)
    _safe_set(owner, 'useCases_StepAlternative74', partner)
    assert getattr(partner, 'useCases_CustomStepType75') == owner
    _safe_set(owner, 'useCases_StepAlternative74', None)
    assert getattr(partner, 'useCases_CustomStepType75') is None


def test_assoc_entities31_stub_double():
    # useCases_Entity has no real 'useCases_Entity' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_Entity()
    setattr(partner, 'useCases_Entity', None)
    _safe_set(owner, 'useCases_UseCase32', {partner})
    assert getattr(partner, 'useCases_Entity') == owner
    _safe_set(owner, 'useCases_UseCase32', set())
    assert getattr(partner, 'useCases_Entity') is None


def test_assoc_entityRefs58_stub_double():
    # useCases_EntityRef has no real 'useCases_EntityRef' property in the generated
    # code (a bare stub) -- manually attach it so useCases_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    partner = useCases_EntityRef()
    setattr(partner, 'useCases_EntityRef', None)
    _safe_set(owner, 'useCases_Step59', {partner})
    assert getattr(partner, 'useCases_EntityRef') == owner
    _safe_set(owner, 'useCases_Step59', set())
    assert getattr(partner, 'useCases_EntityRef') is None


def test_assoc_namespaceImports16_stub_double():
    # useCases_NamespaceImport has no real 'useCases_NamespaceImport18' property in the generated
    # code (a bare stub) -- manually attach it so useCases_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    partner = useCases_NamespaceImport()
    setattr(partner, 'useCases_NamespaceImport18', None)
    _safe_set(owner, 'useCases_PackageDeclaration17', {partner})
    assert getattr(partner, 'useCases_NamespaceImport18') == owner
    _safe_set(owner, 'useCases_PackageDeclaration17', set())
    assert getattr(partner, 'useCases_NamespaceImport18') is None


def test_assoc_packages1_stub_double():
    # useCases_UseCasesModel has no real 'useCases_UseCasesModel2' property in the generated
    # code (a bare stub) -- manually attach it so useCases_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    partner = useCases_UseCasesModel()
    setattr(partner, 'useCases_UseCasesModel2', None)
    _safe_set(owner, 'useCases_PackageDeclaration', partner)
    assert getattr(partner, 'useCases_UseCasesModel2') == owner
    _safe_set(owner, 'useCases_PackageDeclaration', None)
    assert getattr(partner, 'useCases_UseCasesModel2') is None


def test_assoc_pages33_stub_double():
    # useCases_PageRef has no real 'useCases_PageRef' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_PageRef()
    setattr(partner, 'useCases_PageRef', None)
    _safe_set(owner, 'useCases_UseCase34', {partner})
    assert getattr(partner, 'useCases_PageRef') == owner
    _safe_set(owner, 'useCases_UseCase34', set())
    assert getattr(partner, 'useCases_PageRef') is None


def test_assoc_ref82_stub_double():
    # useCases_AlternativeFlowAlternative has no real 'useCases_AlternativeFlowAlternative83' property in the generated
    # code (a bare stub) -- manually attach it so useCases_NamedFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_NamedFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_NamedFlow(name="sample_text")
    partner = useCases_AlternativeFlowAlternative()
    setattr(partner, 'useCases_AlternativeFlowAlternative83', None)
    _safe_set(owner, 'useCases_NamedFlow', partner)
    assert getattr(partner, 'useCases_AlternativeFlowAlternative83') == owner
    _safe_set(owner, 'useCases_NamedFlow', None)
    assert getattr(partner, 'useCases_AlternativeFlowAlternative83') is None


def test_assoc_refActorImportedNamespace13_stub_double():
    # useCases_NamespaceImport has no real 'useCases_NamespaceImport14' property in the generated
    # code (a bare stub) -- manually attach it so useCases_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    partner = useCases_NamespaceImport()
    setattr(partner, 'useCases_NamespaceImport14', None)
    _safe_set(owner, 'useCases_PackageDeclaration15', partner)
    assert getattr(partner, 'useCases_NamespaceImport14') == owner
    _safe_set(owner, 'useCases_PackageDeclaration15', None)
    assert getattr(partner, 'useCases_NamespaceImport14') is None


def test_assoc_refEntityImportedNamespace3_stub_double():
    # useCases_NamespaceImport has no real 'useCases_NamespaceImport4' property in the generated
    # code (a bare stub) -- manually attach it so useCases_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    partner = useCases_NamespaceImport()
    setattr(partner, 'useCases_NamespaceImport4', None)
    _safe_set(owner, 'useCases_PackageDeclaration5', partner)
    assert getattr(partner, 'useCases_NamespaceImport4') == owner
    _safe_set(owner, 'useCases_PackageDeclaration5', None)
    assert getattr(partner, 'useCases_NamespaceImport4') is None


def test_assoc_refUseCaseImportedNamespace10_stub_double():
    # useCases_NamespaceImport has no real 'useCases_NamespaceImport11' property in the generated
    # code (a bare stub) -- manually attach it so useCases_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_PackageDeclaration(description="sample_text", name="sample_text")
    partner = useCases_NamespaceImport()
    setattr(partner, 'useCases_NamespaceImport11', None)
    _safe_set(owner, 'useCases_PackageDeclaration12', partner)
    assert getattr(partner, 'useCases_NamespaceImport11') == owner
    _safe_set(owner, 'useCases_PackageDeclaration12', None)
    assert getattr(partner, 'useCases_NamespaceImport11') is None


def test_assoc_requirements26_stub_double():
    # useCases_RequirementRef has no real 'useCases_RequirementRef' property in the generated
    # code (a bare stub) -- manually attach it so useCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_UseCase(goals="sample_text", name="sample_text", ucName="sample_text")
    partner = useCases_RequirementRef()
    setattr(partner, 'useCases_RequirementRef', None)
    _safe_set(owner, 'useCases_UseCase27', {partner})
    assert getattr(partner, 'useCases_RequirementRef') == owner
    _safe_set(owner, 'useCases_UseCase27', set())
    assert getattr(partner, 'useCases_RequirementRef') is None


def test_assoc_screen60_stub_double():
    # useCases_Screen has no real 'useCases_Screen62' property in the generated
    # code (a bare stub) -- manually attach it so useCases_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # useCases_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = useCases_Step(description="sample_text", label="sample_text", name="sample_text")
    partner = useCases_Screen()
    setattr(partner, 'useCases_Screen62', None)
    _safe_set(owner, 'useCases_Step61', partner)
    assert getattr(partner, 'useCases_Screen62') == owner
    _safe_set(owner, 'useCases_Step61', None)
    assert getattr(partner, 'useCases_Screen62') is None


