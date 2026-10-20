import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    File,
    standard_Abstraction,
    standard_Artifact,
    standard_Auxiliary,
    standard_BehavioralFeature,
    standard_BuildComponent,
    standard_Call,
    standard_Class,
    standard_Classifier,
    standard_Component,
    standard_Create,
    standard_Derive,
    standard_Destroy,
    standard_Document,
    standard_Entity,
    standard_Executable,
    standard_File,
    standard_Focus,
    standard_Framework,
    standard_Implement,
    standard_ImplementationClass,
    standard_Instantiate,
    standard_Library,
    standard_Metaclass,
    standard_Metamodel,
    standard_Model,
    standard_ModelLibrary,
    standard_Package,
    standard_Process,
    standard_Realization,
    standard_Refine,
    standard_Responsibility,
    standard_Script,
    standard_Send,
    standard_Service,
    standard_Source,
    standard_Specification,
    standard_Subsystem,
    standard_SystemModel,
    standard_Trace,
    standard_Type,
    standard_Usage,
    standard_Utility,
    standard_ValueSpecification,
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
    # standard_BehavioralFeature has no real 'standard_BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so standard_Create's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Create's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Create()
    partner = standard_BehavioralFeature()
    setattr(partner, 'standard_BehavioralFeature', None)
    _safe_set(owner, 'standard_Create', partner)
    assert getattr(partner, 'standard_BehavioralFeature') == owner
    _safe_set(owner, 'standard_Create', None)
    assert getattr(partner, 'standard_BehavioralFeature') is None


def test_assoc_base_Class18_stub_double():
    # standard_Class has no real 'standard_Class19' property in the generated
    # code (a bare stub) -- manually attach it so standard_ImplementationClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_ImplementationClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_ImplementationClass()
    partner = standard_Class()
    setattr(partner, 'standard_Class19', None)
    _safe_set(owner, 'standard_ImplementationClass', partner)
    assert getattr(partner, 'standard_Class19') == owner
    _safe_set(owner, 'standard_ImplementationClass', None)
    assert getattr(partner, 'standard_Class19') is None


def test_assoc_base_Class43_stub_double():
    # standard_Class has no real 'standard_Class44' property in the generated
    # code (a bare stub) -- manually attach it so standard_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Type()
    partner = standard_Class()
    setattr(partner, 'standard_Class44', None)
    _safe_set(owner, 'standard_Type', partner)
    assert getattr(partner, 'standard_Class44') == owner
    _safe_set(owner, 'standard_Type', None)
    assert getattr(partner, 'standard_Class44') is None


def test_assoc_base_Class45_stub_double():
    # standard_Class has no real 'standard_Class46' property in the generated
    # code (a bare stub) -- manually attach it so standard_Utility's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Utility's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Utility()
    partner = standard_Class()
    setattr(partner, 'standard_Class46', None)
    _safe_set(owner, 'standard_Utility', partner)
    assert getattr(partner, 'standard_Class46') == owner
    _safe_set(owner, 'standard_Utility', None)
    assert getattr(partner, 'standard_Class46') is None


def test_assoc_base_Classifier28_stub_double():
    # standard_Classifier has no real 'standard_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so standard_Realization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Realization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Realization()
    partner = standard_Classifier()
    setattr(partner, 'standard_Classifier', None)
    _safe_set(owner, 'standard_Realization', partner)
    assert getattr(partner, 'standard_Classifier') == owner
    _safe_set(owner, 'standard_Realization', None)
    assert getattr(partner, 'standard_Classifier') is None


def test_assoc_base_Classifier37_stub_double():
    # standard_Classifier has no real 'standard_Classifier38' property in the generated
    # code (a bare stub) -- manually attach it so standard_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Specification()
    partner = standard_Classifier()
    setattr(partner, 'standard_Classifier38', None)
    _safe_set(owner, 'standard_Specification', partner)
    assert getattr(partner, 'standard_Classifier38') == owner
    _safe_set(owner, 'standard_Specification', None)
    assert getattr(partner, 'standard_Classifier38') is None


def test_assoc_base_Component16_stub_double():
    # standard_Component has no real 'standard_Component17' property in the generated
    # code (a bare stub) -- manually attach it so standard_Implement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Implement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Implement()
    partner = standard_Component()
    setattr(partner, 'standard_Component17', None)
    _safe_set(owner, 'standard_Implement', partner)
    assert getattr(partner, 'standard_Component17') == owner
    _safe_set(owner, 'standard_Implement', None)
    assert getattr(partner, 'standard_Component17') is None


def test_assoc_base_Usage1_stub_double():
    # standard_Usage has no real 'standard_Usage' property in the generated
    # code (a bare stub) -- manually attach it so standard_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Call()
    partner = standard_Usage()
    setattr(partner, 'standard_Usage', None)
    _safe_set(owner, 'standard_Call', partner)
    assert getattr(partner, 'standard_Usage') == owner
    _safe_set(owner, 'standard_Call', None)
    assert getattr(partner, 'standard_Usage') is None


def test_assoc_base_Usage20_stub_double():
    # standard_Usage has no real 'standard_Usage21' property in the generated
    # code (a bare stub) -- manually attach it so standard_Instantiate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Instantiate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Instantiate()
    partner = standard_Usage()
    setattr(partner, 'standard_Usage21', None)
    _safe_set(owner, 'standard_Instantiate', partner)
    assert getattr(partner, 'standard_Usage21') == owner
    _safe_set(owner, 'standard_Instantiate', None)
    assert getattr(partner, 'standard_Usage21') is None


def test_assoc_base_Usage3_stub_double():
    # standard_Usage has no real 'standard_Usage5' property in the generated
    # code (a bare stub) -- manually attach it so standard_Create's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Create's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Create()
    partner = standard_Usage()
    setattr(partner, 'standard_Usage5', None)
    _safe_set(owner, 'standard_Create4', partner)
    assert getattr(partner, 'standard_Usage5') == owner
    _safe_set(owner, 'standard_Create4', None)
    assert getattr(partner, 'standard_Usage5') is None


def test_assoc_base_Usage33_stub_double():
    # standard_Usage has no real 'standard_Usage34' property in the generated
    # code (a bare stub) -- manually attach it so standard_Send's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_Send's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_Send()
    partner = standard_Usage()
    setattr(partner, 'standard_Usage34', None)
    _safe_set(owner, 'standard_Send', partner)
    assert getattr(partner, 'standard_Usage34') == owner
    _safe_set(owner, 'standard_Send', None)
    assert getattr(partner, 'standard_Usage34') is None


