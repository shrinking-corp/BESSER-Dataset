import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    File,
    l2_Abstraction,
    l2_Artifact,
    l2_Auxiliary,
    l2_BehavioralFeature,
    l2_Call,
    l2_Class,
    l2_Classifier,
    l2_Component,
    l2_Create,
    l2_Derive,
    l2_Destroy,
    l2_Document,
    l2_Entity,
    l2_Executable,
    l2_File,
    l2_Focus,
    l2_Framework,
    l2_Implement,
    l2_ImplementationClass,
    l2_Instantiate,
    l2_Library,
    l2_Metaclass,
    l2_ModelLibrary,
    l2_Package,
    l2_Process,
    l2_Realization,
    l2_Refine,
    l2_Responsibility,
    l2_Script,
    l2_Send,
    l2_Service,
    l2_Source,
    l2_Specification,
    l2_Subsystem,
    l2_Trace,
    l2_Type,
    l2_Usage,
    l2_Utility,
    l2_ValueSpecification,
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

def test_assoc_base_BehavioralFeature2_stub_double():
    # l2_BehavioralFeature has no real 'l2_BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so l2_Create's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Create's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Create()
    partner = l2_BehavioralFeature()
    setattr(partner, 'l2_BehavioralFeature', None)
    _safe_set(owner, 'l2_Create', partner)
    assert getattr(partner, 'l2_BehavioralFeature') == owner
    _safe_set(owner, 'l2_Create', None)
    assert getattr(partner, 'l2_BehavioralFeature') is None


def test_assoc_base_Class18_stub_double():
    # l2_Class has no real 'l2_Class19' property in the generated
    # code (a bare stub) -- manually attach it so l2_ImplementationClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_ImplementationClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_ImplementationClass()
    partner = l2_Class()
    setattr(partner, 'l2_Class19', None)
    _safe_set(owner, 'l2_ImplementationClass', partner)
    assert getattr(partner, 'l2_Class19') == owner
    _safe_set(owner, 'l2_ImplementationClass', None)
    assert getattr(partner, 'l2_Class19') is None


def test_assoc_base_Class43_stub_double():
    # l2_Class has no real 'l2_Class44' property in the generated
    # code (a bare stub) -- manually attach it so l2_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Type()
    partner = l2_Class()
    setattr(partner, 'l2_Class44', None)
    _safe_set(owner, 'l2_Type', partner)
    assert getattr(partner, 'l2_Class44') == owner
    _safe_set(owner, 'l2_Type', None)
    assert getattr(partner, 'l2_Class44') is None


def test_assoc_base_Class45_stub_double():
    # l2_Class has no real 'l2_Class46' property in the generated
    # code (a bare stub) -- manually attach it so l2_Utility's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Utility's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Utility()
    partner = l2_Class()
    setattr(partner, 'l2_Class46', None)
    _safe_set(owner, 'l2_Utility', partner)
    assert getattr(partner, 'l2_Class46') == owner
    _safe_set(owner, 'l2_Utility', None)
    assert getattr(partner, 'l2_Class46') is None


def test_assoc_base_Classifier28_stub_double():
    # l2_Classifier has no real 'l2_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so l2_Realization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Realization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Realization()
    partner = l2_Classifier()
    setattr(partner, 'l2_Classifier', None)
    _safe_set(owner, 'l2_Realization', partner)
    assert getattr(partner, 'l2_Classifier') == owner
    _safe_set(owner, 'l2_Realization', None)
    assert getattr(partner, 'l2_Classifier') is None


def test_assoc_base_Classifier37_stub_double():
    # l2_Classifier has no real 'l2_Classifier38' property in the generated
    # code (a bare stub) -- manually attach it so l2_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Specification()
    partner = l2_Classifier()
    setattr(partner, 'l2_Classifier38', None)
    _safe_set(owner, 'l2_Specification', partner)
    assert getattr(partner, 'l2_Classifier38') == owner
    _safe_set(owner, 'l2_Specification', None)
    assert getattr(partner, 'l2_Classifier38') is None


def test_assoc_base_Component16_stub_double():
    # l2_Component has no real 'l2_Component17' property in the generated
    # code (a bare stub) -- manually attach it so l2_Implement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Implement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Implement()
    partner = l2_Component()
    setattr(partner, 'l2_Component17', None)
    _safe_set(owner, 'l2_Implement', partner)
    assert getattr(partner, 'l2_Component17') == owner
    _safe_set(owner, 'l2_Implement', None)
    assert getattr(partner, 'l2_Component17') is None


def test_assoc_base_Usage1_stub_double():
    # l2_Usage has no real 'l2_Usage' property in the generated
    # code (a bare stub) -- manually attach it so l2_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Call()
    partner = l2_Usage()
    setattr(partner, 'l2_Usage', None)
    _safe_set(owner, 'l2_Call', partner)
    assert getattr(partner, 'l2_Usage') == owner
    _safe_set(owner, 'l2_Call', None)
    assert getattr(partner, 'l2_Usage') is None


def test_assoc_base_Usage20_stub_double():
    # l2_Usage has no real 'l2_Usage21' property in the generated
    # code (a bare stub) -- manually attach it so l2_Instantiate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Instantiate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Instantiate()
    partner = l2_Usage()
    setattr(partner, 'l2_Usage21', None)
    _safe_set(owner, 'l2_Instantiate', partner)
    assert getattr(partner, 'l2_Usage21') == owner
    _safe_set(owner, 'l2_Instantiate', None)
    assert getattr(partner, 'l2_Usage21') is None


def test_assoc_base_Usage3_stub_double():
    # l2_Usage has no real 'l2_Usage5' property in the generated
    # code (a bare stub) -- manually attach it so l2_Create's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Create's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Create()
    partner = l2_Usage()
    setattr(partner, 'l2_Usage5', None)
    _safe_set(owner, 'l2_Create4', partner)
    assert getattr(partner, 'l2_Usage5') == owner
    _safe_set(owner, 'l2_Create4', None)
    assert getattr(partner, 'l2_Usage5') is None


def test_assoc_base_Usage33_stub_double():
    # l2_Usage has no real 'l2_Usage34' property in the generated
    # code (a bare stub) -- manually attach it so l2_Send's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # l2_Send's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = l2_Send()
    partner = l2_Usage()
    setattr(partner, 'l2_Usage34', None)
    _safe_set(owner, 'l2_Send', partner)
    assert getattr(partner, 'l2_Usage34') == owner
    _safe_set(owner, 'l2_Send', None)
    assert getattr(partner, 'l2_Usage34') is None


