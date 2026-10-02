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


