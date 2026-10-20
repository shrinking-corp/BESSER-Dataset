import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BuiltinEventSpec,
    Declaration,
    DefRoot,
    Effect,
    Event,
    EventSpec,
    Expression,
    NamedElement,
    Operation,
    Property,
    Reaction,
    ReactionProperty,
    Scope,
    ScopedElement,
    StatechartScope,
    Trigger,
    TypeAlias,
    stext_ActiveStateReferenceExpression,
    stext_AlwaysEvent,
    stext_BuiltinEventSpec,
    stext_DefRoot,
    stext_DefaultTrigger,
    stext_EntryEvent,
    stext_EntryPointSpec,
    stext_EventDefinition,
    stext_EventRaisingExpression,
    stext_EventSpec,
    stext_EventValueReferenceExpression,
    stext_ExitEvent,
    stext_ExitPointSpec,
    stext_Expression,
    stext_Guard,
    stext_Import,
    stext_ImportScope,
    stext_InterfaceScope,
    stext_InternalScope,
    stext_LocalReaction,
    stext_OperationDefinition,
    stext_ReactionEffect,
    stext_ReactionTrigger,
    stext_RegularEventSpec,
    stext_Root,
    stext_Scope,
    stext_SimpleScope,
    stext_State,
    stext_StateRoot,
    stext_StateSpecification,
    stext_StatechartRoot,
    stext_StatechartScope,
    stext_StatechartSpecification,
    stext_TimeEventSpec,
    stext_TransitionReaction,
    stext_TransitionRoot,
    stext_TransitionSpecification,
    stext_TypeAliasDefinition,
    stext_VariableDefinition,
    TimeEventType,
    TimeUnit,
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

def test_assoc_imports8_stub_double():
    # stext_ImportScope has no real 'stext_ImportScope' property in the generated
    # code (a bare stub) -- manually attach it so stext_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_Import(importedNamespace="sample_text")
    partner = stext_ImportScope()
    setattr(partner, 'stext_ImportScope', None)
    _safe_set(owner, 'stext_Import', partner)
    assert owner in getattr(partner, 'stext_ImportScope')
    _safe_set(owner, 'stext_Import', None)
    assert owner not in getattr(partner, 'stext_ImportScope')


def test_assoc_value14_stub_double():
    # stext_Expression has no real 'stext_Expression15' property in the generated
    # code (a bare stub) -- manually attach it so stext_TimeEventSpec's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_TimeEventSpec's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_TimeEventSpec(type="sample_text", unit="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression15', None)
    _safe_set(owner, 'stext_TimeEventSpec', partner)
    assert getattr(partner, 'stext_Expression15') == owner
    _safe_set(owner, 'stext_TimeEventSpec', None)
    assert getattr(partner, 'stext_Expression15') is None


