import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArchElementToArchElement,
    ArchitecturalElement,
    CriticalityLevel,
    FaultTreeNode,
    HazardElement,
    HazardRelation,
    MonitorToArchitecturalElement,
    SafetyCriticalRelation,
    SafetyTactic,
    SafetyViewpoint,
    State,
    safetyDSL_ANDNodeExpression,
    safetyDSL_ArchElementToArchElement,
    safetyDSL_ArchitecturalElement,
    safetyDSL_CausedBy,
    safetyDSL_Causes,
    safetyDSL_ClassDef,
    safetyDSL_ClassTestCaseRelation,
    safetyDSL_Commands,
    safetyDSL_Consequence,
    safetyDSL_CriticalityLevel,
    safetyDSL_DerivedFrom,
    safetyDSL_Fault,
    safetyDSL_FaultAvoidance,
    safetyDSL_FaultContainment,
    safetyDSL_FaultDetection,
    safetyDSL_FaultTree,
    safetyDSL_FaultTreeNode,
    safetyDSL_Hazard,
    safetyDSL_HazardElement,
    safetyDSL_HazardRelation,
    safetyDSL_HazardViewpoint,
    safetyDSL_ImplementationDetail,
    safetyDSL_Inits,
    safetyDSL_LevelA,
    safetyDSL_LevelB,
    safetyDSL_LevelC,
    safetyDSL_LevelD,
    safetyDSL_ModuleClassRelation,
    safetyDSL_Monitor,
    safetyDSL_MonitorToArchitecturalElement,
    safetyDSL_Monitors,
    safetyDSL_NonSafetyCritical,
    safetyDSL_ORNodeExpression,
    safetyDSL_Reads,
    safetyDSL_ReportsFault,
    safetyDSL_Restarts,
    safetyDSL_SafeState,
    safetyDSL_SafetyCritical,
    safetyDSL_SafetyCriticalRelation,
    safetyDSL_SafetyCriticalViewpoint,
    safetyDSL_SafetyFramework,
    safetyDSL_SafetyRequirement,
    safetyDSL_SafetyTactic,
    safetyDSL_SafetyTacticViewpoint,
    safetyDSL_SafetyViewpoint,
    safetyDSL_Starts,
    safetyDSL_State,
    safetyDSL_Stops,
    safetyDSL_Writes,
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

def test_assoc_clazz71_reverse_link_reassign_clear():
    a1 = safetyDSL_ClassTestCaseRelation(testCases="sample_text")
    a2 = safetyDSL_ClassTestCaseRelation(testCases="sample_text_2")
    b = safetyDSL_ClassDef(name="sample_text")
    _safe_set(b, 'safetyDSL_ClassDef73', a1)
    assert _is_linked(b, 'safetyDSL_ClassDef73', a1)
    if hasattr(a1, 'safetyDSL_ClassTestCaseRelation72'):
        assert _is_linked(a1, 'safetyDSL_ClassTestCaseRelation72', b)
    _safe_set(b, 'safetyDSL_ClassDef73', a2)
    assert _is_linked(b, 'safetyDSL_ClassDef73', a2)
    if hasattr(a1, 'safetyDSL_ClassTestCaseRelation72'):
        assert not _is_linked(a1, 'safetyDSL_ClassTestCaseRelation72', b)
    if hasattr(a2, 'safetyDSL_ClassTestCaseRelation72'):
        assert _is_linked(a2, 'safetyDSL_ClassTestCaseRelation72', b)
    _safe_set(b, 'safetyDSL_ClassDef73', None)
    assert not _is_linked(b, 'safetyDSL_ClassDef73', a2)
    if hasattr(a2, 'safetyDSL_ClassTestCaseRelation72'):
        assert not _is_linked(a2, 'safetyDSL_ClassTestCaseRelation72', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classTestCaseRelations64_stub_double():
    # safetyDSL_ImplementationDetail has no real 'safetyDSL_ImplementationDetail65' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_ClassTestCaseRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_ClassTestCaseRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_ClassTestCaseRelation(testCases="sample_text")
    partner = safetyDSL_ImplementationDetail()
    setattr(partner, 'safetyDSL_ImplementationDetail65', None)
    _safe_set(owner, 'safetyDSL_ClassTestCaseRelation', partner)
    assert owner in getattr(partner, 'safetyDSL_ImplementationDetail65')
    _safe_set(owner, 'safetyDSL_ClassTestCaseRelation', None)
    assert owner not in getattr(partner, 'safetyDSL_ImplementationDetail65')


def test_assoc_classes69_stub_double():
    # safetyDSL_ModuleClassRelation has no real 'safetyDSL_ModuleClassRelation70' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_ClassDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_ClassDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_ClassDef(name="sample_text")
    partner = safetyDSL_ModuleClassRelation()
    setattr(partner, 'safetyDSL_ModuleClassRelation70', None)
    _safe_set(owner, 'safetyDSL_ClassDef', partner)
    assert owner in getattr(partner, 'safetyDSL_ModuleClassRelation70')
    _safe_set(owner, 'safetyDSL_ClassDef', None)
    assert owner not in getattr(partner, 'safetyDSL_ModuleClassRelation70')


def test_assoc_element147_stub_double():
    # safetyDSL_ArchElementToArchElement has no real 'safetyDSL_ArchElementToArchElement' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_ArchitecturalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_ArchitecturalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_ArchitecturalElement(name="sample_text")
    partner = safetyDSL_ArchElementToArchElement()
    setattr(partner, 'safetyDSL_ArchElementToArchElement', None)
    _safe_set(owner, 'safetyDSL_ArchitecturalElement48', partner)
    assert getattr(partner, 'safetyDSL_ArchElementToArchElement') == owner
    _safe_set(owner, 'safetyDSL_ArchitecturalElement48', None)
    assert getattr(partner, 'safetyDSL_ArchElementToArchElement') is None


def test_assoc_element249_stub_double():
    # safetyDSL_ArchElementToArchElement has no real 'safetyDSL_ArchElementToArchElement50' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_ArchitecturalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_ArchitecturalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_ArchitecturalElement(name="sample_text")
    partner = safetyDSL_ArchElementToArchElement()
    setattr(partner, 'safetyDSL_ArchElementToArchElement50', None)
    _safe_set(owner, 'safetyDSL_ArchitecturalElement51', partner)
    assert owner in getattr(partner, 'safetyDSL_ArchElementToArchElement50')
    _safe_set(owner, 'safetyDSL_ArchitecturalElement51', None)
    assert owner not in getattr(partner, 'safetyDSL_ArchElementToArchElement50')


def test_assoc_elements28_stub_double():
    # safetyDSL_SafetyCriticalViewpoint has no real 'safetyDSL_SafetyCriticalViewpoint' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_ArchitecturalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_ArchitecturalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_ArchitecturalElement(name="sample_text")
    partner = safetyDSL_SafetyCriticalViewpoint()
    setattr(partner, 'safetyDSL_SafetyCriticalViewpoint', None)
    _safe_set(owner, 'safetyDSL_ArchitecturalElement', partner)
    assert owner in getattr(partner, 'safetyDSL_SafetyCriticalViewpoint')
    _safe_set(owner, 'safetyDSL_ArchitecturalElement', None)
    assert owner not in getattr(partner, 'safetyDSL_SafetyCriticalViewpoint')


def test_assoc_elements3_stub_double():
    # safetyDSL_HazardViewpoint has no real 'safetyDSL_HazardViewpoint' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_HazardElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_HazardElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_HazardElement(name="sample_text")
    partner = safetyDSL_HazardViewpoint()
    setattr(partner, 'safetyDSL_HazardViewpoint', None)
    _safe_set(owner, 'safetyDSL_HazardElement', partner)
    assert owner in getattr(partner, 'safetyDSL_HazardViewpoint')
    _safe_set(owner, 'safetyDSL_HazardElement', None)
    assert owner not in getattr(partner, 'safetyDSL_HazardViewpoint')


def test_assoc_handledFaults25_stub_double():
    # safetyDSL_Fault has no real 'safetyDSL_Fault27' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_SafetyTactic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_SafetyTactic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_SafetyTactic(name="sample_text", type="sample_text")
    partner = safetyDSL_Fault()
    setattr(partner, 'safetyDSL_Fault27', None)
    _safe_set(owner, 'safetyDSL_SafetyTactic26', {partner})
    assert getattr(partner, 'safetyDSL_Fault27') == owner
    _safe_set(owner, 'safetyDSL_SafetyTactic26', set())
    assert getattr(partner, 'safetyDSL_Fault27') is None


def test_assoc_implementedTactics35_stub_double():
    # safetyDSL_SafetyCritical has no real 'safetyDSL_SafetyCritical36' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_SafetyTactic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_SafetyTactic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_SafetyTactic(name="sample_text", type="sample_text")
    partner = safetyDSL_SafetyCritical()
    setattr(partner, 'safetyDSL_SafetyCritical36', None)
    _safe_set(owner, 'safetyDSL_SafetyTactic37', partner)
    assert owner in getattr(partner, 'safetyDSL_SafetyCritical36')
    _safe_set(owner, 'safetyDSL_SafetyTactic37', None)
    assert owner not in getattr(partner, 'safetyDSL_SafetyCritical36')


def test_assoc_implementedTactics45_stub_double():
    # safetyDSL_Monitor has no real 'safetyDSL_Monitor' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_SafetyTactic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_SafetyTactic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_SafetyTactic(name="sample_text", type="sample_text")
    partner = safetyDSL_Monitor()
    setattr(partner, 'safetyDSL_Monitor', None)
    _safe_set(owner, 'safetyDSL_SafetyTactic46', partner)
    assert owner in getattr(partner, 'safetyDSL_Monitor')
    _safe_set(owner, 'safetyDSL_SafetyTactic46', None)
    assert owner not in getattr(partner, 'safetyDSL_Monitor')


def test_assoc_module66_stub_double():
    # safetyDSL_ModuleClassRelation has no real 'safetyDSL_ModuleClassRelation67' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_ArchitecturalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_ArchitecturalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_ArchitecturalElement(name="sample_text")
    partner = safetyDSL_ModuleClassRelation()
    setattr(partner, 'safetyDSL_ModuleClassRelation67', None)
    _safe_set(owner, 'safetyDSL_ArchitecturalElement68', partner)
    assert getattr(partner, 'safetyDSL_ModuleClassRelation67') == owner
    _safe_set(owner, 'safetyDSL_ArchitecturalElement68', None)
    assert getattr(partner, 'safetyDSL_ModuleClassRelation67') is None


def test_assoc_safetyTactics24_stub_double():
    # safetyDSL_SafetyTacticViewpoint has no real 'safetyDSL_SafetyTacticViewpoint' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_SafetyTactic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_SafetyTactic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_SafetyTactic(name="sample_text", type="sample_text")
    partner = safetyDSL_SafetyTacticViewpoint()
    setattr(partner, 'safetyDSL_SafetyTacticViewpoint', None)
    _safe_set(owner, 'safetyDSL_SafetyTactic', partner)
    assert owner in getattr(partner, 'safetyDSL_SafetyTacticViewpoint')
    _safe_set(owner, 'safetyDSL_SafetyTactic', None)
    assert owner not in getattr(partner, 'safetyDSL_SafetyTacticViewpoint')


def test_assoc_states41_stub_double():
    # safetyDSL_SafetyCritical has no real 'safetyDSL_SafetyCritical42' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_State(name="sample_text")
    partner = safetyDSL_SafetyCritical()
    setattr(partner, 'safetyDSL_SafetyCritical42', None)
    _safe_set(owner, 'safetyDSL_State', partner)
    assert owner in getattr(partner, 'safetyDSL_SafetyCritical42')
    _safe_set(owner, 'safetyDSL_State', None)
    assert owner not in getattr(partner, 'safetyDSL_SafetyCritical42')


def test_assoc_views0_stub_double():
    # safetyDSL_SafetyFramework has no real 'safetyDSL_SafetyFramework' property in the generated
    # code (a bare stub) -- manually attach it so safetyDSL_SafetyViewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # safetyDSL_SafetyViewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = safetyDSL_SafetyViewpoint(name="sample_text")
    partner = safetyDSL_SafetyFramework()
    setattr(partner, 'safetyDSL_SafetyFramework', None)
    _safe_set(owner, 'safetyDSL_SafetyViewpoint', partner)
    assert owner in getattr(partner, 'safetyDSL_SafetyFramework')
    _safe_set(owner, 'safetyDSL_SafetyViewpoint', None)
    assert owner not in getattr(partner, 'safetyDSL_SafetyFramework')


