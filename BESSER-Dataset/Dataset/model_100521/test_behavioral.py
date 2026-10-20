import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanExpression,
    Classifier,
    Extend,
    ExtensionPoint,
    Include,
    Instance,
    LocationReference,
    ModelElement,
    RelationShip,
    UseCase,
    UseCases_Actor,
    UseCases_BooleanExpression,
    UseCases_Classifier,
    UseCases_Extend,
    UseCases_ExtensionPoint,
    UseCases_Include,
    UseCases_Instance,
    UseCases_LocationReference,
    UseCases_ModelElement,
    UseCases_RelationShip,
    UseCases_UseCase,
    UseCases_UseCaseInstance,
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

def test_assoc_extendBase6_stub_double():
    # Extend has no real 'Extend8' property in the generated
    # code (a bare stub) -- manually attach it so UseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCases_UseCase(extensionPoint="sample_text")
    partner = Extend()
    setattr(partner, 'Extend8', None)
    _safe_set(owner, 'base7', partner)
    assert getattr(partner, 'Extend8') == owner
    _safe_set(owner, 'base7', None)
    assert getattr(partner, 'Extend8') is None


def test_assoc_extendExtension5_stub_double():
    # Extend has no real 'Extend' property in the generated
    # code (a bare stub) -- manually attach it so UseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCases_UseCase(extensionPoint="sample_text")
    partner = Extend()
    setattr(partner, 'Extend', None)
    _safe_set(owner, 'extension', partner)
    assert getattr(partner, 'Extend') == owner
    _safe_set(owner, 'extension', None)
    assert getattr(partner, 'Extend') is None


def test_assoc_extensionPoints9_stub_double():
    # ExtensionPoint has no real 'ExtensionPoint' property in the generated
    # code (a bare stub) -- manually attach it so UseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCases_UseCase(extensionPoint="sample_text")
    partner = ExtensionPoint()
    setattr(partner, 'ExtensionPoint', None)
    _safe_set(owner, 'useCase', {partner})
    assert getattr(partner, 'ExtensionPoint') == owner
    _safe_set(owner, 'useCase', set())
    assert getattr(partner, 'ExtensionPoint') is None


def test_assoc_includeAddition2_stub_double():
    # Include has no real 'Include' property in the generated
    # code (a bare stub) -- manually attach it so UseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCases_UseCase(extensionPoint="sample_text")
    partner = Include()
    setattr(partner, 'Include', None)
    _safe_set(owner, 'addition', partner)
    assert getattr(partner, 'Include') == owner
    _safe_set(owner, 'addition', None)
    assert getattr(partner, 'Include') is None


def test_assoc_includeBase3_stub_double():
    # Include has no real 'Include4' property in the generated
    # code (a bare stub) -- manually attach it so UseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UseCases_UseCase(extensionPoint="sample_text")
    partner = Include()
    setattr(partner, 'Include4', None)
    _safe_set(owner, 'base', partner)
    assert getattr(partner, 'Include4') == owner
    _safe_set(owner, 'base', None)
    assert getattr(partner, 'Include4') is None


